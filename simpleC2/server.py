import logging
import os
from flask import Flask, request
import json
import requests as req

app = Flask(__name__)

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')

@app.route('/runCommand')
def server_api():
    command = request.args.get('command')
    containerInfoString = os.environ.get('CONTAINTER_INFO')
    print(containerInfoString)
    containerInfo = json.loads(containerInfoString)
    responseList = []
    for i in range(len(containerInfo)):
        url = f"http://{containerInfo[i]['host']}:{containerInfo[i]['port']}/run?command={command}"
        app.logger.info(f"url being hit {url}")
        response = req.request("GET", url, headers={}, data={})
        
        app.logger.info(f"for container {i} response is {response.text}")
        responseList.append(response.text)
    return responseList

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT'))


# requests.request("GET", "bot_a:5001/run?command=ls", headers={}, data={})