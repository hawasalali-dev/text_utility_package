from text_utils import kehre_um, zaehle_woerter

beispiel_satz = "Python macht Spaß und ist sehr nützlich."

# String umkehren
umgekehrt = kehre_um(beispiel_satz)
print("Umgekehrter Text:")
print(umgekehrt)

# Wörter zählen
anzahl = zaehle_woerter(beispiel_satz)
print("\nAnzahl der Wörter:")
print(anzahl)