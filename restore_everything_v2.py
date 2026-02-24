import re
import os
import glob

# More comprehensive dictionary
fixes = {
    'Autoevaluacin': 'Autoevaluación',
    'energa': 'energía',
    'Energa': 'Energía',
    'cintica': 'cinética',
    'rboles': 'árboles',
    'ms ': 'más ',
    'Qu ': 'Qué ',
    'Cmo ': 'Cómo ',
    'Por qu ': 'Por qué ',
    'pequeas': 'pequeñas',
    'dimetro': 'diámetro',
    'podra': 'podría',
    'depsito': 'depósito',
    'clasificacin': 'clasificación',
    'morfologa': 'morfología',
    'diagnstico': 'diagnóstico',
    'trmino': 'término',
    'tcnic': 'técnic',
    'comn': 'común',
    'geodinmico': 'geodinámico',
    'geomorfologa': 'geomorfología',
    'formacin': 'formación',
    'evolucin': 'evolución',
    'tectnico': 'tectónico',
    'hidrologa': 'hidrología',
    'geologa': 'geología',
    'dinmico': 'dinámico',
    'espcifico': 'específico',
    'seccin': 'sección',
    'emblemtico': 'emblemático',
    'cronologa': 'cronología',
    'isosttico': 'isostático',
    'reas ': 'áreas ',
    'mxim': 'máxim',
    'mnim': 'mínim',
    'caracterstic': 'característic',
    'seleccin': 'selección',
    'Disipacin': 'Disipación',
    'estratificacin': 'estratificación',
    'erosin': 'erosión',
    'Erosin': 'Erosión',
    'precipitacin': 'precipitación',
    'denudacin': 'denudación',
    'agradacin': 'agradación',
    'atmsfera': 'atmósfera',
    'bioqumic': 'bioquímic',
    'hidrlisis': 'hidrólisis',
    'combinacin': 'combinación',
    'clsico': 'clásico',
    'vegetacin': 'vegetación',
    'hdrica': 'hídrica',
    'crcava': 'cárcava',
    'progresin': 'progresión',
    'dbiles': 'débiles',
    'gneos': 'ígneos',
    'Estoraques': 'Estoraques',
    'Hjulstrm': 'Hjulström',
    'nica': 'única',
    'nico': 'único',
    'fenmeno': 'fenómeno',
    'elevacin': 'elevación',
    'Inclinacin': 'Inclinación',
    'inclinacin': 'inclinación',
}

def fix_content(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    new_content = content
    for k, v in fixes.items():
        # Avoid replacing inside words if not intended, but for these specific errors it's mostly safe
        new_content = new_content.replace(k, v)
    
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {filepath}")

for f in glob.glob('*.md'):
    fix_content(f)
