#!/bin/bash

DIR="/home/alex/Pictures/Terminal"
BG_IMAGE=$(find "$DIR" -name '*.png' | shuf -n 1)
kitty --override background_image=$BG_IMAGE "$@" &
