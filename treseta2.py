# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 12:55:02 2020

@author: erdsndj
"""

from random import randint
from random import shuffle


class Treseta:

    boje = ['kupe', 'bate', 'spade', 'dinare']
    brojevi = [1, 2, 3, 4, 5, 6, 7, 11, 12, 13]
    poeni = { 1:1, 2:1/3, 3:1/3, 4:0, 5:0, 6:0, 7:0, 11:1/3, 12:1/3, 13:1/3 }
    precedence = { 4:0, 5:1, 6:2, 7:3, 11:4, 12:5, 13:6, 1:7, 2:8, 3:9 }

    def __init__(self):
        self.player_points = 0
        self.comp_points = 0
        self.spil = []
        self.player_hand = []
        self.comp_hand = []
        self.ultima = True
        
    def kreiraj_spil(self):
        self.spil = []
        for boja in self.boje:
            for broj in self.brojevi:
                self.spil.append ( (broj, boja) )
        return self.spil

    def podijeli_karte(self, spil, n):
        return spil[:n], spil[n:]
    
    def odigraj_kartu_i_dodaj_poene(self):
        same_color_found = False
        print("Unesi index karte koju zelis odigrati:")
        unos = input()
        karta = self.player_hand[int(unos)]
        print("KARTA IGRACA: ", karta)
        self.player_hand.remove(karta)
        #print(self.player_hand)
        
        for karta2 in self.comp_hand:
            if (karta2[1] == karta[1]):
                same_color_found = True
                self.comp_hand.remove(karta2)
                print("KARTA KOMPJUTERA: ", karta2, "\n")
                if self.precedence.get(karta[0]) > self.precedence.get(karta2[0]):
                    self.player_points += float(self.poeni.get(int(karta[0])))
                    self.player_points += float(self.poeni.get(int(karta2[0])))
                    self.ultima = True
                else:
                    self.comp_points += float(self.poeni.get(int(karta[0])))
                    self.comp_points += float(self.poeni.get(int(karta2[0])))
                    self.ultima = False
                break
                
        if not same_color_found:
            karta2 = self.comp_hand[randint(0,3)]
            print("KARTA KOMPJUTERA: ", karta2, "\n")
            self.comp_hand.remove(karta2)
            self.player_points += float(self.poeni.get(int(karta[0])))
            self.player_points += float(self.poeni.get(int(karta2[0])))
            self.ultima = True
        print("POENI IGRACA: ", self.player_points)
        print("POENI KOMPJUTERA: ", self.comp_points, "\n")
        print("-------------------------------------------")
    
    def igra(self):
        print("                                                    TRESETA:")
        print("-------------------------------------------------------------------------------------------------------------------")
        self.spil = self.kreiraj_spil()
        shuffle(self.spil)
        print("SPIL: ", self.spil, "\n")
        self.player_hand, self.spil = self.podijeli_karte(self.spil, 4)
        self.comp_hand, self.spil = self.podijeli_karte(self.spil, 4)
        print("RUKA IGRACA: ", self.player_hand)
        print("RUKA KOMPJUTERA: ", self.comp_hand, "\n")
        self.odigraj_kartu_i_dodaj_poene()
        
        while self.spil:
            player_hand_new_card, self.spil = self.podijeli_karte(self.spil, 1)
            comp_hand_new_card, self.spil = self.podijeli_karte(self.spil, 1)
            self.player_hand += player_hand_new_card
            self.comp_hand += comp_hand_new_card
            print("RUKA IGRACA: ", self.player_hand)
            print("RUKA KOMPJUTERA: ", self.comp_hand, "\n")
            self.odigraj_kartu_i_dodaj_poene()
            
        if (self.ultima):
            self.player_points += 1
        else:
            self.comp_points += 1
        print("POENI IGRACA: ", self.player_points)
        print("POENI KOMPJUTERA: ", self.comp_points, "\n")
        if self.player_points > self.comp_points:
            print("IGRAC JE POBJEDNIK")
        elif self.comp_points > self.player_points:
            print("KOMPJUTER JE POBJEDNIK")
        else:
            print("IZJEDNACENO")
        
    
treseta = Treseta()
treseta.igra()
