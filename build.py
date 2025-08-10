# my-portfolio/build.py
"""
Build script for freezing the Flask application into static files.
Run this script to generate the static website for deployment.
"""
from app import freezer

if __name__ == '__main__':
    # Freeze the application into static files
    freezer.freeze()
    print("Static site generation complete! Files are in the 'build' directory.")