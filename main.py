import os
import random
import string
from flask import Flask, make_response

app = Flask(__name__)

def generate_random_number():
    return ''.join(str(random.randint(0, 9)) for _ in range(16))

def generate_random_string(length=16):
    return ''.join(random.choice(string.ascii_letters) for _ in range(length))

@app.route('/')
def home():
    response = make_response("Hello World!", 200)
    response.headers.extend({
        'Authorization': generate_random_number(),
        'X-Token': generate_random_string()
    })
    return response

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
