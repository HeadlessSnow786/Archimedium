from flask import Flask, render_template, request

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

@application.route('/inputTest', methods=['GET', 'POST'])
def inputTest():
    if request.method == 'POST':
            data = request.form['prompt']
            return render_template('inputTest.html', data=data)
    else:
        return render_template('inputTest.html')
    
@application.route('/latexTest')
def latexTest():
    return render_template('latexTest.html')
    
if __name__ == '__main__':
    application.run(debug=True)