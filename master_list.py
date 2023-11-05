#1) 
ld2=[]

n=100
for nbr in range (n+1):
    if nbr%2==0:
        ld2.append(nbr)
print("la liste des eleents divisible par 2 est: ",ld2)
        
#2)
list_int=[3,6,9,4,6,7,78,1]
list_ch=[str(int) for int in list_int]
print("liste converti: ",list_ch)

#3)
list_min=["mwen","ou","nou","albert","bens"]
list_maj=[a.upper() for a in list_min]
print("La liste en majuscule ",list_maj)

#4)
list_int2=list(range(21))
list_d3=[x for x, int2 in enumerate(list_int2) if int2 %3==0 ]
print("indx des elements divisible par 3: ",list_d3)

#5)

list_tuple=[(list_int2[c], list_int2[c+1], list_int2[c+2]) for c in range(0, len(list_int2), 3)]
print("Liste groupe tuple: ",list_tuple)

#6)
list_doublon=[1,1,1,2,2,3,4,5,6,6,6,7,7,8,8,8,8]
list_s_doub=list(set(list_doublon))

print("voici la liste sans doublon: ",list_s_doub)


#7)
l1=[1,4,4,5,6,7,8,9]
l2=[1,4,8,2,3]

e1=set(l1)
e2=set(l2)

list_commun= list(e1.intersection(e2))
print("Men lis ki gen elemean commun yo: ",list_commun)

#8)
list_distinct=list(e1.symmetric_difference(e2))
print("Men lis eleman distinct yo: ",list_distinct)

#9)
dictio={"Nom":"Gui","Prenom":"Hat","Sexe":"F","tel":"34567890","adres":"delmas 20"}

kle=list(dictio.keys())
vale=list(dictio.values())

print("Liste des cles: ",kle)
print("Liste des valeurs: ",vale)

#10)
lis_a=[1,2,3]
lis_b=[4,5,6]
lis_c=[7,8,9]

a_1=set(lis_a)
a_2=set(lis_b)
a_3=set(lis_c)

a_yo=a_1.union(a_2,a_3)

tout_lis=list(a_yo)

print("Men 3 lis yo reuni: ",tout_lis)


