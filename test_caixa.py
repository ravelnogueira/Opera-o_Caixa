from caixa import Caixa
from statuscaixa import status

def test_atende_cliente_cliente_null():
  caixa = Caixa(0)

  msg = caixa.atende_cliente(None)

  assert msg == "É preciso informar um cliente"

def test_atende_cliente_cliente_null():
  caixa = Caixa(0)
  msg = caixa.atende_cliente(None)
  assert msg == "É preciso informar um cliente"

def test_encerra_caixa_fechado():
  caixa = Caixa(0)
  caixa.status = status.DESATIVADO
  msg = caixa.encerra_caixa()
  assert msg == "Caixa já se encontra desativado"

def test_abrir_caixa():
  caixa = Caixa(0)
  msg = caixa.abrir_caixa()

  assert msg == "Caixa já está aberto"

def test_encerra_caixa_atendendo():
  caixa = Caixa(0)
  caixa.atende_cliente("joao")

  msg = caixa.encerra_caixa()

  assert msg == "Caixa Ocupado"









