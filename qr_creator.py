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

print('Öffne die gesuchte Datei!\nAchte darauf, dass diese entweder als xlsx oder csv vorliegt!\nBechte bitte auch, dass die ausgewählte Datei eine Spalte mit dem Namen: Buchungsnummer besitzt.\nDie Einträge aus dieser Spalte werden zu den Dateinamen.\n\n')


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
if 'Buchungsnummer' in raw_data.columns:    
    buchungsnummer = raw_data['Buchungsnummer']
else:
    sys.exit('Die Spalte mit Namen: Buchungsnummer existiert nicht!')

        
print('Wo willst du die Dateien speichern?\nGib hier bitte den Pfad an!\n')

file_path = filedialog.askdirectory()
if not file_path:
   sys.exit('Programm wurde vom Benutzer beendet')

#%%
new_df = raw_data
new_df['Bildname'] = ''
new_df['QR-Code'] = ''
for i, nr in enumerate(buchungsnummer):
    img = qrcode.make(nr, border = 2, box_size = 10, error_correction=qrcode.constants.ERROR_CORRECT_Q)
    new_df['Bildname'][i] = file_path + '/' + nr + ".png"
    img.save(file_path + '/'+ nr + ".png")
    new_df['QR-Code'][i] = img
    new_df['QR-Code'] = new_df.Bildname.map(lambda f: get_thumbnail(file_path + '/' + f))
    

#%%
def get_thumbnail(path):
    i = Image.open(path)
    i.thumbnail((150, 150), Image.LANCZOS)
    return i

def image_base64(im):
    if isinstance(im, str):
        im = get_thumbnail(im)
    with BytesIO() as buffer:
        im.save(buffer, 'jpeg')
        return base64.b64encode(buffer.getvalue()).decode()

def image_formatter(im):
    return f'<img src="data:image/jpeg;base64,{image_base64(im)}">'

#%%
new_df.to_excel(file_path + '/neie2.xlsx')
    