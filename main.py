"""
Programme pour parcourir un fichier
"""
#### Imports et définition des variables globales
import csv
FILENAME = "listes.csv"

#### Fonctions secondaires

def read_data(filename):
    """retourne le contenu du fichier <filename>

    Args:
        filename (str): nom du fichier à lire

    Returns:
        list: le contenu du fichier (1 list par ligne)
    """
    with open(filename, 'r', encoding='UTF8') as file:
        file_read = csv.reader(file , delimiter=';')
        l = [list(map(int, row)) for row in file_read]
    return l

def get_list_k(data, k):
    """ retourne la liste à l'indice k
    Args:
        data
        k : l'indice voulu
    Returns:
        list: list de l'indice k
    """
    return data[k]

def get_first(l):
    """
    Retourne le premier élément de la liste
    """
    return l[0]

def get_last(l):
    """
    Retourne le dernier élément de la liste
    """
    return l[-1]

def get_max(l):
    """
    Retourne l'élément maximum de la liste
    """
    return max(l)

def get_min(l):
    """
    Retourne le minimum de la liste
    """
    return min(l)

def get_sum(l):
    """
    Retourne la somme de la liste
    """
    return sum(l)


#### Fonction principale


def main():
    """
    Fonction main pour tester les méthodes secondaires
    """
    data = read_data(FILENAME)
    print(99, get_list_k(data, 99))
    print('First : ',get_first(data[99]))
    print('Last : ',get_last(data[99]))
    print('Max : ',get_max(data[99]))
    print('Min : ',get_min(data[99]))
    print('Sum : ',get_sum(data[99]))


if __name__ == "__main__":
    main()
