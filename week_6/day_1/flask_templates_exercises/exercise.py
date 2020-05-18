import flask

app = flask.Flask(__name__)

@app.route("blog")
def welcome():
	return "Welcome to the website"

@app.route("blog/articles")
def article_list():


html = flask.render_template_string("blog.html")