set -eo pipefail

if [ $1 = "-h" ]; then
    echo "Usage: ./install.sh <install-path>"
    exit 0
fi

start_dir=$(pwd)

cd $(dirname "${BASH_SOURCE[0]}")
source_path=$(pwd)

echo $1
cd $1 

ln -s $source_path/four-cut.py fourcut