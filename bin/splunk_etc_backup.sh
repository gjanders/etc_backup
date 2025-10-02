#!/bin/bash

SOURCE_DIR="$(dirname "$0")"
# Copy files from source to destination
/opt/splunk/bin/splunk cmd python "$SOURCE_DIR"/splunk_etc_backup.py
