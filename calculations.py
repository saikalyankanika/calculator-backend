
from flask import Flask,jsonify,request
from flask_cors import CORS


# instance of flask application
app = Flask(__name__)
CORS(app)

# home route that returns below text when root url is accessed
@app.route("/calculate", methods=['POST'])
def calculate_expression():
    try:
        data = request.get_json()
        expression = data.get('expression')
        print(type(expression),expression)
        result = eval(expression)
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__': 
    app.run(debug = True)
