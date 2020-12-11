#!/bin/bash

for dir in */
do
    dir=${dir%*/}  # remove the trailing "/"
    image="eu.gcr.io/platform-blocks/blocks/${dir}"
    echo "Building and pushing docker image $image"
    pushd ${dir}
    docker build . -t ${image}
    docker push ${image}
    popd
done
