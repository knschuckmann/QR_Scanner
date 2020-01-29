#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 15:06:18 2020

@author: Kostja
"""
#%%
# for QR generator
import qrcode

# for dynamic file path finder
import tkinter as tk
from tkinter import filedialog

import sys

import pandas as pd

#%%%
# open the data and load in python
root = tk.Tk()
root.withdraw()

endung = 'keine'

print('Öffne die gesuchte Datei!\nAchte darauf, dass diese entweder als xlsx oder csv vorliegt!\n\n')


while endung == 'keine':
    
    file_path = filedialog.askopenfilename()
    if not file_path:
        sys.exit('Programm wurde vom Benutzer beendet')
    if file_path[-4:] == 'xlsx':
        raw_data = pd.read_excel(file_path)
        endung = 'xlsx'        
    elif file_path[-3:] == 'csv':
        raw_data = pd.read_csv(file_path, head)
        endung = 'csv'        
    else:
        endung = 'keine'
        print('Bitte formatiere deine Datei in xlsx oder csv Datei um!\n\nDeine Datei muss außerdem eine Spalte mit Namen: Buchungsnummer besitzen.\n\n\n')
    
#%%
        
print('Wo willst du die Dateien speichern?\nGib hier bitte den Pfad an!\n')
root = tk.Tk()
root.withdraw()

file_path = filedialog.askdirectory()
if not file_path:
   sys.exit('Programm wurde vom Benutzer beendet')

#%%

buchungsnummer = raw_data['Buchungsnummer']

for i, nr in enumerate(buchungsnummer):
    img = qrcode.make(nr, border = 2, box_size = 10, error_correction=qrcode.constants.ERROR_CORRECT_Q)
    img.save(file_path + '/'+ nr + ".png")
   
    