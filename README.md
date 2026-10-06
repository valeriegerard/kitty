# Kit Grafik — HEAJ

Portail de diffusion des ressources graphiques de la Haute École Albert Jacquard
(logos, typographies, couleurs, pictogrammes, motifs, gabarits, charte graphique).
Le kit est une **page HTML unique et autonome** : polices, logos et pages de la
charte sont intégrés dans le fichier.

## Contenu du dossier

| Fichier / dossier | Rôle |
|---|---|
| `kitgrafik.html` | **Gabarit principal** : HTML, CSS et JavaScript du kit. Les gros blocs de données y sont remplacés par des marqueurs `__NOM__`. C'est le fichier à modifier. |
| `build.py` | Script de construction : remplace les marqueurs par le contenu des fichiers de données et écrit `kitgrafik_final.html`. |
| `seed_*.txt`, `seed/`, `seed_formations/`, `logo_createch/`, `qrcode_assets/`, `apostrophe_path.txt` | Fichiers de données : police (base64), tracés SVG des logos, QR code, couvertures et pages de la charte. |
| `make_charte_pages.py` | Régénère les images de la visionneuse à partir d'un PDF de la charte. |
| `kitgrafik_final.html` | Page finale générée par `build.py` (version publiée, incluse pour l'archive). |

## Reconstruire le kit

Prérequis : Python 3 (aucune bibliothèque supplémentaire).

```bash
python3 build.py
```

Le script affiche chaque marqueur remplacé et crée `kitgrafik_final.html`
(environ 7 Mo). Ouvrez ce fichier dans un navigateur pour le tester.

Vérification rapide : aucun marqueur ne doit rester dans le résultat.

```bash
grep -oE '__[A-Z0-9_]+__' kitgrafik_final.html | sort -u
# seul __FONT_READY__ est normal (variable JavaScript, pas un marqueur)
```

## Modifier le kit

- **Textes, mise en page, comportement** : éditez `kitgrafik.html`, puis relancez `python3 build.py`.
- **Ne collez jamais de gros blocs de données** (base64, tracés SVG) dans `kitgrafik.html`. Créez un fichier `.txt`, placez un marqueur `__MON_MARQUEUR__` dans le gabarit et ajoutez-le au dictionnaire `subs` de `build.py`.
- **Remplacer le PDF de la charte** :
  1. `python3 make_charte_pages.py chemin/vers/charte.pdf` (nécessite `pdftoppm`, paquet *poppler*) ;
  2. mettez à jour le poids (`bytes:`) et la date de l'élément `id:'charte'` dans `kitgrafik.html` ;
  3. `python3 build.py`.

## Publier

Le kit est publié comme page Claude (Artifact). Pour mettre à jour la version en
ligne, republiez le fichier `kitgrafik_final.html` à la même adresse. La taille
de la page doit rester sous 16 Mo.

## Limites actuelles

- Les téléchargements sont simulés : les boutons affichent une confirmation
  mais ne servent pas encore les fichiers réels.
- Le PDF de la charte n'est pas dans ce dépôt (`.gitignore`). La visionneuse
  utilise des images de ses 67 pages, intégrées dans la page.
- Certains logos de formations sont encore des placeholders (TG, MJV, MAT, IG, MIG, CP).

## Versionner sur GitHub

```bash
git init
git add .
git commit -m "Kit Grafik — version 56"
git branch -M main
git remote add origin https://github.com/VOTRE-COMPTE/heaj-kit-grafik.git
git push -u origin main
```

Ensuite, à chaque évolution : `git add .`, `git commit -m "description"`, `git push`.
