import re
import os
import glob

def fix_figures(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    # Regex to find figure blocks
    # It catches ```{figure} URL or path\nOptions and Caption\n```
    pattern = re.compile(r'```\{figure\} (.*?)\n(.*?)\n```', re.DOTALL)
    
    def replacer(match):
        url = match.group(1).strip()
        body = match.group(2).strip()
        
        lines = body.split('\n')
        options = []
        caption_lines = []
        in_caption = False
        
        for line in lines:
            trimmed = line.strip()
            if not in_caption and trimmed.startswith(':'):
                options.append(trimmed)
            else:
                if trimmed:
                    in_caption = True
                    # Clean up generic placeholders
                    if trimmed.lower() in ["descripción de la imagen", "decripción de la imagen"]:
                        continue
                    caption_lines.append(trimmed)
        
        new_body = ""
        if options:
            new_body += "\n".join(options) + "\n"
        
        # Add the required blank line before caption
        new_body += "\n"
        
        if caption_lines:
            new_body += "\n".join(caption_lines) + "\n"
            
        return f"```{{figure}} {url}\n{new_body}```"

    improved_content = pattern.sub(replacer, content)
    
    # Also fix the residual mangled characters from previous attempts
    # Adding more specific patterns for common mangles
    mangles = {
        'Ã': 'Á',
        'Ã©': 'é',
        'Ã\xad': 'í',
        'Ã­': 'í',
        'Ã³': 'ó',
        'Ãº': 'ú',
        'Ã±': 'ñ',
        'Â¿': '¿',
        'Â¡': '¡'
    }
    for mangled, correct in mangles.items():
        improved_content = improved_content.replace(mangled, correct)

    if improved_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(improved_content)
        print(f"Fixed figures and encoding in: {filepath}")
        return True
    return False

for f in glob.glob('*.md'):
    fix_figures(f)
