from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def charger_donnees():
    fichier = Path(__file__).with_name("ventes.csv")
    ventes = pd.read_csv(fichier)
    ventes["Total"] = ventes["Quantite"] * ventes["Prix_unitaire"]
    return ventes


def afficher_ventes(ventes):
    print("\nVentes (5 premières lignes) :")
    print(ventes.head())


def afficher_statistiques(ventes):
    chiffre_affaires = np.sum(ventes["Total"])
    quantite_totale = np.sum(ventes["Quantite"])
    prix_moyen = np.mean(ventes["Prix_unitaire"])

    print("\nStatistiques :")
    print(f"Chiffre d'affaires total : {chiffre_affaires:.2f} €")
    print(f"Quantité totale vendue : {quantite_totale}")
    print(f"Prix unitaire moyen : {prix_moyen:.2f} €")


def afficher_ventes_par_produit(ventes):
    chiffre_affaires = ventes.groupby("Produit")["Total"].sum().sort_values(ascending=False)
    meilleur_produit = chiffre_affaires.idxmax()

    print("\nChiffre d'affaires par produit :")
    print(chiffre_affaires)
    print(f"\nProduit ayant généré le plus de chiffre d'affaires : {meilleur_produit}")


def generer_graphique(ventes):
    # graphe 1
    chiffre_par_produit = ventes.groupby("Produit")["Total"].sum()

    plt.figure()
    chiffre_par_produit.plot(kind="bar")
    plt.title("Chiffre d'affaires par produit")
    plt.xlabel("Produit")
    plt.ylabel("Chiffre d'affaires (€)")
    plt.tight_layout()

    # graphe 2
    chiffre_par_mois = ventes.groupby(ventes["Date"].str[:7])["Total"].sum()
        
    plt.figure()
    chiffre_par_mois.plot(kind="line", marker="o")
    plt.title("Évolution du chiffre d'affaires mensuel")
    plt.xlabel("Mois")
    plt.ylabel("Chiffre d'affaires (€)")
    plt.tight_layout()

    plt.show()


def afficher_menu():
    print("\n===== ANALYSE DES VENTES =====")
    print("1. Afficher les ventes")
    print("2. Afficher les statistiques")
    print("3. Afficher les ventes par produit")
    print("4. Générer un graphique")
    print("5. Quitter")


def main():
    ventes = charger_donnees()
    choix = ""

    while choix != "5":
        afficher_menu()
        choix = input("\nVotre choix : ")

        if choix == "1":
            afficher_ventes(ventes)
        elif choix == "2":
            afficher_statistiques(ventes)
        elif choix == "3":
            afficher_ventes_par_produit(ventes)
        elif choix == "4":
            generer_graphique(ventes)
        elif choix == "5":
            print("Au revoir.")
        else:
            print("\nChoix incorrect. Veuillez choisir une option de 1 à 5.")


if __name__ == "__main__":
    main()
