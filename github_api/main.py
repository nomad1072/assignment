from flask import Flask, request, jsonify, make_response
from typing import List, Dict

import requests

app = Flask(__name__)

def searchURL(baseURL: str, query: str, language: str) -> str:
    if language is not None:
        url = baseURL + '?q={}+language:{}'.format(query, language)
    else:
        url = baseURL + '?q={}'.format(query)
    
    return url

def sanitizedResponse(items: List[Dict]) -> List[Dict]:
    repositories = list()
    for item in items:
        repository = dict()
        repository['name'] = item['full_name']
        repository['url'] = item['html_url']
        repository['description'] = item['description']
        repository['language'] = item['language'] if item['language'] else False
        repositories.append(repository)
    
    return repositories

@app.route("/repos", methods=['GET'])
def searchHandler():
    query = request.args.get('q')
    language = request.args.get('language')
    limit = 10 if request.args.get('limit') is None else int(request.args.get('limit'))

    if query is None:
        response = { 'status': 'error', 'message': 'No query parameter specified'}
        return make_response(jsonify(response), 400)

    try:
        url = searchURL("https://api.github.com/search/repositories", query, language)
        response = requests.get(url).json()
        items = response['items'][:limit]
        repositories = sanitizedResponse(items)        
        return make_response(jsonify(repositories), 200)
    
    except Exception as e:
        response = { 'status': 'error', 'message': 'Internal Server Error', 'error': e.message }
        return make_response(jsonify(response), 500)

if __name__ == "__main__":
    app.run()