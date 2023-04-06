from math import*
def Pile():
    return []

def Vide(P):
    return len(P)==0

def empiller(x,P):
    P.append(x)

def depiller(P):
    return P.pop()

def sommet(P):
    return P[-1]

def taille(P):
    return len(p)


def NPI(P):
    assert type(P)==list,'P doit être une liste'
    assert type(P[0])==int or type(P[0])==float, 'Le premier terme de votre liste doit être de type int ou float'
    assert type(P[1])==int or type(P[1])==float or type(P[1])=='v', 'Le deuxième terme de votre liste doit être de type int, float ou être v qui signifie racine carré'
    assert type(P[-1])==str,'Le dernier terme de votre liste doit être un opérateur de type str'
    pile=[]
    for i in range(len(P)):
        if type(P[i])==int or type(P[i])==float:
            empiller(P[i],pile)
        elif P[i]=='+':
            a=depiller(pile)
            b=depiller(pile)
            c=a+b
            empiller(c,pile)
        elif P[i]=='-':
            a=depiller(pile)
            b=depiller(pile)
            c=b-a
            empiller(c,pile)
        elif P[i]=='*':
            a=depiller(pile)
            b=depiller(pile)
            c=b*a
            empiller(c,pile)
        elif P[i]=='/':
            a=depiller(pile)
            b=depiller(pile)
            c=b/a
            empiller(c,pile)
        elif P[i]=='^':
            a=depiller(pile)
            b=depiller(pile)
            c=b**a
            empiller(c,pile)
        elif P[i]=='v':
            a=depiller(pile)
            c=sqrt(a)
            empiller(c,pile)
    if len(pile)==1:return pile
        
'''

__________.__          __                       
\______   \  | _____ _/  |________  _______  ___
 |     ___/  | \__  \\   __\_  __ \/  _ \  \/  /
 |    |   |  |__/ __ \|  |  |  | \(  <_> >    < 
 |____|   |____(____  /__|  |__|   \____/__/\_ \
                    \/                        \/
'''
