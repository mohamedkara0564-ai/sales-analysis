# Rapport - Analyse des ventes e-commerce

## 1. Contexte

Ce projet analyse les ventes d'une entreprise e-commerce britannique à partir du dataset UCI Online Retail. L'objectif est de mieux comprendre les ventes, les produits, les marchés et les comportements clients afin de formuler des recommandations commerciales.

## 2. Problématique

L'entreprise souhaite répondre aux questions suivantes :

- Quel chiffre d'affaires est généré ?
- Comment les ventes évoluent-elles dans le temps ?
- Quels produits et quels pays sont les plus performants ?
- Quels clients ont la plus forte valeur ?
- Quelles actions commerciales peuvent améliorer la performance ?

## 3. Données

Le dataset contient des transactions réalisées entre décembre 2010 et décembre 2011.

Variables principales :

- `InvoiceNo` : numéro de facture ;
- `StockCode` : identifiant produit ;
- `Description` : nom du produit ;
- `Quantity` : quantité ;
- `InvoiceDate` : date et heure ;
- `UnitPrice` : prix unitaire ;
- `CustomerID` : identifiant client ;
- `Country` : pays du client.

Source : UCI Machine Learning Repository - Online Retail.

## 4. Méthodologie

Les étapes réalisées sont :

1. Exploration des données brutes ;
2. Identification des valeurs manquantes, doublons et anomalies ;
3. Nettoyage des données ;
4. Création de variables : chiffre d'affaires, mois, jour, heure et total de facture ;
5. Analyse temporelle, produits, pays et clients ;
6. Segmentation client RFM ;
7. Formulation de recommandations métier.

## 5. Résultats principaux

- Chiffre d'affaires total : **8,887,208.89 £**
- Nombre de commandes : **18,532**
- Nombre de clients : **4,338**
- Panier moyen : **479.56 £**
- Produit le plus vendu : **PAPER CRAFT , LITTLE BIRDIE**
- Produit générant le plus de chiffre d'affaires : **PAPER CRAFT , LITTLE BIRDIE**
- Principal marché : **United Kingdom**
- Quantité totale vendue :  **5,152,002**
- Quantité moyenne par commande :  **278**

## 6. Insights métier

- Évolution des ventes
- Produits
- Marchés géographiques
- Clients
- Segmentation RFM

## 7. Recommandations

1. Mettre en place un programme de fidélité pour les clients VIP et fidèles.
2. Lancer une campagne de réactivation des clients à risque ou inactifs.
3. Proposer une offre de seconde commande aux clients récents.
4. Anticiper les périodes de forte demande afin d'adapter les stocks.
5. Développer les marchés secondaires les plus prometteurs.

## 8. Limites de l'analyse

- Le dataset ne contient pas le coût d'achat des produits : il est donc impossible de calculer la marge ou la rentabilité.
- Les données concernent une période limitée.
- Certains clients ne possèdent pas d'identifiant et ont été exclus de l'analyse client.
- Les annulations ne sont pas incluses dans le chiffre d'affaires des ventes réalisées.