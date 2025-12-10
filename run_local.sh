#!/bin/bash
set -e

# Define virtual environment directory
VENV_DIR="venv"

# Create virtual environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

# Activate virtual environment
source $VENV_DIR/bin/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Clean previous build artifacts
echo "Cleaning previous artifacts..."
rm -rf build *.so *.c

# Compile app.py using Cython
echo "Compiling app.py..."
python build.py build_ext --inplace

# Check if .so file was created
if ls app.*.so 1> /dev/null 2>&1; then
    echo "Compilation successful. Compiled extension found."
else
    echo "Compilation failed! No .so file found."
    exit 1
fi

# Renaming logic (optional, for consistency with docker approach if needed, 
# but python imports .so automatically if name matches)
# Inplace build creates app.cpython-XYZ.so which python imports as 'app'.

echo "Starting Uvicorn..."
echo "Use Ctrl+C to stop the server."

# Run Uvicorn
# We use 'app:app' normally. Python prefers the .so if it exists and we don't delete the .py
# To strictly test the compiled version locally, we would rename app.py, but that messes up the repo.
# Standard python behavior: if .so matches module name in path, it might be preferred or conflict.
# To be essentially sure we are running the compiled version, we can temporarily move app.py
# BUT, Uvicorn usually reloads or looks for source. 
# For 'simple' verification, we rely on the build step succeeding. 
# To TRULY verify compiled code is running, we usually delete app.py as in Docker.
# Let's try to mimic that safely.

# Trap to cleanup and restore app.py on exit
cleanup() {
    echo "Stopping server and cleaning up..."
    if [ -f app.py.bak ]; then
        mv app.py.bak app.py
    fi
    # Optional: remove artifacts to keep dir clean
    # rm -rf build *.so *.c
    echo "Done."
}
trap cleanup EXIT

# Temporarily rename app.py to enforce using the compiled module
mv app.py app.py.bak

# Run uvicorn
uvicorn app:app --host 0.0.0.0 --port 8000 --interface wsgi
