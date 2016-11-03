#!/bin/bash
if [ -f /usr/bin/pip ]; then
	pip install -r requirements.txt
else
	apt-get -y update && apt-get -y install pip
	pip install -r requirements.txt
fi

