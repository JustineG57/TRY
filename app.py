from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate_table', methods=['POST'])
def generate_table():
    html_link = request.form.get('html_link')
    name = request.form.get('name')

    # You can create your table here based on the html_link and name
    # For demonstration purposes, let's create a simple table with the provided data
    table_data = [
        {'Link': html_link, 'Name': name},
        {'Link': 'https://example.com', 'Name': 'Example'}
    ]

    return render_template('table.html', table_data=table_data)

if __name__ == '__main__':
    app.run(debug=True)
