#!/bin/bash
# Makes a request to 0.0.0.0:5000/catch_me that causes a server to respond.
curl -sX PUT -L -d "user_id=98" --header "origin: HolbertonSchool" 0.0.0.0:5000/catch_me
