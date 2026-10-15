"""Tagesbudget mit Uebertrag fuer den KI-Bot.

frei   -> heute noch verfuegbare USD: (Monatsbudget - vor heute verbraucht) / verbleibende Tage inkl. heute,
          minus was heute schon gebucht ist. Was an frueheren Tagen liegen blieb, steckt so automatisch drin.
buchen <usd> <notiz> -> Ausgabe eintragen.
stand  -> eine Zeile fuer den Bericht.
"""
import calendar
import datetime
import json
import sys
from pathlib import Path

DATEI = Path(__file__).resolve().parent.parent / "budget.json"


def laden():
    return json.loads(DATEI.read_text(encoding="utf-8"))


def speichern(d):
    DATEI.write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def rechnen(d, heute):
    monat = heute.strftime("%Y-%m")
    monats_usd = d["monatsbudget_chf"] * d["usd_pro_chf"]
    diesen_monat = [a for a in d["ausgaben"] if a["datum"].startswith(monat)]
    vor_heute = sum(a["usd"] for a in diesen_monat if a["datum"] < heute.isoformat())
    heute_usd = sum(a["usd"] for a in diesen_monat if a["datum"] == heute.isoformat())
    tage_rest = calendar.monthrange(heute.year, heute.month)[1] - heute.day + 1
    tagesbudget = max(0.0, (monats_usd - vor_heute) / tage_rest)
    return {
        "monats_usd": monats_usd,
        "verbraucht_usd": vor_heute + heute_usd,
        "tagesbudget_usd": tagesbudget,
        "frei_usd": max(0.0, tagesbudget - heute_usd - d.get("reserve_usd", 0)),
    }


def main():
    heute = datetime.date.today()
    d = laden()
    befehl = sys.argv[1] if len(sys.argv) > 1 else "stand"
    if befehl == "frei":
        print(f"{rechnen(d, heute)['frei_usd']:.2f}")
    elif befehl == "buchen":
        d["ausgaben"].append(
            {"datum": heute.isoformat(), "usd": round(float(sys.argv[2]), 4), "notiz": " ".join(sys.argv[3:])}
        )
        speichern(d)
    elif befehl == "stand":
        r = rechnen(d, heute)
        print(
            f"Verbraucht diesen Monat: {r['verbraucht_usd']:.2f} von {r['monats_usd']:.2f} USD, "
            f"Tagesbudget heute {r['tagesbudget_usd']:.2f} USD"
        )
    else:
        sys.exit(f"Unbekannter Befehl: {befehl}")


if __name__ == "__main__":
    main()
