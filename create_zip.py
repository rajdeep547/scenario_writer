import os
import zipfile
from pathlib import Path

def create_project_zip():
    """Create a clean zip file of the project"""
    
    # Define what to exclude
    exclude_folders = {
        'node_modules', '__pycache__', 'venv', 'env', 
        '.git', 'build', 'dist', '.next', 'frontend/build'
    }
    
    exclude_files = {
        '.env', '.DS_Store', 'Thumbs.db', '*.pyc', '*.pyo',
        'test_results_*.json', 'output_scenario.json', '*.log'
    }
    
    exclude_extensions = {'.pyc', '.pyo', '.log'}
    
    # Output zip name
    zip_name = "AI_Scenario_Writer_Project.zip"
    
    print(f"📦 Creating {zip_name}...")
    
    with zipfile.ZipFile(zip_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk('.'):
            # Skip excluded folders
            dirs[:] = [d for d in dirs if d not in exclude_folders]
            
            for file in files:
                # Skip excluded files
                if file in exclude_files:
                    continue
                
                # Skip by extension
                if any(file.endswith(ext) for ext in exclude_extensions):
                    continue
                
                # Get full file path
                file_path = os.path.join(root, file)
                
                # Skip the zip file itself
                if file_path == zip_name:
                    continue
                
                # Add to zip
                arcname = os.path.relpath(file_path, '.')
                zipf.write(file_path, arcname)
                print(f"  Added: {arcname}")
    
    # Get file size
    size_mb = os.path.getsize(zip_name) / (1024 * 1024)
    print(f"\n✅ Zip created successfully!")
    print(f"📁 File: {zip_name}")
    print(f"📊 Size: {size_mb:.2f} MB")
    print(f"📍 Location: {os.path.abspath(zip_name)}")

if __name__ == "__main__":
    create_project_zip()