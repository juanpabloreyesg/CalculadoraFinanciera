# -*- coding: utf-8 -*-
import calculadora_riesgo_financiero as crf




def ejecutar_calcular_riesgo_perfiles(p1:dict, p2:dict, p3:dict, p4:dict, p5:dict)->None:
    crf.calcular_riesgo(p1)
    crf.calcular_riesgo(p2)    
    crf.calcular_riesgo(p3)
    crf.calcular_riesgo(p4)
    crf.calcular_riesgo(p5)

def ejecutar_dar_mejor_perfil(p1:dict, p2:dict, p3:dict, p4:dict, p5:dict)->None:
    mejor = crf.dar_mejor_candidato(p1, p2, p3, p4, p5)
    if mejor == None:
        print("No se ha calculado el riesgo de ninguno de los candidatos")
    else:
        print("El mejor perfil es el siguiente: \n")
        mostrar_perfil(mejor)

def mostrar_perfil(perfil:dict)->None:
    
    print("{}".format("="*40))
    print("{:30}{:>10}".format("Nombre:",perfil["Nombre"]))
    print("{:30}{:>10}".format("Apellido:",perfil["Apellido"]))
    print("{:30}{:>10}".format("Edad (Años):",perfil["Edad"]))
    print("{:30}{:>10.1f}".format("Salario mensual (Millones):",perfil["Salario Mensual"]))
    print("{:30}{:>10.1f}".format("Deuda (Millones):",perfil["Deuda"]))
    print("{:30}{:>10}".format("Categoria riesgo:",perfil["Riesgo"]))
    print("{}".format("="*40))

def iniciar_aplicacion()-> None:
    
    perfil_1 = crf.crear_perfil("Robert","Parr", 42, 2.5, 10)
    perfil_2 = crf.crear_perfil("Lucio","Best", 36, 3.5, 8)
    perfil_3 = crf.crear_perfil("Edna","Moda", 50, 17, 0)
    perfil_4 = crf.crear_perfil("Buddy","Pine", 25, 25, 50)
    perfil_5 = crf.crear_perfil("Helen","Parr", 35, 2, 0)
    
    ejecutando = True
    while ejecutando:
        mostrar_perfil(perfil_1)
        mostrar_perfil(perfil_2)
        mostrar_perfil(perfil_3)
        mostrar_perfil(perfil_4)
        mostrar_perfil(perfil_5)
        ejecutando = mostrar_menu(perfil_1, perfil_2, perfil_3, perfil_4, perfil_5)
        if ejecutando:
            input("Presione cualquier tecla para continuar ... ")

def mostrar_menu(p1:dict, p2:dict, p3:dict, p4:dict, p5:dict) -> bool:
    
    print("Menu de opciones")
    print(" 1 - Calcular la categoría de riesgo de los perfiles")
    print(" 2 - Consultar el mejor perfil para otorgar préstamo")
    print(" 3 - Salir de la aplicación")
    
    opcion_elegida = input("Ingrese la opcion que desea ejecutar: ").strip()
    
    continuar_ejecutando = True

    if opcion_elegida == "1":
        ejecutar_calcular_riesgo_perfiles(p1, p2, p3, p4, p5)
    elif opcion_elegida == "2":
        ejecutar_dar_mejor_perfil(p1, p2, p3, p4, p5)
    elif opcion_elegida == "3":
        continuar_ejecutando = False
    else:
        print("La opcion " + opcion_elegida + " no es una opcion valida.")
    
    return continuar_ejecutando

iniciar_aplicacion()

