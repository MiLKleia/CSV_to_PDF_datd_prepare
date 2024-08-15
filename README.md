<h1>Table of Contents<span class="tocSkip"></span></h1>
<div class="toc"><ul class="toc-item"><li><span><a href="#Insatallation-and-launch" data-toc-modified-id="Insatallation-and-launch-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Insatallation and launch</a></span></li><li><span><a href="#Data-and-how-to-use" data-toc-modified-id="Data-and-how-to-use-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Data and how to use</a></span><ul class="toc-item"><li><span><a href="#CSV-file" data-toc-modified-id="CSV-file-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>CSV file</a></span></li><li><span><a href="#How-to-use" data-toc-modified-id="How-to-use-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>How to use</a></span></li><li><span><a href="#Modify-parameters-(avoid-if-possible)" data-toc-modified-id="Modify-parameters-(avoid-if-possible)-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Modify parameters (avoid if possible)</a></span></li></ul></li></ul></div>

# Installation and launch

This work was done using Python 3.8.
install all requirement using pip/pip3.

Launch the UI by running : 

    python3 UI.py

# Data and how to use
## CSV file

.csv file must be as :

    titre, cote
    "this is a string title', AEJD3L
    single_word_title, KDL3P9
    [...]
    
First line 'titre, cote' will be filtered out. Name can be whatever. Order of colomn must be respected : title on left, cote on right. Values must bes separated by commas(','), not ';' or other character. No commas should bes used in titles or cotes.

## How to use

        |
        +-- utils
        |   |
        |   +-- automatic_field.py
        |   +-- Vue.py
        |   
        +-- UI.py
        |  
        +-- base.csv
        
Default name for .csv is 'base.csv'. You can select another file by selecting 'Choisir csv' and clicking on wanted file.

Default date is the day's date. You can modify the date by filling the blank space next to 'Date choisie : DD/MM/YYY'. The date must be made of 8 characters or more (DD/MM/YY or more). The updated date that will be used is display in the label 'Date choisie : XXXXXXXX' where XXXXXXXX is your input.

Default output file name is 'out.pdf'. Fill the blank space next to 'Choisir nom .pdf' to change output name. 

Default value for reader name is empty. Fill the wanted value in the blank space next to 'Lecteur'.

Default value for institute name is empty. Fill the wanted value in the blank space next to 'Institution'.

Default value for archivist name is empty. Fill the wanted value in the blank space next to 'Archiviste'.

Create the output .pdf by clicking 'Créer pdf'. if some values where not filled, default values will be used even if empty.


## Modify parameters (avoid if possible)


Default .csv file cannot contains more than 200 values. this parameter can be change by clicking 'Fichier/Changer nombre max lignes', entering wanted value and clicking 'sélectionner'. New value must be an integer.

Default number of slips/dockets per page is 3. Change this value by clicking 'Fichier/Changer nombre par page', entering wanted value and clicking 'sélectionner'. New value must be an integer between 2 and 6. We recommend using 3 or 4.
