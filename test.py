#! python3.7
# pylint: skip-file

#import pygame

class Auto:
	def __init__(self,_Nummer, _AnzahlReifen=5, _ReifenDruck=1.5, _Marke="Audi"):
		self.Nummer = _Nummer
		self.AnzahlReifen = _AnzahlReifen
		self.ReifenDruck = _ReifenDruck
		self.Marke = _Marke
		self.Spiegel = ["Rückspiegel", "Außenspiegel links", "Außenspiegel rechts"]

	def Hupen(self):
		print("Huuup")

	def SetMarke(self, newMarke):
		self.Marke = newMarke

class Cabrio(Auto):
	def __init__(self, _Nummer, AnzahlReifen=5, _ReifenDruck=1.5, _Marke="Audi"):
		Auto.__init__(self, _Nummer, AnzahlReifen, _ReifenDruck, _Marke)

	def DachHochKlappen(self):
		print("Ich klappe mein Dach hoch")

Auto1 = Auto(1)
Auto1.SetMarke("BMW")

AutoCount = 5
AutoListe = []

while AutoCount != 0:
	AutoListe.append(Auto(AutoCount))
	AutoCount -= 1

for autoItem in AutoListe:
	print(autoItem.Nummer)

Cabrio1 = Cabrio(1)
Cabrio1.Hupen()
Cabrio1.DachHochKlappen()

