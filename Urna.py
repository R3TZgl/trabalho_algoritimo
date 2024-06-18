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

#Definição dos números dos candidatos

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

#Definição das outras variáveis

zona = 244
secao = 5683
eleitores = 0
titulo = 0

while True:

    situacao = input("Digite [s] para inserir o título do eleitor ou [n] para indicar a sua ausência:").lower()
    if situacao == "s":
        titulo = int(input("Digite o título do eleitor: "))
    break
