with open('cisla_2', 'r') as file:
    radky = file.readlines()
bezpecne_radky = 0


def zkontroluj_rozdily(radek):
    for i in range(len(radek) - 1):
        rozdil = abs(radek[i + 1] - radek[i])
        if rozdil > 3 or rozdil == 0:
            return False
    return True


def zkontroluj_serazeni(radek):
    return radek == sorted(radek) or radek == sorted(radek, reverse=True)


def kombinace_s_odebranym_jednim_cislem(radek):
    kombinace = []
    for i in range(len(radek)):
        kombinace.append(radek[:i] + radek[i + 1:])
    return kombinace


for i, radek in enumerate(radky, start=1):
    cisla = [int(c) for c in radek.split()]

    if len(cisla) > 1:
        if zkontroluj_rozdily(cisla) and zkontroluj_serazeni(cisla):
            print(f"Řádek {i} {cisla} je bezpečný.")
            bezpecne_radky += 1
            continue


        bezpecny_pokud_odebereme_1 = False
        for novy_radek in kombinace_s_odebranym_jednim_cislem(cisla):
            if zkontroluj_rozdily(novy_radek) and zkontroluj_serazeni(novy_radek):
                bezpecny_pokud_odebereme_1 = True
                break

        if bezpecny_pokud_odebereme_1:
            print(f"Řádek {i} {cisla} je bezpečný po odstranění jednoho čísla.")
            bezpecne_radky += 1
        else:
            print(f"Řádek {i} {cisla} není bezpečný.")

print(f"Celkový počet bezpečných řádků: {bezpecne_radky}")
