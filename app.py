from flask import Flask, render_template, request
#from telefericotiempo import TT

app = Flask(__name__, template_folder='templates')


def printruta(desde, ruta):
    r = list()
    r.insert(0, desde)
    while ruta[desde] != 0:
        desde = ruta[desde]
        r.insert(0, desde)
    return r


def rutaminima(ini, fin, grafo, k):
    visitados = list()
    queue = list()

    dist = dict()
    ruta = dict()

    for node in list(grafo.keys()):
        ruta[node] = 0
        if node == ini:
            dist[node] = k
        else:
            dist[node] = 1e8

    v = ini
    queue.append(v)

    while queue:

        visitados.append(v)
        if fin in visitados:
            return printruta(fin, ruta), dist[fin]
        # print(v)
        for vecino in grafo[v]:

            # print(vecino)
            if vecino[0] not in visitados:
                queue.append(vecino[0])
                if (dist[v] + vecino[1] < dist[vecino[0]]):
                    dist[vecino[0]] = dist[v] + vecino[1]
                    ruta[vecino[0]] = v
        # d = input()
        v = queue.pop(0)

@app.route('/', methods=["GET", "POST"])
def home():
    lineas =[]
    destinos=[]
    rutamin = dict()
    tiempo=0
    dict_estacion_linea = {"RioSeco": ("Azul"),
                           "UPEA": ("Azul"),
                           "PzaLaPaz": ("Azul"),
                           "PzaLaLibertad": ("Azul"),
                           "16deJulio": ("Azul", "Roja"),
                           "Cementerio": ("Roja"),
                           "Central": ("Roja", "Naranja"),
                           "Armentia": ("Naranja"),
                           "Periferica": ("Naranja"),
                           "Villarroel": ("Naranja", "Blanco"),
                           "Busch": ("Blanco", "Cafe"),
                           "LasVillas": ("Cafe"),
                           "Triangular": ("Blanco"),
                           "DelPoeta": ("Celeste", "Blanco"),
                           "TeatroAlAireLibre": ("Celeste"),
                           "Prado": ("Celeste"),
                           "Libertador": ("Celeste", "Verde", "Amarillo"),
                           "AltoObrajes": ("Verde"),
                           "Obrajes": ("Verde"),
                           "Irpavi": ("Verde"),
                           "Sopocachi": ("Amarillo"),
                           "BuenosAires": ("Amarillo"),
                           "Mirador": ("Amarillo", "Plateado"),
                           "FaroMurillo": ("Plateado", "Morado"),
                           "Obelisco": ("Morado"),
                           "6deMarzo": ("Morado"),
                           "Prado": ("Celeste")
                           }

    TT = dict()

    TT['RioSeco'] = [('UPEA', 426)]
    TT['UPEA'] = [('RioSeco', 426), ('PzaLaPaz', 283)]
    TT['PzaLaPaz'] = [('UPEA', 283), ('PzaLaLibertad', 258)]
    TT['PzaLaLibertad'] = [('PzaLaPaz', 258), ('16deJulio', 268)]
    TT['16deJulio'] = [('PzaLaLibertad', 268), ('Cementerio', 338), ('FaroMurillo', 516)]
    TT['Cementerio'] = [('16deJulio', 338), ('Central', 309)]
    TT['Central'] = [('Cementerio', 309), ('Armentia', 239)]
    TT['Armentia'] = [('Central', 239), ('Periferica', 227)]
    TT['Periferica'] = [('Armentia', 227), ('Villarroel', 274)]
    TT['Villarroel'] = [('Periferica', 274), ('Busch', 237)]
    TT['Busch'] = [('Villarroel', 237), ('Triangular', 288), ('LasVillas', 227)]
    TT['Triangular'] = [('Busch', 288), ('DelPoeta', 196)]
    TT['DelPoeta'] = [('Triangular', 196), ('TeatroAlAireLibre', 210), ('Libertador', 190)]
    TT['LasVillas'] = [('Busch', 227)]
    TT['TeatroAlAireLibre'] = [('DelPoeta', 210), ('Prado', 220)]
    TT['Prado'] = [('TeatroAlAireLibre', 220)]
    TT['Libertador'] = [('DelPoeta', 190), ('AltoObrajes', 205), ('Sopocachi', 397)]
    TT['AltoObrajes'] = [('Libertador', 205), ('Obrajes', 309)]
    TT['Obrajes'] = [('AltoObrajes', 309), ('Irpavi', 467)]
    TT['Irpavi'] = [('Obrajes', 467)]
    TT['Sopocachi'] = [('Libertador', 397), ('BuenosAires', 375)]
    TT['BuenosAires'] = [('Sopocachi', 375), ('Mirador', 240)]
    TT['Mirador'] = [('BuenosAires', 240), ('FaroMurillo', 246)]
    TT['FaroMurillo'] = [('Mirador', 246), ('Obelisco', 480), ('6deMarzo', 487), ('16deJulio', 516)]
    TT['Obelisco'] = [('FaroMurillo', 480)]
    TT['6deMarzo'] = [('FaroMurillo', 487)]

    if request.method == 'POST':
        org1 = request.form['org1']
        org2 = request.form['org2']
        if org1!="invalid" and org2!="invalid" :
            destinos = [org1,org2]
            lineas = [dict_estacion_linea[org1], dict_estacion_linea[org2]]
            #parte de calculo:

            rutamin['ruta'], distmin = rutaminima(org1, org2, TT, 0)
            a=distmin//60
            b=distmin%60
            tiempo=[a,b]
            tam=len(rutamin['ruta'])
    return render_template('index.html', destinos=destinos, lineas=lineas,estacionLinea=dict_estacion_linea, rutamin=rutamin, tiempo=tiempo)


if __name__ == '__main__':
    app.run(debug=True)

