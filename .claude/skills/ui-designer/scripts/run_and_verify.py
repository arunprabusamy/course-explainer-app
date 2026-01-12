#!/usr/bin/env python3
"""
Start Flask application and prepare for visual verification.
This ensures the app is running before Playwright takes screenshots.
"""

import subprocess
import time
import sys
import os

def main():
    """Start Flask server and guide through verification"""
    
    # Check if we're in the right directory
    if not os.path.exists('src/app.py'):
        print("❌ Error: src/app.py not found!")
        print("Make sure you run this from the project root directory.")
        sys.exit(1)
    
    print("🚀 Starting Flask development server...")
    print("-" * 50)
    
    # Start Flask in background
    try:
        proc = subprocess.Popen(
            [sys.executable, "src/app.py"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        
        # Wait for server to initialize
        time.sleep(3)
        
        # Check if process is running
        if proc.poll() is None:
            print("✅ Flask server started successfully!")
            print(f"📝 Process ID: {proc.pid}")
            print("🌐 Application running at: http://127.0.0.1:5000")
            print("-" * 50)
            print()
            print("📸 NEXT STEPS FOR VISUAL VERIFICATION:")
            print()
            print("1. Use Playwright MCP tool to:")
            print("   → Navigate to http://127.0.0.1:5000")
            print("   → Take a full-page screenshot")
            print("   → Save as: test-output/design-check.png")
            print()
            print("2. Analyze the screenshot to understand current design")
            print()
            print("3. Proceed with designing the new feature")
            print()
            print("-" * 50)
            print(f"💡 To stop server: kill {proc.pid}")
            
        else:
            print("❌ Flask server failed to start!")
            stdout, stderr = proc.communicate()
            print("Output:", stdout.decode())
            print("Errors:", stderr.decode())
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ Error starting Flask: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()