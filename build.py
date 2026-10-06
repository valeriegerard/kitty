import re
import json

def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read()

tpl = read('kitgrafik.html')
_vb = json.load(open('seed_formations/viewboxes.json', encoding='utf-8'))

subs = {
    '__FONT_B64__': read('seed_font_b64.txt').strip(),
    '__FRISE_SVG_INNER__': read('seed_frise_inner.txt'),
    '__CHARTE_COVER_B64__': read('seed_charte_cover.txt').strip(),
    '__CHARTE_COVER_HI_B64__': read('seed_charte_cover_hi.txt').strip(),
    '__QR_HEAJ_B64__': read('qrcode_assets/qr_heaj_b64.txt').strip(),
    '__LOGO_COLOR_PATHS__': read('seed/logo_color_paths.txt'),
    '__LOGO_MONO_PATHS__': read('seed/logo_mono_paths.txt'),
    '__CREATECH_VB__': read('logo_createch/vb.txt').strip(),
    '__CREATECH_NOIR_PATHS__': read('logo_createch/seed_createch_noir_paths.txt'),
    '__CREATECH_BLANC_PATHS__': read('logo_createch/seed_createch_blanc_paths.txt'),
    '__APOSTROPHE_PATH__': read('apostrophe_path.txt').strip(),
    '__MEDEA_VB__': _vb['medea_color'],
    '__MEDEA_COLOR__': read('seed_formations/medea_color.txt'),
    '__MEDEA_MONO__': read('seed_formations/medea_mono.txt'),
    '__ANIM3D_VB__': _vb['anim3d_color'],
    '__ANIM3D_COLOR__': read('seed_formations/anim3d_color.txt'),
    '__ANIM3D_MONO__': read('seed_formations/anim3d_mono.txt'),
    '__CGP_VB__': _vb['cgp_color'],
    '__CGP_COLOR__': read('seed_formations/cgp_color.txt'),
    '__CGP_MONO__': read('seed_formations/cgp_mono.txt'),
    '__DDI_VB__': _vb['ddi_color'],
    '__DDI_COLOR__': read('seed_formations/ddi_color.txt'),
    '__DDI_MONO__': read('seed_formations/ddi_mono.txt'),
    '__GREENPACK_VB__': _vb['greenpack_color'],
    '__GREENPACK_COLOR__': read('seed_formations/greenpack_color.txt'),
    '__GREENPACK_MONO__': read('seed_formations/greenpack_mono.txt'),
    '__IR_VB__': _vb['ir_color'],
    '__IR_COLOR__': read('seed_formations/ir_color.txt'),
    '__IR_MONO__': read('seed_formations/ir_mono.txt'),
    '__JV_VB__': _vb['jv_color'],
    '__JV_COLOR__': read('seed_formations/jv_color.txt'),
    '__JV_MONO__': read('seed_formations/jv_mono.txt'),
    '__STORYTELLING_VB__': _vb['storytelling_color'],
    '__STORYTELLING_COLOR__': read('seed_formations/storytelling_color.txt'),
    '__STORYTELLING_MONO__': read('seed_formations/storytelling_mono.txt'),
    '__TRANSMEDIA_VB__': _vb['transmedia_color'],
    '__TRANSMEDIA_COLOR__': read('seed_formations/transmedia_color.txt'),
    '__TRANSMEDIA_MONO__': read('seed_formations/transmedia_mono.txt'),
    '__VFX_VB__': _vb['vfx_color'],
    '__VFX_COLOR__': read('seed_formations/vfx_color.txt'),
    '__VFX_MONO__': read('seed_formations/vfx_mono.txt'),
    '__HEAJ_ROUGE_VB__': _vb['heaj_rouge'],
    '__HEAJ_ROUGE__': read('seed_formations/heaj_rouge.txt'),
    '__SYMBOL_VB__': _vb['symbol_couleur'],
    '__SYMBOL_COULEUR__': read('seed_formations/symbol_couleur.txt'),
    '__SYMBOL_BLANC__': read('seed_formations/symbol_blanc.txt'),
    '__SYMBOL_ROUGE__': read('seed_formations/symbol_rouge.txt'),
    '__IRSYM_VB__': _vb['irsym_rouge'],
    '__IRSYM_ROUGE__': read('seed_formations/irsym_rouge.txt'),
    '__IRSYM_BLANC__': read('seed_formations/irsym_blanc.txt'),
    '__KITGRAFIK_LOGO_PATHS__': read('seed_formations/kitgrafik_heajbe_paths.txt'),
    '__CHARTE_PAGES__': read('seed_charte_pages.txt').strip(),
    '__CHARTE_THUMBS__': read('seed_charte_thumbs.txt').strip(),
    '__KITGRAFIK_LOGO_VB__': read('seed_formations/kitgrafik_heajbe_vb.txt').strip(),
}

out = tpl
for token, val in subs.items():
    count = out.count(token)
    out = out.replace(token, val)
    print(f'{token}: replaced {count} occurrence(s), value len {len(val)}')

# __FONT_READY__ is a JS identifier assignment (window.__FONT_READY__), not a placeholder - leave it.

with open('kitgrafik_final.html', 'w', encoding='utf-8') as f:
    f.write(out)

print('Done. Output bytes:', len(out))
