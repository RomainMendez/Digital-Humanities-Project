# Méthodologie

Dans notre analyse, l’idée centrale est de porter l’analyse sur la différence
entre les deux journaux et leur évolution dans le temps. La méthodologie
détaillée en dessous sera donc appliquée sur les deux journaux séparément.

Le traitement des données sera organisé en 3 catégories.
- La présentation des articles
- Le contexte des articles
- Le contenu des articles

Cependant avant d’en arriver là, nous devons effectuer du pre-processing sur les
données. Le schéma en dessous détaille les outils que nous voulons utiliser pour
obtenir les informations décrites plus haut:

### Pre-processing

À fin de pouvoir conduire notre analyse, nous devons réduire le corpus de façon
à pouvoir explorer les données de manière rapide et interactive. Le corpus de
base se constitue de tous les articles de la _Gazette de Lausanne_ et du
_Journal de Genève_ sortis entre 1900 et 1999. Les données nous parviennent
compressées en format `bzip2` et occupent en total 18 Go d’espace sur disque. Si
les données sont décomprimées, le volume des donnés augmente d’un facteur dix.
Ceci nous cause un problème, car  plus que 200 Go de données ne rentrent pas
dans la mémoire RAM d'un ordinateur, limitant les méthodes de questionnement que
nous pouvons appliquer.

Pour résoudre ce problème, nous pourrions opérer sur les données compressées, en
les décompressant au moment du besoin. Cette approche est raisonnable, mais
introduit de longs temps d'élaboration. Effectivement, le format `bzip2` permet
une forte réduction de la taille des fichiers, mais à un coût d'un long temps de
décompression. Une expérience nous confirme que pour chercher les mots "secret
bancaire" dans un fichier `bzip2` contenant les articles du _Journal de Genève_ de
1970 la décompression `bzip2` nécessite 24.1s alors que le temps de recherche ne
surpasse pas 0.6s. Nous pouvons donc épargner beaucoup de temps en travaillant
sur les données décomprimées à l'avance.

Nous souhaitons ne pas limiter notre corpus aux articles qui contiennent un des
mots clés, car les autres articles nous seront utiles pour effectuer d’autres
analyses, comme par exemple trouver tous les articles écrits par un certain
auteur et voir si l'auteur est plutôt un généraliste, ou un spécialiste. Le
problème suivant est donc de réduire les 200 Go de données brutes pour les
stocker et manipuler aisément. Pour cela, nous décidons d'ignorer les
méta-données sur la position des mots sur la page. Ces dernières occupent
environ 90% du volume des données et ne sont pas nécessaires à nos analyses.
Nous les gardons seulement pour les quelques articles qui contiennent un de nos
mots clés. De cette façon, nous travaillons avec un total d’environ 9 Go de
données décomprimées. Une recherche par mots clés passe ainsi de 1h30 sur les
données compressées à 1 minute sur les données nettoyées et décomprimées.

### Présentation des articles

Dans le cadre de nos questions, nous cherchons à comprendre et comparer la façon
dont le sujet du secret bancaire suisse est abordé dans les deux journaux. Cela
pose la question de la présentation des articles. Dans cette section nous
cherchons à savoir :

A quel page peut-on trouver les articles ?
Cette question nous permettra d’évaluer l’importance du sujet pour les deux journaux, pour savoir si on retrouve le sujet à la première page ou dans des articles qui seront peu lu.
A quel endroit peut-on trouver les articles sur une page ?
Nous voudrions aussi créer une heatmap des articles sur les pages du journal, afin de voir si un motif se répète (par exemple, mis tout le temps en haut ou en bas).
Est-ce que les articles font parti d’une rubrique récurrente ou non ?
Cela nous permettra d’en savoir plus sur le traitement du sujet, est-ce que cela suit l’actualité (à mettre en contexte de l’évolution du sujet) ou que c’est un choix délibéré.
Quel est la longueur d’un article sur le sujet ?
Un long article indique souvent que le sujet est perçu comme important par la rédaction.
Contexte des articles
Dans cette catégorie on s’intéresse à tout ce qui est autour d’un article.
Quand ?
C’est la méta-donnée la plus importante d’un article, car cela peut être mis en relation facilement avec l’évolution du sujet.
Qui ?
Une des questions centrales dans notre sujet, qui est-ce qui s’exprime ? Nous voulons séparer en deux les possibles acteurs.
Journalistes
    Nous voulons tenter de mettre en perspective l’activité d’un journaliste. Est-ce un journaliste généraliste ou spécialisé ? Quel sont les thématiques de ses autres articles ? De quand à quand est-il actif ?
Acteurs externes
    Est-ce que l’auteur ici s’exprime au nom d’une institution comme par exemple une banque ou est-ce un représentant politique ? Quel est le contexte pour cette institution (sous le coup d’une enquête, ou critiqué internationalement ..)

Contenu

Ici nous allons nous intéresser aux articles directement. Cependant nous allons
nous arrêter à des observations objectives. L’idée étant d’utiliser Iramuteq
pour faire ressortir la structure des phrases par exemple, la distribution des
mots (et donc mettre en lumière la différence entre le vocabulaire employé par
les deux journaux, afin de voir si malgré leurs différences de rédaction ils
sont en accord, si on est sur une couverture complètement factuelle ou non).
Nous voulons aussi tenter d’analyser le type de mot utilisé par les journaux
(pour voir s’il y a une différence d’écriture) car nous avons remarqué que
Iramuteq peut faire la différence entre les types de mots (adjectifs, adverbes,
verbes …).

Cette partie va aussi s’appliquer à plusieurs dataset, car nous utiliserons
cette approche pour le plus d’acteurs possibles afin de voir si on peut
synthétiser un peu leur psychologie et comprendre la couverture du sujet.
