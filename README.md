# monmaster_scraping

Simple outil pour télécharger automatiquement les dossiers complets monmaster.

**Mode d'emploi :**
- Placer les quatre fichiers .py dans un dossier
- Si vous n'êtes pas sur Mac, dans le fichier `monmaster_scraping.py` remplacer la ligne `driver = webdriver.Safari()` selon votre plateforme/navigateur internet 
https://www.selenium.dev/documentation/webdriver/getting_started/install_drivers/

- Créer un sous-dossier pour une formation
- Placer dans ce sous-dossier le fichier .xlsx obtenu en téléchargeant "Fichier des candidatures confirmées" dans l'espace monmaster de votre formation

![Capture d’écran 2023-04-26 à 10 37 26](https://user-images.githubusercontent.com/386604/234519453-a9e93deb-6749-436a-bf8c-e8ec64fe6742.png)

- Dans le fichier `parametres.py`, remplacer les ****** par dans l'ordre :
  - votre identifiant
  - votre mot de passe
  - Le chemin et nom du sous-dossier créé plus tôt
  - La référence de votre formation : On le trouve soit dans la colonne "référence" dans la liste des formations candidatables, soit dans l'onglet "Formation candidatable" une fois dans votre formation (sous le cadre rouge de censure dans cette capture)
  
  ![Capture d’écran 2023-04-26 à 10 37 16](https://user-images.githubusercontent.com/386604/234519377-5ec5ff02-0982-4bc5-900f-cf39197927c2.png)

- Générer la liste des candidats à télécharger en lancant le script : `python generer_nocandidats.py` Cela doit créer un fichier `no_candidats.csv` dans le dossier des scripts

- Lancer le script de téléchargement : `python monmaster_scraping.py`
- Aller se faire un (long) café 
- Déplacer tous les fichiers téléchargés dans le sous-dossier de la formation créé plus tôt
- Relancer le script `python generer_nocandidats.py' pour vérifier s'il y a des fichiers manquants (si oui, relancer le script de téléchargement, etc. )
- Si vous souhaitez renommer les fichiers au format Nom_Prenom-code.pdf, lancez le script `python renommer_fichiers.py

