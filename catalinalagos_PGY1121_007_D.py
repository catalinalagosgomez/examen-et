from os import system 
system ("cls")

platinum=["Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible",
          "Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible",]

gold=["Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible",
      "Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible", 
      "Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible"]

silver=[" Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible",
        "Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible",
        "Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible",
        "Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible",
        "Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible","Disponible",]


while True:
    print("""
    *********Creatvos.cl************
    1.-Compra de entradas
    2.-Sitios dispoibles
    3.-Ver listado de asitentes
    4.-Ganancias totales
    5.-Salir
    """)
    op=input("Ingrese una opcion: ")
    match op:
        case"1":
                while True:
                    print("""
                    1.-Platinum, $120.000. (Asientos del 1 al 20)
                    2.-Gold, $80.000. (Asientos del 21 al 50)
                    3.- Silver, 50.000. (asientos del51 al 100)
                    """)
                    opcion=input("ingrese una opcion:")
                    match opcion:
                        case"1":
                            asientos=input("seleccione un asiento del 1 al 20: ")
                            nombre=input("Ingrese su nombre: ")
                            apellido=input("ingrese su apellido: ")
                            rut=input("ingrese su rut: ")
                            match asientos:
                                case"1":
                                    if platinum[0]=="Disponible":
                                        platinum[0]= " X"
                                        print("asiento reservado con exito")
                                       
                                
                                        break
                                    else:
                                        print("asiento no disponible")
                                case"2":
                                    if platinum[1]=="Disponible":
                                        platinum[1]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")

                                case"3": 
                                    if platinum[2]=="Disponible":
                                        platinum[2]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"4":  
                                    if platinum[3]=="Disponible":
                                        platinum[3]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                    pass
                                case"5": 
                                    if platinum[4]=="Disponible":
                                        platinum[4]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                    
                                case"6":  
                                    if platinum[5]=="Disponible":
                                        platinum[5]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                            
                                case"7":  
                                    if platinum[6]=="Disponible":
                                        platinum[6]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"8": 
                                    if platinum[7]=="Disponible":
                                        platinum[7]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"9":  
                                    if platinum[8]=="Disponible":
                                        platinum[8]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"10": 
                                    if platinum[9]=="Disponible":
                                        platinum[9]=" X"
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"11":  
                                    if platinum[10]=="Disponible":
                                        platinum[10]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"12": 
                                    if platinum[11]=="Disponble":
                                        platinum[11]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"13":  
                                    if platinum[12]=="Disponible":
                                        platinum[12]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"14": 
                                    if platinum[13]=="Disponible":
                                        platinum[13]=" X"
                                        print("asiento reservado con exito")

                                    else:
                                        print("asiento no disponible")
                                case"15":  
                                    if platinum[14]=="Disponible":
                                        platinum[14]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"16": 
                                    if platinum[15]=="Disponible":
                                        platinum[15]="  X"
                                        print("asiento reservado con exito")

                                    else:
                                        print("asiento no disponible")
                                case"17":  
                                    if platinum[16]=="Disponible":
                                        platinum[16]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"18": 
                                    if platinum[17]=="Disponible":
                                        platinum[17]=" X"
                                        print("asiento reservado con exito")

                                    else:
                                        print("asiento no disponible")
                                case"19":  
                                    if platinum[18]=="Disponible":
                                        platinum[18]=" X"
                                        print("asiento reservado con exito")
                                    else:
                                        print("asiento no disponible")
                                case"20": 
                                    if platinum[19]=="Disponible":
                                        platinum[19]="X"
                                        print("asiento reservado con exito")

                                    else:
                                        print("asiento no disponible")
                        case"2":
                            asientos=input("seleccione un asiento del 21 al 50: ")
                            nombre=input("Ingrese su nombre: ")
                            apellido=input("ingrese su apellido: ")
                            rut=("ingrese su rut: ")
                            
                            match asientos:
                                case"21":
                                    if gold[0]=="Disponible":
                                        gold[0]=" X"
                                        print("asiento reservado con exito")
                                    else:
                                        print("asiento no disponible")
                                case"22":
                                    if gold[1]=="Disponible":
                                        gold[1]="X"
                                        print("asiento reservado con exito")
                                    else:
                                        print("asiento no disponible")
                                case"23": 
                                    if gold[2]=="Disponible":
                                        gold[2]=" X"
                                        print("asiento reservado con exito")
                                    else:
                                        print("asiento no disponible")
                                case"24":  
                                    if gold[3]=="Disponible":
                                        gold[3]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                    pass
                                case"25": 
                                    if gold[4]=="Disponible":
                                        gold[4]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                    
                                case"26":  
                                    if gold[5]=="Disponible":
                                        gold[5]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                     print("asiento no disponible")
                            
                                case"27":  
                                    if gold[6]=="Disponible":
                                        gold[6]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"28": 
                                    if gold[7]=="Disponible":
                                        gold[7]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"29":  
                                    if gold[8]=="Disponible":
                                        gold[8]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"30": 
                                    if gold[9]=="Disponible":
                                        gold[9]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"31":  
                                    if gold[10]=="Disponible":
                                        gold[10]="X"
                                        print("asiento reservado con exito")

                                    else:
                                        print("asiento no disponible")
                                case"32": 
                                    if gold[11]=="Disponible":
                                        gold[11]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"33":  
                                    if gold[12]=="Disponible":
                                        gold[12]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"34": 
                                    if gold[13]=="Disponible":
                                        gold[13]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"35":  
                                    if gold[14]=="Disponible":
                                        gold[14]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"36": 
                                    if gold[15]=="Disponible":
                                        gold[15]=" X"
                                        print("asiento reservado con exito")

                                    else:
                                        print("asiento no disponible")
                                case"37":  
                                    if gold[16]=="Disponible":
                                        gold[16]="X"
                                        print("asiento reservado con exito")

                                    else:
                                        print("asiento no disponible")
                                case"38": 
                                    if gold[17]=="Disponible":
                                        gold[17]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"39":  
                                    if gold[18]=="Disponible":
                                        gold[18]=" X"
                                        print("asiento reservado con exito")

                                    else:
                                        print("asiento no disponible")
                                case"40": 
                                    if gold[19]=="Disponible":
                                        gold[19]=" No Disponible"
                                        print("asiento reservado con exito")

                                    else:
                                        print("asiento no disponible")

                                case"41":  
                                    if gold[20]=="Disponible":
                                        gold[20]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"42": 
                                    if gold[21]=="Disponible":
                                        gold[21]=" X"
                                        print("asiento reservado con exito")

                                    else:
                                        print("asiento no disponible")
                                case"43":  
                                    if gold[22]=="Disponible":
                                        gold[22]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"44": 
                                    if gold[23]=="Disponible":
                                        gold[23]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"45":  
                                    if gold[24]=="Disponible":
                                        gold[24]="X"
                                        print("asiento reservado con exito")

                                    else:
                                        print("asiento no disponible")
                                case"26": 
                                    if gold[15]=="Disponible":
                                        gold[15]=" X"
                                        print("asiento reservado con exito")

                                    else:
                                        print("asiento no disponible")
                                case"7":  
                                    if gold[26]=="Disponible":
                                        gold[26]="No Disponible"
                                        print("asiento reservado con exito")
                                        print("asiento no disponible")
                                case"48": 
                                    if gold[27]=="Disponible":
                                        gold[27]=" X"
                                        print("asiento reservado con exito")
                                    else:
                                        print("asiento no disponible")
                                case"50": 
                                    if gold[29]=="Disponible":
                                        gold[29]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                        
                        case"3":
                            asientos=input("seleccione un asiento del 51 al 100: ")
                            nombre=input("Ingrese su nombre:")
                            apellido=input("ingrese su apellido")
                            rut=("ingrese su rut")
                            
                            match asientos:
                                case"51":
                                    if silver[0]=="Disponible":
                                        silver [0]=" X"
                                        print("asiento reservado con exito")

                                    else:
                                        print("asiento no disponible")
                                case"52":
                                    if silver[1]=="Disponible":
                                        silver[1]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"53": 
                                    if silver[2]=="Disponible":
                                        silver[2]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"54":  
                                    if silver[3]=="Disponible":
                                        silver[3]="X"
                                        print("asiento reservado con exito")
                                    else:
                                        print("asiento no disponible")
                                    pass
                                case"55": 
                                    if silver[4]=="Disponible":
                                        silver [4]=" X"
                                        print("asiento reservado con exito")

                                    else:
                                        print("asiento no disponible")
                                    
                                case"56":  
                                    if silver[5]=="Disponible":
                                        silver[5]="X"
                                        print("asiento reservado con exito")
                                    else:
                                        print("asiento no disponible")
                            
                                case"57":  
                                    if silver[6]=="Disponible":
                                        silver[6]="X"
                                        print("asiento reservado con exito")

                                    else:
                                        print("asiento no disponible")
                                case"58": 
                                    if silver[7]=="Disponible":
                                        silver[7]=" X"
                                        print("asiento reservado con exito")
                                        print("asiento no disponible")
                                case"59":  
                                    if silver[8]=="Disponible":
                                        silver[8]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"60": 
                                    if silver[9]=="Disponible":
                                        silver[9]=" X"
                                        print("asiento reservado con exito")
                                    else:
                                        print("asiento no disponible")
                                case"61":  
                                    if silver[10]=="Disponible":
                                        silver[10]=" X"
                                        print("asiento reservado con exito")
                                    else:
                                        print("asiento no disponible")
                                case"62": 
                                    if silver[11]=="Disponible":
                                        silver[11]="X"
                                        print("asiento reservado con exito")
                                    else:
                                        print("asiento no disponible")
                                case"63":  
                                    if silver[12]=="Disponible":
                                        silver[12]="X"
                                        print("asiento reservado con exito")

                                    else:
                                        print("asiento no disponible")
                                case"64": 
                                    if silver[13]=="Disponible":
                                        silver[13]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"65":  
                                    if silver[14]=="Disponible":
                                        silver[14]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"66": 
                                    if silver[15]=="Disponible":
                                        silver[15]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"67":  
                                    if silver[16]=="Disponible":
                                        silver[16]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"68": 
                                    if silver[17]=="Disponible":
                                        silver[17]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"69":  
                                    if silver[18]=="Disponible":
                                        silver[18]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"70": 
                                    if silver[19]=="Disponible":
                                        silver[19]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"71":
                                    if silver[20]=="Disponible":
                                        silver [20]="X"
                                        print("asiento reservado con exito")

                                    else:
                                        print("asiento no disponible")
                                case"72":
                                    if silver[21]=="Disponible":
                                        silver[21]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"73": 
                                    if silver[22]=="Disponible":
                                        silver[22]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"74":  
                                    if silver[23]=="Disponible":
                                        silver[23]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                    pass
                                case"75": 
                                    if silver[24]=="Disponible":
                                        silver [24]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                    
                                case"76":  
                                    if silver[25]=="Disponible":
                                        silver[25]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                            
                                case"77":  
                                    if silver[26]=="Disponible":
                                        silver[26]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"78": 
                                    if silver[27]=="Disponible":
                                        silver[27]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"79":  
                                    if silver[28]=="Disponible":
                                        silver[28]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"80": 
                                    if silver[29]=="Disponible":
                                        silver[29]="X"
                                        print("asiento reservado con exito")

                                    else:
                                        print("asiento no disponible")
                                case"81":  
                                    if silver[30]=="Disponible":
                                        silver[30]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"82": 
                                    if silver[31]=="Disponible":
                                        silver[31]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"83":  
                                    if silver[32]=="Disponible":
                                        silver[32]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"84": 
                                    if silver[33]=="Disponible":
                                        silver[33]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"85":  
                                    if silver[34]=="Disponible":
                                        silver[34]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"86": 
                                    if silver[35]=="Disponible":
                                        silver[35]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"87":  
                                    if silver[36]=="Disponible":
                                        silver[36]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"88": 
                                    if silver[37]=="Disponible":
                                        silver[37]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"89":  
                                    if silver[38]=="Disponible":
                                        silver[38]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"90": 
                                    if silver[39]=="Disponible":
                                        silver[39]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"91":  
                                    if silver[40]=="Disponible":
                                        silver[40]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"92": 
                                    if silver[41]=="Disponible":
                                        silver[41]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"93":  
                                    if silver[42]=="Disponible":
                                        silver[42]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"94": 
                                    if silver[43]=="Disponible":
                                        silver[43]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"95":  
                                    if silver[44]=="Disponible":
                                        silver[44]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"96": 
                                    if silver[45]=="Disponible":
                                        silver[45]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"97":  
                                    if silver[46]=="Disponible":
                                        silver[46]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"98": 
                                    if silver[47]=="Disponible":
                                        silver[47]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"99":  
                                    if silver[48]=="Disponible":
                                        silver[48]=" X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
                                case"100": 
                                    if silver[49]=="Disponible":
                                        silver[49]="X"
                                        print("asiento reservado con exito")
                                        break

                                    else:
                                        print("asiento no disponible")
        case"2":
            print("""
                    ******Asientos Disponibles*****
                    1.-Platinum (Asientos del 1 al 20)
                    2.-Gold (Asientos del 21 al 50)
                    3.- Silver  (asientos del51 al 100)
                    
                    """)      
            selec=input("ingrese una opcion")
            match selec:
                        case"1":
                            print(f"""
                                Asiento 1:{platinum[0]}
                                Asiento 2:{platinum[1]}
                                Asiento 3:{platinum[2]}
                                Asiento 4:{platinum[3]}
                                Asiento 5:{platinum[4]}
                                Asiento 6:{platinum[5]}
                                Asiento 7:{platinum[6]}
                                Asiento 8:{platinum[7]}
                                Asiento 9:{platinum[8]}
                                Asiento 10:{platinum[9]}
                                Asiento 11:{platinum[10]}
                                Asiento 12:{platinum[11]}
                                Asiento 13:{platinum[12]}
                                Asiento 14:{platinum[13]}
                                Asiento 15:{platinum[14]}
                                Asiento 16:{platinum[15]}
                                Asiento 17:{platinum[16]}
                                Asiento 18:{platinum[17]}
                                Asiento 19:{platinum[18]}
                                Asiento 20:{platinum[19]}""")
                            
                        case"2":
                            print(f"""
                                Asiento 21:{gold[0]}
                                Asiento 22:{gold[1]}
                                Asiento 23:{gold[2]}
                                Asiento 24:{gold[3]}
                                Asiento 25:{gold[4]}
                                Asiento 26:{gold[5]}
                                Asiento 27:{gold[6]}
                                Asiento 28:{gold[7]}
                                Asiento 29:{gold[8]}
                                Asiento 30:{gold[9]}
                                Asiento 31:{gold[10]}
                                Asiento 32:{gold[11]}
                                Asiento 33:{gold[12]}
                                Asiento 34:{gold[13]}
                                Asiento 35:{gold[14]}
                                Asiento 36:{gold[15]}
                                Asiento 37:{gold[16]}
                                Asiento 38:{gold[17]}
                                Asiento 39:{gold[18]}
                                Asiento 40:{gold[19]}
                                Asiento 41:{gold[20]}
                                Asiento 42:{gold[21]}
                                Asiento 43:{gold[22]}
                                Asiento 44:{gold[23]}
                                Asiento 45:{gold[24]}
                                Asiento 46:{gold[25]}
                                Asiento 47:{gold[6]}
                                Asiento 48:{gold[27]}
                                Asiento 49:{gold[28]}
                                Asiento 50:{gold[29]}
                                """)    
                        case"3":  
                                print(f"""Asiento 51:{silver[0]}
                                Asiento 52:{silver[1]}
                                Asiento 53:{silver[2]}
                                Asiento 54:{silver[3]}
                                Asiento 55:{silver[4]}
                                Asiento 56:{silver[5]}
                                Asiento 57:{silver[6]}
                                Asiento 58:{silver[7]}
                                Asiento 59:{silver[8]}
                                Asiento 60:{silver[9]}
                                Asiento 61:{silver[10]}
                                Asiento 62:{silver[11]}
                                Asiento 63:{silver[12]}
                                Asiento 64:{silver[13]}
                                Asiento 65:{silver[14]}
                                Asiento 66:{silver[15]}
                                Asiento 67:{silver[16]}
                                Asiento 68:{silver[17]}
                                Asiento 69:{silver[18]}
                                Asiento 70:{silver[19]}
                                Asiento 71:{silver[20]}
                                Asiento 72:{silver[21]}
                                Asiento 73:{silver[22]}
                                Asiento 74:{silver[23]}
                                Asiento 75:{silver[24]}
                                Asiento 76:{silver[25]}
                                Asiento 77:{silver[26]}
                                Asiento 78:{silver[27]}
                                Asiento 79:{silver[28]}
                                Asiento 80:{silver[29]}
                                Asiento 81:{silver[30]}
                                Asiento 82:{silver[31]}
                                Asiento 83:{silver[32]}
                                Asiento 84:{silver[33]}
                                Asiento 85:{silver[34]}
                                Asiento 86:{silver[35]}
                                Asiento 87:{silver[36]}
                                Asiento 88:{silver[37]}
                                Asiento 89:{silver[38]}
                                Asiento 90:{silver[39]}
                                Asiento 91:{silver[40]}
                                Asiento 92:{silver[41]}
                                Asiento 93:{silver[42]}
                                Asiento 94:{silver[43]}
                                Asiento 95:{silver[44]}
                                Asiento 96:{silver[45]}
                                Asiento 97:{silver[46]}
                                Asiento 98:{silver[47]}
                                Asiento 99:{silver[48]}
                                Asiento 100:{silver[49]}""")
        case"3":
           print("lista de asistentes: ", nombre, apellido, rut)
        case"4":   
            pass

                               
                                

                        
                

                        
        