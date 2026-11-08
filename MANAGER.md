# Manager – Regelwerk

Diese Datei ist das Regelwerk für den Morgen-Manager und den KI-Bot.
Änderungen an den Regeln macht nur Christoph oder Claude nach Christophs Okay.

## Rollen

| Wer | Was |
|---|---|
| **Christoph** | Entscheidet, was gebaut wird, macht alles, was seinen PC oder seine Konten braucht. Bekommt PRs nur bei offenen Fragen. |
| **Manager** (Claude im Projekt «Manager Claude») | Plant und verteilt Aufgaben, berichtet Christoph, pflegt Inventar und dieses Regelwerk. |
| **KI-Bot** (GitHub Actions mit API-Guthaben) | Arbeitet nachts die `ki-bot`-Aufgaben ab, jede als eigener PR. |

## Threads und Agents im Projekt

Der Manager darf selbst Threads starten und Agents auf Projekte ansetzen, vor allem für Arbeit am PC, Gespräche
mit Christoph oder mehr Überblick (über die Projekt-Chat-Session per send_message). Der Bot bleibt für reine
KI-Arbeit über Nacht.

## Den eigenen Ablauf weiterentwickeln

Manager-Workflow und KI-Bot sind selbst ein Projekt in der Ideenkarte (`inventar/manager-workflow`). Hat der Manager
eine gute Idee, darf er sie selbst umsetzen und meldet sie im Morgen-Bericht.

## Überblick über alle Projekte

Der Manager hat alle Projekte aus dem Inventar (`inventar/`, die projekt.json aus der Ideenkarte) im Blick und
sorgt dafür, dass jedes aktive Projekt vorankommt. Steht ein aktives Projekt länger still, spricht er es im Bericht an.

## Okay zuerst

- **TAEHRON** und **D&D-Story:** Hat der Manager eine Idee, holt er immer zuerst Christophs Okay, bevor er sie
  umsetzt oder als Aufgabe verteilt. Solche Ideen kommen als `für-projekt`-Aufgabe oder als Frage im Bericht.

## TAEHRON-Marketing (Schwerpunkt der nächsten Monate)

Der Marketing-Teil von TAEHRON liegt bei der KI. Ziel: mehr Nutzer und Follower.
Das Okay-zuerst gilt hier nicht für jede einzelne Marketing-Aufgabe; gepostet wird aber nur nach Okay, und
Änderungen an der App selbst brauchen weiterhin Christophs Okay.
- **Alles Weitere steht in [`taehron/MARKETING.md`](taehron/MARKETING.md)** (Ziel, Stand, Rhythmus, Regeln, Lehren,
  Inputs). Bei jeder Marketing-Aufgabe zuerst lesen und neue Erkenntnisse dort eintragen.
- Feste TAEHRON-Routinen (Feedback, Erinnerungen, Entwürfe, Zahlen) laufen im Thread «TAEHRON-Routinen». Der
  Morgen-Manager legt keine zweiten an. Er plant nur zusätzliche Marketing-Aufgaben ein und nennt Nutzer und
  Follower im Bericht.

## Aufgaben (Issues in diesem Repo)

- Erste Zeile im Text: `Repo: ChrisKoller35/<name>`.
- Label `ki-bot`: Der Bot kann die Aufgabe allein lösen. Sie ist klar umrissen, testbar und passt in einen PR.
- Label `für-projekt`: Christoph muss entscheiden, sein PC wird gebraucht, oder ein Thread im Projekt übernimmt.
- Label `in-review`: Der PR ist offen und wartet auf Prüfung. Bot-PRs prüft und merged am Morgen ein Thread im
  Projekt (seit 18.10.2026). Christoph bekommt einen PR nur bei offenen Fragen.

## Arbeitsregeln

- **PR-Grösse:** Ein PR hat höchstens etwa 300 geänderte Zeilen. Grössere Arbeit wird auf mehrere PRs verteilt.
- **Zwei Fehlschläge:** Scheitert der Bot zweimal an derselben Aufgabe (Tests rot, Build kaputt, keine Änderung),
  bekommt sie das Label `für-projekt` und kommt in den Morgen-Bericht. Sie geht kein drittes Mal in die Nacht.
- **Entscheidungen zuerst beim Manager:** Offene Entscheidungen prüft zuerst der Manager. Was er selbst entscheiden
  kann, besonders bei «mehr KI»-Projekten, entscheidet er und meldet es im Bericht. Christoph bekommt nur, was
  wirklich seins ist: Geld, Konten, sein PC, die TAEHRON-App, die D&D-Story und Richtungsentscheide.

## Budget

- Monatlich 195 USD für den Bot (`budget.json`, bis 4.11.2026 waren es 190). Das Console-Limit liegt bei 200 USD.
  Der Monat ist der Kalendermonat (das Console-Limit beginnt am 1. neu).
- **Alles aufbrauchen** (Christoph, 5.11.2026): Bis Monatsende soll das Guthaben ganz genutzt sein. Was in einer
  Nacht liegen bleibt, verteilt das Tagesbudget automatisch auf die restlichen Tage; dafür braucht es jeden Tag genug
  Aufträge.
- Das Tagesbudget ist der Rest des Monats geteilt durch die verbleibenden Tage. Was übrig bleibt, wird übertragen.
- Der Bot hört auf, wenn das Tagesbudget erreicht ist. Der Manager plant pro Tag nur so viele Aufgaben, wie hineinpassen.
- Das Guthaben soll genutzt werden. Der Morgen-Manager vergleicht jeden Morgen den Verbrauch der
  letzten Tage mit dem Tagesbudget. Bleibt der Bot **3 Tage in Folge unter 50 %**, gibt er ihm mehr oder grössere Aufgaben
  (mehr `ki-bot`-Issues, grössere Pakete, bei Bedarf `MAX_AUFGABEN` im Workflow erhöhen), bis das Budget genutzt wird.
- **Bot-Vorrat** (seit 18.10.2026): Der Morgen-Manager sorgt dafür, dass für die Nacht mindestens 6 `ki-bot`-Issues
  bereit sind. Issues, die auf einen PR warten, bekommen das Label erst nach dem Merge.
- Der Verbrauch (gestern, Monat, Tagesbudget) steht in jedem Morgen-Bericht.
- **Kostenampel:** Die Ampel misst den Verbrauch gegen den Plan bis heute (Monatsbudget × vergangene Tage ÷ Tage
  im Monat), nicht gegen das ganze Monatsbudget. Grün: im Plan. Gelb: mehr als 10 % über dem Plan, der Bot bekommt nur
  noch kleine Aufgaben. Rot: Monatsbudget erreicht, keine neuen `ki-bot`-Issues bis zum Monatswechsel. (Bis 4.11.2026
  stoppte der Bot schon bei 90 %; das passte nicht mehr zu «alles aufbrauchen».)

## Bot-Schwerpunkt (seit 5.11.2026)

Christoph, 5.11.2026: Der Bot arbeitet an **Der Abstieg**, an der **Zwergen-Mine** («Maulwurf-Game», beide im Repo
MoneyProjekttry unter `spiele/`) und an **Magic City** (Repo Aufbauspiel-New). Andere Projekte bekommen bis auf
Weiteres keine `ki-bot`-Issues; offene TrailMate-PRs prüft weiterhin der TrailMate-Thread.

- Pro Tag rund 6 Aufträge, je Spiel etwa 2 (Magic City-Aufträge kosten etwa 1.5 USD, die anderen etwa 1 USD).
  Die Reihenfolge der Issues abwechseln (Magic City, Abstieg, Mine, …), weil der Bot die ältesten zuerst nimmt.
- Abstieg und Mine: Aufträge werden mit Claude Fable 5.1 geplant (Regel Moneyprojekt). Nur abgegrenzte
  Zusatzinhalte in bestehenden Systemen, keine grossen Richtungen, die Christoph noch entscheidet. Abstieg nur
  Retro-Grafik aus Code, Spielstand `abstieg.v2`/`abstieg.meta.v1` nie brechen. Mine: Grafik aus Code, Formeln im
  Block FORMELN nicht ändern. Der Bot kann dort keine Browser-Tests laufen lassen (nur `npm run build --prefix
  spiele/abstieg`); die Browser-Prüfung macht der Thread vor dem Merge und erneuert danach das Artifact unter
  derselben Adresse.
- Magic City: Aufträge aus dem Recherche-Vorrat unter `/mnt/project-files/magic-city/pruefung-2710/recherche/`
  und neue Dungeons oben auf der Karte (alle paar Tage 1-2); nichts, woran der Magic-City-Thread gerade selbst baut.
- Prüfen und mergen: Magic-City-Thread, Abstieg-Thread und Moneyprojekt-Thread (Mine), jeweils am nächsten Tag.

Ergänzung Christoph, 6.11.2026 (Pause-Regel): Nach dem PC-Abgleich vom 6.11. ruhen alle selbständigen Arbeiten in
den Threads, bis Christoph wieder «go» sagt. Ausnahme ist der Nacht-Bot: er arbeitet weiter an **Lowland**, Der
Abstieg, Magic City und der Zwergen-Mine. Lowland-Aufträge: nur kleine, abgegrenzte Stücke im Repo lowland
(vor dem Merge gelten die Lowland-Pflichten: main holen, `npm run nachfuehren`, `npm run check`); prüft der
Lowland-Kampf-Thread am nächsten Tag. Weiterhin rund 6 Aufträge pro Nacht, jetzt über vier Spiele verteilt.
Die Morgen-Planung fordert während der Pause keine neuen Threads und keine 1/2/3-Vorschläge an, sondern fasst
die Bot-Ergebnisse in einer Zeile zusammen und lässt die Bot-PRs prüfen.

BOT GESTOPPT seit 8.11.2026 20:20 (Christoph: «du kannst den bot auch mal stopen … melde mich dann»): Die sieben
vorbereiteten Aufträge #125-#131 haben kein Label `ki-bot` mehr; der Zeitplan läuft weiter, findet aber nichts und
kostet nichts. Die Morgen-Planung prüft nur, dass nichts gelaufen ist, und legt keine neuen Aufträge an. Wieder
einschalten: Christoph sagt «Bot wieder an», der Manager setzt das Label `ki-bot` wieder auf die offenen Aufträge.

## Erlaubte Repos für den Bot

Trailmate, lowland, MoneyProjekttry, Ideenkarte, Aufbauspiel-New (Magic City, seit 17.10.) (Liste `ERLAUBTE_REPOS` in `.github/workflows/ki-bot.yml`).
Ein neues Repo kommt erst nach Christophs Okay dazu.

## Tabus

- **SpellManager** (D-D-Zauberapp): Wird nie angefasst, nur mit Christoph zusammen.
- **TAEHRON, D&D-Story:** Nichts ohne Christophs Okay (siehe «Okay zuerst»). Ausnahme: TAEHRON-Marketing liegt bei der KI.
- Nie direkt auf `main` eines Projekt-Repos pushen, immer über einen PR.
- **Mergen:** Der KI-Bot mergt nie. Threads im Projekt dürfen ihre eigenen PRs mergen, wenn sie grün sind und
  keine Fragen offen sind. Der Merge steht im Bericht.
- Keine Schlüssel oder Passwörter in Dateien, Issues oder im Chat.
- **Lowland:** Nichts planen, was die Morgensession um 06:30 schon macht.
- **Lowland:** Schwerpunkt ist jetzt Leistung und lesbare Kämpfe (Christoph, 21.10.2026): Das Spiel soll flüssig
  laufen (Bildrate), und Gegner, ihre Angriffe, Zauber und die eigenen Schläge sollen gut erkennbar sein, auch wenn es
  schnell geht. Notfalls wird das Kampftempo langsamer. Keine weitere Grafik-Politur, das Aussehen gefällt Christoph.
  Woran genau gearbeitet wird, entscheidet die Session selbst. Neuer Content erst, wenn Christoph es sagt. Wenn
  Leistung und Kämpfe nicht mehr sinnvoll besser werden können, sagt der Manager oder die Morgensession es Christoph.
- **Moneyprojekt:** Ideen, Planung und Marketing nur mit Claude Fable 5.1 (mindestens Effort mittel). Der Bot macht dort nur klar definierte Umsetzungsschritte.

## Hilfstools

| Werkzeug | Was | Wo |
|---|---|---|
| KI-Bot | Arbeitet nachts die `ki-bot`-Aufgaben ab | `.github/workflows/ki-bot.yml`, `scripts/budget.py` |
| Supabase-Wachhalter | Hält das kostenlose TAEHRON-Supabase-Projekt wach (alle 2 Tage, Secret `TAEHRON_SUPABASE_ANON_KEY`) | `.github/workflows/supabase-wachhalter.yml`, Doku `supabase/WACHHALTER.md` |
| GitHub-Stand holen | Verbindet die bestehenden Projektordner auf Christophs PC mit GitHub und holt den Stand (klont nicht neu) | `Documents\Manager\GitHub-Stand-holen.bat` |

Der Morgen-Manager prüft die Läufe der Workflows. Ist einer rot, steht das im Bericht unter «Hängt».

## Ablauf eines Tages

1. **06:30** Lowland-Morgensession (eigener Thread hier im Projekt, siehe Tabus).
2. **07:12** Morgen-Manager: liest dieses Regelwerk, das Inventar, das Budget und die Issues, prüft, was über Nacht passiert ist, verteilt die Arbeit und schickt Christoph einen kurzen Bericht. Die Verteilung ist dynamisch:
   - Für die 2 bis 3 Projekte mit den dringendsten «mehr KI»-Aufgaben startet er je einen Thread hier im Projekt.
   - Der Rest geht als `ki-bot`-Issue an den Bot.
   - Projekte, die länger stillstehen, rutschen nach vorne.
   - Lowland wird nicht verteilt (siehe Tabus).
   - Was Christoph braucht, kommt als kurze Frage in den Bericht.
   - Der Bericht hat immer drei Blöcke: **Erledigt**, **Hängt**, **Nächste Entscheidung von dir** (nur was nach den
     Arbeitsregeln wirklich Christophs ist), dazu der Verbrauch mit Kostenampel.
3. **Tagsüber:** Threads prüfen und mergen die Bot-PRs. Christoph beantwortet Fragen und arbeitet in den Threads.
4. **23:00 und 03:00** KI-Bot: arbeitet die `ki-bot`-Aufgaben im Rahmen des Budgets ab.

## Wöchentlicher Rückblick

Jeden **Sonntag** wertet der Manager seine Arbeit der Woche aus und trägt sie hier ein (neuester Eintrag oben):
was gut funktioniert hat, was nicht so gut lief, und Vorschläge, wie diese Datei angepasst werden könnte.
Er darf auch vorschlagen, Regeln zu streichen.

Im Sonntags-Bericht fragt der Manager Christoph auch, wann sein PC in der kommenden Woche ungefähr morgens und abends
an ist. Die Antwort gilt für die Woche: Fragen und Arbeiten, die den PC brauchen, plant er in diese Zeiten.

### Woche vom 2026-11-02 (2.-8.11., Neustart am 5.11.)
- Erledigt: Bis 4.11. Pause (Christophs Wunsch vom 27.10.), Neustart am 5.11. mit neuem Schwerpunkt (Abstieg,
  Zwergen-Mine, Magic City, Lowland; PR #102). Drei Bot-Nächte: 5./6.11. 10 Aufträge (14.57 USD), 6./7.11. und 7./8.11.
  je 6 Aufträge (5.49 und 5.48 USD), alle 22 als PR, 16 davon geprüft und eingebaut, 6 in Prüfung. Threads am 5./6.11.
  (alles im Repo, auf Christophs Wort ohne Rückfrage gemergt): Magic City #61-#78 (Ebene 11+12, Raid I-III,
  Lehrlinge, Feineichung), Lowland 0.38 auf 0.67 (#105-#142: Welt easy, Hof-Leben, Minigames, Dächer), Der Abstieg
  V29 auf V47 (Schicksal, Pakte, Gönner, Tageswelt), Zwergen-Mine V5 auf V9 (Endboss, Kronen, Runde 2), TrailMate
  #58-#65 geprüft und gemergt. PC-Abgleich am 6.11., seither Pause: Christoph testet, nur der Nacht-Bot arbeitet.
- Kosten: November bis 8.11. 25.54 von 195 USD (Bot), Plan bis heute 52 USD, Ampel grün. Oktober 100.24 von 190.
- Gut gelaufen: Der neue Zuschnitt (je 2 kleine Aufträge je Spiel, Entwürfe mit Datei- und Zeilenangaben) gibt
  saubere PRs von 20-240 Zeilen für 0.3-2 USD; die Prüf-Threads finden die Fehler (Abstieg #68: drei Stücke ohne
  wirksamen Haken) und bessern Daten selbst nach. Der erste Lowland-Bot-PR (#143) kam mit Prüfhäkchen durch. Die
  Entwürfe für die Nacht entstehen mit vier parallelen Helfern in rund acht Minuten.
- Nicht gut gelaufen: In Auftrag #116 standen Zahlen, die im Spiel nicht aufgehen (Leben-Malus verschwindet ab
  Ebene 2, Glück wirkt nirgends); Lehre: Haken nur mit Werten, die das Spiel wirklich rechnet. Der Supabase-
  Wachhalter ist seit 31.10. rot (TAEHRON und TrailMate antworten nicht), gemeldet erst am 7.11. Der PC war morgens
  meist aus, die Karten kommen dann einen Tag später. Alle Spiele sind am PC ungespielt, bis Christoph testet.
- Nächste Woche anders: Wachhalter-Fehler jeden Morgen prüfen und beim ersten Mal melden. Abstieg-Aufträge nur mit
  Werten aus `derived`. Während der Pause bleibt die Morgen-Planung bei einer Zeile plus Bot-Prüfung.
- Vorschläge an Christoph (ändern oder streichen):
  1. **Daten-Korrekturen beim Prüfen:** Ein Prüf-Thread darf in einem Bot-PR kleine Daten- oder Textfehler (bis etwa
     10 Zeilen) selbst korrigieren und dann mergen, statt den Bot nochmals zu bemühen oder zu fragen. So lief es am
     7.11. bei Abstieg #68; als Regel unter «Arbeitsregeln» festhalten.
  2. **Wachhalter mit Meldung:** Schlägt der Supabase-Wachhalter zweimal hintereinander fehl, steht es automatisch im
     nächsten Morgen-Bericht unter «Hängt» (Regel unter «Tagesablauf»).
  3. Die zwei Vorschläge vom 25.10. (Projektkarte nur im Inventar, TrailMate-Datenbank über GitHub) warten weiter.

### Woche vom 2026-10-19 (19.-25.10.)
- Erledigt: Lowland mit Schwerpunkt Leistung und lesbare Kämpfe (seit 21.10.) von 0.29 auf 0.36.1: Loot-Sets,
  Turm-Gegner, Startgebiet, Geheimräume mit Truhen, Agents nach Thema mit Prüfung je PR, rote Schweife an
  Gegner-Geschossen, Vorwärmen gegen Ruckler beim ersten Effekt. Magic City, 30 PRs (#15-#44): Karte nach oben
  mit vier neuen Dungeons, Geschichten, Rivalen, Schmiede und Gildenhaus (#29), Umbau zur Gildenstadt (#39),
  Christophs Umbau ohne Baupläne (#43) mit Neueichung (#44), dazu Monsterbuch, Fundbuch und Helden-Ausbildung vom
  Bot. TrailMate, 25 PRs (#14-#38) auf main (u. a. Benachrichtigungen, Profile, Personensuche, Touren teilen,
  Live-Standort, Sicherheit), #39-#43 in Prüfung. Zwergen-Mine Version 5, Der Abstieg bis Version 28 (seit 21.10.
  Pause). Ideenkarte stand still (Bot-Token ohne Schreibrecht). Threads laufen auf Opus mit Leistung max.
  Bot-Zeitplan seit 25.10. sommer- und winterzeitfest.
- Kosten: 58.20 USD von 190 USD (Bot, 42 Aufgaben: Magic City 17 für 34.20, TrailMate 25 für 24.00). Monat bis
  24.10.: 75.16 USD, Ampel grün. Threads über das Max-Abo.
- Gut gelaufen: Der Bot war gut ausgelastet (22.-24.10. 80, 91 und 53 % des Tagesbudgets). Die Threads prüfen und
  mergen seine PRs selbst und finden die Fehler vor dem Merge (Magic City 56 Befunde in #40-#42, TrailMate ein
  Testfehler in #35). Die Lowland-Morgensession arbeitet den Kampf-Plan Schritt für Schritt ab. PC-Updates ohne
  Remote Control (per Bundle) haben funktioniert.
- Nicht gut gelaufen: Mein Auftrag «gern grössere Aufgaben» (21./22.10.) gab Bot-PRs mit 650-1500 Zeilen statt
  höchstens 300; schwer zu prüfen, und am 23.10. blieb der 23:00-Lauf leer. Seit 23.10. wieder klein. Der
  Magic-City-Thread hängt seit Sa 24.10. 07:15 an einer Lösch-Erlaubnis am PC: #45/#46 ungeprüft, keine neuen
  Magic-City-Aufgaben, in der Nacht 24./25.10. nur 5 Aufgaben statt mindestens 6. Gemerkt habe ich es erst am
  Sonntag. Seit dem Ende der Sommerzeit lief der Bot eine Stunde zu früh. Vieles wartet auf Christoph:
  TrailMate-Datenbankregeln 012-025 (seit 22.10.), TAEHRON «Restore project» (Wachhalter rot seit 17.10.),
  Ideenkarte-Token, Zahlen zu Magic-City-Bildern, Lowland und Zwergen-Mine.
- Nächste Woche anders: Jeden Morgen prüfen, ob ein Thread hängt (offene Erlaubnis-Frage, Fehler), und es sofort
  melden. Erlaubnis-Fragen am PC nur in Christophs PC-Zeiten stellen; bleibt eine bis zum Ende der PC-Zeit offen,
  wird sie abgebrochen, und der Thread arbeitet ohne PC weiter. Fällt ein Projekt als Lieferant aus, füllt ein
  anderer Thread die Nacht auf mindestens 6 Aufgaben auf.
- Vorschläge an Christoph (ändern oder streichen):
  1. **Projektkarte nur noch im Inventar:** projekt.json liegt auch in den Repos Aufbauspiel-New, Trailmate und
     Ideenkarte. Weil der Manager sie jeden Morgen auf dem PC auffrischt, sieht es dort aus, als hätte Christoph
     etwas geändert, und PC-Updates stocken. Vorschlag: In diesen Repos die Datei aus Git nehmen und ignorieren;
     die Karte lebt im Manager-Repo (`inventar/`) und als Kopie im Projektordner, die Ideenkarte liest sie wie bisher.
  2. **TrailMate-Datenbank über GitHub:** Neue Datenbankregeln spielt nach dem Merge eine GitHub Action ins
     Supabase-Projekt ein (wie der Wachhalter), statt auf einen Text am PC zu warten. Christoph trägt dafür einmal
     ein Geheimnis im Repo Trailmate ein; der TrailMate-Thread baut die Action und erklärt die Schritte.

### Woche vom 2026-10-15 (erste Woche, 15.-18.10.)
- Erledigt: Morgen-Manager, KI-Bot und Supabase-Wachhalter laufen. Lowland: rund 30 Grafik-PRs (#11-#42) und
  der Baumodus. TrailMate: PR #1-#13, Supabase-Projekt läuft. Ideenkarte: Etappe 2, MD-Liste, Version 0.2.1.
  Magic City wieder aktiv, Gebäude-Idee B+C entschieden, erste 5 Bot-PRs. TAEHRON: Marketing-Plan und erste
  Wochenauswertung. Moneyprojekt: Pino-Linie und erste Erwachsenen-Kurzgeschichte mit 5 Shorts.
  YouTube-Geschichten eingestellt.
- Kosten: 12.44 USD von 190 USD (Bot), Threads über das Max-Abo.
- Gut gelaufen: Threads liefern viel und mergen selbst; seit dem Fix vom 17.10. laufen die Bot-Läufe sauber durch.
- Nicht gut gelaufen: Der Bot lag drei Tage weit unter dem Budget, weil zu wenige Issues bereit waren.
  Der Lauf vom 16.10. war rot (Budget-Push). Der PC war zweimal morgens aus. Ich habe einmal nach dem Mergen
  von PRs gefragt, die schon gemergt waren. Der Wachhalter erreichte TAEHRON am 17.10. abends nicht.
- Nächste Woche anders: Jeden Morgen genug `ki-bot`-Issues bereitstellen, dass beide Nachtläufe voll werden.
  Vor jeder Frage an Christoph den Stand frisch prüfen.
- Vorschläge an Christoph (ändern oder streichen):
  1. **Bot-Vorrat:** Neue Regel unter Budget: «Der Morgen-Manager sorgt dafür, dass für die Nacht mindestens
     6 `ki-bot`-Issues bereit sind. Issues, die auf einen PR warten, bekommen das Label erst nach dem Merge.»
  2. **Wer merged:** In «Rollen» bei Christoph «merged PRs» streichen. Bot-PRs prüft und merged am Morgen ein
     Thread. Christoph bekommt einen PR nur bei offenen Fragen. Label `in-review` heisst dann «wartet auf Prüfung».
  3. **Hilfstools:** Die Zeile «GitHub-Stand holen» korrigieren. Die .bat verbindet die bestehenden Ordner mit
     GitHub, sie klont nicht nach Dokumente\GitHub.
- Christoph 18.10.: Alle drei Vorschläge genehmigt und oben eingetragen. PC diese Woche an: morgens ca. 08:00,
  abends ca. 21:00-22:00.

<!-- Vorlage:
### Woche vom JJJJ-MM-TT
- Erledigt: …
- Kosten: … USD von … USD
- Gut gelaufen: …
- Nicht gut gelaufen: …
- Nächste Woche anders: …
- Vorschläge an Christoph (ändern oder streichen): …
-->
