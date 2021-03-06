#!/bin/bash -e

TARGET_IMAGE="${REGISTRY_URL}/${IMAGE_NAME}"

docker build -t $TARGET_IMAGE .

docker login --username $REGISTRY_USERNAME \
             --password $REGISTRY_PASSWORD \
             $REGISTRY_ADDRESS

# Latest
TARGET_IMAGE_LATEST="${TARGET_IMAGE}:latest"
docker tag ${TARGET_IMAGE} ${TARGET_IMAGE_LATEST}
docker push ${TARGET_IMAGE_LATEST}

# Versioned
VERSION=$(date '+%Y-%m-%d__%H-%M-%S')
TARGET_IMAGE_VERSIONED="${TARGET_IMAGE}:${VERSION}"
docker tag ${TARGET_IMAGE} ${TARGET_IMAGE_VERSIONED}
docker push ${TARGET_IMAGE_VERSIONED}
