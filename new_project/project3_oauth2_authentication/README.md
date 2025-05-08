# OAuth2 Authentication with Flask

This project is a Flask application that implements OAuth2 authentication allowing users to log in using their Google accounts.

## Uses

- Provides secure user authentication using Google OAuth2 without managing passwords.
- Demonstrates integration of OAuth2 protocol in Flask applications.
- Shows how to handle user sessions and retrieve user profile information.
- Useful for building web applications requiring third-party authentication.
- Can be extended to support other OAuth2 providers like Facebook, GitHub, etc.

## Setup

1. Register your application with Google to get `client_id` and `client_secret`.
2. Replace `YOUR_GOOGLE_CLIENT_ID` and `YOUR_GOOGLE_CLIENT_SECRET` in `app.py` with your credentials.

## How to Run

1. Install dependencies:
```
pip install -r requirements.txt
```

2. Run the Flask app:
```
python app.py
```

3. Open your browser and go to `http://127.0.0.1:5000/` to log in with Google.
python app.py
2. Run the Flask app:
