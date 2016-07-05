#!/usr/bin/env bash
BRANCH=master
TARGET_REPO=nullne/nullne.github.io.git
PELICAN_OUTPUT_FOLDER=output

echo -e "Testing travis-encrypt"
echo -e "$VARNAME"

if [ "$TRAVIS_PULL_REQUEST" == "false" ]; then
    echo -e "Starting to deploy to Github Pages\n"
    if [ "$TRAVIS" == "true" ]; then
        git config --global user.email "co.nullne@gmail.com"
        git config --global user.name "nullne"
    fi
    #using token clone gh-pages branch
    git clone --quiet --branch=$BRANCH https://${GH_TOKEN}@github.com/$TARGET_REPO built_website > /dev/null
    #go into directory and copy data we're interested in to that directory
    cd built_website
    rsync -rv --exclude=.git  ../$PELICAN_OUTPUT_FOLDER/* .
    #add, commit and push files
    git add -f .
    git commit -m "春宵一刻值$TRAVIS_BUILD_NUMBER千金"
    git push -fq origin $BRANCH > /dev/null
    echo -e "Deploy completed\n"
fi
