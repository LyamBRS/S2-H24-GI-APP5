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
import random

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
    PONC = ["!", ".", "[", "]", "(", ")", ",", "?", "--", "...", ";", "\n" , "\r"]

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
        """
            Méthode calculant le produit scalaire entre 2 vecteurs :
            Les vecteurs sont d`abord mis en ordre de grandeurs.
            Apres, le produit scalaire est fait en additionnant la multiplication
            de la value du vecteur 1 avec celle du vecteur 2, uniquement si la key
            est presente dans les deux repo, sinon ca donnerait 0.
        Args :
            vector1 (dict) : tableau de hachage contenant tous les ngrammes du premier fichier
            vector2 (dict) : tableau de hachage contenant tous les ngrammes du deuxième fichier

        Returns :
            prod_scal (int) : Produit scalaire entre les deux vecteurs
        """
        # Il faut utiliser le plus petit vecteur a la bonne place, sinon produit matricielle impossible.
        if len(vector1) < len(vector2):
            v1 = vector1
            v2 = vector2
        else:
            v1 = vector2
            v2 = vector1

        prod_scal = 0  # Correction : Calcul du produit des projections des dimensions communes

        # Le produit scalaire des deux vecteurs est uniquement calculee pour les
        # elements identiques des deux vecteurs. Sinon, c'est une multiplication par 0.
        for ngram in v1:
            if ngram in v2:
                prod_scal += v1[ngram] * v2[ngram]
        return prod_scal

    @staticmethod
    def dot_product_dict(dict1: dict, dict2: dict, dict1_size: int, dict2_size: int) -> float:
        """
            Calcule le produit scalaire NORMALISÉ de deux vecteurs représentés par des dictionnaires.
            C`est fait en calculant premierement le produit scalaire des deux dictionnaires.
            Apres, cette valeure est divise par la racine carree du produit scalaire du vecteur 1, multiplie
            avec la racine carre du produit scalaire du deuxieme vecteur avec lui meme.

        Args :
            dict1 (dict) : le premier vecteur
            dict2 (dict) : le deuxième vecteur

        Returns :
            dot_product (float) : Le produit scalaire normalisé de deux vecteurs

        Copyright 2023, F. Mailhot et Université de Sherbrooke
        """

        dot_product = TextAn.scalar_product(dict1, dict2)

        norm = dot_product / ((math.sqrt(TextAn.scalar_product(dict1, dict1)) * math.sqrt(TextAn.scalar_product(dict2, dict2))))

        return norm

    def dot_product_aut(self, auteur1: str, auteur2: str) -> float:
        """
            Calcule le produit scalaire normalisé entre les oeuvres de deux auteurs, en utilisant dot_product_dict()

        Args :
            auteur1 (str) : le nom du premier auteur
            auteur2 (str) : le nom du deuxième auteur

        Returns :
            dot_product (float) : Le produit scalaire normalisé des n-grammes de deux auteurs

        Copyright 2023, F. Mailhot et Université de Sherbrooke
        """
        # Obviously, si les deux auteurs c'est pareil, on peak a 1. N'importe quoi d'autre vas etre en-dessous / proche de.
        if auteur1 == auteur2:
            return 1

        # Les tailles de mots sont pas necessaire dans nos calcules, mais inclues ici pour futur proof
        dot_product = self.dot_product_dict(self.mots_auteurs[auteur1],
                                            self.mots_auteurs[auteur2],
                                            self.taille_mots[auteur1],
                                            self.taille_mots[auteur2])

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
        dot_product = TextAn.dot_product_dict(self.mots_auteurs[auteur], dict_oeuvre, self.taille_mots[auteur],
                                            len(dict_oeuvre))
        return dot_product

    def find_author(self, oeuvre: str) -> []:
        """
            Après analyse des textes d'auteurs connus, la fonction retourne la liste d'auteurs
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

        # Ouvrir le fichier donne
        try:
            file = open(oeuvre, 'r', encoding='utf-8')
            text = file.read()
            file.close()

        except FileNotFoundError:
            print("File: " + oeuvre + " n'existe pas")
            return []

        text = self.uniformizer(text)

        # Analyse du text donnee, comme dans analyse
        for k in range(0, len(text) - self.ngram):  # passe a travers le texte avec le n-gram
            if self.ngram == 1:
                ngrams = (text[k])
            else:
                ngrams = tuple(text[k:k + self.ngram])

            if ngrams not in mots_oeuvre:
                mots_oeuvre[ngrams] = 1
            else:
                mots_oeuvre[ngrams] += 1

        # Les resultats sont ajouter dans un tableau simple pour parse later
        for auteur in self.auteurs:
            liste_auteur.append((auteur, self.dot_product_dict_aut(mots_oeuvre, auteur)))

        #print(self.auteurs, oeuvre)
        resultats = [
            ("Premier_auteur", 0.1234),
            ("Deuxième_auteur", 0.1123),
        ]  # Exemple du format des sorties

        return liste_auteur

    def gen_text_all(self, taille: int, textname: str) -> None:
        """
            Après analyse des textes d'auteurs connus, produire un texte selon des statistiques de l'ensemble des auteurs
            On retrouve une similarite avec analyse, laquel aurait pu etre separer dans des fonctions
            respectifs. Mais bon, flemme et soucis de "ease of reading and understanding".
        Args :
            taille (int) : Taille du texte à générer
            textname (str) : Nom du fichier texte à générer.

        Returns :
            void : ne retourne rien, le texte produit doit être écrit dans le fichier "textname"
        """
        prefix = {}
        generated_text = []

        # Parcourir tout les texts de tous les auteurs
        for auteur in self.auteurs:
            for fileName in self.get_aut_files(auteur):
                text = ""

                # Open the file. Honestly, shouldve been a seperate function in this.
                try:
                    file = open(fileName, 'r', encoding='utf-8')
                    text = file.read()
                    file.close()

                except FileNotFoundError:
                    print("File: " + fileName + " n'existe pas")
                    return

                text = self.uniformizer(text)

                # Parcourir le text par groupe de n grammes un mot a la fois.
                for k in range(0, len(text) - self.ngram - 1):  # passe a travers le texte avec le n-gram

                    # Quel mot suit la suite de ngramme dans le text? Bah, c'est ca le suffix.
                    suffix = (text[k + self.ngram])

                    # Quel ngramme est associer avec ce suffix la?
                    ngrams = tuple(text[k:k + self.ngram])

                    # Welp, le ngram trouve ye pas dans les prefix qu'on a parser avant.
                    if ngrams not in prefix:
                        prefix[ngrams] = {}

                    # Le ngramme a pas ste suffix la dedans, fac on le cree pour plus tard.
                    if suffix not in prefix[ngrams]:
                        prefix[ngrams][suffix] = 1

                    # Plus tard est arrive! Y'a donc plus de probabilitees que ce ngramme suive ce suffix la
                    else:
                        prefix[ngrams][suffix] += 1

        # This first word of the generated text will be selected randomly... Theres nothing to compare for suffix isnt there.
        current_ngram = random.choice(list(prefix.keys()))
        for s in current_ngram:
            generated_text.append(s)

        # On ce deplace de 1 dans la liste en analysant toujours la fin du text.
        # Le dernier ngramme dicte les suffixes a aller chercher.
        # La reoccurance de chaque suffix est ensuite mis dans un random pour donner le plus plausible
        # a ajouter a la fin du ngramme.
        for i in range(taille - self.ngram):
            current_ngram = tuple(generated_text[i:i + self.ngram])
            suffix = prefix[current_ngram]

            populations = list(suffix.keys())
            weights = list(suffix.values())
            choice = random.choices(population=populations, weights=weights)[0] #[0], c'est le text.

            generated_text.append(choice)

        # Generate one string out of the parsed generated text, finally creating a readable text.
        finalized_text: str = ""
        for word in generated_text:
            finalized_text = finalized_text + word + " "
        #print(finalized_text)

        # Write that to a file with the specified name.
        try:
            with open(textname, 'w', encoding='utf-8') as file:
                file.write(finalized_text)
            print("Content has been written to", textname)
        except IOError:
            print("Error: Could not write to file", textname)
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
        for fileName in self.get_aut_files(auteur):
            text = ""
            try:
                file = open(fileName, 'r', encoding='utf-8')
                text = file.read()
                file.close()

            except FileNotFoundError:
                print("File: " + fileName + " n'existe pas")
                return

            text = self.uniformizer(text)

            for k in range(0, len(text) - self.ngram-1):  # passe a travers le texte avec le n-gram
                suffix = (text[k+self.ngram])
                ngrams = tuple(text[k:k + self.ngram])

                if ngrams not in prefix:
                    prefix[ngrams] = {}

                if suffix not in prefix[ngrams]:
                    prefix[ngrams][suffix] = 1
                else:
                    prefix[ngrams][suffix] += 1

        generated_text = []
        current_ngram = random.choice(list(prefix.keys()))
        for s in current_ngram:
            generated_text.append(s)

        # print(f"generated_text:{generated_text}")

        for i in range(taille-self.ngram):
            current_ngram = tuple(generated_text[i:i + self.ngram])
            suffix = prefix[current_ngram]
            populations = list(suffix.keys())
            weights = list(suffix.values())
            choice = random.choices(population=populations, weights=weights)[0]
            generated_text.append(choice)

        # Generate one string out of the parsed generated text
        finalized_text:str = ""
        for word in generated_text:
            finalized_text = finalized_text + word + " "
        print(finalized_text)

        try:
            with open(textname, 'w', encoding='utf-8') as file:
                file.write(finalized_text)
            print("Content has been written to", textname)
        except IOError:
            print("Error: Could not write to file", textname)

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

        liste_de_ngrammes = []
        reoccurance_index = 0
        nth_element = 0
        old_element_reoccurance = 0

        # INITIAL CHECKS. We be checking if the author exist
        if auteur not in self.mots_auteurs:
            print("L'auteur n'existe pas")
            return [[]]

        # Sort the array per amount of reoccurance
        sorted_list = sorted(self.mots_auteurs[auteur].items(), key=lambda item: item[1], reverse=True)

        # Now that the array is sorted by the amount of reocurrance of a ngram, we check if the wanted nth-element is within all range of available indexes
        index = n - 1
        if index > len(sorted_list):
            print(index, ">", len(sorted_list))
            return [[]]

        # Create the array of empty lists. Sure, useless. But eh, it is what it is
        for element in sorted_list:
            liste_de_ngrammes.append([])

        # Add all the nth grams until we reach the index we're looking for. No point in continuing further.
        while reoccurance_index < len(sorted_list):
            current_reoccurance = sorted_list[reoccurance_index][1]

            # Checks if the previous element equals the next element. If thats the case, the index does NOT increase and we have doublons of nth_elements.
            if(old_element_reoccurance != current_reoccurance):
                old_element_reoccurance = current_reoccurance
                nth_element += 1

            # Simply add the ngram at the end of the list. If the index didnt change, then itll still be the nth-element.
            liste_de_ngrammes[nth_element].append(sorted_list[reoccurance_index][0])
            reoccurance_index += 1

            # Aight, we already past the wanted nth_element... dont bother continuing
            if(nth_element > n):
                return liste_de_ngrammes[n]

        # Huh, thats weird... you selected the last possible n value I suppose.
        return liste_de_ngrammes[n]

    def uniformizer(self, text:str) -> dict:
        """
            Uniformise le text donner (grosse string) en liste de mots, tout en enlevant
            les mots de 1 ou 2 lettres (au besoin), la ponctuation (au besoin) ainsi que
            les majuscules. Les ponctuation sont separe des mots aussi.

        Args :
            auteur (str) : Nom de l'auteur à utiliser
            n (int) : Indice du n-gramme à retourner

        Returns :
            ngram (List[Liste[string]]) : Liste de liste de mots composant le n-gramme recherché
            (il est possible qu'il y ait plus d'un n-gramme au même rang)
        """
        # FILE NORMALIZING

        # Removing all capitalized letters.
        text = text.lower()

        # Removing all ponctuation if necessary
        if not self.keep_ponc:
            for char in self.PONC:
                text = text.replace(char, ' ')
        else:
            for char in self.PONC:
                text = text.replace(char, ' ' + char + ' ')

        text = text.split()

        # NORMALIZING: Removing words of specified length
        if self.remove_word_2 or self.remove_word_1:
            # Add the word at the index, for each word in the text, if that isnt 1 big or 2 big and we specified we dont want these
            text = [word
                    for word in text
                    if not (((len(word) == 1) and self.remove_word_1) or ((len(word) == 2) and self.remove_word_2))
                    ]
        return text

    def analyze(self) -> None:
        """
            Fait l'analyse des textes fournis, en traitant chaque oeuvre de chaque auteur
            - Parcours tout les texts de tous les auteurs
            - Chaque text est ouverts.
            - Le text est ensuite uniformiser avec _ref_ uniformizer
            - Par la suite, le text est parcourus 1 mot a la fois, en shiftant un ngramme a travers le tableau de mots
            - Le ngramme est par la suite utilise comme hashage dans un dictionnaire pour calculer le nombre
              de reoccurance de ce ngramme specifique la.

        Args :
            void : toute l'information est contenue dans l'objet TextAn

        Returns :
            void : ne retourne rien, toute l'information extraite est conservée dans des structures internes
        """
        print(f"ANALYSE DES TEXTS:")
        for auteur in self.auteurs:
            print(f"\tAnalyse de l'auteur: {auteur}...")

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

                text = self.uniformizer(text)
                self.taille_mots[auteur] = 0

                print(f"\t\tAnalyse du text de {len(text)} mots: {os.path.basename(fileName)}...")

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
