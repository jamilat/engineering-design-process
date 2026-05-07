#!/bin/bash

set -e

docker build -t venn-app .

docker run --rm \
  -v $(pwd):/engineering-design-process \
  venn-app \
  bash

docker run -it --rm venn-app bash