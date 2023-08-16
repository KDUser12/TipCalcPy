def data_entry():
    total_invoice = input("Veuillez saisir le montant total de la facture : ")
    tip_percentage = input("Veuillez saisir le pourcentage de pourboire que vous souhaitez donner : ")

    try:
        total_invoice = int(total_invoice)
        tip_percentage = int(tip_percentage)
    except ValueError:
        print("Une erreur est survenue, les valeurs que vous avez indiquées ne sont pas bonnes veuillez réessayer.")
        data_entry()
    else:
        return total_invoice, tip_percentage


def tip_calculation(total_invoice, tip_percentage):
    tip_amount = total_invoice * (tip_percentage / 100)
    print("Montant du pourboire : {}".format(tip_amount))
    


if __name__ == "__main__":
    print("Bienvenue dans TipCalcPy - Calculatrice de Pourboire !")
    total_invoice, tip_percentage = data_entry()
    tip_calculation(total_invoice, tip_percentage)

