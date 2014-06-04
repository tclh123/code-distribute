#!/bin/bash

git submodule init
git submodule update

sudo pip install virtualenv

cp ./node/config.sh.example ./node/config.sh
cp ./proxy/config.sh.example ./proxy/config.sh
