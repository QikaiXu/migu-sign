#!/usr/bin/env bash 

curl -H "Cookie: ${COOKIE}" -H "Content-Type: application/json; charset=UTF-8" -X POST -d '{}' 'https://gw.aikan.miguvideo.com/ygw/api/dispatch/migu-activity-custom/sign/sendAward'

