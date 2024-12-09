from app import app

def test_case():
    # Create a test client
    client = app.test_client()

    # Test the home page
    response = client.get("/")
    assert response.status_code == 200
    assert response.data == b"Welcome to the Simple Flask App!"

    # Test the about page
    response = client.get("/about")
    assert response.status_code == 200
    assert response.data == b"This is the about page of the Flask app."

    # Test the contact page
    response = client.get("/contact")
    assert response.status_code == 200
    assert response.data == b"Contact us at contact@flaskapp.com."

    # Test the services page
    response = client.get("/services")
    assert response.status_code == 200
    assert b"<h1>Our Services</h1>" in response.data
