def sendreq():
    print("Sending request...")
    
    import requests

    URL = "http://127.0.0.1:5000"

    json_example = {
        "agente": 1,
        "position": {
            "x": 10,
            "y": 20
        }
    }

    # agentpy_json es el endpoint
    r = requests.post(url=URL+"/agentpy_json", json=json_example)

    print(r.text)