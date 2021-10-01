import sys
from flask import Flask, jsonify, request

sys.path.append("..")

# Ignore the warning(red line) telling you to install the 'brain' package. This script will still run as its meant to
from brain import Brain

# Creating the flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = "dfG#4$dGAjf;Ope9r8en%cs"

# Creating an instance of the 'Brain' class
brain = Brain()


@app.route("/morse", methods=["POST"])
def translate():
    query_string = request.args.get("q")

    if query_string is not None:
        if len(query_string) != 0:
            result = brain.convert_to_morse(query_string)
            message = {"message": "success", "contents": {"morse_equivalent": result, "original_text": query_string}}
            return jsonify(message), 200
        else:
            message = {"message": "Error. Please enter the string you would like to convert."}
            return jsonify(message), 404
    else:
        message = {"message": "Error. Missing query('q') parameter."}
        return jsonify(message), 400


@app.route("/morse/english", methods=["POST"])
def translate_to_english():
    query_string = request.args.get("q")

    if query_string is not None:
        if len(query_string) != 0:
            result = brain.convert_to_english(query_string)
            message = {"message": "success", "contents": {"english_equivalent": result, "morse_text": query_string}}
            return jsonify(message), 200
        else:
            message = {"message": "Error. Please enter the string you would like to convert."}
            return jsonify(message), 404
    else:
        message = {"message": "Error. Missing query('q') parameter."}
        return jsonify(message), 400


if __name__ == "__main__":
    app.run()
