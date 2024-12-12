def vyhledej_slovo(vstup, slovo):
    pocet_radku = len(vstup)
    pocet_sloupcu = len(vstup[0])
    delka_slova = len(slovo)

    # Směry: (řádek, sloupec)
    smer = [
        (0, 1),   # doprava
        (0, -1),  # doleva
        (1, 0),   # dolů
        (-1, 0),  # nahoru
        (1, 1),   # diagonálně doprava dolů
        (-1, -1), # diagonálně doleva nahoru
        (-1, 1),  # diagonálně doprava nahoru
        (1, -1)   # diagonálně doleva dolů
    ]

    def je_validni(x, y):
        return 0 <= x < pocet_radku and 0 <= y < pocet_sloupcu
    vysledky = []
    for i in range(pocet_radku):
        for j in range(pocet_sloupcu):
            # Pokud první písmeno souhlasí, zkusíme najít slovo
            if vstup[i][j] == slovo[0]:
                for dx, dy in smer:
                    k, x, y = 0, i, j
                    while k < delka_slova and je_validni(x, y) and vstup[x][y] == slovo[k]:
                        x += dx
                        y += dy
                        k += 1
                    if k == delka_slova:
                        start = (i, j)
                        end = (x - dx, y - dy)  # Vracíme se o jeden krok zpět
                        vysledky.append((start, end))
    return vysledky # Slovo nalezeno


def diagonalni_hledani(matice, slovo):
    pocet_radku = len(matice)
    pocet_sloupcu = len(matice[0])
    delka_slova = len(slovo)

    # Funkce pro kontrolu, zda je slovo přítomné v daném směru
    def je_slovo_pritomne(x, y, dx, dy):
        for i in range(delka_slova):
            nx, ny = x + i * dx, y + i * dy
            if not (0 <= nx < pocet_radku and 0 <= ny < pocet_sloupcu) or matice[nx][ny] != slovo[i]:
                return False
        return True

    # Procházení všech pozic v matici
    for radek in range(pocet_radku):
        for sloupec in range(pocet_sloupcu):
            # Kontrola diagonálních směrů (dolů doprava a dolů doleva)
            if je_slovo_pritomne(radek, sloupec, 1, 1) or je_slovo_pritomne(radek, sloupec, 1, -1):
                return True

    return False
if __name__ == '__main__':
    with open('vstup', 'r') as file:
        # Převod obsahu do 2D matice
        vstup = [list(radek.strip()) for radek in file.readlines()]
    slovo = "XMAS"
    nalezeno = vyhledej_slovo(vstup, slovo)
    print(f"Slovo '{slovo}' bylo nalezeno: {len(nalezeno)} ")

    slovo = "mas"

    # Spuštění hledání
    if diagonalni_hledani(vstup, slovo):
        print("Slovo bylo nalezeno diagonálně!")