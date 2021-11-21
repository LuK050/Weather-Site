# -*- coding: utf8 -*-
from flask import *
from script.weather import *


class Site:
    app = Flask(__name__)


    @app.route("/", methods = ["GET", "POST"])
    def index():
        
        if request.method == "POST":
            
            if request.form["city"] is None or request.form["city"] == "":
                return render_template("pages/index.html", city = False)
            
            else:
                city = request.form["city"].title()
                weather = Weather.get_weather(city)
                
                if weather is None:
                    return render_template("pages/error.html", error = "Указанный вами город не найден!")
                
                return render_template("pages/index.html", city = city, weather = weather)
        
        else:
            return render_template("pages/index.html", city = False)


    if __name__ == "__main__":
        app.run(debug=True)
