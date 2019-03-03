from flask import Flask, redirect
from flask import jsonify
from flask import request
from JSONOps import JSONOps
from CamelCase import CamelCase
import json, os

app = Flask(__name__)
json_ = JSONOps(path=os.path.join(os.path.dirname(__file__),"files","CamelCase.json"))
camel_case = CamelCase()


@app.route('/all',methods=['GET'])
def getAllCamelCases():
    return jsonify(json.loads(json_.get_from_json()))

@app.route('/camelcase/<string>',methods=['GET'])
def getCamelCase(string):
    if string is None:
        return jsonify({"response":"failure: Invalid Input"})
    try:
        return jsonify({string:json.loads(json_.get_from_json())[string]})
    except:
        return jsonify({"error":"failed"})

@app.route('/camelcase',methods=['PUT'])
def updateCamelCase():
    try:
        json_.append_json_file(request.json)
        return jsonify(request.json)
    except:
        return jsonify({"error":"failed"})        

@app.route('/camelcase/<string>',methods=['POST'])
def createCamelCase(string):
    if string is None:
        return jsonify({"response":"failure: Invalid Input"})
    dat = {string:camel_case.convert_camel_case(string)}
    try:
        json_.append_json_file(dat)
    except Exception as e:
        return jsonify({"response":"failure:{}".format(e)})

    return jsonify(dat)

@app.route('/camelcase/<string>',methods=['DELETE'])
def deleteCamelCase(string):
    if string is None:
        return jsonify({"response":"failure: Invalid Input"})
    try:
        camelcase_db = json.loads(json_.get_from_json())
        del(camelcase_db[string])
        json_.update_json_file(camelcase_db)
    except:
        return jsonify({"response":"failure"})
    return jsonify({'response':'Success'})

camel_case.initialize_camel_case()
app.run(host="0.0.0.0",port=80)