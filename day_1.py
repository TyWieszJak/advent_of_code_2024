with open('cisla', "r") as file:
    cisla = file.read()  # Načte celý obsah souboru jako jeden řetězec
    #print(cisla)

    levy = []  # Pole pro levé čísla
    pravy = []  # Pole pro pravé čísla

    # Rozdělíme řetězec na části podle mezer (pokud je více mezer, použijeme split bez argumentu)
    cisla_split = cisla.split()  # Split dle jakýchkoli bílých znaků

    # Předpokládáme, že každý pár čísel je na sudém a lichém indexu
    for i in range(len(cisla_split)):
        if i % 2 == 0:  # Sudé indexy pro levé číslo
            levy.append(int(cisla_split[i]))  # Přidáme číslo do seznamu (jako integer)
        else:  # Liché indexy pro pravé číslo
            pravy.append(int(cisla_split[i]))


print("Levy:", levy)
print("Pravy:", pravy)

nejmensi_cislo1 = sorted(levy)
nejmensi_cislo2 = sorted(pravy)

print("Seřazená levá čísla:", nejmensi_cislo1)
print("Seřazená pravá čísla:", nejmensi_cislo2)

# Vypočítáme celkový rozdíl mezi čísly
celkovy_rozdil = 0
for i in range(min(len(nejmensi_cislo1), len(nejmensi_cislo2))):
    rozdil = abs(nejmensi_cislo1[i] - nejmensi_cislo2[i])  # Rozdíl mezi čísly
    print(f"Rozdíl na indexu {i}: {rozdil}")
    celkovy_rozdil += rozdil  # Sčítání celkového rozdílu

print(f"Celkový rozdíl: {celkovy_rozdil}")
celkovy_rozdil2 = 0
for cislo in levy:
    pocet_vyskytu = pravy.count(cislo)
    #print(f"Číslo {cislo} se v seznamu pravy vyskytuje {pocet_vyskytu}krát.")
    if pocet_vyskytu > 0:
        # Vypočítáme součin čísla a jeho počtu výskytů
        vysledek = cislo * pocet_vyskytu
        print(f"Součin {cislo} * {pocet_vyskytu} = {vysledek}")
        celkovy_rozdil2 += vysledek
print (celkovy_rozdil2)
