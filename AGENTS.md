GEMINI.md - Projekt: Azubi Urlaubs-Planer (Sachsen)
1. Projektübersicht

Dieses Programm hilft einem Auszubildenden im 2. Lehrjahr in Sachsen, seine begrenzten Urlaubstage (20 Tage/Jahr) optimal zu nutzen. Die Planung ist durch den ständigen Wechsel zwischen Berufsschule (Turnus) und Betrieb sowie unregelmäßige Brückentage hochkomplex.

Ziel: Ein Python-Programm, das unter Berücksichtigung von festen Blockern (Schule) und Feiertagen den "Highscore" für Urlaubszeiträume berechnet.
2. Rolle der KI (Dein Auftrag)

Die KI dient als Senior-Entwickler-Partner und Code-Generator.

    Keine Kernlogik-Entscheidung: Die KI soll nicht selbst raten, wann Urlaub gut wäre (Vermeidung von Halluzinationen bei Datumsberechnungen).

    Algorithmus-Design: Die KI schreibt deterministischen Python-Code, der mathematisch präzise auf einer Master-Timeline rechnet.

    CLI-Interface: Unterstützung beim Bau des interaktiven Setup-Wizards.

3. Festgelegte Design-Entscheidungen (Architektur)
A. Datenstruktur: Die Master-Timeline

Wir verwenden ein Dictionary (oder eine Liste von Objekten), wobei die Keys datetime.date-Objekte des gesamten Jahres sind.

    Layer-Prinzip: Erst Grundierung (Wochenenden), dann Feiertage (Sachsen-spezifisch), dann Schul-Blocker, dann feste Urlaubspläne.

    Jeder Tag hat einen Typ: WORK, SCHOOL, WEEKEND, HOLIDAY, FIXED_VACATION, PROPOSED_VACATION.

B. Daten-Input (Schnittstellen)

    Feiertage: Nutzung der Python-Library holidays (Sachsen/DE).

    Schulplan: Import via schulplan.csv (Format: Startdatum;Enddatum;Typ), da Turnus-Zeiten unregelmäßig sind.

    Konfiguration: config.json speichert User-Präferenzen (Resturlaub, Sparmodus, Gewichtungen).

C. Das Gewichtungssystem (Scoring)

Anstatt starrer Regeln nutzt das Programm ein Punktesystem. Der User priorisiert Regeln (z. B. 2-1-3), die in Multiplikatoren umgerechnet werden:

    Regeln: Brückentage nutzen, lange Blöcke bevorzugen, Einzeltage vermeiden, Sommer-Prio, Sparmodus (Reserve behalten).

D. Technischer Stack

    Sprache: Python 3.x

    Deployment: Optionaler Docker-Container für eine saubere Umgebung.

    Keine lokale LLM-Integration für Berechnungen (wegen Performance und Zuverlässigkeit auf Standard-Hardware).

4. Prioritäten für die nächsten Schritte

    Datenmodell: Definition der Day-Klasse oder Struktur.

    File-Parser: CSV-Reader für den Schulplan bauen.

    Calendar-Builder: Logik zur Erstellung des Master-Kalenders inkl. Feiertags-Integration.