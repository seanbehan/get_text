import lib
from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    Welcome to the Text API.
    Enter a URL and get the text
    <form action="/text" method="get">
        <input type="text" name="url" placeholder="Enter URL: http://example.com">
        <button>Go</button>
    </form>
    """

@app.route("/text")
def text():
    url = request.args.get('url', '')
    if url:
        x = lib.text(url)
        return x, 200, {'Content-Type': 'text/plain; charset=utf-8'}
    else:
        return ''

# if __name__=='__main__':
#     app.run()
