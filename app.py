from flask import Flask, render_template, abort, redirect,request
app = Flask(__name__)
import requests



@app.route('/',methods=["GET","POST"])
def index():
    
    listado = [15,20,25,30,35,40]

    if request.method == "GET":
        return render_template("index.html",listado=listado)
    else:
        valor = int(request.form.get("valores"))
        url = "https://api.rawg.io/api/games"

        params = {
            "key": "d4641e6e548b489f919773236c54f8bb",
            "page_size": valor
        }

        response = requests.get(url, params=params)
    
        data = response.json()
        videojuegos = []

        for var in data["results"]:
            diccionario = {"nombre":var["name"],"imagen": var["background_image"],"año":var["released"]}
            videojuegos.append(diccionario)
        
        return render_template("index.html",videojuegos=videojuegos,listado=listado)
    
app.run("0.0.0.0",5000,debug=True)

