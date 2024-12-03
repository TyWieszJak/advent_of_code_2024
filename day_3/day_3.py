import re


def vypocet_mul(data):
    pattern = re.compile(r"do\(\)|don't\(\)|mul\((\d+),(\d+)\)")
    suma = 0
    povoleno = True

    for match in pattern.finditer(data):
        instrukce = match.group(0)

        if instrukce == "do()":
            povoleno = True
        elif instrukce == "don't()":
            povoleno = False
        elif povoleno and instrukce.startswith("mul"):
            a, b = map(int, match.groups())
            suma += a * b

    return suma

try:
    with open('mul', 'r') as file:
        obsah = file.read()
except FileNotFoundError:
    print("Soubor 'mul' nebyl nalezen.")
    obsah = ""

if obsah:
    vysledek = vypocet_mul(obsah)
    print("Součet povolených mul:", vysledek)
else:
    print("Obsah souboru je prázdný nebo nebyl správně načten.")
