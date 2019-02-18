#!/bin/bash

set -xe

source services/params.sh

# copy the packages
rm -rf services/artifacts/debian/$DOCKER_TAG
mkdir -p services/artifacts/debian/$DOCKER_TAG
mkdir -p services/artifacts/debian/$DOCKER_TAG/debs
mkdir -p services/artifacts/debian/$DOCKER_TAG/java
docker run -it --rm -u $(id -u)\
  -v $PWD/services/artifacts/debian/$DOCKER_TAG:/tohere:Z\
  $BASE/rdkit-build:$DOCKER_TAG bash -c 'cp build/*.deb /tohere/debs && cp Code/JavaWrappers/gmwrapper/org.RDKit.jar /tohere/java && cp Code/JavaWrappers/gmwrapper/libGraphMolWrap.so /tohere/java'

