#!/usr/bin/env python3
"""
Oberflächlicher Trend-Finder
Holt aktuelle Google Trends (Daily Trending Searches)
"""

from pytrends.request import TrendReq
import pandas as pd
from datetime import datetime
import time

# ============================================
# Einstellungen
# ============================================
GEO = "DE"          # "DE" = Deutschland, "AT" = Österreich, "CH" = Schweiz, "" = weltweit
LANGUAGE = "de-DE"  # Sprache der Trends
TIMEZONE = 60       # UTC+1 (Mitteleuropa)
MAX_TRENDS = 20     # Wie viele Trends angezeigt werden sollen


def get_trending_searches(geo: str = GEO) -> pd.DataFrame:
    """Holt die aktuellen Daily Trending Searches"""
    pytrends = TrendReq(hl=LANGUAGE, tz=TIMEZONE)
    
    try:
        df = pytrends.trending_searches(pn=geo if geo else "united_states")
        # pn erwartet Ländername auf Englisch bei manchen Versionen, 
        # deshalb Fallback auf geo-Code
        return df
    except Exception:
        # Fallback: explizit mit geo-Code
        pytrends = TrendReq(hl=LANGUAGE, tz=TIMEZONE)
        df = pytrends.trending_searches(pn="germany" if geo == "DE" else "united_states")
        return df


def get_related_and_rising(keyword: str, geo: str = GEO):
    """Zeigt Related Queries und Rising Searches zu einem Keyword"""
    pytrends = TrendReq(hl=LANGUAGE, tz=TIMEZONE)
    
    pytrends.build_payload([keyword], cat=0, timeframe="now 7-d", geo=geo, gprop="")
    
    related = pytrends.related_queries()
    
    print(f"\n{'='*60}")
    print(f"  Related & Rising zu: '{keyword}'")
    print(f"{'='*60}")
    
    # Top Related
    top = related[keyword]["top"]
    if top is not None and not top.empty:
        print("\nTop Related Queries:")
        print(top.head(10).to_string(index=False))
    else:
        print("\nKeine Top Related Queries gefunden.")
    
    # Rising
    rising = related[keyword]["rising"]
    if rising is not None and not rising.empty:
        print("\nRising Searches (steigend):")
        print(rising.head(10).to_string(index=False))
    else:
        print("\nKeine Rising Searches gefunden.")


def main():
    print("\n" + "="*60)
    print("  OBERFLÄCHLICHER TREND-FINDER")
    print("  Google Trends Daily Searches")
    print("="*60)
    print(f"Zeitpunkt : {datetime.now().strftime('%d.%m.%Y %H:%M:%S')}")
    print(f"Region    : {GEO if GEO else 'Weltweit'}")
    print("-"*60)

    # 1. Aktuelle Trends holen
    try:
        trends_df = get_trending_searches(GEO)
        
        print(f"\nTop {min(MAX_TRENDS, len(trends_df))} aktuelle Trends:\n")
        
        for i, trend in enumerate(trends_df[0].head(MAX_TRENDS), 1):
            print(f"{i:2d}.  {trend}")
            
    except Exception as e:
        print(f"\nFehler beim Abrufen der Trends: {e}")
        print("Tipp: Internetverbindung prüfen oder später nochmal versuchen.")
        return

    # 2. Optional: Detail-Analyse zu einem Keyword
    print("\n" + "-"*60)
    keyword = input("\nMöchtest du Related/Rising zu einem Keyword sehen?\n"
                    "(Einfach Enter drücken zum Beenden, oder Keyword eingeben): ").strip()
    
    if keyword:
        try:
            get_related_and_rising(keyword, GEO)
        except Exception as e:
            print(f"Fehler bei Related Queries: {e}")

    print("\n" + "="*60)
    print("Fertig. Viel Erfolg beim Trend-Spotten!")
    print("="*60 + "\n")


if __name__ == "__main__":
    main()