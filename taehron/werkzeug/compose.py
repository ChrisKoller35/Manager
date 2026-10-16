import subprocess, numpy as np, math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H=1080,1920; FPS=30
AW,AH=760,1273; AX,AY=(W-AW)//2,400
INTER_B='/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'
INTER_M='/usr/share/fonts/opentype/inter/Inter-Medium.otf'
CINZEL='fonts/package/files/cinzel-latin-700-normal.woff'
STAR='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
def F(p,s): return ImageFont.truetype(p,s)

def grad_text(text, font, c1, c2):
    d=ImageDraw.Draw(Image.new('L',(1,1))); b=d.textbbox((0,0),text,font=font)
    w,h=b[2]-b[0]+4,b[3]-b[1]+4
    m=Image.new('L',(w,h),0); ImageDraw.Draw(m).text((-b[0]+2,-b[1]+2),text,font=font,fill=255)
    g=np.zeros((h,w,3)); t=np.linspace(0,1,w)[None,:,None]
    g[:]=np.array(c1)*(1-t)+np.array(c2)*t
    im=Image.fromarray(g.astype('uint8')); im.putalpha(m); return im

def hexc(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))

def wordmark(c1,c2,size=64):
    star=grad_text('✧',F(STAR,int(size*.8)),c1,c1); name=grad_text('TAEHRON',F(CINZEL,size),c1,c2); star2=grad_text('✧',F(STAR,int(size*.8)),c2,c2)
    gap=int(size*.35); w=star.width+name.width+star2.width+2*gap; h=max(name.height,star.height)
    im=Image.new('RGBA',(w,h)); im.alpha_composite(star,(0,(h-star.height)//2)); im.alpha_composite(name,(star.width+gap,(h-name.height)//2)); im.alpha_composite(star2,(w-star2.width,(h-star2.height)//2))
    glow=Image.new('RGBA',im.size,c1+(0,)); glow.putalpha(im.getchannel('A').filter(ImageFilter.GaussianBlur(10)).point(lambda a:int(a*.6)))
    out=Image.new('RGBA',(w+40,h+40)); out.alpha_composite(glow,(20,20)); out.alpha_composite(im,(20,20)); return out

# background
def background():
    y=np.linspace(0,1,H)[:,None,None]
    a=np.array(hexc('#07060d')); b=np.array(hexc('#0e0b1a'))
    bg=(a*(1-y)+b*y)*np.ones((1,W,1))
    yy,xx=np.mgrid[0:H,0:W]
    for cx,cy,r,col,k in [(W*.15,H*.18,700,hexc('#a855f7'),.16),(W*.9,H*.75,750,hexc('#16a34a'),.14),(W*.5,H*.98,600,hexc('#f5b642'),.06)]:
        d=np.exp(-((xx-cx)**2+(yy-cy)**2)/(2*r*r))[...,None]; bg=bg+d*np.array(col)*k
    return Image.fromarray(np.clip(bg,0,255).astype('uint8')).convert('RGBA')
BG0=background(); BG=BG0.copy()
# app frame: glow + border
frame=Image.new('RGBA',(W,H))
g=Image.new('L',(W,H),0); ImageDraw.Draw(g).rounded_rectangle((AX-6,AY-6,AX+AW+6,AY+AH+6),56,fill=255)
g=g.filter(ImageFilter.GaussianBlur(28)).point(lambda v:int(v*.55))
gl=Image.new('RGBA',(W,H),hexc('#4ade80')+(0,)); gl.putalpha(g); BG.alpha_composite(gl)
ImageDraw.Draw(frame).rounded_rectangle((AX-3,AY-3,AX+AW+3,AY+AH+3),50,outline=(168,132,255,110),width=3)
MASK=Image.new('L',(AW,AH),0); ImageDraw.Draw(MASK).rounded_rectangle((0,0,AW-1,AH-1),46,fill=255)
WM=wordmark(hexc('#4ade80'),hexc('#16a34a'),52)
sub=F(INTER_M,26)
BOTTOM=Image.new('RGBA',(W,H)); bd=ImageDraw.Draw(BOTTOM)
BOTTOM.alpha_composite(WM,((W-WM.width)//2,AY+AH+28))
t='DRUIDE · STUFE 3'; bb=bd.textbbox((0,0),t,font=sub); bd.text(((W-(bb[2]-bb[0]))//2,AY+AH+28+WM.height-6),t,font=sub,fill=hexc('#9a92b8'))
BASE=BG.copy(); BASE.alpha_composite(frame); BASE.alpha_composite(BOTTOM)

CAP_FONT=F(INTER_B,70)
def caption_img(lines, accent):
    # lines: list of str; words in accent set get green
    d=ImageDraw.Draw(Image.new('RGBA',(1,1)))
    lh=86; h=lh*len(lines)+10; im=Image.new('RGBA',(W,h))
    dr=ImageDraw.Draw(im)
    for i,l in enumerate(lines):
        words=l.split(' '); widths=[d.textlength(w+' ',font=CAP_FONT) for w in words]
        tw=sum(widths)-d.textlength(' ',font=CAP_FONT); x=(W-tw)/2
        for w,wd in zip(words,widths):
            col=hexc('#4ade80') if w.strip('.,?!:') in accent else hexc('#ece8f7')
            dr.text((x+3,i*lh+5),w,font=CAP_FONT,fill=(0,0,0,160))
            dr.text((x,i*lh),w,font=CAP_FONT,fill=col); x+=wd
    return im
CAPS=[ (0,3.1,['Zauberplätze noch','auf Papier radieren?'],{'Papier'}),
       (3.1,7.7,['12 Klassen,','jede mit eigenem Look'],{'12','Klassen,'}),
       (7.7,12.8,['Slots antippen','statt radieren'],{'antippen'}),
       (12.8,14.8,['Lange Rast:','alles wieder voll'],{'voll'}),
       (14.8,20.5,['400+ Zauber auf Deutsch,','mit eigenen Bildern'],{'400+','Deutsch,'}),
       (20.5,23.8,['Würfel und Regeln','auf einen Blick'],{'Würfel'}) ]
CAPS=[(a,b,caption_img(l,s)) for a,b,l,s in CAPS]
CAP_Y=190

# outro
def outro():
    im=BG0.copy(); d=ImageDraw.Draw(im)
    wm=wordmark(hexc('#f5b642'),hexc('#ffa620'),110)
    im.alpha_composite(wm,((W-wm.width)//2,660))
    def ctext(t,f,y,col):
        bb=d.textbbox((0,0),t,font=f); d.text(((W-(bb[2]-bb[0]))//2,y),t,font=f,fill=col)
    ctext('ZAUBER-APP FÜR ROLLENSPIELE',F(INTER_M,34),660+wm.height+10,hexc('#9a92b8'))
    ctext('Gratis im Browser',F(INTER_B,64),1000,hexc('#ece8f7'))
    ctext('Early Access · offline · ohne Account',F(INTER_M,36),1090,hexc('#9a92b8'))
    # pill
    t='Link im Profil'; f=F(INTER_B,52); bb=d.textbbox((0,0),t,font=f); w=bb[2]-bb[0]+110; x=(W-w)//2
    pl=Image.new('RGBA',(W,H)); ImageDraw.Draw(pl).rounded_rectangle((x,1220,x+w,1330),55,fill=(245,182,66,40),outline=hexc('#f5b642'),width=3); im.alpha_composite(pl); d=ImageDraw.Draw(im)
    ctext(t,f,1246,hexc('#f5b642'))
    fs=F(INTER_M,24)
    for i,l in enumerate(['Enthält Material aus dem SRD 5.1 von Wizards of the Coast LLC (CC BY 4.0).','Nicht verbunden mit Wizards of the Coast. Details: Link im Profil.']):
        ctext(l,fs,1560+i*36,hexc('#6b6389'))
    return im
OUT=outro()
T_OUT=23.8; TOTAL=27.3

def ease(x): x=max(0,min(1,x)); return 1-(1-x)**3
src=subprocess.Popen(['ffmpeg','-loglevel','error','-i','edit.mp4','-f','rawvideo','-pix_fmt','rgb24','-'],stdout=subprocess.PIPE)
enc=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
   '-f','lavfi','-t',str(TOTAL),'-i','anullsrc=r=44100:cl=stereo',
   '-c:v','libx264','-preset','slow','-crf','17','-pix_fmt','yuv420p','-profile:v','high','-movflags','+faststart','-c:a','aac','-b:a','128k','-shortest','out.mp4'],stdin=subprocess.PIPE)
n=int(TOTAL*FPS); last=None
for i in range(n):
    t=i/FPS
    if t<T_OUT+0.6:
        raw=src.stdout.read(860*1440*3)
        if raw and len(raw)==860*1440*3: last=Image.frombytes('RGB',(860,1440),raw)
        app=last.resize((AW,AH),Image.LANCZOS)
        fr=BASE.copy(); fr.paste(app,(AX,AY),MASK)
        for a,b,img in CAPS:
            if a-0.01<=t<b:
                k=ease((t-a)/0.25); kout=1-ease((t-(b-0.2))/0.2) if t>b-0.2 and b<T_OUT else 1
                al=img.getchannel('A').point(lambda v,kk=k*kout:int(v*kk)); im2=img.copy(); im2.putalpha(al)
                fr.alpha_composite(im2,(0,int(CAP_Y+30*(1-k))))
        if t>=T_OUT:
            fr=Image.blend(fr,OUT,ease((t-T_OUT)/0.6))
    else:
        fr=OUT
    if i==0: fr.convert('RGB').save('first.png')
    enc.stdin.write(fr.convert('RGB').tobytes())
enc.stdin.close(); enc.wait(); src.terminate()
print('done')
