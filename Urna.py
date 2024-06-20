# Atividade:

#Vamos realizar uma atividade para compor a segunda nota do segundo bimestre. Esta atividade consiste num projeto/programa de software 
# escrito na linguagem de programação Python para simular uma urna eletrônica utilizada numa eleição municipal. A eleição terá 4 
# candidados a prefeito, 10 candidatos a vereador e 40 eleitores, sendo que os eleitores podem faltar no dia da votação. O mesário 
# será o responsável por realizar a abertura da urma e o encerramento da mesma. Os eleitores podem votar nulo ou branco. Apenas 
# eleitores percententes a zona e seção de votação poderão votar na urma. No encerramento (término da eleição) será exibido o 
# resultado da eleição.

# Quais as regras para a construção do programa:

# usar linguagem python
# usar estrutura de repetição while
# usar estrutura de decisão
# não usar vetor/array
# não usar função
# Verifique qual é a sua equipe. O trabalho terá de ser autêntico da equipe.
# Plágios de solução serão desconsideradas, assim como cópias entre equipes.
# A nota máxima para esta atividade será 10 e os critérios de avaliação a serem adotados são os seguintes:
# criatividade na interface de votação
# uso da estrutura de repetição while
# uso de estruturas de decisão
# incluir comentários no código


#Definição das variáveis dos candidatos

pref1 = "Clemerson"
pref2 = "Busa"
pref3 = "Jhon"
pref4 = "Lucas Lucco"

ver1 = "Colla"
ver2 = "Honda CIVIC"
ver3 = "McLovin"
ver4 = "Panda"
ver5 = "Primo"
ver6 = "CDD"
ver7 = "Chico"
ver8 = "Pajé"
ver9 = "Pelagem"
ver10 = "Samurai"

# Definição dos números dos candidatos

Npref1 = 10
Npref2 = 20
Npref3 = 30
Npref4 = 40

Nver1 = 10000
Nver2 = 20000
Nver3 = 30000
Nver4 = 40000
Nver5 = 50000
Nver6 = 60000
Nver7 = 70000
Nver8 = 80000
Nver9 = 90000
Nver10 = 11000

# Definição das outras variáveis

zona = 244
secao = 5683
eleitores = ausentes = titulo = 0
verificador = urna = vereador = True
presenca = False

while urna:

    # looping para verificar o eleitor
    while verificador:

        verificador_presenca = input("Digite [s] para verificar o eleitor ou [n] para indicar a sua ausência: ").lower()
        
        if verificador_presenca == "s":
            zona = int(input("Verifique a zona do eleitor: "))
            secao = int(input("Verifique a seção do eleitor: "))
            
            if zona != 244 or secao != 5683:
                print("O eleitor não faz parte desta zona ou seção.")
            else:
                titulo = int(input("Digite o título do eleitor: "))
                eleitores += 1
            
            verificador = presenca = False
        
        elif verificador == "n":
            print("Ausência confirmada.")
            ausentes += 1
            verificador = False
            
        
        else:
            print("Favor digitar apenas [s] ou [n]. Tente novamente.")
            verificador = True

    # Votação do vereador
    if presenca:

        while vereador:

            voto_vereador = int(input("Digite o número do seu candidato a vereador: "))

            if voto_vereador == 10000:
                verificador_presenca = input(f"Seu candidato é: {ver1}, número: {voto_vereador}. Deseja confirmar? [s][n]")
                if verificador_presenca == "s":
                    print("Voto confirmado.")
                    vereador = False
    
    if ausentes + eleitores == 40:
        break
    
    verificador = True