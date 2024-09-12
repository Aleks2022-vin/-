from flask import Flask, jsonify
import random

app = Flask(__name__)

# Пример списка изображений с автором
IMAGES = [
    {"url": "https://random.imagecdn.app/500/150", "author": "Author 1"},
    {"url": "https://random.imagecdn.app/600/400", "author": "Author 2"},
    {"url": "https://random.imagecdn.app/400/300", "author": "Author 3"},
    {"url": "https://random.imagecdn.app/500/500", "author": "Author 4"}
]

@app.route('/get-images')
def get_images():
    return jsonify(random.sample(IMAGES, 4))

if __name__ == '__main__':
    app.run(debug=True)