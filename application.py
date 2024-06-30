from flask import Flask, render_template, request

application = Flask(__name__)

@application.route('/')
def index():
    return render_template('index.html')

# @application.route('/inputTest', methods=['GET', 'POST'])
# def inputTest():
   # if request.method == 'POST':
           # data = request.form['prompt']
           # return render_template('inputTest.html', data=data)
   # else:
       # return render_template('inputTest.html')

@application.route('/about')
def about():
    return render_template('about.html')

@application.route('/unit1')
def unit1():
    return render_template('unit1.html')

@application.route('/unit2')
def unit2():
    return render_template('unit2.html')

@application.route('/unit3')
def unit3():
    return render_template('unit3.html')

@application.route('/unit4')
def unit4():
    return render_template('unit4.html')

@application.route('/unit5')
def unit5():
    return render_template('unit5.html')

@application.route('/unit6')
def unit6():
    return render_template('unit6.html')

@application.route('/unit7')
def unit7():
    return render_template('unit7.html')

@application.route('/unit8')
def unit8():
    return render_template('unit8.html')

@application.route('/unit9')
def unit9():
    return render_template('unit9.html')

@application.route('/unit10')
def unit10():
    return render_template('unit10.html')

if __name__ == '__main__':
    application.run(debug=True)