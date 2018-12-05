from flask import Flask,request,jsonify
import requests
application = Flask(__name__)

@application.route('/',methods=['POST'])
def temperature():

 req_data = request.get_json()
 #city_name = req_data['cityname']
 #area_code = req_data['areacode']
 
 for val in req_data['entities']:
  city_name = val['value']
  
 r = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+city_name+',in&appid=d092db6ed0c1484a47477095f3aefb80')
 json_oj = r.json()
 temp = float(json_oj['main']['temp'])
 city = json_oj['name']
 temp_f = (temp - 273.15) * 1.8 + 32
 temp_c = (temp_f - 32) * .55
 return jsonify(temperature=temp_c,
                 cityname = city)

#@app.route('/')
#def index():
#	return 'Hello'

if __name__ == '__main__':
  application.run(debug=True)
