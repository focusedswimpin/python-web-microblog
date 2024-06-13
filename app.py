import datetime
import os
from flask import Flask, redirect, render_template, request
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)

    # Connect to MongoDB using the URI from environment variable
    client = MongoClient(os.getenv("MONGODB_URI"))
    app.db = client.microblog
    app.db.entries = app.db.get_collection('entries')

    @app.route("/", methods=["GET", "POST"])
    def home():
        if request.method == "POST":
            # If the request method is POST, then we can grab the content and do something with it.
            # "content" is the name of the text field.
            entry_content = request.form.get("content")
            # We also need the date when the entry was created.
            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")

            # Insert new entry into MongoDB
            app.db.entries.insert_one({"content": entry_content, "date": formatted_date})

            # Redirect to avoid resubmission on refresh
            return redirect(request.url)

        # Retrieve entries from MongoDB and format dates
        entries_with_date = []
        for entry in app.db.entries.find({}):
            content = entry.get("content", "No content")
            date_str = entry.get("date", "")
            if date_str:
                try:
                    date_formatted = datetime.datetime.strptime(date_str, "%Y-%m-%d").strftime("%b %d")
                except ValueError as e:
                    date_formatted = "Invalid date format"
                    app.logger.error(f"Error parsing date for entry: {entry['_id']}. Error: {str(e)}")
            else:
                date_formatted = "No date"
            
            entries_with_date.append((content, date_str, date_formatted))

        return render_template("home.html", entries=entries_with_date)

    return app
