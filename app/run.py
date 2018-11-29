from flask import Flask, render_template #flask is the framework while Flask is a python class
app = Flask(__name__) #create instance of flask - name is special variable
@app.route('/') #mapped to home url
def home():
    return render_template('index.html')

if __name__ == '__main__': #main is assigned to script when executed. If elsewhere script called hello.py
    app.run(debug=True) #to trace errors but false in production
