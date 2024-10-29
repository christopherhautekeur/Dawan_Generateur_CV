# CV Generator

**Dawan CV Generator** est une application web qui permet de générer des CV et des lettres de motivation personnalisées en fonction des offres d'emploi spécifiques. Elle propose également une fonctionnalité de regroupement des offres d'emploi par localisation tout en filtrant les offres d'alternance non pertinentes.

## Badges

![Build Status](https://img.shields.io/badge/build-passing-brightgreen)
![Version](https://img.shields.io/badge/version-1.0.0-blue)

## Fonctionnalités

- 📝 **Générateur de CV** : Crée un CV automatiquement adapté à chaque offre d'emploi en fonction des compétences et de l'expérience demandées.
- 📄 **Générateur de lettre de motivation** : Génère des lettres de motivation personnalisées basées sur les informations de l'offre.
- 📍 **Filtrage des offres par localisation** : Permet de rechercher et regrouper les offres d'emploi en fonction d'une localisation spécifique (ville, région, etc.).
- ⛔ **Exclusion des offres non pertinentes** : Filtre les offres d'alternance ou celles nécessitant une formation spécifique à côté.
- 📥 **Exportation PDF** : Permet l'export des CV et des lettres de motivation au format PDF.

## Prérequis

Avant de commencer, assurez-vous d'avoir installé les outils et modules suivants :

- [Python 3.x](https://www.python.org/downloads/)
- [Streamlit](https://streamlit.io/)
- Modules Python : ...

## Installation

1. Clonez ce dépôt dans votre environnement local :

   ```bash
   git clone https://github.com/christopherhautekeur/Dawan_Generateur_CV
   cd cv-generator-app
   ```

2. Installez les dépendances :

   ```bash
   pip install -r requirements.txt
   ```

3. Lancez l'application avec Streamlit :

   ```bash
   streamlit run app.py
   ```

## Utilisation

### 1. **Génération de CV**
   - Remplissez le formulaire avec vos informations personnelles (nom, expérience, compétences).
   - Téléversez votre CV actuel pour qu'il soit adapté à l'offre choisie.
   - Sélectionnez une offre d'emploi à partir de la liste des offres disponibles.
   - Cliquez sur **Générer le CV** pour obtenir un CV personnalisé basé sur les mots-clés et les exigences de l'offre.

### 2. **Génération de lettre de motivation**
   - Ajoutez un résumé de vos motivations spécifiques pour le poste.
   - Cliquez sur **Générer la lettre** pour créer automatiquement une lettre de motivation ciblée.

### 3. **Filtrage des offres d'emploi**
   - Entrez une localisation (ville ou région) pour regrouper les offres disponibles.
   - Utilisez le filtre pour exclure les offres d'alternance ou les offres non pertinentes.
   - Affichez les résultats et sauvegardez les offres qui vous intéressent.

## Exemple de résultats

Voici un exemple de CV généré par l'application :

```
# Insérer exemple
```

## Auteurs
- [Alan GUYOLLOT](https://github.com/N0va9)
- [Christopher HAUTEKEUR](https://github.com/christopherhautekeur)
- [Elias DJEDOUI](https://github.com/elias-hue) 

## Licence

Ce projet est sous licence MIT.
