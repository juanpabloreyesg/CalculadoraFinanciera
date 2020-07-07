# -*- coding: utf-8 -*-

def crear_perfil(nombre:str, apellido:str, edad:int, salario_mensual:float, deuda: float):
    return {"Nombre":nombre, "Apellido":apellido, "Edad":edad, "Salario Mensual": salario_mensual, "Deuda":deuda, "Riesgo":"NA"}

def calcular_riesgo(perfil:dict)->None:    
    if perfil["Edad"] < 40:
        if perfil["Salario Mensual"] < 2:
            perfil["Riesgo"] = "C"
        else:
            if perfil["Deuda"] > 1.5*perfil["Salario Mensual"]*12:
                perfil["Riesgo"] = "C"
            else:
                perfil["Riesgo"] = "B"
    else:
        if perfil["Salario Mensual"] < 3.5:
            perfil["Riesgo"] = "C"
        elif perfil["Salario Mensual"] >= 3.5 and perfil["Salario Mensual"] <= 5:
            if perfil["Deuda"] > perfil["Salario Mensual"]*12:
                perfil["Riesgo"] = "B"
            else: 
                perfil["Riesgo"] = "A"
        else:
            if perfil["Deuda"] > 0.8*perfil["Salario Mensual"]*12:
                perfil["Riesgo"] = "B"
            else:
                perfil["Riesgo"] = "A"
                
                
def dar_mejor_candidato(p1:dict, p2:dict, p3:dict, p4:dict, p5:dict)-> dict:
    
    if p1["Riesgo"] == "NA" and p2["Riesgo"] == "NA" and p3["Riesgo"] == "NA" and p4["Riesgo"] == "NA" and p5["Riesgo"] == "NA":
        return None
    else:
        mejor = p1
        
        if mejor["Riesgo"] > p2["Riesgo"]:
            mejor = p2
        if mejor["Riesgo"] > p3["Riesgo"]:
            mejor = p3
        if mejor["Riesgo"] > p4["Riesgo"]:
            mejor = p4
        if mejor["Riesgo"] > p5["Riesgo"]:
            mejor = p5
            
        return mejor
    
    
    