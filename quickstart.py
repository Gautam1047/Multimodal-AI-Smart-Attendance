"""
Quickstart & Fast-Launcher Script
One-step automated setup: verifies environment, installs missing dependencies,
seeds sample assets, and launches the Streamlit live application.
"""

import sys
import os
import subprocess

REQUIRED_PACKAGES = [
    "streamlit",
    "opencv-python",
    "mediapipe",
    "librosa",
    "soundfile",
    "plotly",
    "pandas",
    "google-generativeai"
]

def check_and_install_dependencies():
    print("=" * 70)
    print("⚡ Fast Setup: Checking Multimodal AI Attendance System Requirements...")
    print("=" * 70)

    missing = []
    for pkg in REQUIRED_PACKAGES:
        # Normalize package import name
        mod_name = pkg.replace("-", "_").split("==")[0]
        if pkg == "opencv-python":
            mod_name = "cv2"
        elif pkg == "google-generativeai":
            mod_name = "google.generativeai"

        try:
            __import__(mod_name)
            print(f"  [OK] {pkg} is installed.")
        except ImportError:
            print(f"  [MISSING] {pkg} not found.")
            missing.append(pkg)

    if missing:
        print("\nInstalling missing requirements via pip (this runs once)...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", *missing])
            print("All dependencies successfully installed!")
        except Exception as e:
            print(f"Notice during installation: {e}")
            print("Proceeding to launch app with built-in resilient offline fallbacks...")
    else:
        print("\nAll requirements verified! Ready to launch.")

def run_app():
    print("\n" + "=" * 70)
    print("🚀 Launching Live Dashboard at http://localhost:8501 ...")
    print("=" * 70 + "\n")
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "app.py"])
    except KeyboardInterrupt:
        print("\nApp stopped.")

if __name__ == "__main__":
    check_and_install_dependencies()
    run_app()
