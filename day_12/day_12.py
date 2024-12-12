with open('vstup', 'r') as file:
    # Převod obsahu do 2D matice
    vstup = [list(radek.strip()) for radek in file.readlines()]

def najdi_skupiny(matice):
    rows = len(matice)
    cols = len(matice[0]) if rows > 0 else 0
    navstivene = [[False for _ in range(cols)] for _ in range(rows)]

    def dfs(x, y, pismeno):
        # Pokud jsme mimo rozsah nebo písmeno neodpovídá, vrátíme 0
        if x < 0 or y < 0 or x >= rows or y >= cols or navstivene[x][y] or matice[x][y] != pismeno:
            return 0

        # Označíme aktuální buňku jako navštívenou
        navstivene[x][y] = True

        # Prozkoumáme všechny sousedy (horizontálně, vertikálně)
        velikost = 1
        smery = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in smery:
            velikost += dfs(x + dx, y + dy, pismeno)

        return velikost

    def spocitej_obvod(x, y, pismeno):
        obvod = 0
        smery = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for dx, dy in smery:
            nx, ny = x + dx, y + dy
            # Pokud jsme mimo rozsah nebo sousední buňka má jiné písmeno, přidáme k obvodu
            if nx < 0 or ny < 0 or nx >= rows or ny >= cols or matice[nx][ny] != pismeno:
                obvod += 1
        return obvod

    skupiny = []
    obvody = []

    for i in range(rows):
        for j in range(cols):
            if not navstivene[i][j]:
                velikost_skupiny = dfs(i, j, matice[i][j])
                if velikost_skupiny > 1:
                    skupiny.append((matice[i][j], velikost_skupiny))

                    # Spočítání obvodu
                    obvod = 0
                    for x in range(rows):
                        for y in range(cols):
                            if navstivene[x][y] and matice[x][y] == matice[i][j]:
                                obvod += spocitej_obvod(x, y, matice[i][j])
                    obvody.append((matice[i][j], obvod))

    return skupiny, obvody

# Najdeme skupiny ve vstupní matici
skupiny, obvody = najdi_skupiny(vstup)

# Výpis výsledků
print("Nalezené skupiny stejných písmen vedle sebe:")
for pismeno, velikost in skupiny:
    print(f"Písmeno '{pismeno}' má velikost skupiny {velikost}.")

print("\nObvody skupin:")
celkovy_obvod = 0
for pismeno, obvod in obvody:
    print(f"Písmeno '{pismeno}' má obvod {obvod}.")
    celkovy_obvod += obvod

print(f"\nCelkový obvod všech skupin: {celkovy_obvod}")
