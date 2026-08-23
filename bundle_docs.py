#!/usr/bin/env python3
"""
Single-File dbt Docs Bundler for GitHub Pages.
Combines index.html, manifest.json, and catalog.json into a standalone web app.
"""

import json
import os

TARGET_DIR = "target"
OUTPUT_DIR = "public"

def bundle_docs():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    index_path = os.path.join(TARGET_DIR, "index.html")
    manifest_path = os.path.join(TARGET_DIR, "manifest.json")
    catalog_path = os.path.join(TARGET_DIR, "catalog.json")

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest_data = json.load(f)

    with open(catalog_path, "r", encoding="utf-8") as f:
        catalog_data = json.load(f)

    # Embed data objects directly into the dbt web interface
    search_str = 'parent.postMessage({target: \'oracle\', action: \'ready\'}, \'*\');'
    injection = f"""
        loadProject({json.dumps(manifest_data)}, {json.dumps(catalog_data)});
        {search_str}
    """
    
    bundled_html = html.replace(search_str, injection)

    output_path = os.path.join(OUTPUT_DIR, "index.html")
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(bundled_html)

    print(f"Successfully bundled standalone dbt documentation to: {output_path}")

if __name__ == "__main__":
    bundle_docs()