npcs=[["Raul",(5,15)],["Maria",(15,5)],["Carlos",(10,10)]]
maioratk=0
maiordef=0
atknome=""
defnome=""
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