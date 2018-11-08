from flask import Flask,request,jsonify
import textrank

app = Flask(__name__)

@app.route('/', methods=['POST'])
def create_task():
    input = request.get_json()
    result = []
    for req in input:
        keywords = {}
        keywords["result"] = textrank.obj_to_keywords(req)
        keywords["id"] = req["id"]
        result.append(keywords)
    return jsonify(result)

app.run(debug=True)