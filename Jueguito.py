opc = 0
q = ""

xp = 0

#Emociones
hambre = 0
sueño = 0
energia = 100

#Numeros
hambre = int(hambre)
sueño = int(sueño)
energia = int(energia)
xp = int(xp)

#MENU
while True:
    print(f'''
🍔:{hambre}  💤:{sueño}  ⚡:{energia}

    [POU INVISIBLE]

⭐:{xp}xp

    - Seleccione lo que desee -
    1) Jugar
    2) Dormir
    3) Comer
  
    ''')
    opc = int(input())
    
    if opc == 1:
        if energia <= 24:
            print("¡NO TIENE ENERGIAAAA⚡!")
        if hambre >= 100:
            print("¡TIENE HAMBREEEE🍔!")
        if sueño >= 100:
            print("¡TIENE SUEÑOOOOO💤!")
        else:
            print("¿Desea Jugar con el POU?")
            print("[si]   [no]")
            q = input()
            if q == "si":
                print("¡Has Jugado con el POU!")
                print("- Disminuyo Energia⚡ -")
                energia = energia - 25
                print("- Aumento Hambre🍔    -")
                hambre = hambre + 25
                print("- Aumento Sueño     -")
                sueño = sueño + 50

                print("¡Ha Aumentado la xp!")
                xp = xp + 5

            else:
                print("No jugaste con el POU:(")

    if opc == 2:
        print("¿Desea que el POU Duerma?")
        print("[si]    [no]")
        q = input()
        if q == "si":
            print("¡El POU ha Dormido!")
            print("- Disminuyo Sueño💤 -")
            sueño = sueño - 50

            print("¡Ha Aumentado la xp!")
            xp = xp + 2
        else:
            print("El POU No durmio")

    if opc == 3:
        print("¿Quiere que el POU Coma?")
        print("[si]    [no]")
        q = input()
        if q == "si":
            print("¡El POU ha comido!")
            print("- Disminuyo Hambre -")
            hambre = hambre - 25
            
            print("¡Ha Aumentado la xp!")
            xp = xp + 2
        else:
            print("El POU No COMIO")