def najdi_mas_v_x(vstup, slovo):
    pocet_radku = len(vstup)
    pocet_sloupcu = len(vstup[0])
    delka_slova = len(slovo)

    # Směry pro hledání (diagonální dolů doprava a diagonální nahoru doprava)
    smer = [
        (1, 1),  # diagonálně dolů doprava
        (-1, 1)  # diagonálně nahoru doprava
    ]

    vysledky = []

    def je_validni(x, y):
        return 0 <= x < pocet_radku and 0 <= y < pocet_sloupcu

    # Procházení matice
    for i in range(pocet_radku):
        for j in range(pocet_sloupcu):
            # Pokud první písmeno souhlasí, hledáme slovo
            if vstup[i][j] == slovo[0]:
                prohledane = []
                for dx, dy in smer:
                    x, y = i, j
                    k = 0
                    pozice_slova = []
                    while k < delka_slova and je_validni(x, y) and vstup[x][y] == slovo[k]:
                        pozice_slova.append((x, y))
                        x += dx
                        y += dy
                        k += 1
                    if k == delka_slova:
                        prohledane.append(pozice_slova)
                if len(prohledane) == 2:  # pokud jsou dva výskyty (diagonálně dolů a nahoru)
                    vysledky.append(prohledane)

    return vysledky


def zobraz_matici_s_vysledky(vstup, vysledky):
    # Procházení maticí a zvyraznění nalezených slov
    pro_matici = [radek[:] for radek in vstup]  # Kopírování matice

    for vysledek in vysledky:
        for pozice in vysledek:
            for x, y in pozice:
                pro_matici[x][y] = pro_matici[x][y].upper()  # Zvýraznění písmen

    # Vytisknout upravenou matici
    for radek in pro_matici:
        print(" ".join(radek))


if __name__ == '__main__':
    with open('vstup', 'r') as file:
        # Převod obsahu do 2D matice
        vstup = [list(radek.strip()) for radek in file.readlines()]

    slovo = "MAS"
    vysledky = najdi_mas_v_x(vstup, slovo)

    print(f"Výskyt slova '{slovo}' ve tvaru 'X' nalezen: {len(vysledky)}")
    zobraz_matici_s_vysledky(vstup, vysledky)
