import datetime
import locale

locale.setlocale(locale.LC_ALL, 'pt_BR.utf8')

# CAMINHO ONDE ESTA O TXT (REGISTRO)
caminho_do_arquivo_txt = r'\\SRV-COLIBRI\Users\Public\Documents\solicitacao_de_compra.txt'

# PEDIR O NOME DO FUCIONARIO
instruções_exec = input ("Olá, use o exemplo abaixo para fazer seu pedido\nPor favor, informe o seu nome: RAFAEL\nQue produto você quer solicitar e qual a quantidade?(Utilize apenas virgulas): 5KG QUIABO, 5KG VAGEM\nPara qual dia e hora? (formato dd/mm): 28/MARCO\nPressione ENTER para iniciar\n\n")
nome_funcionario = input("Por favor, informe o seu nome: ")

# PUXAR A DATA AUTOMATICO DO PC
agora = datetime.datetime.now()

# FORMATAR DATA E HORA
data_atual = agora.strftime("%d/%m/%Y")
hora_atual = agora.strftime("%H:%M:%S")

# registro da solicitação
with open(caminho_do_arquivo_txt, "a") as arquivo:
    # INFORMAÇÕES - PRODUTO/HORA/AVISO SOLICITANTE
    produto_qtd = input("Que produto você quer solicitar e qual a quantidade?: ")
    dia_hora = input("Para qual dia e hora? (formato dd/mm): " )
   

    #while dia_hora < data_atual:   
        #dia_hora = input("Insira a data correta: ")
        #if dia_hora >= data_atual:
           #break
    pedido_realizado = input("Seu pedido foi realizado com sucesso!\nPRESSIONE ENTER PARA SAIR")
    arquivo.write(f"{data_atual},{nome_funcionario} solicitou para o dia {dia_hora}:,{produto_qtd}\n\n")

