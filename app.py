from flask import Flask, render_template
from api.routes import api_bp

app = Flask(__name__)

# Register the API blueprint
app.register_blueprint(api_bp)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/books')
def list_books():
    return render_template('books.html')

@app.route('/add_book')
def add_book():
    return render_template('add_book.html')

@app.route('/api/docs')
def api_docs():
    return render_template('api_docs.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
