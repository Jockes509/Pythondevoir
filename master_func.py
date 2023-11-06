import random
import string
import re
import unicodedata


#1) 
def enves_mo(mo):
    mo_dd=mo[::-1]
    return mo_dd

#2)
def kod_alfb_jen(n):
    cara1= string.ascii_letters
    kod_al1=''.join(random.choice(cara1) for _ in range(n))
    return kod_al1

#3) 
def kod_alfb_jen_sr(n):
    if n> 52:
        raise ValueError("nonb ou an depase nonb let alfabetik yo")
    cara2= string.ascii_letters
    kod_al2=''.join(random.sample(cara2,n))
    
    return kod_al2

#4) 
def kod_alfn_jen_sr(n):
    if n> 62:
        raise ValueError("nonb ou an depase nonb let alfanimerik yo")
    
    cara3=string.ascii_letters+string.digits
    kod_al3=''.join(random.sample(cara3,n))
                    
    return kod_al3

#5)
ch=["Steeve emmanuel","Jack boom","Jean Renau","Marie antoinette"]

def slug_jene(ch):
    ch=ch.lower()
    ch= re.sub(r'[^a-z0-9]+', '-',ch)
    ch=ch.strip('-')
    ch=unicodedata.normalize('NFD',ch).encode('ascii','ignore').decode('utf-8')
    
    return ch

#6)
mo="Ayiti"
def sep_vir(mo):
    let=[let for let in mot]
    msv=', '.join(let)
    return msv

#7)
def kripte_mo(mot):
    alfabe="abcdefghijklmnopqrstuvwxyz"
    mo_krip=[]
    
    for letr in mo:
        if letr.isalpha():
            index= alfabe.index(letr.lower())+1
            mo_krip.append(str(index))
        else:
            mo_krip.append(letr)
    
    mo_krip='-'.join(mo_krip)
    
    return mo_krip

#8)
mot_cryp="4-8-11-10-2-17"
def dekripte_mo(mot_cryp):
    alfabe="abcdefghijklmnopqrstuvwxyz"
    ind=mot_cryp.split('-')
    mo_decryp=""
    
    for indeks in ind:
        if indeks.isdigit():
            indeks=int(indeks)-1
            if 0<=indeks<len(alfabe):
                let=alfabe[indeks]
                mo_decryp+= let
            else:
                mo_decryp+= '?'
        else:
            mo_decryp+=indeks
    
    return mo_decryp

#9) 
def permute_val(a,b):
    a,b=b,a
    
    return (a,b)

#10)
def non_inisyal(non):
    inisyal=[]
    for nom in non:
        non_konp=nom.split('-')
        inisyal_non=''.join([part[0] for part in non_konp if part])
        inisyal.append(inisyal_non)
    
    return inisyal
       


