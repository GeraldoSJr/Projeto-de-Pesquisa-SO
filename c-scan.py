def c_scan(tamanho, posicao_atual, requisicoes):
  direcao_atual = 1
  tempo = -1
  requisicoes.sort()
  while len(requisicoes) != 0:
    if direcao_atual == 0:
      tempo += tamanho
      posicao_atual = 0
      direcao_atual = 1
    for i in range(tamanho-posicao_atual):
      tempo += 1
      if(posicao_atual in requisicoes):
        requisicoes.remove(posicao_atual)
      posicao_atual += 1
      if(len(requisicoes) == 0): break

    direcao_atual = 0
  return tempo
