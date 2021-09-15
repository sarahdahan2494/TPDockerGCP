#!/bin/bash
if [ -z "$TOTO"]; then
    echo "la variable d'env toto n'existe pas "
    return 1
fi

while true;
do
    echo $1\($(date+ %H:%M:%S)\)
    sleep 1
    echo $TOTO
done 