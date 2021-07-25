#!/bin/bash -e

TARGET_IMAGE="${REGISTRY_URL}/${IMAGE_NAME}"
TARGET_IMAGE_LATEST="${TARGET_IMAGE}:latest"
VERSION=$(date '+%Y-%m-%d__%H-%M-%S')
TARGET_IMAGE_VERSIONED="${TARGET_IMAGE}:${VERSION}"

docker pull $TARGET_IMAGE_LATEST
docker build -t $TARGET_IMAGE --cache-from $TARGET_IMAGE_LATEST .

docker login --username $REGISTRY_USERNAME \
             --password $REGISTRY_PASSWORD \
             $REGISTRY_ADDRESS

# Latest
docker tag ${TARGET_IMAGE} ${TARGET_IMAGE_LATEST}
docker push ${TARGET_IMAGE_LATEST}

# Versioned
docker tag ${TARGET_IMAGE} ${TARGET_IMAGE_VERSIONED}
docker push ${TARGET_IMAGE_VERSIONED}
