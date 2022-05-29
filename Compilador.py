#pip install tabulate
from tabulate import tabulate
import Analisador

listaTeste = Analisador.analisar()

regraGlobal = {  "E id": "ST",
                 "E num": "ST",
                 "E (": "ST",
                 "T id": "GF",
                 "T num": "GF",
                 "T (": "GF",
                 "S +": "ST+",
                 "S -": "ST-",
                 "S )": "",
                 "S $": "",
                 "G +": "",
                 "G -": "",
                 "G *": "GF*",
                 "G /": "GF/",
                 "G )": "",
                 "G $": "",
                 "F id":"id",
                 "F num":"num",
                 "F (":")E("
                 }

PILHA = "$E"
listaTeste.append("$")
CADEIA= listaTeste
elemento = (PILHA[len(PILHA)-1]) +" "+ CADEIA[0]
REGRA=(f"{elemento[0]}->{regraGlobal[elemento][::-1]}")
PrintGlobal = []
headers=["PILHA","CADEIA","REGRA"]
PrintGlobal.append([PILHA,str(CADEIA),REGRA])
vToken=["id","num","+","-","*","/"]
erro = ["E id","E num","E (","T id","T num","T (","S +","S -",
        "S )","S $","G +","G -","G *","G /","G )","G $","F id","F num","F ("]

while(True):
    
    if(elemento == "E id"):
        PILHA = PILHA[:len(PILHA)-1]
        PILHA=PILHA+regraGlobal[elemento]
        
    elif(elemento == "E num"):
        PILHA = PILHA[:len(PILHA)-1]
        PILHA=PILHA+regraGlobal[elemento]
        
    elif(elemento == "E ("):
        PILHA = PILHA[:len(PILHA)-1]
        PILHA=PILHA+regraGlobal[elemento]
        
    elif(elemento == "T id"):
        PILHA = PILHA[:len(PILHA)-1]
        PILHA=PILHA+regraGlobal[elemento]
        
    elif(elemento == "T num"):
        PILHA = PILHA[:len(PILHA)-1]
        PILHA=PILHA+regraGlobal[elemento]
        
    elif(elemento == "T ("):
        PILHA = PILHA[:len(PILHA)-1]
        PILHA=PILHA+regraGlobal[elemento]
        
    elif(elemento == "S +"):
        PILHA = PILHA[:len(PILHA)-1]
        PILHA=PILHA+regraGlobal[elemento]
        
        REGRA="----"
        PrintGlobal.append([PILHA,str(CADEIA),REGRA])
        PILHA=PILHA[:len(PILHA)-1]
        
        listaTeste.pop(0)
    elif(elemento == "S -"):
        PILHA = PILHA[:len(PILHA)-1]
        PILHA=PILHA+regraGlobal[elemento]
        
        REGRA="----"
        PrintGlobal.append([PILHA,str(CADEIA),REGRA])
        PILHA=PILHA[:len(PILHA)-1]
        
        listaTeste.pop(0)
    elif(elemento == "S )"):
        PILHA = PILHA[:len(PILHA)-1]
        PILHA=PILHA+regraGlobal[elemento]
        
    elif(elemento == "S $"):
        PILHA = PILHA[:len(PILHA)-1]
        PILHA=PILHA+regraGlobal[elemento]
        
    elif(elemento == "G +"):
        PILHA = PILHA[:len(PILHA)-1]
        PILHA=PILHA+regraGlobal[elemento]
        
    elif(elemento == "G -"):
        PILHA = PILHA[:len(PILHA)-1]
        PILHA=PILHA+regraGlobal[elemento]
        
    elif(elemento == "G *"):
        PILHA = PILHA[:len(PILHA)-1]
        PILHA=PILHA+regraGlobal[elemento]
        
        REGRA="----"
        PrintGlobal.append([PILHA,str(CADEIA),REGRA])
        PILHA=PILHA[:len(PILHA)-1]
        
        listaTeste.pop(0)
    elif(elemento == "G /"):
        PILHA = PILHA[:len(PILHA)-1]
        PILHA=PILHA+regraGlobal[elemento]
        
        REGRA="----"
        PrintGlobal.append([PILHA,str(CADEIA),REGRA])
        PILHA=PILHA[:len(PILHA)-1]
        
        listaTeste.pop(0)
    elif(elemento == "G )"):
        PILHA = PILHA[:len(PILHA)-1]
        PILHA=PILHA+regraGlobal[elemento]
        
    elif(elemento == "G $"):
        PILHA = PILHA[:len(PILHA)-1]
        PILHA=PILHA+regraGlobal[elemento]
        
    elif(elemento == "F id"):
        PILHA = PILHA[:len(PILHA)-1]
        PILHA=PILHA+regraGlobal[elemento]

        REGRA="----"
        PrintGlobal.append([PILHA,str(CADEIA),REGRA])
        PILHA=PILHA[:len(PILHA)-2]
        
        listaTeste.pop(0)
    elif(elemento == "F num"):
        PILHA = PILHA[:len(PILHA)-1]
        PILHA=PILHA+regraGlobal[elemento]
        
        REGRA="----"
        PrintGlobal.append([PILHA,str(CADEIA),REGRA])
        PILHA=PILHA[:len(PILHA)-3]
        
        listaTeste.pop(0)
    elif(elemento == "F ("):
        PILHA = PILHA[:len(PILHA)-1]
        PILHA=PILHA+regraGlobal[elemento]


    elemento = (PILHA[len(PILHA)-1]) +" "+ CADEIA[0]
    
    
    if(elemento == "$ $"):
        REGRA="Sucesso"
        PrintGlobal.append([PILHA,str(CADEIA),REGRA])
        print(tabulate(PrintGlobal,headers,tablefmt="pipe"))
        break
    if (elemento not in erro):
            REGRA="Erro"
            PrintGlobal.append([PILHA,str(CADEIA),REGRA])
            print(tabulate(PrintGlobal,headers,tablefmt="pipe"))
            break 

    if(regraGlobal[elemento] in vToken):
        REGRA=(f"{elemento[0]}->{regraGlobal[elemento]}")
        PrintGlobal.append([PILHA,str(CADEIA),REGRA])
    elif(regraGlobal[elemento] == ""):
        REGRA=(f"{elemento[0]}-> λ")
        PrintGlobal.append([PILHA,str(CADEIA),REGRA])
    else:
        REGRA=(f"{elemento[0]}->{regraGlobal[elemento][::-1]}")
        PrintGlobal.append([PILHA,str(CADEIA),REGRA])