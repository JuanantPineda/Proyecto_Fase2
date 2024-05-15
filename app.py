from flask import Flask, render_template, abort, redirect,request
app = Flask(__name__)
import requests



@app.route('/',methods=["GET","POST"])
def index():
    
    listado = [15,20,25,30,35,40]

    if request.method == "GET":
        valor = 10
        url = "https://api.rawg.io/api/games"

        params = {
            "key": "d4641e6e548b489f919773236c54f8bb",
            "page_size": valor
        }

        response = requests.get(url, params=params)
    
        data = response.json()
        videojuegos = []

        for var in data["results"]:
            diccionario = {"nombre": var["name"], "imagen": var["background_image"], "año": var["released"]}
            videojuegos.append(diccionario)

        return render_template("index.html", videojuegos=videojuegos, listado=listado, valor=valor)
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
        
        return render_template("index.html",videojuegos=videojuegos,listado=listado,valor=valor)
    
@app.route('/buscador', methods=["GET", "POST"])
def buscador():
     
    if request.method == "GET":
        videojuegos = []
        return render_template("buscador.html", videojuegos=videojuegos)
    else:
        nombre = request.form.get("nombre")

        url = "https://api.rawg.io/api/games"

        params = {
            "key": "d4641e6e548b489f919773236c54f8bb",
            "search": nombre,
            "page_size": 1
        }

        response = requests.get(url, params=params)
    
        data = response.json()
        videojuegos = []

        for var in data["results"]:
            diccionario = {"nombre":var["name"], "imagen": var["background_image"], "año":var["released"]}
            videojuegos.append(diccionario)

        return render_template("buscador.html", videojuegos=videojuegos,nombre=nombre)


@app.route('/detalle/<nombre>')
def detalle(nombre):
     
    url = "https://api.rawg.io/api/games"

    params = {
        "key": "d4641e6e548b489f919773236c54f8bb",
        "search": nombre,
        "page_size": 1
    }

    response = requests.get(url, params=params)
    
    data = response.json()
    videojuegos = []
    plataforma = []
    genero = []

    for var in data["results"]:
        diccionario = {"nombre":var["name"],"imagen": var["background_image"],"año":var["released"],"puntuacion": var["metacritic"]}
        videojuegos.append(diccionario)
        for var2 in var["platforms"]:
           plataforma.append( var2["platform"]["name"])
        for var3 in var["genres"]:
           genero.append( var3["name"])


    return render_template("detalle.html",videojuegos=videojuegos,plataforma=plataforma,genero=genero)

app.run("0.0.0.0",5000,debug=True)

