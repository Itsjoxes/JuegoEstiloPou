opc = 0
q = ""

xp = 0

#Emociones
hambre = 0
sueño = 0
energia = 100

#Trabajo
enter = ""
conserje = 0
vendedor = 0
repartidor = 0
stripper = 0
qtrabajo = ""

#cosas capitalistas
dinero=0
gratitud=0
muerte=0
comida=0
existencia1=0
existencia2=0
existencia3=0
existencia4=0
existencia5=0
existencia6=0
existencia7=0

#Numeros
hambre = int(hambre)
sueño = int(sueño)
energia = int(energia)
xp = int(xp)

#MENU
while True:
    print(f'''
🍔:{hambre} 💤:{sueño} ⚡:{energia} ⭐:{xp}xp

            ⢀⢀⡠⠤⠒⠒⠲⠤⣤⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠟⠁⠀⠀⠀⠀⠀⠀⠁⠙⡮⣂⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣢⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⣦⣂⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⣠⣝⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠱⣥⠄⠀⠀⠀⠀
⠀⠀⠀⠀⣸⠮⣶⠞⠛⣛⣛⣛⣷⠶⠀⠀⠐⢶⣟⣛⣛⡛⠓⠿⡚⣮⡀⠀⠀⠀
⠀⠀⢀⢪⠛⠁⠀⣠⣚⣶⣶⡶⡆⡗⠀⠀⠰⡇⣶⣿⣿⣟⡢⠄⠀⠙⣮⢄⠀⠀
⠀⢀⢦⡋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⠀⠁⣳⢆⠀
⠀⢨⡧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡤⠀⠀⠀   ⠈⢯⠄
⠀⡬⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⠀⡼⠁⠀⠀  ⠀⠀⠊⡄
⠀⡏⠀⠀⠀⠀⠀⠀⠀⠀⡦⠤⠤⠤⠤⠤⠤⠴⠒⠋⠁⢰⠇⠀⠀⠀⠀⠀⠀⡇
⠰⣳⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠚⠀⠀⠀⠀⠀⢀⣴⠛
⠀⠁⢷⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⢵⠙⠀
⠀⠀⠀⠀⠩⠗⠲⠤⣤⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣀⣠⡤⠴⠶⠚⠋⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠀⠀⠀⠀⠀⠀⠐⠂⠈⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀


Gratitud:{gratitud}          💸:{dinero}

    - Seleccione lo que desee -
    1) Jugar
    2) Dormir
    3) Comer
    4) Trabajar
    5) Tienda
  
    ''')
    opc = input()
    if opc.isnumeric() == False:
        print("INGRESA UN NUMERO VALIDO")
    else:
        opc = int(opc)
        if opc >= 5:
            print("INGRESA UN NUMERO DEL 1-5")
    
    if opc == 1:
        if energia <= 24:
            print("¡NO TIENE ENERGIAAAA⚡!")
        if hambre >= 100:
            print("¡TIENE HAMBREEEE🍔!")
        if sueño >= 100:
            print("¡TIENE SUEÑOOOOO💤!")
        else:
           while True: 
            print("¿Desea Jugar con el POU?")
            print("[si]   [no]")
            q = input().lower()
            if q == "si":
                print("¡Has Jugado con el POU!")
                print("- Disminuyo Energia⚡ -")
                energia = energia - 15
                print("- Aumento Hambre🍔, SUEÑO💤 -")
                hambre = hambre + 25
                sueño = sueño + 50

                print("¡Ha Aumentado la xp!")
                xp = xp + 5
                break

            if q == "no":
                print("No jugaste con el POU:(")
                muerte=muerte+50
                break
            else:
                print("INDICA [si] o [no]")
    if opc == 2:
        print("¿Desea que el POU Duerma?")
        print("[si]    [no]")
        q = input()
        if q == "si":
            print("¡El POU ha Dormido!")
            print("- Disminuyo Sueño💤 -")
            print("- Aumento Energia⚡-")
            sueño = sueño - 50
            energia = energia + 25

            print("¡Ha Aumentado la xp!")
            xp = xp + 2
        else:
            print("El POU No durmio")
            muerte=muerte+50

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
            muerte=muerte+50
            if muerte==150:
                print('''mataste al pou...
    ⠀⠀⠀⠀⠀⠀⠀⢀⡠⢄⠤⠤⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⡠⢊⣡⠑⡀⠀⠀⡑⠨⠳⢦⡀⠀⠀⠀⠀⠀⠀⠀⣀⣀⠤⢄⣀⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⣠⠞⣴⢕⣕⣢⣽⣴⣬⣭⣄⣠⢤⢱⡀⠀⠀⠀⣀⣔⡚⠒⠀⠀⠀⠀⠈⠑⠢⢄⠀⠀
⠀⠀⠀⡜⢁⣬⣾⣿⣿⣿⣿⣿⣿⣿⣿⢻⡯⡝⡇⠀⠀⡴⢗⣤⣤⣶⣶⣶⣤⣬⣇⣀⠀⠈⠣⡀
⠀⠀⠀⢇⢼⢿⣿⣇⣹⣿⣿⣿⣿⣿⣿⣸⡟⢨⡇⠀⠸⡷⣿⡟⣹⣿⣿⡿⠛⣿⣿⣿⣿⣮⣄⢳
⠀⠀⠀⠀⢹⣾⣿⣿⣿⣿⣿⢻⣿⣿⣿⡿⠓⣼⠁⠀⣇⢫⣿⣇⣿⣿⣿⣿⣴⣿⣿⣿⣿⣿⣿⣿
⠀⠀⠀⠀⠨⢿⣿⣿⣿⣿⣿⣿⣿⡿⠛⣀⢀⠏⣀⠀⡏⠘⣤⣿⣿⣿⣿⣿⣿⡿⢻⣿⣿⣟⣾⠏
⠀⠀⠀⠀⠀⠫⢝⡛⠟⠛⠟⡋⢉⡡⠊⣀⠞⠰⢈⢷⡧⡀⠁⢅⡙⠿⣿⣿⣿⣿⣿⣿⡿⡻⠋⠀
⠀⠀⠀⠀⠀⠀⠀⢨⠣⠭⣙⠐⡢⣔⠚⠃⠀⠀⠀⠁⠻⢬⡢⢌⡣⠤⣀⠋⠛⠛⣛⠽⠊⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢠⠃⠀⡘⢆⠈⣇⡀⠀⠒⠑⠀⠀⠀⠀⠀⠀⠙⠮⠥⢰⣖⡞⣍⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⡰⠁⠀⠀⠀⠀⠈⢣⠶⠀⠀⠀⠀⠠⣀⡀⠀⢄⠀⠀⠀⠀⠀⢀⠈⢢⠀⠀⠀⠀⠀
⠀⠀⠀⠀⡔⠁⠀⠀⡀⠀⠀⡈⢄⣑⠨⡖⠄⢀⠀⠁⢀⠌⠈⡱⣐⠠⠀⠀⠀⠀⠀⠱⠀⠀⠀⠀
⠀⠀⠀⡜⠀⠀⠀⠀⠀⡀⠀⠀⣰⡀⠣⣞⣤⣵⣽⣶⣾⣶⣤⠀⠢⠑⠡⠂⠀⠀⠀⠁⢡⠀⠀⠀
⠀⠀⢰⠀⠀⠀⠀⠀⠈⠀⠐⠀⠢⡀⠑⡗⣟⡭⠚⠋⠉⠃⡪⠀⠐⠄⡀⠄⠀⢀⠀⠂⡀⡆⠀⠀
⠀⠀⠇⠀⠀⠀⠀⠀⠀⠃⢠⠕⢆⢤⣎⢭⠈⠀⠀⠀⠀⠁⠀⠐⡉⠀⠈⠄⢀⠀⠀⠀⠄⢰⠀⠀
⠀⠸⠀⠀⠀⠀⠀⠀⠀⠄⠄⠀⡀⠁⢩⠟⢀⠂⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⠀⠸⠀⠀
⠀⡇⠀⠀⠀⠀⠘⡠⠀⠀⠉⠢⢡⡄⡡⢎⠀⡁⠀⠀⠀⠄⠠⠄⠠⡀⠀⠀⠁⠀⠀⠀⠀⠀⡀⠀
⢸⠀⠀⠀⠀⠀⠐⠁⡀⠀⡐⠠⢓⣄⠀⡬⠦⡁⠀⠀⠘⠂⠀⠀⠁⠀⠀⠀⠀⠢⠀⠀⠀⠀⡇⠀
⡆⠀⠀⠀⠀⠀⠀⢠⠁⠐⠀⠀⢠⡁⢠⠀⠁⠠⠀⢀⠀⠀⠀⠀⠀⠤⠀⠀⠀⠀⠀⠀⠀⠁⠇⠀
⡇⠀⠀⠀⠀⠀⠀⠀⠀⡠⣐⣔⣀⠀⠀⠈⠀⠀⠀⠀⠀⠂⠐⠀⠠⡈⠀⠁⠀⠀⠀⠠⠀⠅⠀⠀
⡇⠀⠀⠀⠀⠀⠀⠁⠔⠑⠀⡠⢄⠠⠔⠠⠂⠄⢁⠄⠀⠂⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⠀
⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠁⠀⠀⠀⠐⡕⡀⠠⠈⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠇⠀
⠸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡗⠁⠀⠈⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡜⠀⠀
⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⡀⡔⠀⠀⠀
⠀⠀⠐⢍⠑⠒⠒⠒⠒⠒⠒⠓⠒⠂⠂⠔⠒⠒⠒⠓⠒⠒⠒⠈⠀⠉⠩⠀⢀⢦⡣⠊⠀⠀⠀⠀
⠀⠀⠀⠀⠉⠢⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠦⠊⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⣲⣤⣄⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⣀⣀⣠⣤⡴⠚⠁⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')
                
    if opc == 4:
        print("""
        Actualmente la comida esta a un precio totalmente elevado,
        y tenemos que trabajar para ganar dinero para con suerte
        alimentarnos
              
        - Pulsa ENTER para continuar... -      
              """)
        enter = input()
        while True:
            print("""
            Veo que buscas trabajo... Dime ¿Que trabajo quieres?
            1) Conserje  +💸
            2) Vendedor  +💸  -⚡
            3) Repartidor ++💸  ---⚡
            0) Salir
            --------------------------      
            4) $$$$ +++💸 ---💤 -⚡
                """)
            opc = int(input())
            if opc == 0:
                print("Volveras pronto...")
                break 
            if opc == 1:
                print("Conserje: Tiene Mala Paga pero al menos no te esfuerzas")
                print("Desea trabajar aqui?")
                print("[Si]  [No]")
                qtrabajo = input()

                if qtrabajo == "si":
                    print("Perfecto...")
                    print("Tu paga fue transferida")
                    dinero = dinero + 5
                    break
                    
                else:
                    print("Bueno... Volveras en otra ocasion")
                    break

            if opc == 2:
                if energia <= 15:
                    print("Dudo que puedas trabajar con esa Energia...")
                else:
                    print("Vendedor: Trabajo que se Gana Poco mas pero te consumira energia")
                    print("Desea trabajar aqui?")
                    print("[Si]  [No]")
                    qtrabajo = input()

                    if qtrabajo == "si":
                        print("Perfecto...")
                        print("Tu paga fue transferida")
                        print("- ENERGIA ⚡ DISMINUIDA -")
                        energia = energia - 15
                        dinero = dinero + 10
                        break
                    
                    else:
                        print("Bueno... Volveras en otra ocasion")
                        break
            if opc == 3:
                if energia <= 25:
                    print("Dudo que puedas trabajar con esa Energia...")
                else:
                    print("Repartidor: Trabajo que se Gana mucho pero te consumira mucha energia")
                    print("Desea trabajar aqui?")
                    print("[Si]  [No]")
                    qtrabajo = input()

                    if qtrabajo == "si":
                        print("Perfecto...")
                        print("Tu paga fue transferida")
                        print("- ENERGIA ⚡ DISMINUIDA -")
                        energia = energia - 25
                        dinero = dinero + 10
                        break
                    
                    else:
                        print("Bueno... Volveras en otra ocasion")
                        break
            if opc == 4:
                if xp <= 50:
                    print("Desbloquea este Trabajo con 500XP⭐")
                if energia <= 25:
                    print("Dudo que puedas trabajar con esa Energia...")
                if sueño <= 75:
                    print("Duerme un poco esto es muy agotador")
                
                else: 
                    print("????: Trabajo de Noche pero te consumira...")
                    print("Desea trabajar aqui?")
                    print("[Si]  [No]")
                    qtrabajo = input()

                    if qtrabajo == "si":
                        print("Perfecto... veo que puedes...")
                        print("Tu paga fue transferida")
                        print("- ENERGIA ⚡, SUEÑO 💤 DISMINUIDA -")
                        energia = energia - 25
                        sueño = sueño - 75
                        dinero = dinero + 100
                        break
                    
                    else:
                        print("Bueno... Volveras en otra ocasion")
                        break

    if opc == 5:
        while True:
            print(f'''   
                TIENDA GENERAL    💸:{dinero}
                1)  Hamburguesa    $30
                2)  Papas Fritas   $15
                3)  Agua Sin Gas   $5
                4)  Agua Con Gas   $5
                5)  Coca Cola      $15
                6)  Trozo de Pizza $25
                7) Personas Transgenero
                de su mismo genero  $150
                8) terminar la compra
                                    ''')
            opc=int(input("seleccione una opcion"))
            if opc==1:  
                existencia1=int(input("Cuantas quiere? "))
                dinero=dinero-existencia1*30
                if dinero<=-1:
                    print("necesitas trabajar")
            if opc==2:
                existencia2=int(input("Cuantas quiere? "))
                dinero=existencia2*15
                if dinero<=-1:
                    print("necesitas trabajar")
            if opc==3:
                existencia3=int(input("Cuantas quiere? "))
                dinero=existencia3*5
                if dinero<=-1:
                    print("necesitas trabajar")
            if opc==4:
                existencia4=int(input("Cuantas quiere? "))
                dinero=existencia4*5
                if dinero<=-1:
                    print("necesitas trabajar")
            if opc==5:
                existencia5=int(input("Cuantas quiere? "))
                dinero=dinero-existencia5*15
                if dinero<=-1:
                    print("necesitas trabajar")
            if opc==6:
                existencia6=int(input("Cuantas quiere? "))
                dinero=dinero-existencia5*25
                if dinero<=-1:
                    print("necesitas trabajar")
            if opc==7:
                existencia7=int(input("Cuantas quiere? "))
                dinero=dinero-existencia5*150
                if dinero<=-1:
                    print("necesitas trabajar")
            if opc==8:
                break
        
