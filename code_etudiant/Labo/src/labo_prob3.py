#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
    Code pour explorer le troisième exercice du laboratoire - APP du cours GIF270

    L'exercice 3 touche les arbres AVL et l'élément suivant :
        - Redéfinition de la méthode rotate_right

    Copyright 2018-2023, Frédéric Mailhot et Université de Sherbrooke
"""
from __future__ import annotations

from labo_prob3_common import LaboProb3Common
from labo_prob3_common import AVLTreeCommon
from labo_prob3_common import TreeNode

#  Vous devrez modifier la classe AVLTree, et redéfinir la méthode rotate_right pour que le tout fonctionne.
#  Le code disponible à la section 6.17 du livre est recopié dans la classe AVLTreeCommon.
#  Vous devrez redéfinir la méthode rotate_right (qui est analogue à la méthode rotateLeft fournie dans AVLTreeCommon).
#  La méthode rotate_left qui est définie dans la classe AVLTreeCommon peut clarifier comment procéder.
#  Vous pouvez utiliser l'analyse effectuée dans l'exercice 3 du procédural 1,
#       pour déterminer comment calculer les nouveaux "balance factors".


class AVLTree(AVLTreeCommon):

    def rotate_right(self, rotation_root: TreeNode) -> None:
        """Rotation d'un sous-arbre vers la droite :

        Args :
            rotation_root (TreeNode) : Noeud sur lequel effectuer la rotation droite

        Returns :
            (void) : Au retour, la rotation droite a été effectuée et tous les noeuds ont été ajustés
        """
        if rotation_root.has_left_child() is None:
            return
        new_root = rotation_root.left_child#
        rotation_root.left_child = new_root.right_child#
        if new_root.right_child:
            new_root.right_child.parent = rotation_root
        new_root.parent = rotation_root.parent
        if rotation_root.is_root():
            self.root = new_root
        else:
            if rotation_root.is_right_child():
                rotation_root.parent.right_child = new_root
            else:
                rotation_root.parent.left_child = new_root
        new_root.right_child = rotation_root
        rotation_root.parent = new_root
        rotation_root.balance_factor = (
                rotation_root.balance_factor - 1 - max(new_root.balance_factor, 0)
        )
        new_root.balance_factor = (
                new_root.balance_factor - 1 + min(rotation_root.balance_factor, 0)
        )
        return


# Main : lecture des paramètres et appel des méthodes appropriées
def main() -> None:
    """Démarrage de l'exercice 3 du labo :
        - Crée une instance de la classe LaboProb3, utilisée pour implémenter un arbre AVL
        - Ajoute des nombres dans un arbre AVL (avec rotation active ou inactive)
        - Imprime le résultat (ordre des valeurs, profondeur maximale de l'ardre)

    Returns :
        (void) : Au retour, l'exécution est terminée
    """
    p3 = LaboProb3Common(AVLTree)
    p3.do_something()
    return


if __name__ == "__main__":
    main()
