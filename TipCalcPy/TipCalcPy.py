# Fonction pour saisir les données de manière répétée jusqu'à ce qu'elles soient valides
# noinspection PyShadowingNames
def data_entry():
    while True:
        total_invoice = input("Veuillez saisir le montant total de la facture : ")
        tip_percentage = input("Veuillez saisir le pourcentage de pourboire que vous souhaitez donner : ")

        try:
            total_invoice = float(total_invoice)
            tip_percentage = float(tip_percentage)
            return total_invoice, tip_percentage
        except ValueError:
            print(
                "Une erreur est survenue, les valeurs que vous avez indiquées ne sont pas bonnes. Veuillez réessayer.")


# Fonction pour afficher les résultats
# noinspection PyShadowingNames
def display_results(tip_amount, total_amount_payable):
    print("Montant du pourboire : {}".format(tip_amount))
    print("Montant total à payer : {}".format(total_amount_payable))


if __name__ == "__main__":
    print("Bienvenue dans TipCalcPy - Calculatrice de Pourboire !")

    # Saisie des données
    total_invoice, tip_percentage = data_entry()

    # Calcul du pourboire
    tip_amount = total_invoice * (tip_percentage / 100)

    # Calcul du montant total
    total_amount_payable = total_invoice + tip_amount

    # Affichage des résultats
    display_results(tip_amount, total_amount_payable)

    input("Appuyez sur entrer pour quitter le programme.")
