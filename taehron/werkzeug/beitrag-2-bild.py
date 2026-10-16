import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H=1080,1350
INTER_B='/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'; INTER_M='/usr/share/fonts/opentype/inter/Inter-Medium.otf'; INTER_S='/usr/share/fonts/opentype/inter/Inter-SemiBold.otf'
CINZEL='/tmp/claude-0/fonts/package/files/cinzel-latin-700-normal.woff'; STAR='/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
F=ImageFont.truetype
def hexc(h): h=h.lstrip('#'); return tuple(int(h[i:i+2],16) for i in (0,2,4))
AMB=hexc('#f5b642'); TXT=hexc('#ece8f7'); DIM=hexc('#9a92b8'); BLUE=hexc('#38bdf8')
# background
y=np.linspace(0,1,H)[:,None,None]; bg=(np.array(hexc('#07060d'))*(1-y)+np.array(hexc('#0e0b1a'))*y)*np.ones((1,W,1))
yy,xx=np.mgrid[0:H,0:W]
for cx,cy,r,col,k in [(W*.12,H*.15,600,hexc('#a855f7'),.18),(W*.9,H*.7,650,hexc('#0284c7'),.16),(W*.5,H*1.0,500,AMB,.07)]:
    bg=bg+np.exp(-((xx-cx)**2+(yy-cy)**2)/(2*r*r))[...,None]*np.array(col)*k
im=Image.fromarray(np.clip(bg,0,255).astype('uint8')).convert('RGBA'); d=ImageDraw.Draw(im)
def ctext(parts,f,y):
    tw=sum(d.textlength(t,font=f) for t,_ in parts); x=(W-tw)/2
    for t,c in parts: d.text((x,y),t,font=f,fill=c); x+=d.textlength(t,font=f)
# wordmark
def grad(text,font,c1,c2):
    b=d.textbbox((0,0),text,font=font); w,h=b[2]-b[0]+4,b[3]-b[1]+4
    m=Image.new('L',(w,h),0); ImageDraw.Draw(m).text((-b[0]+2,-b[1]+2),text,font=font,fill=255)
    g=np.zeros((h,w,3)); t=np.linspace(0,1,w)[None,:,None]; g[:]=np.array(c1)*(1-t)+np.array(c2)*t
    o=Image.fromarray(g.astype('uint8')); o.putalpha(m); return o
n_=grad('TAEHRON',F(CINZEL,44),AMB,hexc('#ffa620')); st=grad('✧',F(STAR,36),AMB,AMB)
wm=Image.new('RGBA',(n_.width+2*st.width+40,max(n_.height,st.height))); wm.alpha_composite(st,(0,(wm.height-st.height)//2)); wm.alpha_composite(n_,(st.width+20,(wm.height-n_.height)//2)); wm.alpha_composite(st,(wm.width-st.width,(wm.height-st.height)//2))
glow=Image.new('RGBA',wm.size,AMB+(0,)); glow.putalpha(wm.getchannel('A').filter(ImageFilter.GaussianBlur(8)).point(lambda a:int(a*.5)))
im.alpha_composite(glow,((W-wm.width)//2,58)); im.alpha_composite(wm,((W-wm.width)//2,58)); d=ImageDraw.Draw(im)
ctext([('Dein Zauberbuch ',TXT),('am Tisch.',AMB)],F(INTER_B,66),138)
ctext([('Charakter gebaut? Hier hast du deine Zauber',DIM)],F(INTER_M,30),232)
ctext([('und Zauberplätze im Blick, direkt auf dem Tablet.',DIM)],F(INTER_M,30),272)
# tablet
shot=Image.open('tab_view2.png').convert('RGB')
SH_=870; SW_=int(shot.width*SH_/shot.height); shot=shot.resize((SW_,SH_),Image.LANCZOS)
B=22; tw,th=SW_+2*B,SH_+2*B; tx,ty=(W-tw)//2,335
g=Image.new('L',(W,H),0); ImageDraw.Draw(g).rounded_rectangle((tx,ty,tx+tw,ty+th),48,fill=255)
gl=Image.new('RGBA',(W,H),BLUE+(0,)); gl.putalpha(g.filter(ImageFilter.GaussianBlur(30)).point(lambda v:int(v*.45))); im.alpha_composite(gl)
d=ImageDraw.Draw(im); d.rounded_rectangle((tx,ty,tx+tw,ty+th),48,fill=hexc('#15121f'),outline=(168,132,255),width=3)
m=Image.new('L',(SW_,SH_),0); ImageDraw.Draw(m).rounded_rectangle((0,0,SW_-1,SH_-1),28,fill=255)
im.paste(shot,(tx+B,ty+B),m); d=ImageDraw.Draw(im)
# callouts
def callout(lines,x,y,tx_,ty_,align):
    f=F(INTER_S,25)
    for i,l in enumerate(lines):
        w=d.textlength(l,font=f); xx=x if align=='l' else x-w
        d.text((xx,y+i*32),l,font=f,fill=AMB if i==0 else TXT)
    sx = x+ (0 if align=='l' else 0)
    d.line([(tx_,ty_),( (x-12) if align=='l' else (x+12), y+16)],fill=AMB+(255,),width=2); d.ellipse((tx_-6,ty_-6,tx_+6,ty_+6),fill=AMB)
L=tx-14; R=tx+tw+14
callout(['Slots','antippen'],R+4,410,418,437,'l')
callout(['Rast setzt','alles zurück'],L-4,1110,262,1191,'r')
callout(['Würfel auf','einen Blick'],R+4,800,582,944,'l')
callout(['200 Zauber','auf Deutsch'],L-4,620,262,800,'r')
ctext([('Gratis im Browser · ',DIM),('taehron.com',AMB)],F(INTER_S,32),1272)
im.convert('RGB').save('beitrag-2.png'); print(tx,tw)
