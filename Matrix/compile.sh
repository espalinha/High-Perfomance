#!/bin/bash

cd C/

gcc -c functions.c -fPIC

gcc -o libfunc.so -shared functions.o