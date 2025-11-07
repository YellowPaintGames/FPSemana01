npcs=[[],[],[]]
maioratk=0
maiordef=0
atknome=""
defnome=""
counter=0
while counter<3:
    nome=input("Nome do player: ")
    atk=int(input("Ataque: "))
    defs=int(input("Defesa: "))
    npcs[counter]=[nome,(atk,defs)]
    counter+=1
for i in npcs:
    atk,defs=i[1]
    print(i[0])
    print(atk)
    print(defs)
    if atk>maioratk:
        maioratk=atk
        atknome=i[0]
    if defs>maiordef:
        defnome=i[0]
        maiordef=defs
print("Maior ataque: ",atknome," com ",maioratk," pontos de ataque")
print("Maior defesa: ",defnome," com ",maiordef," pontos de defesa")