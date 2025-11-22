
# Nossa aplicação tem o objetivo de utilizar uma base de dados semisestruturada do dados.gov
# A base escolhida foi a de Salas da Ancine por todo o país 
# Diante disso escolhemos a temática de analisar os dados e descobrimos que daria para fazer uma análise de dados com relação a 
# Acessibilidade das salas
# Usando: ASSENTOS_CADEIRANTES, ASSENTOS_MOBILIDADE_REDUZIDA, ASSENTOS_OBESIDADE, ACESSO_ASSENTOS_COM_RAMPA, ACESSO_SALA_COM_RAMPA, BANHEIROS_ACESSIVEIS
# Como  Análises possíveis: 
# Quais estados possuem salas mais acessíveis? 
# Percentual de salas com acessibilidade completa?
# Quais cidades têm melhores condições para pessoas com necessidades especiais?

def selecaoDecolunas():
    return
def analiseEstados():
    return
def percentualSalaComacessebilidade():
    return
def melhoresCidades():
    return
def menu():
    print("===== MENU DE OPÇÕES =====\n")
    print("1- ANALISAR POR ESTADO\n2- PERCENTUAL SALA COM ACESSIBILIDADE\n3- MELHORES CIDADES COM ACESSIBILIDADE\n0- SAIR")

    escolha = int(input("DIGITE SUA OPÇÃO PARA NAVEGAR: "))

    while escolha != 0:
        if escolha == 1:
            print("EXIBINDO ANÁLISE POR ESTADOS...")
            analiseEstados()
        elif escolha == 2:
            print("EXIBINDO ANÁLISE POR PERCENTUAL DE SALAS COM ACESSIBILIDADE...")
            percentualSalaComacessebilidade()
        elif escolha == 3:
            print("EXIBINDO ANÁLISE DE MELHORES CIDADES COM ACESSIBILIDADE...")
            melhoresCidades()
        else:
            print("VOCÊ DIGITOU ALGO INVÁLIDO! TENTE NOVAMENTE")

        escolha = int(input("DIGITE SUA OPÇÃO PARA NAVEGAR: "))

    print("SAINDO...")
    
menu()