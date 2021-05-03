# MuffinLight
Une version allégée de Muffin, faite pour tourner côté serveur avec Python

## Mise en place
- Télécharger l'archive
- Remplacer pod.jpg par votre image de podcast
- Installer les dépendances avec pip (mutagen, bottle, marko, paste)
- Editer les informations dans config.py avec vos informations à vous. Dans la partie base_description, %%comment%% sera remplacé par le contenu du Commentaire de votre fichier MP3, ou du champs description de votre .json. Et le champ audio_base permet d'ajouter une URL de tracking d'écoutes comme podtrac

## Ajouter un épisode
- Déposez simplement un fichier .MP3 avec les bons tags dans `/public/audio`. Le site les détectera tout seul

Vous pouvez modifier les paramètres d'un épisode pour mettre une meilleur description par exemple, en ajoutant un fichier .json du même nom que votre fichier .MP3 et pouvant contenir les paramètres suivants :
```JSON
{
  "title": "",
  "description": "",
  "itunes_explicit": "yes/no",
  "itunes_season": "0",
  "itunes_episode": "0",
  "itunes_episode_type": "",
  "pub_date": "timestamp"
}
```

## Crédits
Le logo de Muffin a été fait par [Mifflue](https://twitter.com/LaMifflue)