def bonus_credit(bonus, montant):
    return montant / (100 / bonus) + montant

if __name__ == '__main__':
    bonus = int(input("Si votre bonus est de 500 %, entrez 500 : "))
    montant = int(input("Entrez le montant de votre achat : "))
    print(f"Vous avez obtenu {bonus_credit(bonus, montant):,.0f} FCFA de credits. Felicitations 🎉".replace(",", " "))