# bs1-melodeiprogrammierer

Programm, um ein PBASIC-Programm für den BASIC Stamp 1 automatisiert zu schreiben.

## Zweck und Funktionsweise
Das erzeugte PBASIC-Programm lässt eine Melodei erklingen und automatisiert die Zuordnung von Tönen zu PBASIC-spezifischen Tonnummern.

* GROSSBUCHSTABEN entsprechen erhöhten Halbtönen, z.B. C = cis
* x bezeichnet ganz kurze Pausen zwischen Tönen, wie zwischen zwei gleichen Tönen
* Leerzeichen bezeichnet Pausen

### Zuordnungstabelle der Töne
| Ton     | c | cis / des | d | dis / es | e | f | fis / ges | g | gis / as | a | ais / b | h |
|---------|---|-----------|---|----------|---|---|-----------|---|----------|---|---------|---|
| Eingabe | c | C         | d | D        | e | f | F         | g | G        | a | b       | h |
