"""
Chapitre 11.1

Classes pour représenter un personnage.
"""


import random

import utils


class weapon:
	name = ""
	attack = 0
	lvl_min = 0
	UNARMED = 20

	def __init__(self,name:str,attack:float,lvl:int):
		self.name = name
		self.attack = attack
		self.lvl_min = lvl

	def make_unarmed(self):
		self.__init__("unarmed", self.UNARMED, 0)


class Character:
	def __init__(self,name,maxHP,attack,defense,lvl):
		self.name = name
		self.maxHP = maxHP
		self.attack = attack
		self.defense = defense
		self.lvl = lvl
		self.HP = maxHP
	def changeHP(self,dHP):
		self.HP = min(max(0,self.HP+dHP),self.maxHP)

def deal_damage(attacker, defender):
	damage = attacker.weapon.attack
	print(f"{attacker.name} used {attacker.weapon.name}")
	if random.random() < 0.065:
		print("  Critical hit!")
	print(f"  {defender.name} took {damage} dmg")

def run_battle(c1, c2):
	# TODO: Initialiser attaquant/défendeur, tour, etc.
	print(f"{attacker.name} starts a battle with {defender.name}!")
	while True:
		# TODO: Appliquer l'attaque
		# TODO: Si le défendeur est mort
			print(f"{defender.name } is sleeping with the fishes.")
			break
		# Échanger attaquant/défendeur
	# TODO: Retourner nombre de tours effectués
