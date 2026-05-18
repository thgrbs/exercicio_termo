import random

titulo = "Terminho"
banco_palavras = []

with open('palavras.txt') as word_file:
    for line in word_file:
        banco_palavras.append(line.strip())

palavra_sortida = random.choice(banco_palavras)

letra_deslocada = []
letra_errada = []

max_turnos = 5
turnos = 0

print ("Bem Vindo ao", titulo, "!")
print ("A palavra tem", len(palavra_sortida), "letras")
print ("Você tem", max_turnos -turnos, "turnos restantes")

while turnos < max_turnos:
    palpite = input("Digite uma palavra: ").lower()

    if len(palpite) != len(palavra_sortida) or not palpite.isalpha():
        print("Digite apenas palavras com 5 letras")
        continue

    index = 0

    for c in palpite:
        if c ==  palavra_sortida[index]:
            print(c.upper(), end="")
            if c in letra_deslocada:
                letra_deslocada.remove(c)

        elif c in palavra_sortida:
            if c not in letra_deslocada:
                letra_deslocada.append(c)
            print('_', end= "")

        else:
            if c not in letra_errada:
                letra_errada.append(c)
            print('_', end= "")

        index += 1

    print("\n")
    print("Letras deslocadas: ",letra_deslocada)
    print("Letras erradas: ",letra_errada)
    turnos += 1

    if palpite == palavra_sortida:
        print("Você ganhou!!!")
        break

    if turnos == max_turnos:
        print("Vixe, você perdeu, a palavra correta era:", palavra_sortida)
        break

    print ("Você tem", max_turnos - turnos, "turnos restantes")
