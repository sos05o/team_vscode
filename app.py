from flask import Flask, render_template, redirect, session, request, url_for


app = Flask(__name__)
app.secret_key = ''.join(rd.choices(string.ascii_letters, k=256))

@app.route('/')
def top_page():
    return render_template('index.html')


@app.route('/develop_a')
def develop_a():
    pass

@app.route('/develop_b')
def develop_b():
    pass


if __name__=='__main__':
    app.run(debug=True)