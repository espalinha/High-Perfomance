#!/bin/bash

#Creating the shared lib

cd ./C/

gcc -c functions.c -fPIC

gcc -o libfunc.so -shared functions.o