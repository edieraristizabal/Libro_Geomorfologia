import re
import os
import glob

# Extensive dictionary for restoration
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
    'magnitud-frecuencia': 'magnitud-frecuencia', # just in case
    'clima-tecnolog': 'clima-tecnolog',
    'erosin': 'erosión',
    'precipitacin': 'precipitación',
    'denudacin': 'denudación',
    'agradacin': 'agradación',
    'litosfera': 'litosfera', # no accent usually
    'atmsfera': 'atmósfera',
    'bioqumic': 'bioquímic',
    'hidrlisis': 'hidrólisis',
    'laterit': 'laterit',
}

def fix_content(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    new_content = content
    for k, v in fixes.items():
        new_content = new_content.replace(k, v)
    
    # Fix broken image tags in MenM.md or elsewhere
    # This pattern handles the case where the tag might be split across lines
    image_pattern = re.compile(r'<image src=\s*([^\s>]+)\s*(?:width=\s*\"([^\"]+)\")?\s*>', re.DOTALL)
    
    def image_replacer(match):
        url = match.group(1).strip()
        width = match.group(2).strip() if match.group(2) else "600"
        return f"\n```{{figure}} {url}\n:width: {width}\n\n```\n"

    new_content = image_pattern.sub(image_replacer, new_content)
    
    # Second pass for the specific broken one in MenM.md screenshot
    # "<image src= https://i.pinimg.com/1200x/62/28/3a/62283a9708b7af24606949964a493053.jpg\n   width=\"500\">"
    specific_pattern = re.compile(r'<image src=\s*https://i.pinimg.com/1200x/62/28/3a/62283a9708b7af24606949964a493053.jpg\s+width=\"500\">', re.DOTALL)
    new_content = specific_pattern.sub(r'\n```{figure} https://i.pinimg.com/1200x/62/28/3a/62283a9708b7af24606949964a493053.jpg\n:width: 500\n\n```\n', new_content)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {filepath}")

for f in glob.glob('*.md'):
    fix_content(f)
