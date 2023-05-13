#!/bin/bash
curl -X POST -H 'Content-type: application/json' http://localhost:5000/add  -d '{ "name": "smallled", "count": "10", "description": "A small led" }'
curl -X POST -H 'Content-type: application/json' http://localhost:5000/add  -d '{ "name": "redled", "count": "30", "description": "A  led" }'
curl -X POST -H 'Content-type: application/json' http://localhost:5000/add  -d '{ "name": "sallled", "count": "10", "description": "A ssall led" }'
