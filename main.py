from flask import Flask, request, jsonify
from main_1 import main1

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def json_generator():
    req_body = request.get_json(silent=True)
    print(req_body)
    request_args = request.args

    if request.method == 'GET':
        user_query = request.args.get('query')
        print(user_query)
    else:  # POST request
        req_body = request.get_json()
        print(req_body)
        user_query = req_body.get('query')
        print(user_query)
        chat_sessionid = req_body.get('chat_sessionid')
        sessionid = req_body.get('sessionid')
        action = req_body.get('action')
        question = req_body.get('question')
        response = req_body.get('response')
        
    if not user_query:
        user_query = req_body.get('query')

    response = main1(req_body, "MD", "apac")
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
