##############
# SAE S01.01 #
##############

def liste_amis(amis, prenom):
    """
        Retourne la liste des amis de prenom en fonction du tableau amis.
    """
    prenoms_amis = []
    i = 0
    while i < len(amis)//2:
        if amis[2 * i] == prenom:
            prenoms_amis.append(amis[2*i+1])
        elif amis[2*i+1] == prenom:
            prenoms_amis.append(amis[2*i])
        i += 1
    return prenoms_amis

def nb_amis(amis, prenom):
    """ Retourne le nombre d'amis de prenom en fonction du tableau amis. """
    return len(liste_amis(amis, prenom))


def personnes_reseau(amis):
    """ Retourne un tableau contenant la liste des personnes du réseau."""
    people = []
    i = 0
    while i < len(amis):
        if amis[i] not in people:
            people.append(amis[i])
        i += 1
    return people

def taille_reseau(amis):
    """ Retourne le nombre de personnes du réseau."""
    return len(personnes_reseau(amis))

def lecture_reseau(path):
    """ Retourne le tableau d'amis en fonction des informations contenues dans le fichier path."""
    f = open(path, "r")
    l = f.readlines()
    f.close()
    amis = []
    i = 0
    while i < len(l):
        fr = l[i].split(";")
        amis.append(fr[0].strip())
        amis.append(fr[1].strip())
        i += 1
    return amis

def dico_reseau(amis):
    """ Retourne le dictionnaire correspondant au réseau."""
    dico = {}
    people = personnes_reseau(amis)
    i = 0
    while i < len(people):
        dico[people[i]] = liste_amis(amis, people[i])
        i += 1
    return dico

def nb_amis_plus_pop (dico_reseau):
    """ Retourne le nombre d'amis des personnes ayant le plus d'amis."""
    personnes = list(dico_reseau)
    maxi = len(dico_reseau[personnes[0]])
    i = 1
    while i < len(personnes):
        if maxi < len(dico_reseau[personnes[i]]):
            maxi = len(dico_reseau[personnes[i]])
        i += 1
    return maxi


def les_plus_pop (dico_reseau):
    """ Retourne les personnes les plus populaires, c'est-à-dire ayant le plus d'amis."""
    max_amis = nb_amis_plus_pop(dico_reseau)
    most_pop = []
    personnes = list(dico_reseau)
    i = 1
    while i < len(personnes):
        if len(dico_reseau[personnes[i]]) == max_amis:
            most_pop.append(personnes[i])
        i += 1
    return most_pop

##############
# SAE S01.02 #
##############

def create_network(list_of_friends):
    '''Retourne un réseau d’amis à partir d’un tableau de couples d’amis en le parcourant seulement qu’une seule fois.'''
    dico = {}
    i = 0
    while i < len(list_of_friends):
        if list_of_friends[i] not in dico and list_of_friends[i+1] not in dico:
            dico[list_of_friends[i]] = [list_of_friends[i+1]]
            dico[list_of_friends[i+1]] = [list_of_friends[i]]

        elif list_of_friends[i] in dico and list_of_friends[i+1] not in dico:
            dico[list_of_friends[i]].append(list_of_friends[i+1])
            dico[list_of_friends[i+1]] = [list_of_friends[i]]
            
        elif list_of_friends[i] not in dico and list_of_friends[i+1] in dico:
            dico[list_of_friends[i+1]].append(list_of_friends[i])
            dico[list_of_friends[i]] = [list_of_friends[i+1]]
            
        else:
            dico[list_of_friends[i]].append(list_of_friends[i+1])
            dico[list_of_friends[i+1]].append(list_of_friends[i])  
        i += 2
    return dico


def get_people(network):
    '''Retourne un tableau contenant toutes les personnes appartenant au réseau.'''
    persons = list(network)
    return persons

def are_friends(network, person1, person2):
    '''Affiche si les deux personnes saisi en parametre sont amis selon un réseau.''' 
    amis_pers1 = network[person1]
    i = 0
    while i < len(amis_pers1):
        if amis_pers1[i] == person2:
            return True
        i += 1
    return False

def all_his_friends(network, person, group):
    '''Affiche si la personne saisi en parametre est amie avec toutes les personnes du groupe à partir d’un réseau.'''
    i = 0
    while i < len(group):
        if are_friends(network, person, group[i]) == False:
            return False
        i += 1
    return True

def is_a_community(network, group):
    '''Affiche si ce groupe est une communauté (si toutes les personnes sont tous amis entres elles) à partir d’un réseau.'''
    i = 0
    while i < len(group):
        n = 0
        while n < len(group):
            if n != i:
                if are_friends(network, group[i], group[n]) == False:
                    return False
            n += 1
        i += 1
    return True


def find_community(network, group):
    '''Trouve une communauté où il n'existe personne qui puisse être ajoutée dans cette communauté dans un réseau d'amis selon l'heuristique suivante:
    - On part d'une communauté vide.
    - On considère les personnes les unes après les autres. Pour chacune des personnes, si celle-ci est amie avec tous les membres de la communauté déjà créée, alors on l'ajoute à la communauté.
    Et la retourne en fonction de l'heuristique.'''
    community = []
    i = 0
    while i < len(group):
        res = True
        n = 0
        while n < len(community):
            if n != i:
                if are_friends(network, group[i], community[n]) == False:
                    res = False
            n += 1

        if res == True:
            community.append(group[i])  

        i += 1
    return community

def order_by_decreasing_popularity(network, group):
    '''Trie et retourne un groupe de personnes selon la popularité (nombre d'amis) décroissante à partir d’un réseau.'''
    statut = False
    while not statut:
        statut = True
        i = 0
        while i < len(group)-1:
            if len(network[group[i+1]]) > len(network[group[i]]):
                statut = False
                group[i], group[i+1] = group[i+1], group[i]
            i += 1
    return group


def find_community_by_decreasing_popularity(network):
    '''Trie l'ensemble des personnes du réseau selon l'ordre décroissant de popularité puis retourner la communauté 
    trouvée en appliquant l'heuristique de construction de communauté maximale.'''
    persons = list(network)
    order_by_decreasing_popularity(network, persons)
    find_community(network, persons)
    return persons

def find_community_from_person(network, person):
    '''Retourne une communauté maximale contenant une personne selon l'heuristique :
    on choisit une personne du réseau,
    •	on crée une communauté contenant juste cette personne,
    •	on considère les amis de cette personne par ordre de popularité décroissante. Pour chacune de ces personnes, si celle-ci est amie avec tous les membres de la communauté déjà créée, alors on l'ajoute à la communauté.'''
    community = [person]
    amis = list(network[person])
    order_by_decreasing_popularity(network, amis)
    community += find_community(network, amis)
    return community

def find_max_community(network):
    '''Retourne la plus grande communauté trouvé en appliquant l'heuristique de recherche de communauté maximale donnée par find_community_from_person pour toutes les personnes du réseau.'''
    community = []
    persons = list(network)
    i = 0
    while i < len(persons)-1:
        if len(find_community_from_person(network, persons[i])) < len(find_community_from_person(network, persons[i+1])):
            community = find_community_from_person(network, persons[i+1])
        i += 1
    return community