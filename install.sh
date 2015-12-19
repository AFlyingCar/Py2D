#!/bin/bash

function installDependency {
	sudo apt-get install "$1" || { exit 1; }
}

function installFile {
	sudo wget -t 10 -P "$1" http://raw.githubusercontent.com/AFlyingCar/Py2D/master/Py2D/"$2" || { exit 1; }
}

if [[ $# -eq 0 ]]; then
	idir="~/.Py2D"
else
	idir="$1"
fi

echo 'Updating repository list.'
sudo apt-get update || { exit 1; }

echo 'Installing Pygame'
installDependency python-pygame

echo 'Installing Py2D'
filelist="`wget -qO- http://raw.githubusercontent.com/AFlyingCar/Py2D/master/MANIFEST`"
while read -r line; do
	echo "Installing $line... "
	installFile "$idir" "$line"
done <<< "$filelist"

touch ~/.py2d_inst_dir
echo "$idir" >> "~/.py2d_inst_dir"
