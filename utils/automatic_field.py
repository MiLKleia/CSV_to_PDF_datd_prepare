import numpy as np
import pandas as pd
from reportlab.pdfgen import canvas 
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics 
from reportlab.lib import colors 


FILE_NAME = 'out.pdf'
DATE = '15/08/24'
READER = 'John Doe'
INSTITUTE = 'quelque part'
ARCHIVIST = 'Titi'
MAX_CHAR_LINE = 80
PATH = 'base.csv'


def get_std_lines(date, reader, institute, archivist):
    lines = []
    string = ('Date : ' + date + '\t' + 'Archiviste : ' + archivist ).expandtabs(60)
    lines.append(string)
    string = "Nom du lecteur : " + reader
    lines.append(string)
    string = "Institution : " + institute
    lines.append(string)
    return lines
    
def load_data(path):
    Data_Image = pd.read_csv(path,sep=",", on_bad_lines='skip') 
    np_Data_Image = Data_Image.to_numpy()
    return np_Data_Image


def main(file_name, date, reader, institute, archivist, path_csv, n=3):

    data = load_data(path_csv)
    pdf = canvas.Canvas(file_name, pagesize=A4)
    step = 842 // n
    counter = 1
    for title, cote in data :
        title = str(title)
        cote= str(cote)
        if counter%n == 1 : 
        # NEW PAGE, DRAW LINES
            for j in range(n-1) : 
                pdf.line(10, (j+1) * step, 585, (j+1) * step ) 
        
        i = n - (counter-1)% n
        top = ((i) * step ) -(60 -(n-3) * 15)
        text = pdf.beginText(30, top)
        text.setFont("Helvetica", 14) 
        text.setFillColor(colors.black) 
        text.setLeading(23.)
        
        lines = get_std_lines(date, reader, institute, archivist)
        for line in lines :
            text.textLine(line)
        if n > 4 : 
            text.setFont("Helvetica", 7)
            text.textLine("")  
            text.setFont("Helvetica", 14)
        else : 
            text.textLine("")
        text.setFont("Helvetica-Bold", 16) 
        text.textLine("Cote : " + cote)
        text.setFont("Helvetica", 14)
        if len(title) < MAX_CHAR_LINE:  
            text.textLine("Titre : " + title) 
        elif len(title) < 2 * MAX_CHAR_LINE : 
            text.textLine("Titre : " + title[:MAX_CHAR_LINE-1])
            text.textLine(title[MAX_CHAR_LINE :])
        elif len(title) < 3 * MAX_CHAR_LINE and n > 4: 
            text.textLine("Titre : " + title[:MAX_CHAR_LINE-1])
            text.textLine(title[MAX_CHAR_LINE : (2*MAX_CHAR_LINE)]+ "[...]")
        elif len(title) < 3 * MAX_CHAR_LINE : 
            text.textLine("Titre : " + title[:MAX_CHAR_LINE-1])
            text.textLine(title[MAX_CHAR_LINE : (2*MAX_CHAR_LINE)+5])
            text.textLine(title[(2*MAX_CHAR_LINE)+6:])
        elif len(title) > 3 * MAX_CHAR_LINE and n > 4: 
            text.textLine("Titre : " + title[:MAX_CHAR_LINE-1])
            text.textLine(title[MAX_CHAR_LINE : (2*MAX_CHAR_LINE)]+ "[...]")
        else : 
            text.textLine("Titre : " + title[:MAX_CHAR_LINE-1])
            text.textLine(title[MAX_CHAR_LINE : (2*MAX_CHAR_LINE)+5])
            text.textLine(title[(2*MAX_CHAR_LINE)+6: 3*MAX_CHAR_LINE] + "[...]")
                
                
        pdf.drawText(text)  
        if counter%n ==0 : 
            pdf.showPage() 
        counter += 1 

    
    pdf.save()

      

    





if __name__ == "__main__":
    main(FILE_NAME, DATE, READER, INSTITUTE, ARCHIVIST, PATH)
