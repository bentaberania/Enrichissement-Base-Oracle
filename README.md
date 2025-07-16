# Enrichissement massif d’une base de données Oracle

Ce projet, réalisé par **Rania Bentabe**, a pour objectif de générer 1 million de tuples et de les charger dans une base Oracle via SQL*Loader.

## Contenu du projet

- Nettoyage et transformation de données CSV (notebooks Jupyter)
- Génération massive de données synthétiques
- Chargement Oracle avec `SQL*Loader`
- Génération automatique d’un dictionnaire de données Oracle
- Script SQL de création de tables : `create_coop.sql`

## Mode d'emploi

Consultez le fichier [`Mode_d_emploi_ProjetStage_BentabeRania.pdf`](./Mode_d_emploi_ProjetStage_BentabeRania.pdf) pour les instructions détaillées (prérequis, installation, exécution).

## 📄 Structure

```text
📂 ProjetStage[BentabeRania]
├── cleansingWine.csv
├── create_coop.sql
├── Data.ipynb
├── Script.ipynb
├── vinR.csv, producteurR.csv, recolteR.csv
├── recolte_augmente_1M.dat / .csv
├── recolte.ctl / .log
├── Mode_d_emploi_ProjetStage_BentabeRania.pdf
└── Dictionnaire/
