#!/usr/bin/python3
"""Programm, um ein PBASIC-Programm für den BASIC Stamp 1 automatisiert zu schreiben.
GROSSBUCHSTABEN entsprechen erhöhten Halbtönen, z.B. C = cis
x bezeichnet ganz kurze Pausen zwischen Tönen, wie zwischen zwei gleichen Tönen
Leerzeichen bezeichnet Pausen"""

toene={"c":82, "C":85, "d":87, "D":89, "e":92, "f":94, "F":96, "g":97, "G":99, "a":101, "b":102, "h":104}

PIN = input("Füget ein den Anschlusspin: ")
code="' {$STAMP BS1}\n" + "SYMBOL Lautspr = {0}\nOUTPUT Lautspr\nB1=10\n\n".format(PIN)

melodei = input("Füget ein die Melodei: ")

for note in melodei:
    if note == "x":
        befehl = "PAUSE 100\n"
    elif note == " ":
        befehl = "PAUSE 500\n"
    else:
        befehl = "SOUND Lautspr, ({1},B1)\n".format(PIN, toene[note])
    code += befehl

print("\n" + code + "\n END")
