from os import stat
from wsgiref.validate import InputWrapper
from statuscaixa import status
from cliente import Cliente

resposta_Encerramento_Afirmativa = ["SIM","sim","s"]
resposta_Encerramento_Negativa = ["não","Não","nao","n"]

class Caixa():
  def __init__(self, numero):
    self.numero = numero
    self.status = status.LIVRE
    self.Total_Atendimentos = 0
 
  def atende_cliente(self, cliente:Cliente)->str:
    if (cliente == None):
      return "É preciso informar um cliente"
    
    if (self.status == status.OCUPADO):
      return "Caixa Ocupado"
    
    if (self.status == status.DESATIVADO):
      return "Caixa fora do ar"
    
    else:
      self.cliente = cliente
      self.status = status.OCUPADO
      return "OK"

  def finaliza_atendimento(self):
    if(self.status == status.OCUPADO):
      self.status = status.LIVRE
      self.Total_Atendimentos +=1
      return
    
    if(self.status == status.DESATIVADO):
      return "Caixa desativado"
      
  def encerra_caixa(self):
    if(self.status == status.DESATIVADO):
      return "Caixa já se encontra desativado"

    if(self.status == status.OCUPADO):
          return "Caixa Ocupado"
    else:
      self.status == status.DESATIVADO

  def abrir_caixa(self):
    if(self.status != status.DESATIVADO):
      return "Caixa já está aberto"

    else:
      self.status = status.LIVRE


  def Mostrar_estatistica(self):
    return self.Total_Atendimentos
  
  def Mostrar_Status(self):
    return self.status

  def esta_disponivel(self):
    return self.status == status.LIVRE

