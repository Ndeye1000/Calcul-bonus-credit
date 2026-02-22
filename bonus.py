def bonus_credit(bonus, montant):
    return montant * (100 / bonus) + montant

if __name__ == '__main__':
    bonus = int(input("Si votre bonus est de 20 %, entrez 20 : "))
    montant = int(input("Entrez le montant de votre achat : "))
    print(f"Vous avez obtenu {bonus_credit(bonus, montant)} FCFA de credits. Felicitations 🎉")