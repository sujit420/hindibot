*********Training is offline*********
1. for intent_classifier training
    python intent_classifier.py

    training is done using hindiR

2. for ner training
    python train.py

3. all data files are in their corresponding folders
    hindi - native hindi data
    hindiR - hindi WX data (converted using wxc converter)

**********Prediction is done using api**********
1. tornado server is used (will run on 8000 port by default)
2. python BotServer.py will start the server

there are total 4 service

1. ner (will do ner tagging)
   curl -X POST \
  http://localhost:8000/ner/predict \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: 2b51822b-aa2e-b503-4ebf-e6a59e7c7f7a' \
  -H 'content-type: application/json' \
  -d '{
  "queries":["मैं इंदिरानगर से यशवंतपुर रेलवे स्टेशन जाना चाहता हूं"]
}
'

result - {
    "data": {
        "output": [
            {
                "Person": "मैं"
            },
            {
                "Loc": "इंदिरानगर"
            },
            {
                "Loc": "यशवंतपुर रेलवे स्टेशन"
            }
        ]
    }
}

2. intent classification (smalltalk/cab_book)
    curl -X POST \
  http://localhost:8000/intent/predict \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: 32549c36-614c-5303-16a6-fddd523b7441' \
  -H 'content-type: application/json' \
  -d '{
  "queries":["मैं इंदिरानगर से यशवंतपुर रेलवे स्टेशन जाना चाहता हूं"]
}
'
result - {
    "data": {
        "output": "cab_book"
    }
}

3. smalltalk response
    curl -X POST \
  http://localhost:8000/smalltalk/predict \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: d86247fa-3ad2-5d85-4012-e9f7305dd827' \
  -H 'content-type: application/json' \
  -d '{
  "queries":["आप कैसे हैं?"]
}
'
result - {
    "data": {
        "output": "मैं ठीक हूं, आपके क्या हाल हैं?"
    }
}

4. all (it will run evrything in pipeline)
     curl -X POST \
  http://localhost:8000/smalltalk/predict \
  -H 'Cache-Control: no-cache' \
  -H 'Postman-Token: d86247fa-3ad2-5d85-4012-e9f7305dd827' \
  -H 'content-type: application/json' \
  -d '{
  "queries":["आप कैसे हैं?"]
}
'
result - {
    "data": {
        "output": "मैं ठीक हूं, आपके क्या हाल हैं?"
    }
}


