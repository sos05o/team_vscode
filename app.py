from flask import Flask, render_template, redirect, session, request, url_for
# import numpy as np


app = Flask(__name__)

@app.route('/')
def top_page():
    return render_template('index.html')


@app.route('/develop_a')
def develop_a():
    pass

@app.route('/develop_b')
def develop_b():
    return render_template("circle.html")

@app.route("/calculation")
def calculation():
    n = float(request.args.get("num"))

    # pi = np.pi()
    pi = 3.14

    result = []

    result.append(2*n*pi)
    result.append(n**2*pi)

    print(result)

    return render_template("result_b.html", result=result)


if __name__=='__main__':
    app.run(debug=True)