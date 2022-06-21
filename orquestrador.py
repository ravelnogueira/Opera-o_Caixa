from typing import NoReturn, List
from caixa import Caixa
from cliente import Cliente
from fila_atendimento import FilaAtendimento

class Orquestra_Caixa():

  def __init__(self, numero_caixas: int)->None:
    self.numero_caixas:int = numero_caixas
    self.fila_espera:FilaAtendimento = FilaAtendimento()
    self.lista_caixas:List[Caixa] = []
    for i in range(numero_caixas):
      self.lista_caixas.append(Caixa(i+1))

  def atende_cliente(self, cliente: Cliente):
    for caixa in self.lista_caixas:
      if (caixa.esta_disponivel()):
        caixa.Atende_Cliente(cliente)
        return
    self.fila_espera.fim_fila(cliente)
    print(f'{cliente} foi para a fila')

  def finaliza_atendimento(self, numero_caixa: int):
    caixa = self.lista_caixas[numero_caixa-1]

    msg = caixa.finaliza_atendimento()
    if (msg == "OK"):
      print (msg)
      return

    if (self.fila_espera.tamanho_fila() > 0):
      cliente = self.fila_espera.proximo_cliente()
      self.atende_cliente(cliente)
      print(f'Atendedendo {cliente}, restam {self.fila_espera.tamanho_fila()} na fila')
  
  def mostra_numero_caixa(self):
    return len(self.lista_caixas)
  
  def teste(self):
    print(self.fila_espera.tamanho_fila())

        
caixa = Orquestra_Caixa(4)

caixa.mostra_numero_caixa()
caixa.atende_cliente("Ravel")
caixa.atende_cliente("Toninho")
caixa.atende_cliente("Aureo")
caixa.atende_cliente("Marinho")
caixa.atende_cliente("Villarim")
caixa.atende_cliente("Patricia")

caixa.teste()
caixa.finaliza_atendimento(3)
caixa.finaliza_atendimento(4)
caixa.mostra_numero_caixa().__str__()
