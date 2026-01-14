#!/usr/bin/env python3
"""
Start Flask application and prepare for visual verification.
"""

import subprocess
import time
import sys
import os
import urllib.request

def is_flask_running():
    """Check if Flask server is running using standard library"""
    try:
        # Standard library way to check the URL
        with urllib.request.urlopen('http://127.0.0.1:5000', timeout=2) as response:
            return response.getcode() == 200
    except Exception:
        return False

def main():
    """Start Flask server if needed and guide through verification"""
    
    # Check directory
    if not os.path.exists('src/app.py'):
        print("❌ Error: src/app.py not found!")
        print("Make sure you run this from the project root directory.")
        sys.exit(1)

    if is_flask_running():
        print("✅ Flask server is already running!")
    else:
        print("🚀 Starting Flask development server...")

        try:
            # We use Popen so it runs in the background
            subprocess.Popen(
                [sys.executable, "src/app.py"],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                start_new_session=True # Keeps it running independently
            )
        
            # Wait for server to initialize
            time.sleep(3)
        
            if is_flask_running():
                print("✅ Flask server started successfully!")
            else:
                print("❌ Failed to start Flask server. Check src/app.py for errors.")
                sys.exit(1)    
            
        except Exception as e:
            print(f"❌ Error starting Flask: {e}")
            sys.exit(1)

    print("-" * 50)
    print("👉 ACTION REQUIRED: Use Playwright MCP now.")
    print("1. Navigate to http://127.0.0.1:5000")
    print("2. Take a screenshot: 'test-output/before-design.png'")
    print("-" * 50)

if __name__ == "__main__":
    main()