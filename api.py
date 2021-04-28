# api.py

from flask import Flask, jsonify, request, abort

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def index():
    info = {
        "mensaje" : "Bienvendio al curso.",
        "acciones" : [
            "GET /curriculum",
            "POST /mensajes",
        ],
    }
    return jsonify(info)

@app.route('/curriculum', methods=['GET'])
def cv():
    url_imagen = request.host_url + "static/Calavera.png"
    cv = {
        "nombre" : "Simón",
        "apellido" : "Saint-André",
        "residencia" : "Argentina",
        "experiencia" : [{
            "posición" : "< describe >",
            "empresa" : "< nombre >",
            "desde" : "< fecha >",
            "hasta" : "< fecha >",
            "descripcion" : "< detalles >",
        }],
        "educación" : {
            "nivel" : "< nivel de tus estudios >",
            "título" : "Licenciado en Cs. Físicas",
            "insittucion" : "UBA",
            "facultad" : "EXACTAS",
        },
        "intereses" : ["python", "sneks", "rest"],
        "redes" : {
            "github" : "https://github.com/sstandre"
        },
        "foto" : url_imagen

    }
    return jsonify(cv)
 
@app.route('/mensajes', methods=['POST'])
def contacto():
    mensaje = request.get_data()
    if not mensaje:
        abort(400, description="Debe enviar su mensaje en el body del POST.")
    print(f"MENSAJE DE CONTACTO: {mensaje}")
    return "Gracias por su mensaje." 


if __name__ == "__main__":
    app.run()