from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')

def main():
	return render_template('index.html')

@app.route('/', methods=['POST'])


def mathematicla():
	text = request.form['text']
	operation = request.form['operation']
	api = 'https://newton.now.sh/api/v2//' + operation + '/' + text
	data = requests.get(api).json()
	result = data['result']
	return render_template('index.html', result=result, equation=operation)


if __name__=='__main__':
	app.run()