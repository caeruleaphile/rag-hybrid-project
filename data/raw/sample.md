# La recherche hybride dans les systèmes RAG

## Pourquoi combiner deux index

La recherche hybride associe un index vectoriel à un index lexical de type BM25, ce qui permet de capter à la fois les similarités de sens et les correspondances exactes de termes.

Un index purement vectoriel excelle sur les questions formulées différemment du texte source, mais peut rater un identifiant technique, un nom propre ou un code d'erreur qui doit matcher mot pour mot.

## Fusionner les scores

Une fois les deux listes de résultats obtenues, on les combine généralement par Reciprocal Rank Fusion (RRF), qui pondère chaque document selon son rang dans chaque liste plutôt que selon son score brut.

## Limites

- Coût de maintenance de deux index au lieu d'un
- Nécessité d'un identifiant de chunk partagé entre les deux systèmes
- Réglage du poids relatif de chaque source de score
