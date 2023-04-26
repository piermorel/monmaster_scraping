import os
import glob
import pandas as pd

from parametres import code_formation
from parametres import folder_path

file = glob.glob(folder_path+"*"+code_formation+".xlsx")
print(file)
if len(file) != 1:
    raise ValueError("Fichiers .xlsx non trouvé ou multiple")
    
tot = pd.read_excel(file[0])

def rename_files(fpath, prefix, df):
    for i, row in df.iterrows():
        old_name = prefix + row['Numéro de candidat'] + '.pdf'
        new_name = row['Nom de naissance'].replace(' ','') + '_' + row['Prénom'].replace(' ','') + '-' + row['Numéro de candidat'] + '.pdf'
        try:
            os.rename(fpath+old_name, fpath+new_name)
        except FileNotFoundError:
            print(f"Fichier {old_name} non trouvé")


# Call the rename_files function with the prefix and dataframe as arguments
rename_files(folder_path,code_formation+'-', tot)