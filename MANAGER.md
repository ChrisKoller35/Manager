# Manager – Regelwerk

Diese Datei ist das Regelwerk für den Morgen-Manager und den KI-Bot. Beide lesen sie bei jedem Lauf.
Änderungen an den Regeln macht nur Christoph oder Claude nach Christophs Okay.

## Rollen

| Wer | Was |
|---|---|
| **Christoph** | Entscheidet, was gebaut wird, merged PRs, macht alles, was seinen PC oder seine Konten braucht. |
| **Manager** (Claude im Projekt «Manager Claude») | Plant jeden Morgen, verteilt Aufgaben, berichtet Christoph, pflegt Inventar und dieses Regelwerk. |
| **KI-Bot** (GitHub Actions mit API-Guthaben) | Arbeitet nachts die `ki-bot`-Aufgaben ab, jede als eigener PR. |
| **Threads im Projekt** | Arbeit, bei der Christoph mitredet (Ideenkarte-Etappen, Lowland-Morgensession, Content). |

## Aufgaben (Issues in diesem Repo)

- Erste Zeile im Text: `Repo: ChrisKoller35/<name>`.
- Label `ki-bot`: Der Bot kann die Aufgabe allein lösen. Sie ist klar umrissen, testbar und passt in einen PR.
- Label `für-projekt`: Christoph muss entscheiden, sein PC wird gebraucht, oder ein Thread im Projekt übernimmt.
- Label `in-review`: Der PR ist offen und wartet auf Christoph.

## Budget

- Monatlich 190 USD für den Bot (`budget.json`). Das Console-Limit liegt bei 200 USD, die Differenz ist der Puffer.
- Das Tagesbudget ist der Rest des Monats geteilt durch die verbleibenden Tage. Was übrig bleibt, wird übertragen.
- Der Bot hört auf, wenn das Tagesbudget erreicht ist. Der Manager plant pro Tag nur so viele Aufgaben, wie hineinpassen.

## Erlaubte Repos für den Bot

Trailmate, lowland, MoneyProjekttry, Ideenkarte (Liste `ERLAUBTE_REPOS` in `.github/workflows/ki-bot.yml`).
Ein neues Repo kommt erst nach Christophs Okay dazu.

## Tabus

- **SpellManager** (D-D-Zauberapp): Wird nie angefasst, nur mit Christoph zusammen.
- Nie auf `main` eines Projekt-Repos pushen, nie selbst mergen. Das macht immer Christoph.
- Keine Schlüssel oder Passwörter in Dateien, Issues oder im Chat.
- **Lowland:** Nichts planen, was die Morgensession um 06:30 schon macht.
- **Moneyprojekt:** Ideen, Planung und Marketing nur mit Claude Fable 5.1 (mindestens Effort mittel). Der Bot macht dort nur klar definierte Umsetzungsschritte.

## Ablauf eines Tages

1. **06:30** Lowland-Morgensession (eigenes Projekt).
2. **07:12** Morgen-Manager: liest dieses Regelwerk, das Inventar, das Budget und die Issues, prüft, was über Nacht passiert ist, legt neue Aufgaben an und schickt Christoph einen kurzen Bericht.
3. **Tagsüber:** Christoph merged PRs, beantwortet Fragen und arbeitet in den Threads.
4. **23:00 und 03:00** KI-Bot: arbeitet die `ki-bot`-Aufgaben im Rahmen des Budgets ab.

## Wöchentlicher Rückblick

Jeden Montag ergänzt der Manager hier einen Eintrag (neuester oben): was gut lief, was nicht, was er an seinem
Vorgehen ändert. Regeländerungen schlägt er Christoph vor und trägt sie erst nach dessen Okay oben ein.

<!-- Vorlage:
### Woche vom JJJJ-MM-TT
- Erledigt: …
- Kosten: … USD von … USD
- Gut gelaufen: …
- Nicht gut gelaufen: …
- Nächste Woche anders: …
- Regelvorschlag an Christoph: …
-->
