# Reel «Das sagen Tester»: Zitat-Folien 1080x1920 mit App-Bild im Hintergrund, Outro wie bei den Shorts
import subprocess, json
from PIL import Image, ImageDraw, ImageFont, ImageFilter
W,H,FPS=1080,1920,30
IB='/usr/share/fonts/opentype/inter/Inter-ExtraBold.otf'; IM='/usr/share/fonts/opentype/inter/Inter-Medium.otf'
CZ='fonts/package/files/cinzel-latin-700-normal.woff'
AMB=(245,182,66); TXT=(236,232,247); DIM=(154,146,184)
outro=Image.open('s3/outro.png').convert('RGB')
app=Image.open('s4/final.png').convert('RGB').resize((W,int(W*1440/860)))
base=Image.new('RGB',(W,H),(7,6,13)); base.paste(app,(0,(H-app.height)//2))
base=base.filter(ImageFilter.GaussianBlur(14)); base=Image.blend(base,Image.new('RGB',(W,H),(7,6,13)),0.72)
def ctext(d,t,f,y,col):
    bb=d.textbbox((0,0),t,font=f); d.text(((W-(bb[2]-bb[0]))//2-bb[0],y),t,font=f,fill=col)
def slide(top, lines, small):
    im=base.copy(); d=ImageDraw.Draw(im)
    ctext(d,top,ImageFont.truetype(IM,40),420,DIM)
    f=ImageFont.truetype(IB,84); y=820-len(lines)*55
    ctext(d,'«',ImageFont.truetype(CZ,160),y-190,AMB)
    for l in lines: ctext(d,l,f,y,TXT); y+=110
    if small: ctext(d,small,ImageFont.truetype(IM,38),y+40,DIM)
    ctext(d,'✧ TAEHRON ✧',ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',46),1560,AMB)
    return im
S=[(2.0,slide('Echte Stimmen aus dem Test',['Was sagen Tester','über TAEHRON?'],None)),
   (2.4,slide('Tester, Druide Stufe 3',['Ich finde die Seite','genial. Einfach super.'],None)),
   (2.0,slide('Tester, Druide Stufe 3',['Schönes Design.'],None)),
   (2.4,slide('Tester, Druide Stufe 3',['Die App gefällt mir','sehr gut. Danke sehr!'],None)),
   (2.4,slide('Dein Zauberbuch am Tisch',['Probier’s selbst.'],'Gratis im Browser · ohne Account')),
   (3.6,outro)]
enc=subprocess.Popen(['ffmpeg','-y','-loglevel','error','-f','rawvideo','-pix_fmt','rgb24','-s',f'{W}x{H}','-r',str(FPS),'-i','-',
  '-f','lavfi','-i','anullsrc=r=44100:cl=stereo','-c:v','libx264','-crf','17','-pix_fmt','yuv420p','-movflags','+faststart','-c:a','aac','-shortest','r1/reel-das-sagen-tester.mp4'],stdin=subprocess.PIPE)
prev=None
for dur,im in S:
    n=int(dur*FPS)
    for i in range(n):
        fr=Image.blend(prev,im,min(1,i/8)) if prev is not None and i<8 else im
        enc.stdin.write(fr.tobytes())
    prev=im
enc.stdin.close(); enc.wait()
S[1][1].save('r1/vorschau-zitat.png'); print('ok', sum(d for d,_ in S))
