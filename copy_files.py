import os
import shutil

ROOT = r"c:\Users\catul\OneDrive\Videos\Documents\GitHub\RAJNIKANT"

def copy_and_replace(src_rel, dst_rel, replacements):
    src = os.path.join(ROOT, src_rel)
    dst = os.path.join(ROOT, dst_rel)
    with open(src, "r", encoding="utf-8") as f:
        content = f.read()
    for old, new in replacements:
        content = content.replace(old, new)
    with open(dst, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Successfully wrote {dst_rel} ({len(content)} chars)")

copy_and_replace(
    "class8-english-grammar-present-indefinite.html",
    r"classes\class-8\english\grammar\present-indefinite\index.html",
    [
        ('href="class8-english-portal.html"', 'href="../../index.html"'),
        ('href="website-skeleton-layout.html"', 'href="../../../../../website-skeleton-layout.html"')
    ]
)
