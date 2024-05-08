def cscan(disco, requisicoes):
  requisicoes.sort()
  respostas = []
  tempo = 0
  seeks_realizados = -1
  rotacoes = 0

  while(len(requisicoes) != 0):
    #definindo as trilhas que serão percorridas a partir do bloco atual e da direção atual
    if(disco.direcao_atual == 1):
      trilhas_a_serem_varridas = [trilha for i, trilha in enumerate(disco.trilhas) if i >= disco.get_index_trilha_atual()]
    else:
     trilhas_a_serem_varridas = [trilha for i, trilha in enumerate(disco.trilhas) if i <= disco.get_index_trilha_atual()]
     trilhas_a_serem_varridas = trilhas_a_serem_varridas[::-1]

    #percorrendo cada trilha do disco que estã na direção de leitura
    for index, trilha in enumerate(trilhas_a_serem_varridas):
      rotacoes += 1
      seeks_realizados += 1
      #reordenando a lista para que o primeiro elemento seja o bloco atual
      indice_x = trilha.index(disco.bloco_atual)
      trilha_formatada = trilha[indice_x:] + trilha[:indice_x]

      #verificando se o bloco que esta sendo lido esta na lista de requisições
      for bloco in trilha_formatada:
        #armazenando a ordem das respostas
        if(bloco in requisicoes):
          respostas.append(bloco)
          requisicoes.remove(bloco)
      if(index == len(trilhas_a_serem_varridas) - 1): #se for a ultima trilha da direção a ser varrida, mudar o bloco atual para algum da trilha anterior
        if(disco.direcao_atual == 1):
          disco.bloco_atual = min(trilha_formatada) - 1
        else:
          disco.bloco_atual = max(trilha_formatada) + 1
      else:
        if(disco.direcao_atual == 1):
          disco.bloco_atual = max(trilha_formatada) + 1
        else:
          disco.bloco_atual = min(trilha_formatada) - 1
  
    #mudar a direção de leitura
    disco.direcao_atual = not disco.direcao_atual
  
  tempo = rotacoes * disco.get_tempo_rotacao() + seeks_realizados * disco.get_tempo_seek()

  print("Tempo total:", tempo)
  print("Seeks:", seeks_realizados)
