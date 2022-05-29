def analisar():
    Linha_de_teste = input(str("Informe a Expreção: "))
    token = ""
    Linha = []

    Alpha=['a', 'e', 'i', 'o', 'u', 'b', 'c', 'd',' f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x','z']
    number = ['1','2','3','4','5','6','7','8','9','0'] 
    Operators = ['+','-','/','*'] 

    while(True):

        for i in Linha_de_teste:
            
            if(i in  Alpha):
                if(token == ""):
                    token = token + i  
                elif(token[0] in Alpha):
                    token = token + i
                else:
                    Linha.append(token)
                    token = "" + i      
            
            if(i in number):
                if(token == ""):
                    token = token + i  
                elif(token[0] in number):
                    token = token + i
                else:
                    Linha.append(token)
                    token = "" + i
            
            if(i in Operators):
                
                if(token == ""):
                    token = token + i 
                elif(token[0] in Operators):
                    token = token + i
                    
                else:
                    Linha.append(token)
                    token = "" + i
            
            if(i == " "):
                Linha.append(token)
                token = ""

        if(token != ""):
            Linha.append(token)
        
        break
    return Linha