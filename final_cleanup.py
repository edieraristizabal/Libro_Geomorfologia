import re
import os
import glob

def fix_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # 1. Normalize line endings to \n and remove double \n added by previous scripts
    # First, convert any \r\n to \n
    content = content.replace('\r\n', '\n')
    
    # Remove excessive blank lines in Jupytext header
    header_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL)
    if header_match:
        header = header_match.group(1)
        # Compact the header (remove extra newlines between fields)
        flat_header = "\n".join([line.strip() for line in header.split('\n') if line.strip()])
        # Restore some indentation for YAML
        indented_header = ""
        depth = 0
        for line in flat_header.split('\n'):
            if line.endswith(':'):
                indented_header += "  " * depth + line + "\n"
                depth += 1
            elif line.startswith('-'):
                indented_header += "  " * depth + line + "\n"
            else:
                # heuristic for ending sections
                if depth > 0 and not line.startswith(' '):
                     # keep depth if it's a child of a dict
                     pass
                indented_header += "  " * depth + line + "\n"
        
        # Actually simpler: just remove empty lines in the header block
        clean_header = re.sub(r'\n+', '\n', header)
        content = content.replace(header, clean_header)

    # 2. Fix specific mangled words
    word_fixes = {
        'técúnico': 'técnico',
        'técúnic': 'técnic',
        'técuúnico': 'técnico',
        'éú': 'é',
        'óú': 'ó',
        'áú': 'á',
        'íú': 'í',
        'úú': 'ú',
        'ñú': 'ñ',
        'técnicoo': 'técnico',
        'comúnn': 'común',
    }
    for k, v in word_fixes.items():
        content = content.replace(k, v)

    # 3. Ensure figure syntax is clean (blank lines around captions)
    content = re.sub(r'```\{figure\} (.*?)\n(.*?)\n```', 
                     lambda m: f"```{{figure}} {m.group(1).strip()}\n{m.group(2).strip()}\n```", 
                     content, flags=re.DOTALL)

    # 4. Final sweep for missing characters
    missing_char_fixes = {
        'Autoevaluacin': 'Autoevaluación',
        'energa': 'energía',
        'cintica': 'cinética',
        'rboles': 'árboles',
        'erosin': 'erosión',
        'clasificacin': 'clasificación',
        'morfologa': 'morfología',
        'diagnstico': 'diagnóstico',
        'trmino': 'término',
        'comn': 'común',
        'evolucin': 'evolución',
        'formacin': 'formación',
        'tectnico': 'tectónico',
        'geologa': 'geología',
        'hidrologa': 'hidrología',
        'dinmico': 'dinámico',
        'espcifico': 'específico',
    }
    for k, v in missing_char_fixes.items():
        content = content.replace(k, v)

    # 5. Fix the double newline issue (heuristic: replace triple newlines with double)
    content = re.sub(r'\n{3,}', '\n\n', content)

    with open(filepath, 'w', encoding='utf-8', newline='\n') as f:
        f.write(content)
    print(f"Cleanedup: {filepath}")

for md in glob.glob('*.md'):
    fix_file(md)
