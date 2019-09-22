import os
import pandas as pd
import webbrowser
os.chdir(r'C:\Users\akash.warkhade\Documents\PY')
from flask import Flask, render_template, request
#from flask.ext.googlemaps import GoogleMap
#from  flask_googlemaps import GooogleMaps
app = Flask(__name__)
 
@app.route('/')
def student():
   return render_template('content.html')
 
@app.route('/getclinics',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      getclinics = int(request.form['Service ID'])
      print(getclinics)
      #for value in getclinics.values():
       # print(value)
        #i=int(value)
      df1=pd.read_csv('clinicservicelocations.csv')
      df3=df1[(df1.ServiceID==getclinics)]
      df4=df3[["Name","Suburb","State","Email","Service","Lat","Lon"]]
      return render_template("sisid.html",  data_frame=df4.to_html())

@app.route('/locator',methods = ['POST', 'GET'])
def kk():
 if request.method == 'POST':
  locate = request.form['Service_type']
  print(locate)
  #for value in locate.values():
   #     print(value)
        #i=str(value)
  df1=pd.read_csv('clinicservicelocations.csv')
  #i=str(value)
  df2=df1[(df1.Service==locate)]
  for lat,lon in zip(df2["Lat"],df2["Lon"]):
   lat = lat
   lon = lon
   String_link = "http://maps.google.com/maps?q=loc:" + ("%f,%f" %(lat, lon))
   print(String_link)
   webbrowser.open_new_tab(String_link)
  return ('', 204)  
 
if __name__ == '__main__':
   app.run()
