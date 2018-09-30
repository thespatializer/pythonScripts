# -*- coding: utf-8 -*-

"""
© 2016 TheSpatializer
https://github.com/thespatializer

@author: TheSpatializer
"""

""" 1\ Détermination des occurences des caractères """

def countChar(chn):
    count = {}
    for car in chn:
        if car in count:
            count[car] += 1
        else:
            count[car] = 1
    return(count)

##Exemple
# >>> countChar("Call me Ishmael.")
# {'a': 2, ' ': 2, 'C': 1, 'e': 2, 'I': 1, 'h': 1, 'm': 2, 'l': 3, '.': 1, 's': 1}

""" 2\ Construction de l'arbre """

from heapq import heapify,heappop,heappush
"""
heapify(list):

Transforme une liste désordonnée en un arbre binaire à partir de ses éléments :

    >>> m = [23,4,65,8,109,1]
    >>> heapify(m)              # Agrégation des éléments de m
    >>> print(m)
    [1, 4, 23, 8, 109, 65]      # L'ordre ici n'a pas de sens évident mais on
                                # comprend l'intérêt avec la fonction suivante

———————————————————————————————————————————————————————————————————————————————————

heappop(list):

Pop (envoie et supprime l'élément itéré) dans l'ordre croissant (naturel pour les
humains) les éléments d'un arbre binaire :

    >>> for i in range(len(m)):
    ...     heappop(m)
    ...    
    1
    4
    8
    23
    65
    109

———————————————————————————————————————————————————————————————————————————————————

heappush(list, élément)

Insère un élément dans un heap (arbre binaire) et réordonne l'arbre en fonction du
nouvel élément :

    >>> m8=[23,4,65,109,1]          # correspond à m mais sans l'élément 8
    >>> heapify(m8)
    >>> print(m8)
    [1, 4, 65, 109, 23]             #arbre binaire différent de m
    >>> heappush(m8, 8)
    >>> print(m8)
    [1, 4, 8, 109, 23, 65]          # arbre binaire identique à m
"""

def huffTree(chn):
    occ = countChar(chn)
    tas = []

    # Construction d'un tas avec les lettres sous forme de feuilles
    for (car, nbOcc) in occ.items():
        tas.append((nbOcc, {'carac': car}))
    # Transformation du tas en un arbre binaire
    heapify(tas)

    # Agrégation des éléments du tas-arbre
    while len(tas) >= 2:
        occ1, gauche = heappop(tas)
        occ2, droite = heappop(tas)
        # Création d'un arbre binaire contenant les occurrences et les chemins
        # On l'insert dans tas car il elle été vidée par heappop
        heappush(tas, (occ1 + occ2, {'gauche': gauche, 'droite': droite}))

    # Renvoi de l'arbre sans le nombre de caractères de la chaîne
    # Ce dernier a permis de trier avec heappush mais n'est plus utile
    totalOcc, tree = heappop(tas)
    return(tree)

##Exemple
# >>> huffTree("Call me Ishmael.")
# {'droite': {'droite': {'droite': {'carac': 'l'}, 'gauche': {'droite': {'carac':
# 'h'}, 'gauche': {'carac': 'I'}}}, 'gauche': {'droite': {'droite': {'carac':
# 'C'}, 'gauche': {'carac': '.'}}, 'gauche': {'carac': 'm'}}}, 'gauche':
# {'droite': {'droite': {'carac': 'e'}, 'gauche': {'carac': 'a'}}, 'gauche':
# {'droite': {'carac': ' '}, 'gauche': {'carac': 's'}}}}

""" 3\ Codage de l'arbre """
def encodeHuffTree(chn):
    tree = huffTree(chn)
    treeCode = {}
    
    # Création d'une fonction récursive. Elle se termine lorsque tous les
    # noeuds ont été parcourus (il ne reste que les feuilles)
    def codeTree(tempCode, noeud):
        if 'gauche' in noeud:
            # Cas d'un noeud de l'arbre
            codeTree(tempCode + [0], noeud['gauche'])
            codeTree(tempCode + [1], noeud['droite'])
        else:
            # On attribue son code à la feuille (caractère)
            treeCode[noeud['carac']] = tempCode
    
    # Premier appel de la fonction récursive
    codeTree([], tree)
    return(treeCode)

##Exemple
# >>> encodeHuffTree("Call me Ishmael.")
# {'a': [0, 1, 0], ' ': [0, 0, 1], 'C': [1, 0, 1, 1], 'e': [0, 1, 1], 'I': [1, 1,
# 0, 0], 'h': [1, 1, 0, 1], 'm':  # [1, 0, 0], 'l': [1, 1, 1], '.': [1, 0, 1, 0],
# 's': [0, 0, 0]}

""" 4\ Codage de la chaîne de caractère """
def encodeChn(chn):
    treeCode = encodeHuffTree(chn)
    code = "" 
    
    # Itération de la chaîne
    for car in chn:
        # Le codage de chaque caractère est ajouté au code final
        for i in treeCode[car]:
            code += str(i)
    return(code)

##Exemple
# >>> encodeChn("Call me Ishmael.")
# '1011010111111001100011001110000011011000100111111010'

""" 5\ Décodage avec l'arbre """
def decodeHuff(code,treeCode):
    code_li = []
    # Conversion de code de string à list
    for val in code:
        code_li.append(int(val))
    
    chn = ""
    codeCar = []
    # Reconstruction de la phrase à partir de l'arbre
    while len(code_li) != 0:
        for car in treeCode:
            codeCar=treeCode[car]
            # Si le codage du caractère corrspond à la portion de code
            if codeCar==code_li[:len(codeCar)]:
                # Le caractère a été décodé
                chn += car
                # On supprime la partie du code décodée
                code_li.__delslice__(0,len(codeCar))
    return(chn)

##Exemple
# >>> code = encodeChn("Hello World!")
# >>> arbre = encodeHuffTree("Hello World!")
# >>> decodeHuff(code, arbre)
# 'Hello World!'
