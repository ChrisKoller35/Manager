# Kurzvideo-Werkzeug (TAEHRON)

1. Repo klonen, `npm ci --ignore-scripts`, `npx vite --port 5173` starten.
2. `node rec.mjs` nimmt die echte App per Playwright (Chromium, Handy-Viewport 390×653) als Frames auf (CDP-Screencast) und setzt Tipp-Kreise.
3. Frames zu `raw.mp4` zusammensetzen (concat mit Zeitstempeln aus meta.json), schneiden zu `edit.mp4`.
4. `python3 compose.py` legt Hintergrund, Rahmen, Texte und Outro darüber → `out.mp4` (1080×1920, 30 fps, stille Tonspur).
Schriften: Cinzel (npm @fontsource/cinzel), Inter (System).
