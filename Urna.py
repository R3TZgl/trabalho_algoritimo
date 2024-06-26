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

votosNpref1 = votosNpref2 = votosNpref3 = votosNpref4 = votosNver1 = votosNver2 = votosNver3 = votosNver4 = votosNver5 = votosNver6 = votosNver7 = votosNver8 = votosNver9 = votosNver10 = 0

zona = 244
secao = 5683
eleitores = ausentes = titulo = nuloVer = brancoVer = nuloPref = brancoPref = 0
urna =  True
presenca = False

while urna:

    verificador_titulo = verificador = vereador = prefeito = True

    # looping para verificar o eleitor
    while verificador:

        verificador = presenca = False
        verificador_candidato = ""

        verificador_presenca = input(
            "Digite [s] para verificar o eleitor ou [n] para indicar a sua ausência: "
        ).lower()

        if verificador_presenca == "s":
            zona = int(input("Verifique a zona do eleitor: "))
            secao = int(input("Verifique a seção do eleitor: "))

            if zona != 244 or secao != 5683:
                print("O eleitor não faz parte desta zona ou seção.")
            else:
                while verificador_titulo:	
                    titulo = int(input("Digite o título do eleitor: "))                    
                    
                    #como todos os 0 antes de um outro número são desconsiderados, no caso de um título (000000000001) seria igual a (1). Por conta disso foi feito apenas um verificador para não passar os 12 dígitos
                    if titulo < 999999999999:
                    	verificador_titulo = False
                    else:
                     	print("Título inválido! O título deve conter no máximo 12 dígitos.")
                eleitores += 1
                presenca = True

        elif verificador_presenca == "n":
            print("Ausência confirmada.")
            ausentes += 1
            verificador = True
            verificador = False

        else:
            print("Favor digitar apenas [s] ou [n]. Tente novamente.")
            verificador = True

    # Votação do vereador
    if presenca:

        while vereador:

            verificador_candidato = ""

            voto_vereador = int(
                input(
                    "Digite o número do seu candidato a vereador ou 0(nulo) 1(branco): "
                ))

            if voto_vereador == 10000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver1}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False
                    votosNver1 += 1

            elif voto_vereador == 20000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver2}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False
                    votosNver2 += 1

            elif voto_vereador == 30000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver3}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False
                    votosNver3 += 1

            elif voto_vereador == 40000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver4}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False
                    votosNver4 += 1

            if voto_vereador == 50000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver5}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False
                    votosNver5 += 1

            elif voto_vereador == 60000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver6}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False
                    votosNver6 += 1

            elif voto_vereador == 70000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver7}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False
                    votosNver7 += 1

            elif voto_vereador == 80000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver8}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False
                    votosNver8 += 1

            elif voto_vereador == 90000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver9}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False
                    votosNver9 += 1

            elif voto_vereador == 11000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver10}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False
                    votosNver10 += 1

            elif voto_vereador == 0:
                verificador_candidato = input(
                    f"Seu voto é nulo. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False
                    nuloVer += 1

            elif voto_vereador == 1:
                verificador_candidato = input(
                    f"Seu voto é branco. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False
                    brancoVer += 1
            else:
            	print("Número inválido! Tente novamente.")

            # Votação do prefeito

        while prefeito:

            voto_candidato = ""

            voto_prefeito = int(input("Digite o número do seu candidato a prefeito ou 0(nulo) e 1(branco): "))

            if voto_prefeito == 10:
                verificador_candidato = input(f"Seu candidato é: {pref1}, número: {voto_prefeito}. Deseja confirmar? [s][n]")
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    prefeito = False
                    votosNpref1 += 1

            elif voto_prefeito == 20:
                verificador_candidato = input(f"Seu candidato é: {pref2}, número: {voto_prefeito}. Deseja confirmar? [s][n]")
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    prefeito = False
                    votosNpref2 += 1

            elif voto_prefeito == 30:
                verificador_candidato = input(f"Seu candidato é: {pref3}, número: {voto_prefeito}. Deseja confirmar? [s][n]")
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    prefeito = False
                    votosNpref3 += 1

            elif voto_prefeito == 40000:
                verificador_candidato = input(f"Seu candidato é: {pref4}, número: {voto_prefeito}. Deseja confirmar? [s][n]")
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    prefeito = False
                    votosNpref4 += 1

            elif voto_vereador == 0:
                verificador_candidato = input(f"Seu voto é nulo. Deseja confirmar? [s][n]")
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    prefeito = False
                    nuloPref += 1

            elif voto_vereador == 1:
                verificador_candidato = input(f"Seu voto é branco. Deseja confirmar? [s][n]")
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    prefeito = False
                    brancoPref += 1
            else:
            	print("Número inválido! Tente novamente.")

        verificador = True

    if ausentes + eleitores == 40:
        break

print("A eleições terminaram!")
print(f"Eleitores: {eleitores} \n Ausentes: {ausentes}")
print(f"Resultados da votação de Vereador: \n {ver1}: {votosNver1} \n {ver2}: {votosNver2} \n {ver3}: {votosNver3} \n {ver4}: {votosNver4} \n {ver5}: {votosNver5} \n {ver6}: {votosNver6} \n {ver7}: {votosNver7} \n {ver8}: {votosNver8} \n {ver9}: {votosNver9} \n {ver10}: {votosNver10} \n Nulos: {nuloVer} \n Brancos: {brancoVer} \n ")
print(f"Resultados da votação de Prefeito: \n {pref1}: {votosNpref1} \n {pref2}: {votosNpref2} \n {pref3}: {votosNpref3} \n {pref4}: {votosNpref4} \n Nulos: {nuloPref} \n Branco: {brancoPref} \n ")
