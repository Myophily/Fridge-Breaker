"""Fridge Breaker - Entry point for Streamlit app"""

import sys
from pathlib import Path

# Add src directory to path
src_path = Path(__file__).parent / "src"
sys.path.insert(0, str(src_path))

# Import and run main app
from app import main

if __name__ == "__main__":
    main()
