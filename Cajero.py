from os import system
import string

def Principal():
    print("------------------------")
    print("*  Ismael Paulino #27  *")
    print("*  Cajero automatico.  *")
    print("------------------------")
    pin = '1234'
    monto = 100000
    entrada = str(input("Ingrese el pin de acceso: "))
    if entrada == pin:
        print("--------------------------")
        print("*     Menu principal     *")
        print("--------------------------")
        print("* 1. Depositar.          *")
        print("* 2. Retirar.            *")
        print("--------------------------")
        op = int(input("Elije la opcion que deseas hacer: "))
    else: 
        print("------------------------------------")
        print("* Pin incorrecto, intente de nuevo *")
        print("------------------------------------")
        system("pause")
        system("cls")
        return Principal()
        

    if op == 1:
        deposito = int(input("Ingrese la cantidad que quieres depositar: "))
        monto = monto + deposito
        print(f"Su monto actualizado es: {monto}")

    elif op == 2:
        retirar = int(input("Ingrese la cantidad que quieres retirar: "))
        if retirar > monto:
            print("\nEl retiro exede su monto actual")
            system("pause")
            system("cls")
            return Principal()
        else:
            monto = monto - retirar
            print(f"\nSu monto actualizado es: {monto}")
    else: 
        print("La opcion es invalida.")

    
    print("Desea salir:")
    print("1. Si")
    print("2. No")
    op = input("Elige una opcion: ")
        
            
    if op == "2":
        system("cls")
        return Principal()
        
Principal()