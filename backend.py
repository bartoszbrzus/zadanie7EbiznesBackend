from flask import Flask, jsonify, request
import openai

app = Flask(__name__)

openai.api_key = input('Enter your API KEY: ')


@app.route('/api/data', methods=['GET'])
def get_data():
    payload = request.get_json()
    chat = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=payload.get('content')
    )
    reply = chat.choices[0].message.content
    return jsonify(reply)


if __name__ == '__main__':
    app.run(port=8000)
