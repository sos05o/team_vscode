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
    return render_template("circle.html")

@app.route("/calculation")
def calculation():
    n = float(request.args.get("num"))

    # pi = np.pi()
    pi = 3.14

    result = []

    result.append(2*n*pi)
    result.append(n**2*pi)

    return render_template("result_b.html", result=result)

@app.route('/dev_a_1')
def dev_a_1():
    price = request.args.get('price')
    hour = request.args.get('hour')

    dev = int(price) * int(hour)

    return render_template('develop_1_ans.html', dev = dev)


if __name__=='__main__':
    app.run(debug=True)