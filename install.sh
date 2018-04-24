set -eo pipefail

if [ $1 = "-h" ]; then
    echo "Usage: ./install.sh <install-path>"
    exit 0
fi

pip3 install pyperclip readchar --user

start_dir=$(pwd)

cd $(dirname "${BASH_SOURCE[0]}")
source_path=$(pwd)

cd $1 

rm $1/fourcut 2>/dev/null || true
ln -s $source_path/four_cut.py fourcut