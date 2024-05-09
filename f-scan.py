class DiscoFScan:
  def __init__(self, tamanho, posicao_atual, direcao_atual,requisicoes):
    self.tamanho = tamanho
    self.posicao_atual = posicao_atual
    self.direcao_atual = direcao_atual
    self.fila_subida = []
    self.fila_descida = []
    self.adicionar_requisicao(requisicoes)

  def getQuantSeeks(self,requisicao):
    return abs(requisicao - self.posicao_atual)

  def adicionar_requisicao(self, requisicoes):
    for requisicao in requisicoes:
      if requisicao >= self.posicao_atual:
        self.fila_subida.append(requisicao)
        self.fila_subida.sort()
      else:
        self.fila_descida.append(requisicao)
        self.fila_descida.sort(reverse=True)

  def atender_requisicao(self):
    tempo = 0
    while len(self.fila_subida) != 0 or len(self.fila_descida) != 0:
      if self.direcao_atual == 1:
        fila_atual = self.fila_subida
      else:
        fila_atual = self.fila_descida

      while(len(fila_atual) != 0):
        proxima_requisicao = fila_atual.pop(0)
        tempo += self.getQuantSeeks(proxima_requisicao)
        self.posicao_atual = proxima_requisicao

      self.direcao_atual = not self.direcao_atual

    return tempo
