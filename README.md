# monmaster_scraping

Simple outil pour télécharger automatiquement les dossiers monmaster
- Dans le fichier .py, remplacer les ****** par dans l'ordre
  - le code de la formation (dans l'URL pour accéder à la liste des candidatures)
  - votre identifiant
  - votre mot de passe
- Remplacer la ligne `driver = webdriver.Safari()` selon votre plateforme/navigateur internet
- Télécharger la liste des candidats de votre formation au format excel "Fichier des candidatures confirmées", copier le contenu de la colonne "Numéro de candidat" dans un fichier texte avec comme première ligne le texte "no". Sauvegarder sous le nom "no_candidats.csv" dans le dossier du script.
- Lancer le script
- Si interruption inopinée, enlever les candidats déjà téléchargés de la liste "no_candidats.csv" et recommencer

