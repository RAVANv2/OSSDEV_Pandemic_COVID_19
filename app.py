from flask import Flask, render_template, request, redirect, flash, url_for 
import requests
app = Flask(__name__)

@app.route('/',methods=['Get','Post'])
def homepage():   
    country = 'India'
    if request.method == 'POST':
        country = request.form['country']
    url = "https://api.covid19api.com/countries"
    ans = requests.get(url).json()
    for i in ans:
        if i['Country'] == country:
            print(country)
    return render_template('main.html',newCountry=country)

# @app.route('/pendemic/')
# def pendemic(x):
#     return render_template('pendemic.html',newCountry=x)

if __name__=="__main__":
    app.run(debug=True)