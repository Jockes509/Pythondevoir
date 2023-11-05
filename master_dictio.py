#1) 
diction={"Nom":"Jean","Prenom":"Manille","Sexe":"M","tel":5678890}
lis_val=[]

for k in diction: 
    val=diction[k]
    lis_val.append(val)
    
print("Men lis vale yo: ",lis_val)
print() 
#2) 
val_user= input("antre yon vale svp: ")

if val_user.startswith("{") and val_user.endswith("}"):
    print(f"vale '{val_user}' gen akolad ni devan ni deye")
else:
    print(f"vale '{val_user}' pa gen akolad ni devan ni deye")

#3) 
for kle in diction:
    print("Men kle yo: ",kle)

print("")

#4)
for vale in diction.values():
    print("Men vale yo: ",vale)
print()

#5)
dic_kopi= diction.copy()

print("Men ezilta kopi an: ",dic_kopi)
print()

#6)
for ky,valu in diction.items():
    if isinstance(valu,str):
        diction[ky]=f"_{valu}_"

print("Men rezilta ak underscore an",diction)

#7)
dictionar= {"pt1":"12", "pt2":"44","pt3":"39"}

n_dic={}

for kl, vl in dictionar.items():
    if vl.isdigit():
        n_dic[kl]=vl

print("Men nouvo diksyone a: ",n_dic)
print()
#8)
dico= {"nom": "paula", "prenom":"dicaprio","sexe":"f","date-n":"2000"}

list_tup= [(kle,vale) for kle, vale in dico.items()]
print("resultat #8: ",list_tup)
print()

#9)
tuple1=list_tup

dico2={}

for clave, valor in tuple1: 
    dico2[clave]= valor
print("Dico2 steeve: ",dico2)
    
print("Le dictionnaire: ",dico2)

#10)

