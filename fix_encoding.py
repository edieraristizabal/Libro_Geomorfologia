import os
import glob

# Mapping of mangled sequences to correct characters
replacements = {
    'Ã¡': 'á',
    'Ã©': 'é',
    'Ã\xad': 'í',  # \xad is the hex for the hidden char sometimes in Ã­
    'Ã­': 'í',     # normal í mangling
    'Ã³': 'ó',
    'Ãº': 'ú',
    'Ã±': 'ñ',
    'Ã\x81': 'Á',
    'Ã\x89': 'É',
    'Ã\x8d': 'Í',
    'Ã\x93': 'Ó',
    'Ã\x9a': 'Ú',
    'Ã\x91': 'Ñ',
    'Â¿': '¿',
    'Â¡': '¡',
    'Ã ': 'Á', # Sometimes Á mangles differently
}

def fix_file(filepath):
    try:
        # Read as bytes to avoid any decoding errors
        with open(filepath, 'rb') as f:
            content = f.read().decode('utf-8', errors='ignore')
        
        original_content = content
        for mangled, correct in replacements.items():
            content = content.replace(mangled, correct)
        
        if content != original_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed encoding in: {filepath}")
            return True
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
    return False

# Target all markdown files
md_files = glob.glob('*.md')
fixed_count = 0
for md_file in md_files:
    if fix_file(md_file):
        fixed_count += 1

print(f"Total files fixed: {fixed_count}")
