import os
import re
import shutil

ROOT = r"c:\Users\catul\OneDrive\Videos\Documents\GitHub\RAJNIKANT"

def read_text(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def write_text(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def safe_copy(src, dst):
    os.makedirs(os.path.dirname(dst), exist_ok=True)
    shutil.copy2(src, dst)
    print(f"Copied: {src} -> {dst}")

# 1. Create all directory paths
classes_dirs = [
    # Class 8 grammar tree
    os.path.join(ROOT, "classes", "class-8", "english", "grammar", "voice", "past", "past-perfect"),
    os.path.join(ROOT, "classes", "class-8", "english", "grammar", "present-indefinite"),
    os.path.join(ROOT, "classes", "class-8", "maths"),
    os.path.join(ROOT, "classes", "class-8", "science"),
    os.path.join(ROOT, "classes", "class-8", "hindi"),
    os.path.join(ROOT, "classes", "class-8", "social-science"),
    os.path.join(ROOT, "classes", "class-8", "gk-gs"),
    
    # Class 10 tree
    os.path.join(ROOT, "classes", "class-10", "english", "chapters", "chapter-2"),
    os.path.join(ROOT, "classes", "class-10", "english", "grammar"),
    os.path.join(ROOT, "classes", "class-10", "science", "chapters", "chapter-4"),
    os.path.join(ROOT, "classes", "class-10", "gk", "days"),
    os.path.join(ROOT, "classes", "class-10", "maths"),
    os.path.join(ROOT, "classes", "class-10", "hindi"),
    os.path.join(ROOT, "classes", "class-10", "social-science"),

    # GK module tree
    os.path.join(ROOT, "gk", "days"),
    os.path.join(ROOT, "gk", "master-gk", "days"),
]

for d in classes_dirs:
    os.makedirs(d, exist_ok=True)

# Also ensure classes 1-12 subject dirs exist
for c in range(1, 13):
    class_dir = os.path.join(ROOT, "classes", f"class-{c}")
    if c <= 5:
        subjs = ["english", "hindi", "maths", "evs", "gk"]
    elif c <= 8:
        subjs = ["english", "hindi", "maths", "science", "social-science", "gk-gs"]
    elif c <= 10:
        subjs = ["english", "hindi", "maths", "science", "social-science", "gk-gs"]
    else:
        subjs = ["english", "hindi", "physics", "chemistry", "maths", "biology", "commerce", "arts"]
    for s in subjs:
        os.makedirs(os.path.join(class_dir, s), exist_ok=True)

print("Directory structure ready.")
