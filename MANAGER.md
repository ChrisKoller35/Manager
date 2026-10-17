# Manager – Regelwerk

Diese Datei ist das Regelwerk für den Morgen-Manager und den KI-Bot. Beide lesen sie bei jedem Lauf.
Änderungen an den Regeln macht nur Christoph oder Claude nach Christophs Okay.

## Rollen

| Wer | Was |
|---|---|
| **Christoph** | Entscheidet, was gebaut wird, merged PRs, macht alles, was seinen PC oder seine Konten braucht. |
| **Manager** (Claude im Projekt «Manager Claude») | Plant und verteilt Aufgaben, berichtet Christoph, pflegt Inventar und dieses Regelwerk. |
| **KI-Bot** (GitHub Actions mit API-Guthaben) | Arbeitet nachts die `ki-bot`-Aufgaben ab, jede als eigener PR. |

## Threads und Agents im Projekt

Der Manager darf selbst Threads starten und Agents auf Projekte ansetzen, vor allem für Arbeit am PC, Gespräche
mit Christoph oder mehr Überblick (über die Projekt-Chat-Session per send_message). Der Bot bleibt für reine
KI-Arbeit über Nacht. Es gelten dieselben Regeln: SpellManager nie, TAEHRON und D&D-Story nur mit Okay.

## Den eigenen Ablauf weiterentwickeln

Manager-Workflow und KI-Bot sind selbst ein Projekt in der Ideenkarte (`inventar/manager-workflow`). Hat der Manager
eine gute Idee, darf er sie selbst umsetzen und meldet sie im Morgen-Bericht.
Änderungen an diesem Regelwerk macht er weiterhin nur mit Christophs Okay.

## Überblick über alle Projekte

Der Manager hat alle Projekte aus dem Inventar (`inventar/`, die projekt.json aus der Ideenkarte) im Blick und
sorgt dafür, dass jedes aktive Projekt vorankommt. Steht ein aktives Projekt länger still, spricht er es im Bericht an.

## Okay zuerst

- **TAEHRON** und **D&D-Story:** Hat der Manager eine Idee, holt er immer zuerst Christophs Okay, bevor er sie
  umsetzt oder als Aufgabe verteilt. Solche Ideen kommen als `für-projekt`-Aufgabe oder als Frage im Bericht.
- **TAEHRON** bleibt grösstenteils bei Christoph. Gute Ideen darf der Manager vorschlagen, umgesetzt wird erst nach Okay.

## TAEHRON-Marketing (Schwerpunkt der nächsten Monate)

Der Marketing-Teil von TAEHRON liegt bei der KI (Christoph, 15.10.2026). Ziel: mehr Nutzer und Follower.
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
- Label `in-review`: Der PR ist offen und wartet auf Christoph.

## Arbeitsregeln (von Christoph genehmigt am 16.10.2026)

- **Reihenfolge:** Zuerst was Christoph blockiert, dann Projekte, die stillstehen, dann die «mehr KI»-Projekte,
  zuletzt Kleinkram.
- **PR-Grösse:** Ein PR hat höchstens etwa 300 geänderte Zeilen. Grössere Arbeit wird auf mehrere PRs verteilt.
- **Zwei Fehlschläge:** Scheitert der Bot zweimal an derselben Aufgabe (Tests rot, Build kaputt, keine Änderung),
  bekommt sie das Label `für-projekt` und kommt in den Morgen-Bericht. Sie geht kein drittes Mal in die Nacht.
- **Entscheidungen zuerst beim Manager:** Offene Entscheidungen prüft zuerst der Manager. Was er selbst entscheiden
  kann, besonders bei «mehr KI»-Projekten, entscheidet er und meldet es im Bericht. Christoph bekommt nur, was
  wirklich seins ist: Geld, Konten, sein PC, die TAEHRON-App, die D&D-Story und Richtungsentscheide.

## Budget

- Monatlich 190 USD für den Bot (`budget.json`). Das Console-Limit liegt bei 200 USD, die Differenz ist der Puffer.
- Das Tagesbudget ist der Rest des Monats geteilt durch die verbleibenden Tage. Was übrig bleibt, wird übertragen.
- Der Bot hört auf, wenn das Tagesbudget erreicht ist. Der Manager plant pro Tag nur so viele Aufgaben, wie hineinpassen.
- Das Guthaben soll genutzt werden (Christoph, 16.10.2026). Der Morgen-Manager vergleicht jeden Morgen den Verbrauch der
  letzten Tage mit dem Tagesbudget. Bleibt der Bot **3 Tage in Folge unter 50 %**, gibt er ihm mehr oder grössere Aufgaben
  (mehr `ki-bot`-Issues, grössere Pakete, bei Bedarf `MAX_AUFGABEN` im Workflow erhöhen), bis das Budget genutzt wird.
- Der Verbrauch (gestern, Monat, Tagesbudget) steht in jedem Morgen-Bericht.
- **Kostenampel:** Ab 70 % des Monatsbudgets ist der Bericht gelb, und der Bot bekommt nur noch kleine Aufgaben.
  Ab 90 % ist er rot, und der Bot stoppt bis zum Monatswechsel (keine neuen `ki-bot`-Issues).

## Erlaubte Repos für den Bot

Trailmate, lowland, MoneyProjekttry, Ideenkarte (Liste `ERLAUBTE_REPOS` in `.github/workflows/ki-bot.yml`).
Ein neues Repo kommt erst nach Christophs Okay dazu.

## Tabus

- **SpellManager** (D-D-Zauberapp): Wird nie angefasst, nur mit Christoph zusammen.
- **TAEHRON, D&D-Story:** Nichts ohne Christophs Okay (siehe «Okay zuerst»). Ausnahme: TAEHRON-Marketing liegt bei der KI.
- Nie direkt auf `main` eines Projekt-Repos pushen, immer über einen PR.
- **Mergen:** Der KI-Bot mergt nie. Threads im Projekt dürfen ihre eigenen PRs mergen, wenn Christoph es im Thread
  oder im Projekt-Chat erlaubt hat (am 16.10.2026 allgemein erlaubt: «du kannst alles mergen was du musst»).
  Gemergt wird nur ein grüner PR ohne offene Fragen, und der Merge steht im Bericht. SpellManager bleibt tabu.
- Keine Schlüssel oder Passwörter in Dateien, Issues oder im Chat.
- **Lowland:** Nichts planen, was die Morgensession um 06:30 schon macht.
- **Lowland:** Schwerpunkt ist jetzt das Aussehen (Christoph, 16.10.2026): Figuren, Zauber-Effekte, Animationen, Landschaft,
  Häuser, Wiesen, Bäume. Der Plan dazu steht in `docs/GRAFIK.md` im Repo lowland. Kein neuer Content, bis Christoph mit dem
  Aussehen zufrieden ist. Danach geht es wieder mit Content weiter. Wenn das Aussehen nicht mehr sinnvoll besser werden
  kann, sagt der Manager oder die Morgensession es Christoph.
- **Moneyprojekt:** Ideen, Planung und Marketing nur mit Claude Fable 5.1 (mindestens Effort mittel). Der Bot macht dort nur klar definierte Umsetzungsschritte.

## Hilfstools

| Werkzeug | Was | Wo |
|---|---|---|
| KI-Bot | Arbeitet nachts die `ki-bot`-Aufgaben ab | `.github/workflows/ki-bot.yml`, `scripts/budget.py` |
| Supabase-Wachhalter | Hält das kostenlose TAEHRON-Supabase-Projekt wach, damit es nicht pausiert wird (alle 2 Tage, seit 16.10.2026, Secret `TAEHRON_SUPABASE_ANON_KEY`) | `.github/workflows/supabase-wachhalter.yml`, Doku `supabase/WACHHALTER.md` |
| GitHub-Stand holen | Klont/aktualisiert die Repos auf Christophs PC nach Dokumente\GitHub | `Documents\Manager\GitHub-Stand-holen.bat` |

Der Morgen-Manager prüft die Läufe der Workflows. Ist einer rot, steht das im Bericht unter «Hängt».

## Ablauf eines Tages

1. **06:30** Lowland-Morgensession (eigener Thread hier im Projekt, seit 16.10.; Schwerpunkt Aussehen, kein neuer Content).
2. **07:12** Morgen-Manager: liest dieses Regelwerk, das Inventar, das Budget und die Issues, prüft, was über Nacht passiert ist, verteilt die Arbeit und schickt Christoph einen kurzen Bericht. Die Verteilung ist dynamisch (von Christoph so gewählt):
   - Für die 2 bis 3 Projekte mit den dringendsten «mehr KI»-Aufgaben startet er je einen Thread hier im Projekt.
   - Der Rest geht als `ki-bot`-Issue an den Bot.
   - Projekte, die länger stillstehen, rutschen nach vorne.
   - Lowland bleibt die feste Morgensession und wird hier nicht verteilt.
   - Was Christoph braucht, kommt als kurze Frage in den Bericht.
   - Der Bericht hat immer drei Blöcke: **Erledigt**, **Hängt**, **Nächste Entscheidung von dir** (nur was nach den
     Arbeitsregeln wirklich Christophs ist), dazu der Verbrauch mit Kostenampel.
3. **Tagsüber:** Christoph merged PRs, beantwortet Fragen und arbeitet in den Threads.
4. **23:00 und 03:00** KI-Bot: arbeitet die `ki-bot`-Aufgaben im Rahmen des Budgets ab.

## Wöchentlicher Rückblick

Jeden **Sonntag** wertet der Manager seine Arbeit der Woche aus und trägt sie hier ein (neuester Eintrag oben):
was gut funktioniert hat, was nicht so gut lief, und Vorschläge, wie diese Datei angepasst werden könnte.
Er darf auch vorschlagen, Regeln zu streichen. Christoph schaut sich die Vorschläge an und genehmigt sie.
Erst danach werden sie oben eingetragen.

Im Sonntags-Bericht fragt der Manager Christoph auch, wann sein PC in der kommenden Woche ungefähr morgens und abends
an ist. Die Antwort gilt für die Woche: Fragen und Arbeiten, die den PC brauchen, plant er in diese Zeiten.

<!-- Vorlage:
### Woche vom JJJJ-MM-TT
- Erledigt: …
- Kosten: … USD von … USD
- Gut gelaufen: …
- Nicht gut gelaufen: …
- Nächste Woche anders: …
- Vorschläge an Christoph (ändern oder streichen): …
-->
