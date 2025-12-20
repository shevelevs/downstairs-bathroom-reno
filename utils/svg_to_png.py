#!/usr/bin/env python3
"""
SVG to PNG Converter
Converts all bathroom_wall*.svg files to PNG format
"""

import os
import glob
from pathlib import Path
import cairosvg

def convert_svg_to_png(svg_path, png_path, scale=2):
    """
    Convert SVG file to PNG
    
    Args:
        svg_path: Path to input SVG file
        png_path: Path to output PNG file
        scale: Scale factor for output resolution (default: 2 for higher quality)
    """
    try:
        cairosvg.svg2png(
            url=svg_path,
            write_to=png_path,
            scale=scale
        )
        print(f"✓ Converted: {Path(svg_path).name} -> {Path(png_path).name}")
        return True
    except Exception as e:
        print(f"✗ Error converting {svg_path}: {e}")
        return False

def main():
    """Convert all bathroom_wall SVG files to PNG"""
    # Get the project directory (parent of utils)
    project_dir = Path(__file__).parent.parent
    
    # Find all bathroom_wall*.svg files
    svg_pattern = str(project_dir / "bathroom_wall*.svg")
    svg_files = sorted(glob.glob(svg_pattern))
    
    if not svg_files:
        print("No bathroom_wall*.svg files found!")
        return
    
    print(f"Found {len(svg_files)} SVG file(s) to convert\n")
    
    success_count = 0
    for svg_path in svg_files:
        # Create PNG filename (same name, different extension)
        png_path = svg_path.replace('.svg', '.png')
        
        if convert_svg_to_png(svg_path, png_path):
            success_count += 1
    
    print(f"\nConversion complete: {success_count}/{len(svg_files)} files converted successfully")

if __name__ == "__main__":
    main()

