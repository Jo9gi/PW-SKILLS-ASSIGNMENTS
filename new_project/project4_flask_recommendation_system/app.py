from flask import Flask, render_template

app = Flask(__name__)

# Sample recommendation data with links
recommendations = [
    {"title": "Learn Python", "description": "Start with Python basics and advance to web development.", "link": "https://www.python.org/about/gettingstarted/"},
    {"title": "Explore Data Science", "description": "Understand data analysis, visualization, and machine learning.", "link": "https://www.datascience.com/learn-data-science"},
    {"title": "Build Flask Apps", "description": "Create web applications using Flask framework.", "link": "https://flask.palletsprojects.com/en/latest/"},
    {"title": "Master APIs", "description": "Learn how to consume and build RESTful APIs.", "link": "https://restfulapi.net/"},
    {"title": "Deploy to Cloud", "description": "Deploy your applications on cloud platforms like AWS, Azure, or Heroku.", "link": "https://aws.amazon.com/getting-started/"}
]

@app.route('/')
def home():
    return render_template('index.html', recommendations=recommendations)

if __name__ == '__main__':
    app.run(debug=True)
