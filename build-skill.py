#!/usr/bin/env python3
"""Build idx-stock-analyst.skill from the source files in this repo.

Run: python3 build-skill.py
Produces: idx-stock-analyst.skill  (a .zip with .skill extension, installable in Cowork)
"""
import os, zipfile

NAME = "idx-stock-analyst"
OUT = NAME + ".skill"
INCLUDE = ["SKILL.md", "references"]   # only the skill itself, not README / evals / LICENSE
SKIP_FILES = {".DS_Store"}

if os.path.exists(OUT):
    os.remove(OUT)

with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
    for item in INCLUDE:
        if os.path.isfile(item):
            z.write(item, f"{NAME}/{item}")
        elif os.path.isdir(item):
            for dp, _, fns in os.walk(item):
                for fn in fns:
                    if fn in SKIP_FILES or fn.endswith(".pyc"):
                        continue
                    full = os.path.join(dp, fn)
                    z.write(full, f"{NAME}/{full}")

print(f"Built: {OUT} ({os.path.getsize(OUT)} bytes)")
