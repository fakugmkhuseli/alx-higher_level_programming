#!/usr/bin/node
const request = require('fs');
const request = require('request');
request(process.argv[2]).pipe(fs.createwriteStream(process.argv[3]));
