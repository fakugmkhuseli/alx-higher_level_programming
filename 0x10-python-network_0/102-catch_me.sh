#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes a server to respond.
curl -sL -X PUT -H "Origin: X-School" -d "user_id=98" 0.0.0.0:5000/catch_me
