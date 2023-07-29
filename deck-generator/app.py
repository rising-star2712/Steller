
from flask import Flask, send_file, make_response, request
from hmtl_gen import generate_presentation
import json
app = Flask(__name__)

@app.route('/')
def home():
    return send_file('home.html')


@app.route('/get_html', methods=['POST'])
def fetch_html():
    request_data = request.json
    topic = request_data.get("topic")
    if not topic:
        return {"error": "Please provide a topic"}

    style = request_data.get("style", "style1")
    num_slides = request_data.get("num_slides", 5)
    image_source = request_data.get("image_source", "Pexel")
    html_content = generate_presentation(topic, style, num_slides,image_source)

    return html_content


if __name__ == '__main__':
    app.run(debug=True)