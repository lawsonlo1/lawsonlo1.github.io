#mentorapp.py

from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)

# Connect to the MongoDB Atlas cluster
client = MongoClient('mongodb+srv://lawsonlo1:<Gothampearl123>@gothamdata.wgyabvu.mongodb.net/?retryWrites=true&w=majority')
db = client['gothamdata']
emails_collection = db['emails']

# Existing route for the landing page
@app.route('/')
def landing_page():
    return render_template('index.html')

# New route to handle form submission
@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']  # Get the submitted email from the form
    # Store the email in the MongoDB collection
    emails_collection.insert_one({'email': email})
    return 'Thank you for subscribing!'

if __name__ == '__main__':
    app.run(port=5000)
