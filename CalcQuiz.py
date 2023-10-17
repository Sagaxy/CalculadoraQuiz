import os

clear = lambda:os.system("cls")
notas = []
soma = 0
media = 0

print("\n\n#### CERTIFIQUE SE DE QUE ESCREVEU UMA DAS OPÇÕES ####\n")


while True:
    try:
        print("/==========================================\\")
        print("| Digite o valor da nota OU uma das opções |")
        print("\\==========================================/")
        print(f"notas:{notas}")
        
        entradaNota = input("\n[E] encerrar programa\n\n[C] calcular\n\n[F] formatar media formato 2.0 pts\n\nSua resposta -->")

        if(entradaNota == "e" or entradaNota == "E"):
            break
            
        elif(entradaNota == "c" or entradaNota == "C"):
            notas.sort(reverse = True)
            numeroDeNotas = len(notas*75)//100
            
            for i in range(numeroDeNotas):
                soma = soma + notas[i]
                
            media = soma/numeroDeNotas
            clear()
            print(f"\n\n#####A média do seu quiz é de: {media} ####\n\n")
        
        elif(entradaNota == "f" or entradaNota == "F"):
            mediaFormatada = (media*0.2)
            print(mediaFormatada)
            break

        else:
            entradaNota = float(entradaNota)
            notas.append(entradaNota)
            clear()
    except:
        clear()
        print("\n\n<<RESPOSTA INVÁLIDA, TU É BURRO?>>\n\n")