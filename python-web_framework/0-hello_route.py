'''script that creates web application using flask'''
   
    
'''importing flask'''
from flask import Flask

'''creates the variable application name'''
app = Flask(__name__)

'''route for retrieving hello HBNB'''
@app.route('/', strict_slashes=False)
def hbnb():
    return 'Hello HBNB!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)