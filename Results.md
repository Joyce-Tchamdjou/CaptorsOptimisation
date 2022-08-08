# Optimisation et Métaheuristiques
*TCHAMDJOU MBOTCHACK Joyce Pascale _ 3A ENSTA*


## Présentation de l'archive
============================
Le présente archive est constituée autour d'un dossier _sho.joy_ contenant les dossiers _docs_ pour les utilitaires, _sho_ pour les dépendances et les fichiers _snp.py_, _snp_run.py_ et _snp_landscapes.py_.
Ce programme permet de proposer une solution au problème de placement de capteurs. Il consiste à placer un certain nombre de capteurs dans un domaine tout en maximisant la surface totale couverte par les capteurs. Pour résoudre ce problème d'optimisation, il était nécessaire de créer une fonction objectif qui sera évaluée par notre algorithme et qui est définie dans _sho/pb.py_ définie à partir du framework **SHO** fourni par M. Johann Dreo et dont la structure et le fonctionnement sont spécifiés dans le second README fournis avec le dossier de base.

### Exécutables
Le code principal est implémenté dans le fichier *snp.py*. C'est celui qui sera utilisé pour la compétition, il suffit simplement de l'exécuter, les paramètres, dont le solveur, ont déjà été fixés.

En dehors des codes fournis par le professeur, j'ai également créé un fichier *snp\_run.py*, qui n'est pas vraiment nécessaire d'exécuter. C'est juste une copie du fichier *snp.py* sans les affichages à la fin pour simplifier l'implémentation de mon EAF, Empirical Attainment Function et de mon EDCF, Empirical Distributive Cumulated Function.

## Démarche de choix des paramètres 
===================================
Pour la compétition d'algorithmes pour la résolution du problème de placement de capteurs, le solveur qui a été choisi est celui basé sur le recuit simulé, le *simulated_annealing*. 
Ce choix a été motivé en le comparant au niveau des performances aux autres solveurs à savoir l'algorithme gloutonnier, *greedy* et l'algorithme évolutionnaire, *population_based*. Le solveur basé sur le recuit simulé a en moyenne des valeurs meilleures bonnes que les deux autres même si le temps mis est pratiquement le double de celui du *population_based*. De plus, en ce qui concerne ce solveur, il faut choisir le mode d'évolution de la température entre "propotional", "square" et "logarithmic". Dans ce cas, l'évolution proportionnelle de la température semble la mieux adaptée car elle est la moins instable des trois et arrive à converger vers al solution finale plus rapidement.

## EAF et ECDF
Dans le dossier *sho*, on trouve le fichier *eaf.py* qui contient les fonctions qui implémentent l'EAF et l'ECDF. Pour observer les deux graphes, il suffit de modifier les paramètres dans l'appel de fonction au bas du document et d'éxecuter le fichier. Les paramètres à modifier sont respectivement le nom du solveur, "num\_greedy", "num\_simulated\_annealing", "num\_population\_based" et le nombre de runs pour lesquels on veut observer les performances. 
A la suite de cette exécution, on a en sortie deux figures consécutives, une pour l'EAF et une pour l'ECDF par la suite.




