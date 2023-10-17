
notas = []
soma = 0
media = 0

while True:
    
    entradaNota = float(input("\n\n<<--Digite o valor da Nota ou uma das opções-->>\n\n[99] encerrar programa \
        \n\n[98] calcular\n\n[97] formatar media 0~2.0 pts(caso a entrada tenha sido de 0~10.0)\n\nSua resposta -->"))

    if(entradaNota == 99):
        break
        
    elif(entradaNota == 98):
        notas.sort(reverse = True)
        numeroDeNotas = len(notas)*75//100
        
        for i in range(numeroDeNotas):
            soma = soma + notas[i]
            
        media = soma/numeroDeNotas
        print(f"A média do seu quiz é de: {media}")
    
    elif(entradaNota == 97):
        mediaFormatada = (media*2)/10
        print(mediaFormatada)

    else:
        notas.append(entradaNota)
            