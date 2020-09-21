from flask import Flask, render_template, request
import genetic

app = Flask(__name__, static_url_path='/static')


@app.route('/', methods=["GET"])
def index():
    results = ''
    if request.args.get('input_string'):
        input_string = request.args.get('input_string')
        results = genetic.main(input_string)
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
