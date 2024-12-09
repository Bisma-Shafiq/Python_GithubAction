from flask import Flask

# Create a Flask app
app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to the Simple Flask App!"
@app.route("/about")
def about():
    return "This is the about page of the Flask app."
@app.route("/contact")
def contact():
    return "Contact us at contact@flaskapp.com."
@app.route("/services")
def services():
    return """
    <h1>Our Services</h1>
    <ul>
        <li>Web Development</li>
        <li>Data Analysis</li>
        <li>Machine Learning Solutions</li>
    </ul>
    """
# Run the app
if __name__ == "__main__":
    app.run(debug=True)
