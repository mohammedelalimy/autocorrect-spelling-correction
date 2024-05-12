from flask import Flask, render_template, request, jsonify
from transformers import pipeline

# Initialize the spelling correction pipeline with max_new_tokens parameter
spelling_correction_pipe = pipeline("text2text-generation", model="Elalimy/english_spelling_correction",
                                    max_new_tokens=100)

# Initialize Flask app
app = Flask(__name__)


# Define a route to render the form
@app.route('/')
def index():
    return render_template('index.html')


# Define a route for spelling correction
@app.route('/correct', methods=['POST'])
def correct_spelling():
    # Get the input text from the request
    text = request.form['text']

    # Perform spelling correction
    corrected_text = spelling_correction_pipe(text)[0]['generated_text'].strip()

    # Return the corrected text as JSON
    return jsonify({'corrected_text': corrected_text})


if __name__ == '__main__':
    # Run the Flask app
    app.run(debug=True)
