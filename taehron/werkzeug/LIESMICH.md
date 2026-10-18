# Kurzvideo-Werkzeug (TAEHRON)

1. Repo klonen, `npm ci --ignore-scripts`, `npx vite --port 5173` starten.
2. `node rec.mjs` nimmt die echte App per Playwright (Chromium, Handy-Viewport 390×653) als Frames auf (CDP-Screencast) und setzt Tipp-Kreise.
3. Frames zu `raw.mp4` zusammensetzen (concat mit Zeitstempeln aus meta.json), schneiden zu `edit.mp4`.
4. `python3 compose.py` legt Hintergrund, Rahmen, Texte und Outro darüber → `out.mp4` (1080×1920, 30 fps, stille Tonspur).
Schriften: Cinzel (npm @fontsource/cinzel), Inter (System).

## Regel-Shorts (ab 18.10.2026)
- App lokal starten (`npx vite --port 5173`), dann `PLAN='[2,2,1,1]' HPDOWN=4 REST='Lange Rast' node rec-rast.mjs kleriker 5 out` (Playwright, Sprache DE, Stufe wird gesetzt, Slots je Zeile von rechts abgehakt).
- `python3 assemble.py out` macht `out/raw.mp4` und zeigt die Zeitmarken.
- `python3 compose3.py config.json` wie compose2, plus Aufruf «Folg …» im Outro (`cta`) und Hook ab dem ersten Bild.
- `python3 reel-zitate.py` baut das Zitat-Reel (Folien + Outro).
