#!/bin/bash
uvicorn src.main:app --host 0.0.0.0 --port $PORT --ssl-keyfile=./keystore/key.pem --ssl-certfile=./keystore/cert.pem