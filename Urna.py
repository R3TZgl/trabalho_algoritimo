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
verificador = urna = vereador = prefeito = True
presenca = False

while urna:

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
                titulo = int(input("Digite o título do eleitor: "))
                eleitores += 1
                presenca = True

        elif verificador_presenca == "n":
            print("Ausência confirmada.")
            ausentes += 1

        else:
            print("Favor digitar apenas [s] ou [n]. Tente novamente.")
            verificador = True

    # Votação do vereador
    if presenca:

        while vereador:

            voto_vereador = int(
                input("Digite o número do seu candidato a vereador: "))

            if voto_vereador == 10000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver1}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False

            if voto_vereador == 20000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver2}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False

            if voto_vereador == 30000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver3}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False

            if voto_vereador == 40000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver4}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False

            if voto_vereador == 50000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver5}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False

            if voto_vereador == 60000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver6}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False

            if voto_vereador == 70000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver7}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False

            if voto_vereador == 80000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver8}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False

            if voto_vereador == 90000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver9}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False

            if voto_vereador == 11000:
                verificador_candidato = input(
                    f"Seu candidato é: {ver10}, número: {voto_vereador}. Deseja confirmar? [s][n]"
                )
                if verificador_candidato == "s":
                    print("Voto confirmado.")
                    vereador = False

            # Votação do prefeito

            while prefeito:

                voto_prefeito = int(
                    input("Digite o número do seu candidato a vereador: "))

                if voto_prefeito == 10:
                    verificador_candidato = input(
                        f"Seu candidato é: {pref1}, número: {voto_prefeito}. Deseja confirmar? [s][n]"
                    )
                    if verificador_candidato == "s":
                        print("Voto confirmado.")
                        prefeito = False

                if voto_prefeito == 20:
                    verificador_candidato = input(
                        f"Seu candidato é: {pref2}, número: {voto_prefeito}. Deseja confirmar? [s][n]"
                    )
                    if verificador_candidato == "s":
                        print("Voto confirmado.")
                        prefeito = False

                if voto_prefeito == 30:
                    verificador_candidato = input(
                        f"Seu candidato é: {pref3}, número: {voto_prefeito}. Deseja confirmar? [s][n]"
                    )
                    if verificador_candidato == "s":
                        print("Voto confirmado.")
                        prefeito = False

                if voto_prefeito == 40000:
                    verificador_candidato = input(
                        f"Seu candidato é: {pref4}, número: {voto_prefeito}. Deseja confirmar? [s][n]"
                    )
                    if verificador_candidato == "s":
                        print("Voto confirmado.")
                        prefeito = False

            verificador = True

    if ausentes + eleitores == 40:
        print(
            f"Eleição concluida. Total de {eleitores} eleitores presentes e {ausentes} ausentes."
        )
        break
