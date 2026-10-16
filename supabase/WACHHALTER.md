# Supabase-Wachhalter

Supabase pausiert Gratisprojekte nach einer Woche mit zu wenig Datenbank-Aktivität
([Supabase-Doku](https://supabase.com/docs/guides/platform/free-project-pausing)).
Der Workflow `.github/workflows/supabase-wachhalter.yml` liest darum alle 2 Tage eine Zeile aus
einer kleinen Tabelle (echte Datenbank-Abfrage, nicht nur ein Verbindungstest). Schlägt es fehl,
ist der Lauf unter Actions rot.

## Ein Projekt einrichten

1. GitHub, Repo Manager > **Settings > Secrets and variables > Actions > New repository secret**:
   Name `<PROJEKT>_SUPABASE_ANON_KEY`, Wert = **anon public** Key des Supabase-Projekts
   (Supabase-Dashboard > Project Settings > API Keys; nicht den `service_role`/`secret`-Key).
2. In der Workflow-Datei unter `matrix.include` einen Eintrag mit `projekt`, `url` (Project URL)
   und `tabelle` (eine kleine Tabelle, die es im Projekt gibt) ergänzen.
3. Hat das Projekt noch keine Tabelle: `wachhalter.sql` im Supabase **SQL Editor** ausführen,
   dann nutzt der Workflow automatisch die Funktion `wachhalter()`.
4. **Actions > Supabase-Wachhalter > Run workflow** einmal von Hand starten, grün = fertig.

Eingerichtet: TAEHRON (Tabelle `entitlements`, Key liegt in der TAEHRON-App in `.env.local`).
