# Manager-Bot

Arbeitsteilung (von Christoph am 15.10.2026 freigegeben):

- **Manager** läuft im Claude-Projekt «Manager Claude», einmal am Morgen. Er liest alle `projekt.json`
  und die GitHub-Aktivität und legt hier Issues an:
  - Label `ki-bot`: Der KI-Bot arbeitet die Aufgabe ab. Die erste Zeile im Text ist `Repo: ChrisKoller35/<name>`.
  - Label `für-projekt`: Die Aufgabe ist für Christoph oder für einen Thread im Projekt.
- **KI-Bot** (`.github/workflows/ki-bot.yml`) läuft nachts. Er nimmt das älteste `ki-bot`-Issue und
  öffnet dafür einen PR im Ziel-Repo, danach bekommt das Issue das Label `in-review`.

## Inventar

`inventar/PROJEKTE.md` ist die Übersicht, `inventar/<id>/projekt.json` sind Kopien der Dateien aus den Projektordnern.

## Regeln

- Der Bot arbeitet nur in Repos aus `ERLAUBTE_REPOS`, öffnet immer einen PR, merged nie und pusht nie auf `main`.
- Der SpellManager ist tabu.
- Budget: 190 USD pro Monat (`budget.json`), aufgeteilt auf die Tage, was übrig bleibt, wird übertragen (`scripts/budget.py`).
  Das Monatslimit in der Claude Console (200 USD) ist die Notbremse.

## Einrichten (einmalig, Christoph)

1. Repo `Manager` anlegen (erledigt, Dateien hat Claude hochgeladen).
2. Secret `ANTHROPIC_API_KEY` anlegen (Claude Console, API Keys).
3. Secret `BOT_GITHUB_TOKEN` anlegen: ein Fine-grained Token mit Zugriff nur auf `Manager`, `Trailmate`, `lowland` und `MoneyProjekttry` (die freigegebenen
   Repos). Rechte: Contents (lesen und schreiben), Pull requests (lesen und schreiben), Issues (lesen und schreiben).
4. Labels `ki-bot`, `für-projekt` und `in-review` anlegen.
5. Unter «Actions» den KI-Bot einmal von Hand starten («Run workflow»), um ihn zu testen.
