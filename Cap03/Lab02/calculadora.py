# Calculadora em Python

def imprimeCabecario():
	print ("\n- - - - Semissatto's  Python Calculator - - - -\n")

def imprimeOpcoes():
	print ("Selecione o número da operação desejada:\n")
	print ("1 - Soma\n")
	print ("2 - Subtração\n")
	print ("3 - Multiplicação\n")
	print ("4 - Divisão\n")

def leOpcao():
	opcao = int(input("Digite sua opção (1/2/3/4):"))
	if opcao < 5 and opcao > 0:
		return opcao
	else:
		print ("Opção inválida\n")
		return -1

def soma(arg1, arg2):
	print ( "\n%s + %s = %f" %(str(arg1), str(arg2), float(arg1)+float(arg2) ))
	return float(arg1) + float(arg2)

def subtracao(arg1, arg2):
	print ( "\n%s - %s = %f" %(str(arg1), str(arg2), float(arg1)-float(arg2) )) 
	return float(arg1) - float(arg2)

def mult(arg1, arg2):
	print ( "\n%s * %s = %f" %(str(arg1), str(arg2), float(arg1)*float(arg2) )) 
	return float(arg1) * float(arg2)

def div(arg1, arg2):
	print ( "\n%s / %s = %f" %(str(arg1), str(arg2), float(arg1)/float(arg2) )) 
	return float(arg1) / float(arg2)

# Programa principal
imprimeCabecario()
imprimeOpcoes()
opcao = leOpcao()
arg1 = float(input("Digite o primeiro número: "))
arg2 = float(input("Digite o segundo número: "))

if opcao == -1:
	quit()

elif opcao == 1:
	soma(arg1, arg2)

elif opcao == 2:
	subtracao(arg1, arg2)

elif opcao == 3:
	mult(arg1, arg2)

else:
	div(arg1, arg2)
