from pathlib import Path

path = Path(r'c:\Users\HP RYZEN 7\Downloads\menu-tipo-pagina-moderno\index.html')
text = path.read_text(encoding='utf-8')

old_root = """  :root{\n    --brand: #000000;\n    --brand-ink: #ffffff;\n    --ink: #333333;\n    --surface: #FDFDFD;\n    --nav-h: 72px;\n    --radius: 12px;\n    --gutter: clamp(12px, 3vw, 24px);\n    --top-gap: max(var(--gutter), env(safe-area-inset-top));\n    --shadow: 0 10px 30px rgba(0,0,0,.1);\n    --speed: 320ms;\n  }\n"""
new_root = """  :root{\n    --brand: #05020d;\n    --brand-ink: #f5f4ff;\n    --ink: #1f2133;\n    --surface: #fdf9ff;\n    --nav-h: 72px;\n    --radius: 14px;\n    --gutter: clamp(12px, 3vw, 28px);\n    --top-gap: max(var(--gutter), env(safe-area-inset-top));\n    --shadow: 0 24px 60px rgba(12,8,46,.25);\n    --speed: 320ms;\n    --accent: #f4c76c;\n    --accent-ink: #261602;\n    --glass: rgba(255,255,255,.08);\n    --glass-border: rgba(255,255,255,.18);\n    --glass-glow: 0 18px 42px rgba(73,32,120,.35);\n  }\n"""
