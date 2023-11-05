# MASTER STR (index, split, replace, lower, upper, title)

cara="Ayiti Ak Rep Dominiken"
# 1)
cara_lower=cara.lower()
print(cara_lower)

#2) 
cara_split=cara.split()
print(cara_split)

#3)
cara_title=cara.title()
print(cara_title)

#4)
cara_join= ''.join(word[0] for word in cara.split())
print(cara_join)

#5)
cara_replace=cara.replace('A','@')
print(cara_replace)

#6)
cara_inverse= cara[::-1]
cara_upper=cara_inverse.upper()
print(cara_upper)


#7) 
cara2="for another love"
cara_index= cara2.find('a')
if cara_index !=-1:
    print("the index for the first letter a is: ",cara_index)

#8) 
indexTot=0
for i, ca in enumerate(cara):
    if ca=='a' or ca=='A':
        indexTot+=i
print("Total tout index karakte a nan chen lan se: ",indexTot)

#9)
inda=[]
for ind, car in enumerate(cara):
    if car.lower()=='a':
        inda.append(ind)
print("Men lis index karaakte a yo: ",inda)

#10)
cse= cara.replace(' ','')
print(cse)
