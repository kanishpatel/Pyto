#!/bin/bash

cd "$(dirname "${BASH_SOURCE[0]}")"

source environment.sh

export PYTHON_CROSSENV=1
export PYODIDE_PACKAGE_ABI=1

cd ../skimage
python3 setup.py build
python3 ../tools/make_frameworks.py skimage SkImage
../tools/copy-scripts.sh build/lib*/* ../../../downloadable-site-packages/compiled/skimage
