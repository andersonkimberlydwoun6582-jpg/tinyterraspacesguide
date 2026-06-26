# Fix generator script: move Vanta.js out of f-string to fix syntax
import os

root = r"C:\Users\86183\Documents\Codex\2026-06-26\https-mp-weixin-qq-com-s\tinyterraspacesguide"
fp = os.path.join(root, "scripts", "generate_all.py")

with open(fp, "r", encoding="utf-8") as f:
    lines = f.readlines()

# Find the VANTA JS block inside the f-string and fix it
new_lines = []
in_fstring = False
for i, line in enumerate(lines):
    # Check if we're inside the make_page_html f-string return
    if "return f'''" in line:
        in_fstring = True
    if in_fstring and "'''" in line and i > 0:
        # End of f-string
        in_fstring = False
    
    # Fix curly braces in JS code inside f-string  
    if in_fstring:
        # Check if line has { that needs escaping (not Python expressions)
        # Simple approach: lines with JS code patterns
        stripped = line.strip()
        # Skip lines that are f-string Python expressions
        if any(stripped.startswith(x) for x in ["document", "if (document", "try", "catch", "VANTA", "AOS", "</script>", "/*", "*/"]):
            # Escape { and } for f-string
            line = line.replace("{", "{{").replace("}", "}}")
            # Restore Python expressions that use single braces
            line = line.replace("{{lang}}", "{lang}")
            line = line.replace("{{lp}}", "{lp}")
            line = line.replace("{{title}}", "{title}")
            line = line.replace("{{desc}}", "{desc}")
            line = line.replace("{{content}}", "{content}")
            line = line.replace("{{curr_section}}", "{curr_section}")
            # Restore {n}, {e}, {s}, {d} used in f-string loops
            line = line.replace("{{n}}", "{n}")
            line = line.replace("{{e}}", "{e}")
            line = line.replace("{{s}}", "{s}")
            line = line.replace("{{d}}", "{d}")
            # Restore {cards}
            line = line.replace("{{cards}}", "{cards}")
    new_lines.append(line)

with open(fp, "w", encoding="utf-8") as f:
    f.writelines(new_lines)

print("Fixed JS braces in f-string")

import py_compile
try:
    py_compile.compile(fp, doraise=True)
    print("Syntax: OK")
except Exception as e:
    print(f"Still broken: {e}")
