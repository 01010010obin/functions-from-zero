# functions-from-zero
MLOps

[![python application test with github actions](https://github.com/01010010obin/functions-from-zero/actions/workflows/main.yml/badge.svg)](https://github.com/01010010obin/functions-from-zero/actions/workflows/main.yml)

### To call Microservices

'''bash 
curl -X 'POST' \
  'https://silver-sniffle-qjgj5757q94c4vg5-8080.app.github.dev/wiki' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "name": "Machine Learning"
}'
'''

### Build container 
'docker build .'
'docker image ls'

### Run container 

'docker run -p 127.0.0.1:8080:8080 fb3dae7aa7c1'

### Invoke POST request

run 'invoke.sh'