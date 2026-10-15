# Projekt-Inventar

Stand: 2026-10-15. Alle Pfade relativ zu `C:\Users\chris\Documents`. In jedem Hauptordner liegt eine `projekt.json`.
Markierungen und Status von Christoph am 15.10. bestätigt bzw. korrigiert.

| Projekt | Typ | Status | Markierung | Zuletzt | Stand | Ordner |
|---|---|---|---|---|---|---|
| D&D-Story: Der Spiegeldämon | story | aktiv | mehr-ich | 2026-10-13 | Kampagne mit fertiger Ordnerstruktur, wird laufend ergänzt | `D-D-Story` |
| TAEHRON (Zauber-App) | app | aktiv | mehr-ich | 2026-10-14 | Live auf taehron.netlify.app, offene PRs, Social-Media-Content läuft | `Dungeon und Dragon App\D-D-App-Alles-Zusammen` |
| SpellManager (persönliche D&D-App) | app | aktiv | mehr-ich | 2026-03-10 | Christophs persönliche D&D-App, sehr wichtig. Lokaler Ordner Stand März 2026, GitHub zuletzt Sept 2026 | `SpellManager` |
| Cashfish (Fisch-Game) | game | pausiert | mehr-ki | 2026-02-21 | Läuft lokal über Vite, KI-Sprite-Workflow vorhanden, seit Feb 2026 ruhig | `Mein Eigenes Game Version 06.01.26\Cashfish2-main` |
| Magic City (Aufbauspiel, Vorlage) | game | archiviert | mehr-ki | 2026-03-31 | Wird nicht weiterentwickelt, dient nur noch als Vorlage für Lowland | `Aufbauspiel` |
| Fantasy Explorer Engine-Vergleich | experiment | archiviert | mehr-ki | 2026-04-07 | Abgeschlossen, wird nicht weitergeführt | `Game Test 3` |
| TrailMate | app | aktiv | mehr-ki | 2026-03-25 | 8 Bau-Dokumente geplant, App-Gerüst mit Expo seit März 2026 | `Trailmate start\TrailMate` |
| Walkie-Talkie App | app | archiviert | mehr-ki | 2026-04-16 | Wird nicht weitergeführt. Client und Server in Python, Demo-Video und Homepage vorhanden | `WalkiTalki App` |
| Rally-Kamera-Controller | tool | pausiert | gemischt | 2026-03-17 | Erster Prototyp (app.py), ein Commit | `Rallykamera` |
| Inventory Zero-One (Artefakte) | web | archiviert | gemischt | 2026-02-11 | Aus der Ideenkarte genommen (15.10.2026), nichts gelöscht | `Inventory-Zero-One` |
| QR-Code-Generator (KBZSG) | tool | fertig | mehr-ki | 2026-02-02 | Einfache Web-Seite, seit Feb 2026 unverändert (vermutet fertig) | `Qr Code Generator` |
| YouTube-Geschichten (Hörbuch-Videos) | story | aktiv | mehr-ki | 2026-10-15 | Zu gross geworden, neu geplant: B17 fertigstellen, dann kapitelweise als Video hochladen | `Youtub Geschichte 01` |
| Lowland (Projekt «Third person nur mit code») | game | aktiv | mehr-ki | 2026-10-15 | Claude baut jeden Morgen um 06:30 rund 45 Minuten, Vorschlag am Abend um 21:30 (Testwoche bis 17.10.) | `Lowland Third Person Game` |
| Ideenkarte | tool | aktiv | mehr-ki | 2026-10-14 | Etappe 1 fertig (Ordnerbaum, Markdown-Anzeige, mehrere Projekte) | `Ideenkarte` |
| Manager-Workflow (Manager + KI-Bot) | tool | aktiv | mehr-ki | 2026-10-15 | Läuft seit 15.10.2026 (Morgen-Manager, KI-Bot, Lowland-Session); Manager darf ihn selbst weiterentwickeln | `Manager` |
| Moneyprojekt (Geld mit digitalen Produkten) | business | idee | mehr-ki | 2026-10-15 | Nur die Projektidee ist notiert, die Auswahl der Projekte steht noch aus | `Moneyprojekttry` |

## Nicht aufgenommen (Kleinkram oder unklar)

- `Git` – Übungs-Repo «Mein erstes Projekt mit Github»
- `Raphi`, `untitled`, `ConnectionView*.qml` – Qt/QML-Ansicht (vermutlich für Raphi)
- `Zeichnungs buch` – nur ein PDF
- `aquarium.html`, `game.html` – einzelne Spielereien im Documents-Ordner
- `Codex`, `Neuer Ordner` – Codex-Plugins bzw. leer
- Persönliche Dokumente, Bewerbungen, Steuern, Anno 1800, League of Legends – keine Projekte

## Schema der projekt.json

| Feld | Bedeutung |
|---|---|
| `schema` | Version, aktuell `ideenkarte-projekt/1` |
| `id`, `name` | stabile ID und Anzeigename |
| `typ` | `story`, `game`, `app`, `tool`, `web`, `experiment`, `business` |
| `beschreibung`, `stand` | worum es geht, wo es steht (ein Satz) |
| `status` | `idee`, `aktiv`, `pausiert`, `fertig`, `archiviert` |
| `regeln` | feste Regeln für Agents, z.B. «nur ändern, wenn Christoph dabei ist» |
| `markierung` | `mehr-ich`, `mehr-ki`, `gemischt`; `markierungGeprueft` = von Christoph bestätigt |
| `zuletztGeaendert` | letzte Änderung im Ordner |
| `ordner` | `haupt` plus `weitere` zugehörige Ordner |
| `repo`, `technik`, `start` | GitHub-Link, Technik, wie man es startet |
| `einstiegsdateien` | was ein Agent zuerst lesen soll |
| `struktur` | Ordner und was darin liegt (z.B. Feinde/ → Stats, Fähigkeiten) |
| `naechsteAufgaben` | Liste aus `text` und `wer` (`ich` oder `ki`) |
| `aktualisiert`, `aktualisiertVon` | wann und von wem die Datei zuletzt gepflegt wurde |
