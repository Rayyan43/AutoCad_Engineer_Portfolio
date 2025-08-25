from flask import Flask, request, jsonify
import json
import os

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit_form():
    # Retrieve form data
    name = request.form.get('name')
    email = request.form.get('email')
    subject = request.form.get('subject')
    message = request.form.get('message')

    # Validate form data
    if not name or not email or not message:
        return jsonify({'error': 'Missing required fields'}), 400

    # Prepare data for storage
    form_data = {
        'name': name,
        'email': email,
        'subject': subject,
        'message': message
    }

    # Ensure the submissions directory exists
    os.makedirs('submissions', exist_ok=True)

    # Write data to a file
    submission_id = len(os.listdir('submissions')) + 1
    file_path = f'submissions/submission_{submission_id}.json'

    with open(file_path, 'w') as file:
        json.dump(form_data, file)

    return jsonify({'success': True, 'message': 'Form submitted successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)