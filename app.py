from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/inputTest', methods=['GET', 'POST'])
def inputTest():
    if request.method == 'POST':
            data = request.form['prompt']
            return render_template('inputTest.html', data=data)
    else:
        return render_template('inputTest.html')
    
@app.route('/latexTest')
def latexTest():
    return render_template('latexTest.html')
    
if __name__ == '__main__':
    app.run(debug=True)