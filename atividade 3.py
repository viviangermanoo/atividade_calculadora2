def calculadora(num1, num2, operacao):
   
  if operacao == 1:
        return num1 + num2  
  elif operacao == 2:
        return num1 - num2  
  elif operacao == 3:
        return num1 * num2  
  elif operacao == 4:
        return num1/num2
    if num2 == 0:
        return "Erro: Divisão por zero"  
    return num1 / num2 
  else:
        return 0 
executar ==True
while (executar == True):
     print("Insira aqui um número equivalente a operação que deseja realizar:")
     print("1 - Adição")
     print("2 - Subtração")
     print("3 - Multiplicação")
     print("4 - Divisão") 
     print("5 - NENHUM") 
     operacao = int (input())       
     if (operacao < 0) or (operacao > 4):
      print("Escolha apenas números entre 1 a 4!!")
      elif (operacao= 0):
            executar = False
      else:
            print("Insira aqui um número:")
            num1 = int(input())
            print("Agora outro número:")
            num2 = int(input())
            total= calculadora(num1,num2, operacao)
            print("Seu resultado foi:", resultado)
