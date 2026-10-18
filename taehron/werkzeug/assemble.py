# Frames mit Zeitstempeln -> raw.mp4 (30 fps), gibt Markenzeiten relativ zum Start aus
import json,sys,subprocess
out=sys.argv[1]; m=json.load(open(out+'/meta.json')); meta=m['meta']; t0=meta[0][1]
with open(out+'/list.txt','w') as f:
    for i,(name,ts) in enumerate(meta):
        d=(meta[i+1][1]-ts) if i+1<len(meta) else 0.5
        f.write(f"file '{name.split('/')[-1] if False else name}'\nduration {d:.4f}\n")
    f.write(f"file '{meta[-1][0]}'\n")
subprocess.run(['ffmpeg','-y','-loglevel','error','-f','concat','-safe','0','-i',out+'/list.txt','-vf','fps=30,scale=860:1440:flags=lanczos,format=yuv420p','-c:v','libx264','-crf','14',out+'/raw.mp4'],check=True)
print({k:round(v-t0,2) for k,v in m['marks'].items()}, 'len', round(meta[-1][1]-t0,2))
