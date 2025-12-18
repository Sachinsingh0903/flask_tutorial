from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient, errors
import os
from dotenv import load_dotenv

load_dotenv()
uri=os.getenv('uri')
# Create a new client and connect to the server
client = MongoClient(uri)

app = Flask(__name__)

# Replace with your MongoDB Atlas connection string
# MONGO_URI = "YOUR_CONNECTION_STRING"
# client = MongoClient(MONGO_URI)
db = client['mydatabase']
collection = db['mycollection']

@app.route('/', methods=['GET', 'POST'])
def index():
    error = None
    if request.method == 'POST':
        # Get form data
        name = request.form.get('name')
        email = request.form.get('email')

        # Validate data
        if not name or not email:
            error = "All fields are required."
        else:
            try:
                # Insert into MongoDB
                collection.insert_one({'name': name, 'email': email})
                return redirect(url_for('success'))
            except errors.PyMongoError as e:
                error = f"Error inserting into database: {str(e)}"
    return render_template('index.html', error=error)

@app.route('/success')
def success():
    return "Data submitted successfully"

@app.route('/todo')
def todo():
    return render_template('todo.html')

if __name__ == '__main__':
    app.run(debug=True)