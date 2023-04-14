from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
   return '호빵맨'

@app.route('/curry')
def mypage():  
   return '카레빵맨'

@app.route('/sick')
def breadpage():  
   return '식빵맨'

if __name__ == '__main__':  
   app.run('0.0.0.0',port=5000,debug=True)