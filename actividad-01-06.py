import os,time
os.system("cls")

vacantes = 20
accesos = True
correos = []
postulantes = []

while accesos:
    try:
        print("=== SISTEMA DE POSTULACIÓN MAGÍSTER ===")
        print("")
        print("1. Registrar postulante")
        print("2. Ver postulantes registrados")
        print("3. Buscar postulante por correo")
        print("4. Ver postulantes aceptados")
        print("5. Ver estadísticas")
        print("6. Mostrar vacantes disponibles")
        print("7. Salir")
        time.sleep(2)

        opcion = 0
        while opcion not in [1,2,3,4,5,6,7]:
            opcion = int(input("\nIngrese opcion: "))
        
        if opcion == 1:
            while True: 
                nombre = input("Ingrese su nombre: \n").title()
                if nombre.isalpha() and len(nombre) > 0:
                    break
                else:
                    print("nombre invalido. Debe contener solo letras")
            while True: 
                apellido = input("Ingrese su apellido: \n").title()
                if apellido.isalpha() and len(apellido) > 0:
                    break
                else:
                    print("apellido invalido. Debe contener solo letras")
            edad = 0
            while 17 >= edad <= 60:
                edad = int(input("Ingrese su edad: "))
                if  17 > edad < 60:
                    print("La edad debe estar entre 17 y 60")
            
            correo = " "
            accesocrreo = True
            while accesocrreo:
                flag = True
                for i in correos:
                    if i == correo:
                        flag = False
                if "@" in correo and "." in correo and " " not in correo:
                    break
                correo = str(input("Ingrese su correo electronico: "))
            correos.append(correo)


            carrera = str(input("ingrese la carrera de origen: "))
            promedio = 0
            while 1 > promedio < 7:
                promedio = int(input("Ingrese su promedio de notas: "))
                if 1 > promedio < 7:
                    print("Su promedio debe estar entre 1 y 7")
            vacantes -= 1
            
            if promedio >5.5 and edad >= 20 and vacantes >= 1:
                estado = "ACEPTADO"
            else:
                estado = "RECHAZADO"

            postulante = {"nombre": nombre,"apellido": apellido,"edad": edad,"correo": correo,"carrera": carrera,"promedio": promedio,"estado": estado}
            postulantes.append(postulante)
            print("")
            time.sleep(2)

        elif opcion == 2:
            if len(postulantes) > 0: 
                for x in postulantes:
                    print(f"Nombre completo: {p["nombre"]} {p["apellido"]}")
                    print(f"Edad: {p["edad"]}")
                    print(f"Correo: {p["correo"]}")
                    print(f"Carrera: {p["carrera"]}")
                    print(f"Promedio: {p["promedio"]}")
                    print(f"Estado: {p["estado"]}")
                    print("******************")
        elif opcion == 3:
            print("hola")
        elif opcion == 4:
            print("hola")
        elif opcion == 5:
            print("hola")
        elif opcion == 6:
            print("hola")
        else:
            break
    except:
        print("\nDatos no validos, intente denuevo\n")
        time.sleep(2)

