import re
fp = r"C:\Users\86183\Documents\Codex\2026-06-26\https-mp-weixin-qq-com-s\tinyterraspacesguide\scripts\generate_all.py"
with open(fp, encoding="utf-8") as f:
    txt = f.read()

# Remove VANTA_JS block (between VANTA_JS = and the next '''
txt = re.sub(r"\nVANTA_JS = .*?\n'''", "\n'''", txt, flags=re.DOTALL)

with open(fp, "w", encoding="utf-8") as f:
    f.write(txt)

import py_compile
try:
    py_compile.compile(fp, doraise=True)
    print("OK")
except Exception as e:
    print(f"Fail: {e}")
