from flask import Flask, render_template, redirect, session, request, url_for


app = Flask(__name__)

@app.route('/')
def top_page():
    return render_template('index.html')


@app.route('/develop_a')
def develop_a():
    return render_template('develop_1.html')

@app.route('/develop_b')
def develop_b():
    pass

@app.route('/dev_a_1')
def dev_a_1():
    price = request.args.get('price')
    hour = request.args.get('hour')

    dev = int(price) * int(hour)

    return render_template('develop_1_ans.html', dev = dev)


if __name__=='__main__':
    app.run(debug=True)