#!/bin/bash
# SVG to PNG Converter using macOS qlmanage
# Converts all bathroom_wall*.svg files to PNG format

echo "Converting SVG files to PNG..."
echo ""

# Change to project directory
cd "$(dirname "$0")/.."

# Counter for successful conversions
count=0

# Loop through all bathroom_wall*.svg files
for svg_file in bathroom_wall*.svg; do
    if [ -f "$svg_file" ]; then
        # Get the base name without extension
        base_name="${svg_file%.svg}"
        png_file="${base_name}.png"
        
        # Convert using qlmanage (macOS built-in tool)
        qlmanage -t -s 2048 -o . "$svg_file" > /dev/null 2>&1
        
        # qlmanage creates files with .png.png extension, rename them
        if [ -f "${svg_file}.png" ]; then
            mv "${svg_file}.png" "$png_file"
            echo "✓ Converted: $svg_file -> $png_file"
            ((count++))
        else
            echo "✗ Failed to convert: $svg_file"
        fi
    fi
done

echo ""
echo "Conversion complete: $count file(s) converted successfully"

