#flask api - sum: 30

from flask import Flask, jsonify, request
import json

app = Flask(__name__)


@app.route('/sum')
def sum_numbers():
    num1 = request.args.get('a')
    num2 = request.args.get('b')
    sumnum = int(num1) + int(num2)

    return jsonify(
        "sum: " + "{}".format(sumnum)   
    )

if __name__=='__main__':
    app.run(debug=True)

