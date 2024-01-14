from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/unitSix', methods=['GET', 'POST'])
def unitSix():
    if request.method == 'POST':
            data = request.form['prompt']
            return render_template('unitSix.html', data=data)
    else:
        return render_template('unitSix.html')
    
if __name__ == '__main__':
    app.run(debug=True)