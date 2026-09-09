#!/usr/bin/env python3
"""
MarkItDown Integration — Convert files to Markdown

Convert PDFs, Word docs, Excel files, and more to Markdown
for analysis by LLMs or manual review.
"""

import os
import sys
from pathlib import Path

try:
    from markitdown import MarkItDown
except ImportError:
    print("❌ markitdown not installed")
    print("   Run: pip install markitdown")
    sys.exit(1)


class DocumentConverter:
    """Convert various document formats to Markdown."""
    
    def __init__(self):
        self.converter = MarkItDown()
    
    def convert_file(self, file_path: str) -> str:
        """Convert a file to Markdown."""
        path = Path(file_path)
        
        if not path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        result = self.converter.convert(str(path))
        return result.text_content
    
    def convert_pdf(self, pdf_path: str) -> str:
        """Convert PDF to Markdown."""
        return self.convert_file(pdf_path)
    
    def convert_word(self, docx_path: str) -> str:
        """Convert Word document to Markdown."""
        return self.convert_file(docx_path)
    
    def convert_excel(self, xlsx_path: str) -> str:
        """Convert Excel file to Markdown."""
        return self.convert_file(xlsx_path)
    
    def convert_any(self, file_path: str) -> str:
        """Auto-detect and convert any supported format."""
        return self.convert_file(file_path)
    
    def convert_folder(self, folder_path: str, output_dir: str = "converted") -> list:
        """Convert all supported files in a folder."""
        folder = Path(folder_path)
        output = Path(output_dir)
        output.mkdir(parents=True, exist_ok=True)
        
        supported_extensions = {'.pdf', '.docx', '.xlsx', '.txt', '.html', '.md'}
        converted = []
        
        for file_path in folder.iterdir():
            if file_path.suffix.lower() in supported_extensions:
                output_path = output / f"{file_path.stem}.md"
                content = self.convert_file(str(file_path))
                
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                
                converted.append(output_path)
                print(f"✅ Converted: {file_path.name} → {output_path.name}")
        
        return converted


def main():
    """Main demonstration."""
    print("=" * 60)
    print("📄 MarkItDown — Document Converter")
    print("=" * 60)
    
    converter = DocumentConverter()
    
    print("\nSupported formats:")
    print("  • PDF (.pdf)")
    print("  • Word (.docx)")
    print("  • Excel (.xlsx)")
    print("  • Text (.txt)")
    print("  • HTML (.html)")
    print("  • Markdown (.md)")
    
    print("\nUsage:")
    print('  converter = DocumentConverter()')
    print('  content = converter.convert_file("contract.pdf")')
    print('  print(content)')
    
    print("\nBatch conversion:")
    print('  files = converter.convert_folder("./documents")')


if __name__ == "__main__":
    main()
