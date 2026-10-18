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

- Monatlich 190 USD für den Bot (`budget.json`). Das Console-Limit liegt bei 200 USD.
- Das Tagesbudget ist der Rest des Monats geteilt durch die verbleibenden Tage. Was übrig bleibt, wird übertragen.
- Der Bot hört auf, wenn das Tagesbudget erreicht ist. Der Manager plant pro Tag nur so viele Aufgaben, wie hineinpassen.
- Das Guthaben soll genutzt werden. Der Morgen-Manager vergleicht jeden Morgen den Verbrauch der
  letzten Tage mit dem Tagesbudget. Bleibt der Bot **3 Tage in Folge unter 50 %**, gibt er ihm mehr oder grössere Aufgaben
  (mehr `ki-bot`-Issues, grössere Pakete, bei Bedarf `MAX_AUFGABEN` im Workflow erhöhen), bis das Budget genutzt wird.
- **Bot-Vorrat** (seit 18.10.2026): Der Morgen-Manager sorgt dafür, dass für die Nacht mindestens 6 `ki-bot`-Issues
  bereit sind. Issues, die auf einen PR warten, bekommen das Label erst nach dem Merge.
- Der Verbrauch (gestern, Monat, Tagesbudget) steht in jedem Morgen-Bericht.
- **Kostenampel:** Ab 70 % des Monatsbudgets ist der Bericht gelb, und der Bot bekommt nur noch kleine Aufgaben.
  Ab 90 % ist er rot, und der Bot stoppt bis zum Monatswechsel (keine neuen `ki-bot`-Issues).

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
- **Lowland:** Schwerpunkt ist jetzt Look und Grafik: Das Spiel soll insgesamt besser aussehen,
  woran genau gearbeitet wird, entscheidet die Session selbst. Ideen sammelt `docs/GRAFIK.md` im Repo lowland. Kein
  neuer Content, bis Christoph mit dem Aussehen zufrieden ist. Danach geht es wieder mit Content weiter. Wenn das
  Aussehen nicht mehr sinnvoll besser werden kann, sagt der Manager oder die Morgensession es Christoph.
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
