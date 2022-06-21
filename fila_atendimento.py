from cliente import Cliente
class FilaAtendimento:
  def __init__(self):
    self.fila = []

  def proximo_cliente(self):
    if (len(self.fila) == 0):
      return None

    return self.fila.pop(0)

  def fim_fila(self, cliente:Cliente):
    self.fila.append(cliente)
  
  def tamanho_fila(self):
    return len(self.fila)
