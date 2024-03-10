#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Code pour explorer le deuxième exercice du laboratoire - APP du cours GIF270

    L'exercice 2 touche les tableaux de hachage et leur redéfinition en Python :
        - Redéfinition de la méthode pour établir l'égalité entre deux objets
        - Redéfinition de la méthode de hachage pour obtenir un nombre à partir d'un objet
        - Redéfinition de la méthode d'ajout d'un bigramme dans un vecteur (dict qui contient un ensemble de bigrammes)
        - Redéfinition de la méthode pour calculer la taille d'un vecteur
        - Redéfinition du produit scalaire entre deux vecteurs
        - Redéfinition de la méthode de calcul du cosinus de l'angle entre deux vecteurs

  Copyright 2018-2024, Frédéric Mailhot et Université de Sherbrooke
"""

from labo_prob2_common import LaboProb2Common
from labo_prob2_common import BigramCommon
import math
from typing import Any


# Pour ce problème, vous devez :
#   - compléter les méthodes suivantes de la classe Bigramme :
#       - __eq__()
#       - __hash__()
#   - compléter les méthodes suivantes de la classe LaboProb2 :
#       - add_bigram()
#       - add_bigram_object()
#       - add_bigram_other()
#       - vector_size()
#       - scalar_product()
#       - cosine()
# Lire les commentaires au début de chacune de ces méthodes pour savoir plus précisément ce qui doit être fait.
#
# Important: - Vous ne devez modifier aucun code dans le fichier labo_prob2_common.py
#            - Vous n'avez pas à modifier la méthode add_bigram_vector, mais sachez qu'elle ne fonctionne pas...
#
# Note :
#       1. Vous pouvez constater que la classe Bigram hérite de la classe BigramCommon.
#       On doit y redéfinir les méthodes __eq__() et __hash__()
#
#       2. De même, la classe LaboProb2 hérite de la classe LaboProb2Common.
#       Ici encore, on redéfinit un certain nombre de méthodes :
#           add_bigram(), add_bigram_object(), add_bigram_other(), vector_size(), scalar_product(), cosine().


class Bigram(BigramCommon):
    """Création de méthodes permettant de personnaliser un dictionnaire (tableau de hachage)
    - Dans cette classe, on redéfinit comment faire le hash et comparer deux objets de type Bigram
    """

    def __eq__(self, other) -> bool:
        """Redéfinition de l'égalité entre deux bigrammes :
            - L'un des bigrammes est self (celui avec lequel __eq__ est appelé)
            - Le deuxième bigramme est other, fourni en paramètre

        Args :
            other (Bigram) : Le bigramme avec lequel il faut se comparer

        Returns :
            (bool) : Retourne True ou False, selon l'égalité entre les bigrammes
        """
        # Vous devez coder ici comment déterminer que deux paires de mots sont les mêmes.
        # Le paramètre "other" est un autre bigramme (instance de la classe Bigramme).
        # Pour le moment, la comparaison ne fait que vérifier que les objets sont des instances de la même classe.
        # Vous devrez ajouter d'autres conditions qui déterminent que deux bigrammes sont égaux (ou non).
        # Note: Il n'est pas nécessaire d'utiliser la méthode "isinstance".
        #       Elle est utilisée ici simplement pour démontrer qu'elle existe,
        #       et qu'on peut facilement vérifier si les classes de deux objets correspondent
        return isinstance(other, self.__class__) and (self.word1 == other.word1) and (self.word2 == other.word2)

    def __hash__(self) -> int:
        """Redéfinition de la méthode de hachage d'un bigramme :
            - Doit utiliser les deux mots du bigramme

        Args :
            (void) : Toute l'information nécessaire (a et b) se trouve dans le bigramme

        Returns :
            (int) : Retourne la valeur de hachage
        """
        # Faire en sorte que la fonction de hachage utilise les deux mots du bigramme.
        # Pour le moment, on n'utilise que le premier mot.
        # Vous devez changer ce qui est utilisé comme entrée dans la fonction de hachage.
        # Vous pourriez utiliser une combinaison des deux mots, avec un séparateur qui est une chaîne de caractères
        # ne comprenant pas de lettre.
        mykey = self.word1 + "::" + self.word2  # Correction : Combiner les deux mots avec un séparateur distinct
        return hash(mykey)


class LaboProb2(LaboProb2Common):
    """Classe de test pour valider la personalisation d'un dictionnaire (tableau de hachage)
        - Classe hérite de ParsingClass2, qui lit les paramètres de la ligne de commande
    """

    @staticmethod
    def add_bigram(bigram: Any, bigram_dict: dict) -> None:
        """Méthode appelée pour ajouter un bigramme au dictionnaire fourni :

        Args :
            bigram (Any) : object (arbitraire) qui représente un bigramme et qui est utilisé comme clé
            bigram_dict (dict) : tableau de hachage de bigrammes.  Utilisé pour emmagasiner et compter les bigrammes

        Returns :
            (void) : Le nouveau bigramme est ajouté au dictionnaire de bigrammes fourni
        """
        if bigram in bigram_dict:
            bigram_dict[bigram] += 1
        else:
            bigram_dict[bigram] = 1
        return

    @staticmethod  # Cette méthode est statique, parce qu'elle n'utilise aucune valeur de l'objet.
    def add_bigram_vector(word1: str, word2: str, bigram_dict: dict) -> None:
        """Méthode appelée pour créer un vecteur de deux mots et pour l'ajouter au dictionnaire fourni :
            - Est-ce que cette méthode fonctionne ?  Pourquoi ?
            - Si elle ne fonctionne pas, utilisez plutôt les méthodes add_bigram_object et add_bigram_other

        Args :
            word1 (str) : premier mot
            word2 (str) : deuxième mot
            bigram_dict (dict) : tableau de hachage de bigrammes.  Utilisé pour emmagasiner et compter les bigrammes

        Returns :
            (void) : Le nouveau bigramme est ajouté au dictionnaire de bigrammes fourni
        """
        # Code invalide.  Utiliser pour découvrir quel est le problème, mais il n'est pas nécessaire de le corriger :
        #   Regarder quel est le type de l'erreur (TypeError) associée à la ligne 109 de add_bigram()
        # Plutôt que de modifier le code, inclure le paramètre "-p 2" ou "-p 3" sur la ligne de commande
        #    pour utiliser les méthodes add_bigram_object() et add_bigram_other()
        bigram = [word1, word2] # Création d'un bigramme
        LaboProb2.add_bigram(bigram, bigram_dict) # Ajout du bigramme dans le tableau de hachage
        return

    @staticmethod
    def add_bigram_object(word1: str, word2: str, bigram_dict: dict) -> None:
        """Méthode appelée pour créer un bigramme (à l'aide des deux mots fournis)
            et pour l'ajouter au dictionnaire fourni :

        Args :
            word1 (str) : premier mot
            word2 (str) : deuxième mot
            bigram_dict (dict) : tableau de hachage de bigrammes.  Utilisé pour emmagasiner et compter les bigrammes

        Returns :
            (void) : Le nouveau bigramme est ajouté au dictionnaire de bigrammes fourni
        """
        # Ici, remplacez les prints par votre code.
        # L'utilisation de la classe Bigram est probablement justifiée...
        # Modifier l'appel à la méthode add_bigram pour ajouter le bigramme complet au tableau de bigrammes
        bigram = Bigram(word1, word2)  # Correction : Création d'un bigramme
        LaboProb2.add_bigram(bigram, bigram_dict) # Correction : Ajout de l'objet bigramme dans le tableau de hachage
        return

    @staticmethod
    def add_bigram_other(word1: str, word2: str, bigram_dict: dict) -> None:
        """Méthode appelée pour créer un bigramme (à l'aide des deux mots fournis)
            et pour l'ajouter au dictionnaire fourni, la clé étant un vecteur :

        Args :
            word1 (str) : premier mot
            word2 (str) : deuxième mot
            bigram_dict (dict) : tableau de hachage de bigrammes.  Utilisé pour emmagasiner et compter les bigrammes

        Returns :
            (void) : Le nouveau bigramme est ajouté au dictionnaire de bigrammes fourni
        """
        # Ici, remplacez les prints par votre code.
        # Que pouvez-vous utiliser pour remplacer un vecteur, mais qui est immuable ?
        bigram = (word1, word2)  # Correction : Utilisation d'un tuple plutôt qu'un vecteur
        LaboProb2.add_bigram(bigram, bigram_dict)
        return

    @staticmethod  # Cette méthode est statique, parce qu'elle n'utilise aucune valeur de l'objet
    def vector_size(vector: dict) -> float:
        """Méthode appelée pour calculer la taille d'un vecteur (tableau de hachage, dict) :

        Args :
            vector (dict) : tableau de hachage contenant tous les bigrammes

        Returns :
            size (int) : La taille du vecteur
        """
        # Ici, vous devez calculer la taille totale du vecteur (le tableau de hachage vector, de type dict).
        # Comme pour tout vecteur, la taille est obtenue en calculant la racine carrée de
        # la somme des carrés des projections dans chacune des dimensions.
        # Cette somme de carrés représente le produit scalaire du vecteur avec lui-même
        # Ici, chaque bigramme distinct est une dimension
        # Remplacez le print et la valeur de retour par le code approprié.

        size = LaboProb2.scalar_product(vector, vector)  # Correction : Calcul de la norme au carré, puis racine
        size = math.sqrt(size)
        return size

    @staticmethod
    def scalar_product(vector1: dict, vector2: dict) -> int:
        """Méthode calculant le produit scalaire entre 2 vecteurs :

        Args :
            vector1 (dict) : tableau de hachage contenant tous les bigrammes du premier fichier
            vector2 (dict) : tableau de hachage contenant tous les bigrammes du deuxième fichier

        Returns :
            prod_scal (int) : Produit scalaire entre les deux vecteurs
        """
        # Ici, vous devez calculer le produit scalaire entre les deux vecteurs.
        # Pour ce faire, vous devez multiplier les valeurs des projections dans chacune des dimensions.
        # De nouveau, les dimensions correspondent aux bigrammes.
        # Si un bigramme existe dans un seul des vecteurs, alors la projection est nulle dans l'autre,
        #   et en conséquence le produit pour cette dimension est nul.
        # Remplacez le print et les lignes suivantes par le code approprié.
        if len(vector1) < len(vector2):  # Correction : choisir le vecteur avec le moins de dimensions
            v1 = vector1
            v2 = vector2
        else:
            v1 = vector2
            v2 = vector1

        prod_scal = 0  # Correction : Calcul du produit des projections des dimensions communes
        for ngram in v1:
            if ngram in v2:
                prod_scal += v1[ngram] * v2[ngram]
        return prod_scal

    @staticmethod
    def cosine(vector1: dict, vector2: dict) -> float:
        """Méthode calculant le cosinus de l'angle entre 2 vecteurs (produit scalaire normalisé) :

        Args :
            vector1 (dict) : tableau de hachage contenant tous les bigrammes du premier fichier
            vector2 (dict) : tableau de hachage contenant tous les bigrammes du deuxième fichier

        Returns :
            angle_cos (float) : Cosinus de l'angle entre les deux vecteurs (produit scalaire normalisé)
        """
        # Ici, vous devez calculer le cosinus de l'angle entre les deux vecteurs, soit le produit scalaire normalisé.
        # Pour normaliser un vecteur, il faut diviser chacune des projections par la longueur totale du vecteur.
        # Vous devez donc :
        #   - Effectuer le produit scalaire entre les deux vecteurs,
        #     puis diviser le résultat par leurs longueurs respectives.
        # Remplacer le print et les lignes qui suivent par le code approprié.
        # Note: Assurez-vous que le résultat ne dépasse pas 1.0, sinon math.acos() causera une exception.
        # Remplacer les lignes qui suivent par le code approprié.

        size1 = LaboProb2.vector_size(vector1)
        size2 = LaboProb2.vector_size(vector2)

        if (size1 == 0) or (size2 == 0):  # Correction : si l'un des vecteurs est de taille 0, retourner 0.0
            angle_cos = 0.0
        else:  # Correction : Sinon, calculer le produit scalaire normalisé.
            angle_cos = LaboProb2.scalar_product(vector1, vector2) / (size1 * size2)
            if angle_cos > 1.0:  # Correction : L'angle d'un vecteur avec lui-même a parfois des erreurs d'arrondi
                angle_cos = 1.0  # Correction : Dans ce cas, corriger à 1.0 (sinon acos cause une exception)

        return angle_cos


# main : lecture des paramètres et appel des méthodes appropriées
def main() -> None:
    """Démarrage de l'exercice 2 du labo :
        - Crée une instance de la classe LaboProb2, utilisée pour tester les mots de deux fichiers
        - LaboProb2 devrait utiliser des instances de la classe Bigramme,
          qui doit redéfinir les opérations d'égalité et de hachage

    Returns :
        (void) : Au retour, l'exécution est terminée
    """
    # Vous n'avez rien à modifier dans la méthode main()
    p2 = LaboProb2()
    match p2.args.p:
        case 1:
            p2.define_add_bigram_func(LaboProb2.add_bigram_vector)
        case 2:
            p2.define_add_bigram_func(LaboProb2.add_bigram_object)
        case 3:
            p2.define_add_bigram_func(LaboProb2.add_bigram_other)
        case _:
            print("Exercice 2, type inconnu de traitement d'objets dans un tableau de hachage (doit être 1,2 ou 3)")
    p2.read()
    p2.do_something()
    return


if __name__ == "__main__":
    main()
