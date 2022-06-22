from orquestrador import *
from caixa import * 
 
def test_atende_cliente():
  caixas = Orquestra_Caixa(4)
  cliente = 'joao'
  msg = caixas.atende_cliente(cliente)

  assert msg == f'Caixa 1 atendendo {cliente}'

def test_finaliza_atendimento():
  caixas = Orquestra_Caixa(4)
  msg = caixas.finaliza_atendimento(1)

  assert msg == "Caixa já se encontra livre"



