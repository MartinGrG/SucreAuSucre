"""
Ce script permet d'afficher le temps de calcul et l'erreur relative sur un graphique
pour chaque fonction de calcul d'intégrale
"""

import matplotlib.pyplot as plt
from analyse import *
from methode_rectangles import *
from methode_trapezes import *
from methode_simpson import *

from calculs import *


# Définition des paramètres : a et b les bornes de l'intervalle a < b,
# liste_coefficient : la liste des coefficients du polynôme de degrés 3
a = 0
b = 100
coef = [1,-200,-300,4]


# TEMPS DE CALCUL
# Tracé temps de calcul en fonction du nombre de segments de chaque méthode
# RECTANGLES
def tracer_tps_calcul_rectangles():
    comparaison = compare(methode_rectangle_python, methode_rectangle_numpy, coef, a, b)
    rect_base_tps = comparaison[0][0, 0, :]
    rect_numpy_tps = comparaison[0][1, 0, :]
    liste_nbre_seg = comparaison[1]
    plt.plot(liste_nbre_seg, rect_base_tps, 'r-', label='Méthode des rectangles de base')
    plt.plot(liste_nbre_seg, rect_numpy_tps, 'b--', label='Méthode des rectangles Numpy')
    plt.title('RECTANGLES : Tracé du temps de calcul en fonction du nombre de segments')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul')
    plt.legend()
    # Affichage du graphique
    plt.show()


# TRAPÈZES
def tracer_tps_calcul_trapezes():
    comparaison = compare(methode_trapezes_python, methode_trapezes_numpy, coef, a, b)
    trap_base_tps = comparaison[0][0, 0, :]
    trap_numpy_tps = comparaison[0][1, 0, :]
    trap_existante_tps = compare(methode_trapezes_existante, methode_trapezes_numpy, coef, a, b)[0][0, 0, :]
    liste_nbre_seg = comparaison[1]
    plt.plot(liste_nbre_seg, trap_base_tps, 'r-', label='Méthode des trapèzes de base')
    plt.plot(liste_nbre_seg, trap_numpy_tps, 'b--', label='Méthode des trapèzes Numpy')
    plt.plot(liste_nbre_seg, trap_existante_tps, 'g-.', label='Méthode des trapèzes existante')
    # Affichage du titre, des légendes et du nom des axes
    plt.title('TRAPÈZES : Tracé du temps de calcul en fonction du nombre de segments')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul')
    plt.legend()
    # Affichage du graphique
    plt.show()


# SIMPSON
def tracer_tps_calcul_simpson():
    comparaison = compare(methode_simpson_python, methode_simpson_numpy, coef, a, b)
    simp_base_tps = comparaison[0][0, 0, :]
    simp_numpy_tps = comparaison[0][1, 0, :]
    simp_existante_tps = compare(methode_simpson_existante, methode_simpson_numpy, coef, a, b)[0][0, 0, :]
    liste_nbre_seg = comparaison[1]
    plt.plot(liste_nbre_seg, simp_base_tps, 'r-', label='Méthode Simpson de base')
    plt.plot(liste_nbre_seg, simp_numpy_tps, 'b--', label='Méthode Simpson Numpy')
    plt.plot(liste_nbre_seg, simp_existante_tps, 'g-.', label='Méthode Simpson existante')
    # Affichage du titre, des légendes et du nom des axes
    plt.title('SIMPSON : Tracé du temps de calcul en fonction du nombre de segments')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul')
    plt.ylim(0, 0.0002)
    plt.legend()
    # Affichage du graphique
    plt.show()


# ERREURS RELATIVES
# Tracé de l'erreur en fonction du nombre de segments de chaque méthode
# RECTANGLES
def tracer_err_rectangle():
    comparaison = compare(methode_rectangle_python, methode_rectangle_numpy, coef, a, b)
    rect_base_err = comparaison[0][0, 2, :]
    rect_numpy_err = comparaison[0][1, 2, :]
    liste_nbre_seg = comparaison[1]
    plt.plot(liste_nbre_seg, rect_base_err, 'r-', label='Méthode des rectangles de base')
    plt.plot(liste_nbre_seg, rect_numpy_err, 'b--', label='Méthode des rectangles Numpy')
    # Affichage du titre, des légendes et du nom des axes
    plt.title('RECTANGLES : Tracé des erreurs relatives en fonction du nombre de segments')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur relative')
    plt.legend()
    # Affichage du graphique
    plt.show()


# TRAPÈZES
def tracer_err_trapeze():
    comparaison = compare(methode_trapezes_python, methode_trapezes_numpy, coef, a, b)
    trap_base_err = comparaison[0][0, 2, :]
    trap_numpy_err = comparaison[0][1, 2, :]
    trap_existante_err = compare(methode_trapezes_existante, methode_trapezes_numpy, coef, a, b)[0][0, 2, :]
    liste_nbre_seg = comparaison[1]
    plt.plot(liste_nbre_seg, trap_base_err, 'r-', label='Méthode des trapèzes de base')
    plt.plot(liste_nbre_seg, trap_numpy_err, 'b--', label='Méthode des trapèzes Numpy')
    plt.plot(liste_nbre_seg, trap_existante_err, 'g-.', label='Méthode des trapèzes existante')
    # Affichage du titre, des légendes et du nom des axes
    plt.title('TRAPÈZES : Tracé des erreurs relatives en fonction du nombre de segments')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur relative')
    plt.legend()
    # Affichage du graphique
    plt.show()


# SIMPSON
def tracer_err_simpson():
    comparaison = compare(methode_simpson_python, methode_simpson_numpy, coef, a, b)
    simp_base_err = comparaison[0][0, 2, :]
    simp_numpy_err = comparaison[0][1, 2, :]
    simp_existante_err = compare(methode_simpson_existante, methode_simpson_numpy, coef, a, b)[0][0, 2, :]
    liste_nbre_seg = comparaison[1]
    plt.plot(liste_nbre_seg, simp_base_err, 'r-', label='Méthode Simpson de base')
    plt.plot(liste_nbre_seg, simp_numpy_err, 'b--', label='Méthode Simpson Numpy')
    plt.plot(liste_nbre_seg, simp_existante_err, 'g-.', label='Méthode Simpson existante')
    # Affichage du titre, des légendes et du nom des axes
    plt.title('SIMPSON : Tracé des erreurs relatives en fonction du nombre de segments')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur relative')
    plt.legend()
    # Affichage du graphique
    plt.show()


# TEMPS CALCUL
# Tracé du temps en fonction du nombre de segments pour comparer numpy et python
def tracer_tps_calcul_numpy_python():
    comparaison_rect = compare(methode_rectangle_python, methode_rectangle_numpy, coef, a, b)
    comparaison_trap = compare(methode_trapezes_python, methode_trapezes_numpy, coef, a, b)
    comparaison_simp = compare(methode_simpson_python, methode_simpson_numpy, coef, a, b)
    liste_nbre_seg = comparaison_rect[1]
    # Affichage python
    rect_python_tps = comparaison_rect[0][0, 0, :]
    trap_python_tps = comparaison_trap[0][0, 0, :]
    simp_python_tps = comparaison_simp[0][0, 0, :]
    plt.plot(liste_nbre_seg, rect_python_tps, 'r-', label='Méthode des rectangles')
    plt.plot(liste_nbre_seg, trap_python_tps, 'g-', label='Méthode des trapèzes')
    plt.plot(liste_nbre_seg, simp_python_tps, 'b-', label='Méthode Simpson')
    plt.title('BASE : Tracé du temps de calcul en fonction du nombre de segments')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul (sec)')
    plt.legend()
    # Affichage du graphique
    plt.show()
    # Affichage numpy
    rect_numpy_tps = comparaison_rect[0][1, 0, :]
    trap_numpy_tps = comparaison_trap[0][1, 0, :]
    simp_numpy_tps = comparaison_simp[0][1, 0, :]
    plt.plot(liste_nbre_seg, rect_numpy_tps, 'r-', label='Méthode des rectangles')
    plt.plot(liste_nbre_seg, trap_numpy_tps, 'g-', label='Méthode des trapèzes')
    plt.plot(liste_nbre_seg, simp_numpy_tps, 'b-', label='Méthode Simpson')
    plt.title('NUMPY : Tracé du temps de calcul en fonction du nombre de segments')
    plt.xlabel('Nombre de segments')
    plt.ylabel('Temps de calcul (sec)')
    plt.legend()
    # Affichage du graphique
    plt.show()


# ERREUR RELATIVE
# Tracé de l'erreur en fonction du nombre de segments pour comparer numpy et python
def tracer_err_numpy_python():
    comparaison_rect = compare(methode_rectangle_python, methode_rectangle_numpy, coef, a, b)
    comparaison_trap = compare(methode_trapezes_python, methode_trapezes_numpy, coef, a, b)
    comparaison_simp = compare(methode_simpson_python, methode_simpson_numpy, coef, a, b)
    liste_nbre_seg = comparaison_rect[1]
    # Affichage python
    rect_python_err = comparaison_rect[0][0, 2, :]
    trap_python_err = comparaison_trap[0][0, 2, :]
    simp_python_err = comparaison_simp[0][0, 2, :]
    plt.plot(liste_nbre_seg, rect_python_err, 'r-', label='Méthode des rectangles')
    plt.plot(liste_nbre_seg, trap_python_err, 'g-', label='Méthode des trapèzes')
    plt.plot(liste_nbre_seg, simp_python_err, 'b-', label='Méthode Simpson')
    plt.title("BASE : Tracé de l'erreur relative en fonction du nombre de segments")
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur relative [%]')
    plt.legend()
    # Affichage du graphique
    plt.show()
    # Affichage numpy
    rect_numpy_err = comparaison_rect[0][1, 2, :]
    trap_numpy_err = comparaison_trap[0][1, 2, :]
    simp_numpy_err = comparaison_simp[0][1, 2, :]
    plt.plot(liste_nbre_seg, rect_numpy_err, 'r-', label='Méthode des rectangles')
    plt.plot(liste_nbre_seg, trap_numpy_err, 'g-', label='Méthode des trapèzes')
    plt.plot(liste_nbre_seg, simp_numpy_err, 'b-', label='Méthode Simpson')
    plt.title("NUMPY : Tracé de l'erreur relative en fonction du nombre de segments")
    plt.xlabel('Nombre de segments')
    plt.ylabel('Erreur relative [%]')
    plt.legend()
    # Affichage du graphique
    plt.show()


def tracer_rectangle():
    comparaison = compare(methode_rectangle_python, methode_rectangle_numpy, coef, a, b)
    rect_base_err = comparaison[0][0, 2, :]
    rect_numpy_err = comparaison[0][1, 2, :]
    rect_base_tps = comparaison[0][0, 0, :]
    rect_numpy_tps = comparaison[0][1, 0, :]
    liste_nbre_seg = comparaison[1]

    fig, axs = plt.subplots(1, 2)

    axs[0].plot(liste_nbre_seg, rect_base_tps, 'r-', label='Méthode des rectangles de base')
    axs[0].plot(liste_nbre_seg, rect_numpy_tps, 'b--', label='Méthode des rectangles Numpy')
    axs[0].set_title('Tracé du temps de calcul en fonction \n du nombre de segments')
    axs[0].set(xlabel='Nombre de segments', ylabel='Temps de calcul')

    plt.title('Méthode des rectangles')
    axs[1].plot(liste_nbre_seg, rect_base_err, 'r-', label='Méthode des rectangles de base')
    axs[1].plot(liste_nbre_seg, rect_numpy_err, 'b--', label='Méthode des rectangles Numpy')
    axs[1].set_title('Tracé des erreurs relatives en fonction \n du nombre de segments')
    axs[1].set(xlabel='Nombre de segments', ylabel='Erreur relative')

    plt.legend()
    # Affichage du graphique
    plt.show()


def tracer_trapeze():
    comparaison1 = compare(methode_trapezes_python, methode_trapezes_numpy, coef, a, b)
    comparaison2 = compare(methode_trapezes_existante, methode_trapezes_numpy, coef, a, b)
    trap_base_err = comparaison1[0][0, 2, :]
    trap_numpy_err = comparaison1[0][1, 2, :]
    trap_existante_err = comparaison2[0][0, 2, :]
    trap_base_tps = comparaison1[0][0, 0, :]
    trap_numpy_tps = comparaison1[0][1, 0, :]
    trap_existante_tps = comparaison2[0][0, 0, :]
    liste_nbre_seg = comparaison1[1]

    fig, axs = plt.subplots(1, 2)

    axs[0].plot(liste_nbre_seg, trap_base_tps, 'r-', label='Méthode des trapèzes de base')
    axs[0].plot(liste_nbre_seg, trap_numpy_tps, 'b--', label='Méthode des trapèzes Numpy')
    axs[0].plot(liste_nbre_seg, trap_existante_tps, 'g--', label='Méthode des trapèzes existante')
    axs[0].set_title('Tracé du temps de calcul en fonction \n du nombre de segments')
    axs[0].set(xlabel='Nombre de segments', ylabel='Temps de calcul')

    plt.title('Méthode des rectangles')
    axs[1].plot(liste_nbre_seg, trap_base_err, 'r-', label='Méthode des trapèzes de base')
    axs[1].plot(liste_nbre_seg, trap_numpy_err, 'b--', label='Méthode des trapèzes Numpy')
    axs[1].plot(liste_nbre_seg, trap_existante_err, 'g--', label='Méthode des trapèzes existante')
    axs[1].set_title('Tracé des erreurs relatives en fonction \n du nombre de segments')
    axs[1].set(xlabel='Nombre de segments', ylabel='Erreur relative')

    plt.legend()
    # Affichage du graphique
    plt.show()


def tracer_simpson():
    comparaison1 = compare(methode_simpson_python, methode_simpson_numpy, coef, a, b)
    comparaison2 = compare(methode_simpson_existante, methode_simpson_numpy, coef, a, b)
    simp_base_err = comparaison1[0][0, 2, :]
    simp_numpy_err = comparaison1[0][1, 2, :]
    simp_existante_err = comparaison2[0][0, 2, :]
    simp_base_tps = comparaison1[0][0, 0, :]
    simp_numpy_tps = comparaison1[0][1, 0, :]
    simp_existante_tps = comparaison2[0][0, 0, :]
    liste_nbre_seg = comparaison1[1]

    fig, axs = plt.subplots(1, 2)

    axs[0].plot(liste_nbre_seg, simp_base_tps, 'r-', label='Méthode de Simpson de base')
    axs[0].plot(liste_nbre_seg, simp_numpy_tps, 'b--', label='Méthode de Simpson Numpy')
    axs[0].plot(liste_nbre_seg, simp_existante_tps, 'g--', label='Méthode de Simpson existante')
    axs[0].set_title('Tracé du temps de calcul en fonction \n du nombre de segments')
    axs[0].set(xlabel='Nombre de segments', ylabel='Temps de calcul')
    axs[0].set_ylim(0, 0.0002)

    plt.title('Méthode des rectangles')
    axs[1].plot(liste_nbre_seg, simp_base_err, 'r-', label='Méthode de Simpson de base')
    axs[1].plot(liste_nbre_seg, simp_numpy_err, 'b--', label='Méthode de Simpson Numpy')
    axs[1].plot(liste_nbre_seg, simp_existante_err, 'g--', label='Méthode de Simpson existante')
    axs[1].set_title('Tracé des erreurs relatives en fonction \n du nombre de segments')
    axs[1].set(xlabel='Nombre de segments', ylabel='Erreur relative')
    # axs[1].set_ylim(-.5e-12,.5e-12)
    plt.legend()
    # Affichage du graphique
    plt.show()


def tracer_numpy():
    comparaison1 = compare(methode_simpson_numpy, methode_rectangle_numpy, coef, a, b)
    comparaison2 = compare(methode_trapezes_numpy, methode_simpson_numpy, coef, a, b)
    simp_err = comparaison1[0][0, 2, :]
    rect_err = comparaison1[0][1, 2, :]
    trap_err = comparaison2[0][0, 2, :]
    simp_tps = comparaison1[0][0, 0, :]
    rect_tps = comparaison1[0][1, 0, :]
    trap_tps = comparaison2[0][0, 0, :]
    liste_nbre_seg = comparaison1[1]

    fig, axs = plt.subplots(1, 2)

    axs[0].plot(liste_nbre_seg, rect_tps, 'r-', label='Méthode des rectangles avec numpy')
    axs[0].plot(liste_nbre_seg, trap_tps, 'b-', label='Méthode des trapèzes avec numpy')
    axs[0].plot(liste_nbre_seg, simp_tps, 'g-', label='Méthode de Simpson avec numpy')
    axs[0].set_title('Tracé du temps de calcul en fonction \n du nombre de segments')
    axs[0].set(xlabel='Nombre de segments', ylabel='Temps de calcul')

    plt.title('Méthode des rectangles')
    axs[1].plot(liste_nbre_seg, rect_err, 'r-', label='Méthode des rectangles avec numpy')
    axs[1].plot(liste_nbre_seg, trap_err, 'b-', label='Méthode des trapèzes avec numpy')
    axs[1].plot(liste_nbre_seg, simp_err, 'g-', label='Méthode de Simpson avec numpy')
    axs[1].set_title('Tracé des erreurs relatives en fonction \n du nombre de segments')
    axs[1].set(xlabel='Nombre de segments', ylabel='Erreur relative')

    plt.legend()
    # Affichage du graphique
    plt.show()


def tracer_python():
    comparaison1 = compare(methode_simpson_python, methode_rectangle_python, coef, a, b)
    comparaison2 = compare(methode_trapezes_python, methode_simpson_python, coef, a, b)
    simp_err = comparaison1[0][0, 2, :]
    rect_err = comparaison1[0][1, 2, :]
    trap_err = comparaison2[0][0, 2, :]
    simp_tps = comparaison1[0][0, 0, :]
    rect_tps = comparaison1[0][1, 0, :]
    trap_tps = comparaison2[0][0, 0, :]
    liste_nbre_seg = comparaison1[1]

    fig, axs = plt.subplots(1, 2)

    axs[0].plot(liste_nbre_seg, rect_tps, 'r-', label='Méthode des rectangles de base')
    axs[0].plot(liste_nbre_seg, trap_tps, 'b-', label='Méthode des trapèzes de base')
    axs[0].plot(liste_nbre_seg, simp_tps, 'g-', label='Méthode de Simpson de base')
    axs[0].set_title('Tracé du temps de calcul en fonction \n du nombre de segments')
    axs[0].set(xlabel='Nombre de segments', ylabel='Temps de calcul')

    plt.title('Méthode des rectangles')
    axs[1].plot(liste_nbre_seg, rect_err, 'r-', label='Méthode des rectangles de base')
    axs[1].plot(liste_nbre_seg, trap_err, 'b-', label='Méthode des trapèzes de base')
    axs[1].plot(liste_nbre_seg, simp_err, 'g-', label='Méthode de Simpson de base')
    axs[1].set_title('Tracé des erreurs relatives en fonction \n du nombre de segments')
    axs[1].set(xlabel='Nombre de segments', ylabel='Erreur relative')

    plt.legend()
    # Affichage du graphique
    plt.show()

#Tracer les graphes :
tracer_tps_calcul_rectangles()
tracer_tps_calcul_trapezes()
tracer_tps_calcul_simpson()
tracer_err_rectangle()
tracer_err_trapeze()
tracer_err_simpson()

tracer_tps_calcul_numpy_python()
tracer_err_numpy_python()

tracer_rectangle()
tracer_trapeze()
tracer_simpson()
tracer_python()
tracer_numpy()

tracer_simpson()
