#!/bin/bash
set -e
task test
uvicorn src.api.app:server --host 0.0.0.0 --port 8000 --reload
