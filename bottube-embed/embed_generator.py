#!/usr/bin/env python3
"""
BoTTube Embed Code Generator
Generates embed codes for BoTTube videos.
"""

import json

def generate_embed_code(video_id, size="640x360"):
    """Generate iframe embed code for a BoTTube video."""
    width, height = size.split("x")
    return f'''<iframe width="{width}" height="{height}" 
src="https://bottube.ai/embed/{video_id}" 
frameborder="0" 
allowfullscreen 
allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture">
</iframe>'''

def generate_markdown_badge(video_id, title):
    """Generate markdown badge for BoTTube video."""
    return f'''[![Watch on BoTTube](https://bottube.ai/badge/{video_id}.svg)](https://bottube.ai/watch/{video_id})'''

SIZES = {
    "small": "560x315",
    "medium": "640x360", 
    "large": "854x480",
    "hd": "1280x720"
}

def main():
    video_id = input("Enter video ID: ").strip()
    print("\nEmbed Codes:\n")
    
    for name, size in SIZES.items():
        code = generate_embed_code(video_id, size)
        print(f"{name} ({size}):")
        print(code)
        print()
    
    # oEmbed discovery link
    oembed_url = f"https://bottube.ai/oembed?url=https://bottube.ai/watch/{video_id}&format=json"
    print(f"oEmbed Discovery:")
    print(f'<link rel="alternate" type="application/json+oembed" href="{oembed_url}">')

if __name__ == "__main__":
    main()
