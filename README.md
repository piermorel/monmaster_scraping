# monmaster_scraping

Simple outil pour télécharger automatiquement les dossiers complets monmaster
- Dans le fichier .py, remplacer les ****** par dans l'ordre
  - le code de la formation (dans l'URL pour accéder à la liste des candidatures)
  - votre identifiant
  - votre mot de passe
- Remplacer la ligne `driver = webdriver.Safari()` selon votre plateforme/navigateur internet https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/
- Télécharger la liste des candidats de votre formation au format excel "Fichier des candidatures confirmées", copier le contenu de la colonne "Numéro de candidat" dans un fichier texte avec comme première ligne le texte "no". Sauvegarder sous le nom "no_candidats.csv" dans le dossier du script.
Le fichier ressemble à cela (codes étudiants anonymisés ici) :
![Exemple no_candidats](https://user-images.githubusercontent.com/386604/234013834-1ea3caa8-267d-4c0e-9aaa-54a98b8c1a90.png)
- Lancer le script : `python monmaster_scraping.py`
- Si interruption inopinée, enlever les candidats déjà téléchargés de la liste "no_candidats.csv" et recommencer

