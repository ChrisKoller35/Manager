# Reel «3 Klassen, 3 Looks»: drei App-Ansichten als Wisch-Karussell, Frage am Ende, Outro wie bei den Shorts
# Aufruf: python3 reel-klassen.py out.mp4   (erwartet k1/druide.png, k1/magier.png, k1/paladin.png, s4c/outro.png)
import subprocess, sys, numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H,FPS=1080,1920,30
IB='/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'; IM='/usr/share/fonts/opentype/inter/Inter-Medium.otf'
CZ='fonts/package/files/cinzel-latin-700-normal.woff'; STAR='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def hexc(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
AMB=hexc('#f5b642'); TXT=hexc('#ece8f7'); DIM=hexc('#9a92b8')
def F(p,s): return ImageFont.truetype(p,s)
def background(glowcol):
    y=np.linspace(0,1,H)[:,None,None]; a=np.array(hexc('#07060d')); b=np.array(hexc('#0e0b1a'))
    bg=(a*(1-y)+b*y)*np.ones((1,W,1)); yy,xx=np.mgrid[0:H,0:W]
    for cx,cy,r,col,k in [(W*.15,H*.18,700,hexc('#a855f7'),.16),(W*.9,H*.75,750,glowcol,.16),(W*.5,H*.98,600,AMB,.06)]:
        d=np.exp(-((xx-cx)**2+(yy-cy)**2)/(2*r*r))[...,None]; bg=bg+d*np.array(col)*k
    return Image.fromarray(np.clip(bg,0,255).astype('uint8')).convert('RGBA')
def ctext(d,t,f,y,col):
    bb=d.textbbox((0,0),t,font=f); d.text(((W-(bb[2]-bb[0]))//2-bb[0],y),t,font=f,fill=col)
def framed(shot, col):
    AW,AH=760,1273; AX,AY=(W-AW)//2,440
    im=Image.new('RGBA',(W,H),(0,0,0,0))
    glow=Image.new('L',(W,H),0); ImageDraw.Draw(glow).rounded_rectangle((AX-6,AY-6,AX+AW+6,AY+AH+6),48,fill=255)
    gl=Image.new('RGBA',(W,H),col+(0,)); gl.putalpha(glow.filter(ImageFilter.GaussianBlur(28)).point(lambda v:int(v*.55))); im.alpha_composite(gl)
    s=Image.open(shot).convert('RGBA').resize((AW,AH),Image.LANCZOS)
    m=Image.new('L',(AW,AH),0); ImageDraw.Draw(m).rounded_rectangle((0,0,AW-1,AH-1),40,fill=255); s.putalpha(m)
    im.alpha_composite(s,(AX,AY)); d=ImageDraw.Draw(im); d.rounded_rectangle((AX-3,AY-3,AX+AW+2,AY+AH+2),42,outline=col+(230,),width=4)
    return im
def slide(col, head, sub, shot=None, big=None, lines=()):
    im=background(col); d=ImageDraw.Draw(im)
    if shot: im.alpha_composite(framed(shot,col)); d=ImageDraw.Draw(im)
    y=150
    for i,l in enumerate(head):
        f=F(IB,92 if i==0 else 92); 
        bb=d.textbbox((0,0),l,font=f); x=(W-(bb[2]-bb[0]))//2-bb[0]
        # Schatten
        d.text((x+3,y+3),l,font=f,fill=(0,0,0,170)); d.text((x,y),l,font=f,fill=col if i==len(head)-1 else TXT); y+=108
    if sub: ctext(d,sub,F(IM,40),y+6,DIM)
    if lines:
        yy=760
        for l in lines: ctext(d,l,F(IB,78),yy,TXT); yy+=100
    if big: ctext(d,big,F(IM,38),yy+30,DIM)
    ctext(d,'✧ TAEHRON ✧',F(STAR,46),1780,AMB)
    return im.convert('RGB')
G=hexc('#4ade80'); B=hexc('#60a5fa'); Y=hexc('#eab308'); V=hexc('#a855f7')
S=[(1.7, slide(V,['3 Klassen,','3 Looks.'],'Jede Klasse hat ihre eigene Ansicht.',None,None,['Druide. Magier.','Paladin.'])),
   (2.7, slide(G,['Druide'],'Grün · Zauberplätze, HP, Wildform','k1/druide.png')),
   (2.7, slide(B,['Magier'],'Blau · Zauberbuch mit Grad 1 bis 3','k1/magier.png')),
   (2.7, slide(Y,['Paladin'],'Gold · Eidzauber, Handauflegen, Kanal','k1/paladin.png')),
   (2.6, slide(V,['Welche Klasse','als Nächstes?'],None,None,'12 Klassen · gratis im Browser · taehron.com',['Schreib’s in die','Kommentare!'])),
   (3.8, Image.open('s4c/outro.png').convert('RGB'))]
out=sys.argv[1]
enc=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
  '-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-c:v','libx264','-crf','17','-pix_fmt','yuv420p','-movflags','+faststart','-c:a','aac','-shortest',out],stdin=subprocess.PIPE)
prev=None; T=12
for idx,(dur,im) in enumerate(S):
    n=int(dur*FPS)
    for i in range(n):
        if prev is not None and i<T:
            k=i/T; e=1-(1-k)**3  # Wisch von rechts wie ein Karussell
            fr=Image.new('RGB',(W,H)); off=int(W*e); fr.paste(prev,(-off,0)); fr.paste(im,(W-off,0))
        else: fr=im
        enc.stdin.write(fr.tobytes())
    prev=im
enc.stdin.close(); enc.wait(); S[1][1].save('k1/vorschau.png'); S[4][1].save('k1/vorschau-frage.png'); print('ok', sum(d for d,_ in S))
