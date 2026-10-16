-- Einmal im Supabase-Dashboard unter SQL Editor ausführen (pro Projekt).
-- Kleine Lese-Funktion für den Wachhalter: liest nur die Uhrzeit der
-- Datenbank, schreibt nichts und gibt keine Daten preis.
create or replace function public.wachhalter()
returns timestamptz
language sql
stable
as $$ select now() $$;

grant execute on function public.wachhalter() to anon;

select public.wachhalter();
