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

# Lister tous les fichiers
files = os.listdir(folder_path)

# Seulement inclure fichiers avec préfixe
files = [f for f in files if f.startswith(code_formation+'-')]

# Extraire les codes candidats des noms de fichiers
codes = [f.replace(code_formation+'-', '').replace('.pdf', '') for f in files]

# Ranger dans un dataframe
df = pd.DataFrame({'Code': codes})

print('\n Codes fichiers :')
print(df)

# Trouver les manquants
missing_codes = tot[~tot['Numéro de candidat'].isin(df['Code'])][['Numéro de candidat']].reset_index(drop=True)


# Renommer la colonne "no"
missing_codes = missing_codes.rename(columns={'Numéro de candidat': 'no'})

print('\n Codes manquants :')
print(missing_codes)

missing_codes.to_csv('no_candidats.csv', index=False)