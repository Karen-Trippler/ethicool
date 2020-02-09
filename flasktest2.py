from flask import Flask, request #import main Flask class and request object

app = Flask(__name__) #create the Flask app

@app.route('/', methods=['GET', 'POST'])
def query_example():
    language = request.args.get('language') #if key doesn't exist, returns None
    framework = request.args['framework'] #if key doesn't exist, returns a 400, bad request error
    website = request.args.get('website')

    return '''<h1>The language value is: {}</h1>
              <h1>The framework value is: {}</h1>
              <h1>The website value is: {}'''.format(language, framework, website)

if __name__ == '__main__':
    app.run(debug=True, port=5000) #run app in debug mode on port 5000