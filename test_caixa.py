from caixa import Caixa

def test_atende_cliente_cliente_null():
  caixa = Caixa(0)

  msg = caixa.Atende_Cliente(None)

  assert msg == "É preciso informar um cliente"

def test_atende_cliente_cliente_null():
  caixa = Caixa(0)
  msg = caixa.Atende_Cliente(None)
  assert msg == "É preciso informar um cliente"