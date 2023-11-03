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
