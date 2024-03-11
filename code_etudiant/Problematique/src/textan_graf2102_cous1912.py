#!/usr/bin/env python3
# -*- coding: utf-8 -*-


""" Ce fichier contient la classe TextAn, à utiliser pour résoudre la problématique.
    C'est un gabarit pour l'application de traitement des fréquences de mots dans les oeuvres d'auteurs divers.

    Les méthodes apparaissant dans ce fichier définissent une API qui est utilisée par l'application
    de test test_textan.py
    Les paramètres d'entrée et de sortie (Application Programming Interface, API) sont définis,
    mais le code est à écrire au complet.
    Vous pouvez ajouter toutes les méthodes et toutes les variables nécessaires au bon fonctionnement du système

    La classe TextAn est invoquée par la classe TestTextAn (contenue dans test_textan.py) :

        - Tous les arguments requis sont présents et accessibles dans args (dans le fichier test_textan.py)
        - Note : vous pouvez tester votre code en utilisant les commandes :
            + "python test_textan.py"
            + "python test_textan.py -h" (donne la liste des arguments possibles)
            + "python test_textan.py -v" (mode "verbose", qui indique les valeurs de tous les arguments)

    Copyright 2018-2023, F. Mailhot et Université de Sherbrooke
"""
import math
import os

from textan_common import TextAnCommon


class TextAn(TextAnCommon):
    """Classe à utiliser pour coder la solution à la problématique :

        - La classe héritée TextAnCommon contient certaines fonctions de base pour faciliter le travail :
            - recherche des auteurs
            - ouverture des répertoires
            - et autres (voir la classe TextAnCommon pour plus d'information)
            - La classe ParsingClassTextAn est héritée par TextAnCommon et lit la ligne de commande
        - Les interfaces du code à développer sont présentes, mais tout le code est à écrire
        - En particulier, il faut compléter les fonctions suivantes :
            - dot_product_dict (dict1, dict2)
            - dot_product_aut (auteur1, auteur2)
            - doct_product_dict_aut (dict, auteur)
            - find_author (oeuvre)
            - gen_text (auteur, taille, textname)
            - get_nth_element (auteur, n)
            - analyze()

    Copyright 2018-2023, F. Mailhot et Université de Sherbrooke
    """

    # Signes de ponctuation à retirer (compléter cette liste incomplète)
    PONC = ["!", ".", "[", "]", "(", ")", ",", "?", "--", "...", ]

    def __init__(self) -> None:
        """Initialize l'objet de type TextAn lorsqu'il est créé

        Args :
            (void) : Utilise simplement les informations fournies dans la classe TextAnCommon

        Returns :
            (void) : Ne fait qu'initialiser l'objet de type TextAn
        """

        # Initialisation des champs nécessaires aux fonctions fournies
        super().__init__()

        # Au besoin, ajouter votre code d'initialisation de l'objet de type TextAn lors de sa création

        return

    # Ajouter les structures de données et les fonctions nécessaires à l'analyse des textes,
    #   la production de textes aléatoires, la détection d'oeuvres inconnues,
    #   l'identification des n-ièmes mots les plus fréquents
    #
    # If faut coder les fonctions find_author(), gen_text(), get_nth_element() et analyse()
    # La fonction analyse() est appelée en premier par test_textan.py
    # Ensuite, selon ce qui est demandé, les fonctions find_author(), gen_text() ou get_nth_element() sont appelées

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
        # print(vector1, vector2)
        # return sum((a*b) for a, b in zip(v1, v2))
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
    def dot_product_dict(
            dict1: dict, dict2: dict, dict1_size: int, dict2_size: int
    ) -> float:
        """Calcule le produit scalaire NORMALISÉ de deux vecteurs représentés par des dictionnaires

        Args :
            dict1 (dict) : le premier vecteur
            dict2 (dict) : le deuxième vecteur

        Returns :
            dot_product (float) : Le produit scalaire normalisé de deux vecteurs

        Copyright 2023, F. Mailhot et Université de Sherbrooke
        """

        # Les lignes qui suivent ne servent qu'à éliminer un avertissement.
        # Il faut les retirer et les remplacer par du code fonctionnel
        dot_product = 0

        # common_keys = set(dict1.keys()) & set(dict2.keys())
        #
        # for ngram in common_keys:
        #     dot_product += dict1[ngram] * dict2[ngram]

        dot_product = TextAn.scalar_product(dict1, dict2)

        norm = dot_product / ((math.sqrt(TextAn.scalar_product(dict1, dict1)) * math.sqrt(TextAn.scalar_product(dict2, dict2))))

        return norm

    def dot_product_aut(self, auteur1: str, auteur2: str) -> float:
        """Calcule le produit scalaire normalisé entre les oeuvres de deux auteurs, en utilisant dot_product_dict()

        Args :
            auteur1 (str) : le nom du premier auteur
            auteur2 (str) : le nom du deuxième auteur

        Returns :
            dot_product (float) : Le produit scalaire normalisé des n-grammes de deux auteurs

        Copyright 2023, F. Mailhot et Université de Sherbrooke
        """

        # Les lignes qui suivent ne servent qu'à éliminer un avertissement.
        # Il faut les retirer et les remplacer par du code fonctionnel

        if auteur1 == auteur2:
            return 1

        dot_product = self.dot_product_dict(self.mots_auteurs[auteur1], self.mots_auteurs[auteur2],
                                            self.taille_mots[auteur1], self.taille_mots[auteur2])

        return dot_product

    def dot_product_dict_aut(self, dict_oeuvre: dict, auteur: str) -> float:
        """Calcule le produit scalaire normalisé entre une oeuvre inconnue et les oeuvres d'un auteur,
           en utilisant dot_product_dict()

        Args :
            dict_oeuvre (dict) : la liste des n-grammes d'une oeuvre inconnue
            auteur (str) : le nom d'un auteur

        Returns :
            dot_product (float) : Le produit scalaire normalisé des n-grammes de deux auteurs

        Copyright 2023, F. Mailhot et Université de Sherbrooke
        """

        # Les lignes qui suivent ne servent qu'à éliminer un avertissement.
        # Il faut les retirer et les remplacer par du code fonctionnel

        dot_product = TextAn.dot_product_dict(self.mots_auteurs[auteur], dict_oeuvre, self.taille_mots[auteur],
                                            len(dict_oeuvre))
        return dot_product

    def find_author(self, oeuvre: str) -> []:
        """Après analyse des textes d'auteurs connus, retourner la liste d'auteurs
            et le niveau de proximité (un nombre entre 0 et 1) de l'oeuvre inconnue
            avec les écrits de chacun d'entre eux

        Args :
            oeuvre (str) : Nom du fichier contenant l'oeuvre d'un auteur inconnu

        Returns :
            resultats (Liste[(string, float)]) : Liste de tuples (auteurs, niveau de proximité),
            où la proximité est un nombre entre 0 et 1)
        """
        liste_auteur = []
        mots_oeuvre = {}
        text = ""

        try:
            file = open(oeuvre, 'r', encoding='utf-8')
            text = file.read()
            file.close()

        except FileNotFoundError:
            print("File: " + oeuvre + " n'existe pas")

        text = text.lower()
        text = text.split()

        for k in range(0, len(text) - self.ngram):  # passe a travers le texte avec le n-gram
            if self.ngram == 1:
                ngrams = (text[k])
            else:
                ngrams = tuple(text[k:k + self.ngram])

            if ngrams not in mots_oeuvre:
                mots_oeuvre[ngrams] = 1
            else:
                mots_oeuvre[ngrams] += 1

        for auteur in self.auteurs:
            liste_auteur.append((auteur, self.dot_product_dict_aut(mots_oeuvre, auteur)))

        # Les lignes suivantes ne servent qu'à éliminer un avertissement.
        # Il faut les retirer lorsque le code est complété
        print(self.auteurs, oeuvre)
        resultats = [
            ("Premier_auteur", 0.1234),
            ("Deuxième_auteur", 0.1123),
        ]  # Exemple du format des sorties

        # Ajouter votre code pour déterminer la proximité du fichier passé en paramètre avec chacun des auteurs
        # Retourner la liste des auteurs, chacun avec sa proximité au fichier inconnu
        # Plus la proximité est grande, plus proche l'oeuvre inconnue est des autres écrits d'un auteur
        #   Le produit scalaire entre le vecteur représentant les oeuvres d'un auteur
        #       et celui associé au texte inconnu pourrait s'avérer intéressant...
        #   Le produit scalaire devrait être normalisé avec la taille du vecteur associé au texte inconnu :
        #   proximité = (A dot product B) / (|A| |B|)   où A est le vecteur du texte inconnu et B est celui d'un auteur,
        #           "dot product" est le produit scalaire, et |X| est la norme (longueur) du vecteur X

        return liste_auteur

    def gen_text_all(self, taille: int, textname: str) -> None:
        """Après analyse des textes d'auteurs connus, produire un texte selon des statistiques de l'ensemble des auteurs

        Args :
            taille (int) : Taille du texte à générer
            textname (str) : Nom du fichier texte à générer.

        Returns :
            void : ne retourne rien, le texte produit doit être écrit dans le fichier "textname"
        """

        # Ce print ne sert qu'à éliminer un avertissement. Il doit être retiré lorsque le code est complété
        print(self.auteurs, taille, textname)

        return

    def gen_text_auteur(self, auteur: str, taille: int, textname: str) -> None:
        """Après analyse des textes d'auteurs connus, produire un texte selon des statistiques d'un auteur

        Args :
            auteur (str) : Nom de l'auteur à utiliser
            taille (int) : Taille du texte à générer
            textname (str) : Nom du fichier texte à générer.

        Returns :
            void : ne retourne rien, le texte produit doit être écrit dans le fichier "textname"
        """
        prefix = {}
        print(auteur)
        for fileName in self.get_aut_files(auteur):
            text = ""
            try:
                file = open(fileName, 'r', encoding='utf-8')
                text = file.read()
                file.close()

            except FileNotFoundError:
                print("File: " + fileName + " n'existe pas")

            text = text.lower()
            if not self.keep_ponc:
                for char in self.PONC:
                    text = text.replace(char, ' ')

            text = text.split()
            self.taille_mots[auteur] = 0

            for k in range(0, len(text) - self.ngram):  # passe a travers le texte avec le n-gram
                ngram_act = list(self.mots_auteurs[auteur].keys())[i]
                ngram_next = list(self.mots_auteurs[auteur].keys())[i + 1]
                prefix_temp = ngram_act[0] + "::" + ngram_act[1]
                suffix = []

                if self.ngram == 1:
                    ngrams = (text[k])
                else:
                    ngrams = tuple(text[k:k + self.ngram])

                if ngrams not in prefix:
                    prefix[ngrams] = 1
                    self.taille_mots[auteur] += 1
                else:
                    self.mots_auteurs[auteur][ngrams] += 1

        for i in range(len(self.mots_auteurs[auteur])):
            # On met le ngram

            if ngram_act not in prefix:
                prefix[prefix_temp] = suffix
                prefix[prefix_temp].append(ngram_next[1])

            else:
                prefix[prefix_temp].append(ngram_next[1])

        print("ALLO")
        # Ce print ne sert qu'à éliminer un avertissement. Il doit être retiré lorsque le code est complété
        print(self.auteurs, auteur, taille, textname)

        return

    def get_nth_element(self, auteur: str, n: int) -> [[str]]:
        """Après analyse des textes d'auteurs connus, retourner le n-ième plus fréquent n-gramme de l'auteur indiqué

        Args :
            auteur (str) : Nom de l'auteur à utiliser
            n (int) : Indice du n-gramme à retourner

        Returns :
            ngram (List[Liste[string]]) : Liste de liste de mots composant le n-gramme recherché
            (il est possible qu'il y ait plus d'un n-gramme au même rang)
        """
        # Les lignes suivantes ne servent qu'à éliminer un avertissement.
        # Il faut les retirer lorsque le code est complété
        if auteur not in self.mots_auteurs:
            print("L'auteur n'est pas")
            return

        sorted_list = sorted(self.mots_auteurs[auteur].items(), key=lambda item: item[1], reverse=True)

        """
        .items() permet de grouper les key av leurs valeurs et de les mettre en tuple 
        ex: my_dict = {'a': 1, 'b': 2, 'c': 3}  --->>    dict_items([('a', 1), ('b', 2), ('c', 3)])

        key=lambda item: item[1] permet d'indiquer qu'on veut trier en fonction des valeurs du ngram qui se situe à l'index 1
        reverse = True indique qu"on veut un ordre décroissant
        Bref, ça fait une liste partant du ngram le plus utilisé par l'auteur
        """

        index = n - 1
        if index > len(sorted_list):
            print(index, ">", len(sorted_list))
            return [[]]

        nth_element = []
        nth_element.append(sorted_list[index][0])
        """
        JE change cela : nb_element = sorted_list[index]  
        POUR ça:  nb_element = sorted_list[index][1]   
        """
        nb_element = sorted_list[index][1]
        compteur = 1

        while sorted_list[index - compteur][1] == nb_element:
            nth_element.append(sorted_list[index - compteur][
                                   0])  # verifie les elements avant n pr savoir si certains ont le mm nb d'apparition
            compteur += 1
        while sorted_list[index + compteur][1] == nb_element:
            nth_element.append(sorted_list[index + compteur][0])
            compteur += 1
        return nth_element

    def analyze(self) -> None:
        """Fait l'analyse des textes fournis, en traitant chaque oeuvre de chaque auteur

        Args :
            void : toute l'information est contenue dans l'objet TextAn

        Returns :
            void : ne retourne rien, toute l'information extraite est conservée dans des structures internes
        """

        # Ajouter votre code ici pour traiter l'ensemble des oeuvres de l'ensemble des auteurs
        # Pour l'analyse :  faire le calcul des fréquences de n-grammes pour l'ensemble des oeuvres
        #   d'un certain auteur, sans distinction des oeuvres individuelles,
        #       et recommencer ce calcul pour chacun des auteurs
        #   En procédant ainsi, les oeuvres comprenant plus de mots auront un impact plus grand sur
        #   les statistiques globales d'un auteur.
        # Il serait possible de considérer chacune des oeuvres d'un auteur comme ayant un poids identique.
        #   Pour ce faire, il faudrait faire les calculs de fréquence pour chacune des oeuvres
        #       de façon indépendante, pour ensuite les normaliser (diviser chaque vecteur par sa norme),
        #       avant de les additionner pour obtenir le vecteur complet d'un auteur
        #   De cette façon, les mots d'un court poème auraient une importance beaucoup plus grande que
        #   les mots d'une très longue oeuvre du même auteur. Ce n'est PAS ce qui vous est demandé ici.

        # Ces trois lignes ne servent qu'à éliminer un avertissement. Il faut les retirer lorsque le code est complété

        # faut passer a travers tous les auteurs

        # faut ouvrir tous les documents des auteurs

        # lire tous les documents des auteurs

        # faire les n-grames

        # Get all authors and analyse their respective texts
        for auteur in self.auteurs:
            print(f"Analyse de l'auteur: {auteur}...")

            # Analyses each texts available for that author
            for fileName in self.get_aut_files(auteur):
                text = ""

                # FILE OPENING
                try:
                    file = open(fileName, 'r', encoding='utf-8')
                    text = file.read()
                    file.close()

                except FileNotFoundError:
                    print("\tFile: " + fileName + " n'existe pas")

                # FILE NORMALIZING
                text = text.lower()
                if not self.keep_ponc:
                    for char in self.PONC:
                        text = text.replace(char, ' ')

                text = text.split()
                self.taille_mots[auteur] = 0
                new_text = text

                if self.remove_word_1:
                    new_text = [
                        word
                        for word in text
                        if not (len(word) <= 1)
                    ]
                text = new_text

                if self.remove_word_2:
                    new_text = [
                        word
                        for word in text
                        if not (len(word) <= 2)
                    ]
                text = new_text
                print(f"\tAnalyse du text de {len(text)} mots: {os.path.basename(fileName)}...")

                for k in range(0, len(text) - self.ngram):  # passe a travers le texte avec le n-gram
                    if self.ngram == 1:
                        ngrams = (text[k])
                    else:
                        ngrams = tuple(text[k:k + self.ngram])

                    if ngrams not in self.mots_auteurs[auteur]:
                        self.mots_auteurs[auteur][ngrams] = 1
                        self.taille_mots[auteur] += 1
                    else:
                        self.mots_auteurs[auteur][ngrams] += 1
        return
