from flask import Flask, render_template, request
from xml.dom.pulldom import START_ELEMENT, parse, parseString

app = Flask(__name__)

@app.route('/',methods=['GET', 'POST'])
def upload():
	if request.method == 'GET':
		return render_template("index.html")
	elif request.method == 'POST':
		file = request.files.get('file')
		data = parseString(file.read())
		content = ''
		for event, node in data:
			data.expandNode(node)
			content = node.toxml()
		return render_template("index.html",data=content)

if __name__ == "__main__":
    app.run('0.0.0.0',5000)
