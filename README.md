# nalo_test

Après avoir cloné le repo, pour lancer l'application il faut:

- Etre à la racine du projet
- Puis lancer les commandes suivantes dans l'ordre.
- lancer la commande `make build`
- lancer la commande `make create_user`
- lancer la commande `make update_db`
- lancer la commande `make run`

Une fois l'application lancée, les urls pour utiliser l'application sont:
- http://localhost:3000/new_command (pour passer une nouvelle commande)
- http://localhost:3000/command (pour voir le détail d'une commande)
- http://localhost:3000/admin (Pour voir la liste des recette et remplir les pot de glaces) le username et le MDP sont ceux utiliser lors de la commande `make create_user`

Pour lancer les tests il fait rentrer la commande `make test` à la racine du projet
