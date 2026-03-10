#!/bin/bash

echo "Extracting commit author details..."

AUTHOR_NAME=$(git log -1 --pretty=format:'%an')
AUTHOR_EMAIL=$(git log -1 --pretty=format:'%ae')

echo "Author Name: $AUTHOR_NAME"
echo "Author Email: $AUTHOR_EMAIL"

if [[ "$AUTHOR_NAME" != *.* ]]; then
    echo "ERROR: Username must contain '.'"
    exit 1
fi

if [[ "$AUTHOR_EMAIL" != *@optimumdataanalytics.com ]]; then
    echo "ERROR: Email must belong to @optimumdataanalytics.com"
    exit 1
fi

echo "Identity validation passed."
