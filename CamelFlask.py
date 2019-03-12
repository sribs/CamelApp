from flask import Flask, redirect
from flask import jsonify
from flask import request
from JSONOps import JSONOps
from CamelCase import CamelCase
from Dictionary import Dictionary
import json, os, sys

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
    #dat = {string:camel_case.convert_camel_case(string)}
    dat = {string:camel_case.convert_camelcase_dp(string)}
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

if __name__=="__main__":
    try:
        print(sys.argv, len(sys.argv))
        if len(sys.argv) == 2:
            camel_case.initialize_camel_case_api(sys.argv[-1])
        if len(sys.argv) >= 2:
            camel_case.initialize_camel_case_api(sys.argv[-3],sys.argv[-2],sys.argv[-1])
        else:
            print("Arguments Parsing Error: Insufficient Arguments")
            exit(0)
    except Exception as e:
        print("Arguments Parsing error:",e)
    print(camel_case.camel_dict.is_word("hello"))
    app.run(host="0.0.0.0",port=80)