#!/usr/bin/env python3
"""
Code-o-dachi Launcher
Simple launcher script for the Code-o-dachi application
"""

import sys
import subprocess

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 6):
        print("❌ Python 3.6 or higher is required!")
        print(f"Current version: {sys.version}")
        return False
    return True

def check_tkinter():
    """Check if tkinter is available"""
    try:
        import tkinter
        return True
    except ImportError:
        print("❌ tkinter is not available!")
        print("Please install tkinter for your Python distribution.")
        return False

def main():
    """Main launcher function"""
    print("🚀 Code-o-dachi Launcher")
    print("=" * 30)
    
    # Check requirements
    if not check_python_version():
        sys.exit(1)
        
    if not check_tkinter():
        sys.exit(1)
        
    print("✅ All requirements satisfied!")
    print("🎮 Starting Code-o-dachi...")
    print()
    
    # Launch the main application
    try:
        from code_o_dachi import main as run_game
        run_game()
    except ImportError:
        # Fallback: run as subprocess
        subprocess.run([sys.executable, "code_o_dachi.py"])

if __name__ == "__main__":
    main()