"""Régénère les images de la visionneuse de la charte à partir du PDF.

Usage :  python3 make_charte_pages.py chemin/vers/charte.pdf
Nécessite poppler (commande `pdftoppm`). Écrit seed_charte_pages.txt (pages
en 1280 px) et seed_charte_thumbs.txt (miniatures en 240 px), puis lancez
`python3 build.py`.
"""
import sys, glob, json, base64, subprocess, tempfile, os

if len(sys.argv) != 2:
    sys.exit(__doc__)
pdf = sys.argv[1]
with tempfile.TemporaryDirectory() as tmp:
    for prefix, width, quality, out in (('p', 1280, 60, 'seed_charte_pages.txt'),
                                        ('t', 240, 55, 'seed_charte_thumbs.txt')):
        subprocess.run(['pdftoppm', '-jpeg', '-jpegopt', f'quality={quality}',
                        '-scale-to-x', str(width), '-scale-to-y', '-1',
                        pdf, os.path.join(tmp, prefix)], check=True,
                       stderr=subprocess.DEVNULL)
        files = sorted(glob.glob(os.path.join(tmp, f'{prefix}-*.jpg')))
        data = ['data:image/jpeg;base64,' + base64.b64encode(open(f, 'rb').read()).decode()
                for f in files]
        with open(out, 'w') as fh:
            fh.write(json.dumps(data))
        print(f'{out} : {len(files)} pages')
