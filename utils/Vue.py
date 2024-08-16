import numpy as np
import pandas as pd
import os
import tkinter 
import tkinter.filedialog as filedialog
from datetime import date

import utils.automatic_field as pdf



INVALID_CSV = 1
ERROR_TOO_MANY_VALUES = 3
ERROR_TOO_MANY_ROWS = 4
ERROR_NO_REDO = 2
ERROR_NEW_MAX_LEN = 5
ERROR_CHOICE_n = 6



ALL_IMAGES = 'images'

FILE_NAME = 'test.pdf'
DATE = str(date.today().strftime('%d/%m/%Y'))
READER = ''
INSTITUTE = ''
ARCHIVIST = ''
PATH = 'base.csv'

MAX_LEN_CSV = 200
NUM_PER_PAGE = 3

def modify_NUM_PER_PAGE(n):
    global NUM_PER_PAGE
    try:
        val = int(n)
        if val > 1 and val < 7 :
            NUM_PER_PAGE = val
            return 0
        else : 
            return ERROR_CHOICE_n
    except ValueError:
        return ERROR_NEW_MAX_LEN



def modify_MAX_LEN_CSV(n):
    global MAX_LEN_CSV
    try:
        val = int(n)
        if val > 0 :
            MAX_LEN_CSV = val
            return 0
        else : 
            return ERROR_NEW_MAX_LEN
    except ValueError:
        return ERROR_NEW_MAX_LEN

            
def modify_FILE_NAME(string):
    global FILE_NAME
    if len(string)>0 :
         if string[max(0,len(string)-4):len(string)] == ".pdf" : 
            FILE_NAME = str(string)
         else :
            FILE_NAME = str(string) + ".pdf"
    
def modify_READER(string):
    global READER 
    READER = str(string)
    
def modify_DATE(string):
    global DATE 
    if len(string)<8:
        DATE = str(date.today().strftime('%d/%m/%Y'))
    else : 
        DATE = string
        
def modify_INSTITUTE(string):
    global INSTITUTE 
    INSTITUTE = str(string)
    
def modify_ARCHIVIST(string):
    global ARCHIVIST 
    ARCHIVIST = str(string)
    
def modify_PATH(string):
    global PATH 
    if string[max(0,len(string)-4):len(string)] == ".csv" : 
        data = pdf.load_data(string)
        u, v = data.shape
        if u > MAX_LEN_CSV: 
            return ERROR_TOO_MANY_VALUES
        elif v > 2 :
            return ERROR_TOO_MANY_ROWS
        else :
            PATH = str(string)
            return 0
    else :
        return INVALID_CSV


class Folder_Processing(object):
    def __init__(self):
        self.ON = True
        
    def display_error(self, val_error):
        root = tkinter.Tk()
        root.title('ERROR')
        root.geometry("250x170")
        if val_error == INVALID_CSV :
            error_msg = "Format fichier invalid. \nDoit être .csv. \n"
        elif val_error == ERROR_NO_REDO :
            error_msg = "You should not see this \n"
        elif val_error == ERROR_TOO_MANY_VALUES :
            error_msg = "Maximum " + str(MAX_LEN_CSV) + " lignes de données.  \n"
        elif val_error == ERROR_TOO_MANY_ROWS :
            error_msg = "Maximum 2 colonnes dans le csv,\nau format 'titre,cote' \n"
        elif val_error == ERROR_NEW_MAX_LEN :
            error_msg = "La valeur doit être un\n entier positif \n"
        elif val_error == ERROR_CHOICE_n :
            error_msg = "La valeur doit être un\n entier compris entre 2 et 6 \n"
        else :
            error_msg = "erreur inconnue \n"
        T = tkinter.Label(root)
        b2 = tkinter.Button(root, text = "Exit", command = root.destroy) 
        T.pack()
        T.config(text = error_msg)
        b2.pack()
        tkinter.mainloop()
        
    def choose_folder(self):
        file_name = filedialog.askopenfilenames()
        
        err = modify_PATH(os.path.basename(os.path.normpath(file_name[0])))
        if err > 0:
            self.display_error(err)
        
    def create_pdf(self):
        pdf.main(FILE_NAME, DATE, READER, INSTITUTE, ARCHIVIST, PATH, NUM_PER_PAGE)
                       
    def update_MAX_LEN(self):
        def get_entry_value():
            n = entry.get()
            err = modify_MAX_LEN_CSV(n)
            root.destroy()
            
            if err > 0 :
                self.display_error(err)

        root = tkinter.Tk()
        root.title("choix de la taille max")
        entry = tkinter.Entry(root)
        entry.pack()
        button = tkinter.Button(root, text="sélectionner", command=get_entry_value)
        button.pack() 
        
    def update_CHOICE_n(self):
        def get_entry_value():
            n = entry.get()
            err = modify_NUM_PER_PAGE(n)
            root.destroy()
            
            if err > 0 :
                self.display_error(err)

        root = tkinter.Tk()
        root.title("choix nombre par page")
        entry = tkinter.Entry(root)
        entry.pack()
        button = tkinter.Button(root, text="sélectionner", command=get_entry_value)
        button.pack() 
        
    def executer(self):
        def majAffichage():
            get_date()
            label_date.config(text = "Date choisie : " + DATE)
            fenetre.after(1000, majAffichage)
            get_values()
            
            
        
        def get_date():
            n = entry_date.get()
            modify_DATE(n)
            
        def get_values():
            fn = entry_file_name.get()
            modify_FILE_NAME(fn)
            
            re = entry_reader.get()
            modify_READER(re)
            
            inst = entry_institute.get()
            modify_INSTITUTE(inst)
            
            arch = entry_archivist.get()
            modify_ARCHIVIST(arch)
            
            
            
            
    
        """ Initialise et lance le programme. """
        # fenetre principale
        fenetre = tkinter.Tk()
        fenetre.title("Create PDF")
        fenetre.geometry("800x200")
        fenetre.resizable(0, 0)
        # menu
        menu = tkinter.Menu(fenetre)
        fenetre.config(menu=menu)
        filemenu = tkinter.Menu(menu)
        menu.add_cascade(label="Fichier", menu=filemenu)
        filemenu.add_separator()
        filemenu.add_command(label="Changer nombre max lignes", command=self.update_MAX_LEN)
        filemenu.add_command(label="Changer nombre par page", command=self.update_CHOICE_n)
        filemenu.add_command(label="Quitter", command=fenetre.destroy)
        
        ### Date and select csv
        label_date_jour = tkinter.Label(fenetre)
        label_date_jour.grid(row=1,column=0)
        label_date_jour.config(text = "Date : " + DATE)
        
        button1=tkinter.Button(fenetre, text="Choisir csv",command=self.choose_folder, width=20, height = 1)
        button1.grid(row=1,column=1)
        
        label_date = tkinter.Label(fenetre)
        label_date.grid(row=2,column=0)
        label_date.config(text = "Date choisie :")
        
        entry_date = tkinter.Entry(fenetre, width=50)
        entry_date.grid(row=2,column=1)
        
        ### File_name
        label_nom_pdf = tkinter.Label(fenetre)
        label_nom_pdf.grid(row=3,column=0)
        label_nom_pdf.config(text = "Choisir nom .pdf :")
        
        entry_file_name = tkinter.Entry(fenetre, width=50)
        entry_file_name.grid(row=3,column=1)
        
        ### Reader
        label_reader = tkinter.Label(fenetre)
        label_reader.grid(row=4,column=0)
        label_reader.config(text = "Lecteur :")
        
        entry_reader = tkinter.Entry(fenetre, width=50)
        entry_reader.grid(row=4,column=1)
        
        ### Institute
        label_institute = tkinter.Label(fenetre)
        label_institute.grid(row=5,column=0)
        label_institute.config(text = "Institution :")
        
        entry_institute = tkinter.Entry(fenetre, width=50)
        entry_institute.grid(row=5,column=1)
        
        ### Archivist
        label_archivist = tkinter.Label(fenetre)
        label_archivist.grid(row=6,column=0)
        label_archivist.config(text = "Archiviste :")
        
        entry_archivist = tkinter.Entry(fenetre, width=50)
        entry_archivist.grid(row=6,column=1)
        
        
        
        
        button6=tkinter.Button(fenetre, text="Créer PDF",command=self.create_pdf, width=20, height = 1)
        button6.grid(row=7,column=1)
        
        
        fenetre.grid_columnconfigure(0, minsize=250)
        fenetre.grid_columnconfigure(1, minsize=800-250)
        for i in range(7):
            
            fenetre.grid_rowconfigure(i+1, minsize=13)
        
        
        majAffichage()
        # lance le programme
        fenetre.mainloop()

