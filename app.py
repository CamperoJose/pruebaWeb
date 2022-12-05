from flask import Flask, render_template, request

# from telefericotiempo import TT

app = Flask(__name__, template_folder='templates')

TT = dict()

TT['RioSeco'] = [['UPEA', 426]]
TT['UPEA'] = [['RioSeco', 426], ['PzaLaPaz', 283]]
TT['PzaLaPaz'] = [['UPEA', 283], ['PzaLaLibertad', 258]]
TT['PzaLaLibertad'] = [['PzaLaPaz', 258], ['16deJulio', 268]]
TT['16deJulio'] = [['PzaLaLibertad', 268], ['Cementerio', 338], ['FaroMurillo', 516]]
TT['Cementerio'] = [['16deJulio', 338], ['Central', 309]]
TT['Central'] = [['Cementerio', 309], ['Armentia', 239]]
TT['Armentia'] = [['Central', 239], ['Periferica', 227]]
TT['Periferica'] = [['Armentia', 227], ['Villarroel', 274]]
TT['Villarroel'] = [['Periferica', 274], ['Busch', 237]]
TT['Busch'] = [['Villarroel', 237], ['Triangular', 288], ['LasVillas', 227]]
TT['Triangular'] = [['Busch', 288], ['DelPoeta', 196]]
TT['DelPoeta'] = [['Triangular', 196], ['TeatroAlAireLibre', 210], ['Libertador', 190]]
TT['LasVillas'] = [['Busch', 227]]
TT['TeatroAlAireLibre'] = [['DelPoeta', 210], ['Prado', 220]]
TT['Prado'] = [['TeatroAlAireLibre', 220]]
TT['Libertador'] = [['DelPoeta', 190], ['AltoObrajes', 205], ['Sopocachi', 397]]
TT['AltoObrajes'] = [['Libertador', 205], ['Obrajes', 309]]
TT['Obrajes'] = [['AltoObrajes', 309], ['Irpavi', 467]]
TT['Irpavi'] = [['Obrajes', 467]]
TT['Sopocachi'] = [['Libertador', 397], ['BuenosAires', 375]]
TT['BuenosAires'] = [['Sopocachi', 375], ['Mirador', 240]]
TT['Mirador'] = [['BuenosAires', 240], ['FaroMurillo', 246]]
TT['FaroMurillo'] = [['Mirador', 246], ['Obelisco', 480], ['6deMarzo', 487], ['16deJulio', 516]]
TT['Obelisco'] = [['FaroMurillo', 480]]
TT['6deMarzo'] = [['FaroMurillo', 487]]

TP = dict()
precio_teleferico = 2



TP['Azul'] = [['Roja', precio_teleferico], ['Plateada', precio_teleferico]]
TP['Plateada'] = [['Roja', precio_teleferico], ['Amarilla', precio_teleferico], ['Morada', precio_teleferico]]
TP['Naranja'] = [['Roja', precio_teleferico], ['Blanca', precio_teleferico]]
TP['Roja'] = [['Naranja', precio_teleferico], ['Azul', precio_teleferico], ['Plateada', precio_teleferico]]
TP['Verde'] = [['Celeste', precio_teleferico], ['Amarilla', precio_teleferico]]
TP['Celeste'] = [['Blanca', precio_teleferico], ['Amarilla', precio_teleferico], ['Verde', precio_teleferico]]
TP['Blanca'] = [['Naranja', precio_teleferico], ['Cafe', precio_teleferico], ['Celeste', precio_teleferico]]
TP['Amarilla'] = [['Plateada', precio_teleferico], ['Verde', precio_teleferico], ['Celeste', precio_teleferico]]
TP['Morada'] = [['Plateada', precio_teleferico]]
TP['Cafe'] = [['Blanca', precio_teleferico]]

R2P = dict()

R2P['Roja'] = ['Central', 'Cementerio', '16deJulio']
R2P['Azul'] = ['RioSeco', 'UPEA', 'PzaLaPaz', 'PzaLaLibertad', '16deJulio']
R2P['Naranja'] = ['Central', 'Armentia', 'Periferica', 'Villarroel']
R2P['Blanca'] = ['Villarroel', 'Busch', 'Triangular', 'DelPoeta']
R2P['Cafe'] = ['Busch', 'LasVillas']
R2P['Celeste'] = ['Prado', 'TeatroAlAireLibre', 'DelPoeta', 'Libertador']
R2P['Verde'] = ['Libertador', 'AltoObrajes', 'Obrajes', 'Irpavi']
R2P['Amarilla'] = ['Libertador', 'Sopocachi', 'BuenosAires', 'Mirador']
R2P['Plateada'] = ['Mirador', 'FaroMurillo', '16deJulio']
R2P['Morada'] = ['Obelisco', 'FaroMurillo', '6deMarzo']

P2R = {'RioSeco': ['Azul'], 'UPEA': ['Azul'], 'PzaLaPaz': ['Azul'], 'PzaLaLibertad': ['Azul'],
        '16deJulio': ['Roja', 'Azul', 'Plateada'], 'Cementerio': ['Roja'], 'Central': ['Roja', 'Naranja'],
        'Armentia': ['Naranja'], 'Periferica': ['Naranja'], 'Villarroel': ['Naranja', 'Blanca'], 'Busch':
            ['Blanca', 'Cafe'], 'Triangular': ['Blanca'], 'DelPoeta': ['Blanca', 'Celeste'], 'LasVillas': ['Cafe'],
        'TeatroAlAireLibre': ['Celeste'], 'Prado': ['Celeste'], 'Libertador': ['Celeste', 'Verde', 'Amarilla'],
        'AltoObrajes': ['Verde'], 'Obrajes': ['Verde'], 'Irpavi': ['Verde'], 'Sopocachi': ['Amarilla'],
        'BuenosAires': ['Amarilla'], 'Mirador': ['Amarilla', 'Plateada'], 'FaroMurillo': ['Plateada', 'Morada'],
        'Obelisco': ['Morada'], '6deMarzo': ['Morada']}


def deshabilitarlineas(lineas, precio_teleferico):

    TT['RioSeco'] = [['UPEA', 426]]
    TT['UPEA'] = [['RioSeco', 426], ['PzaLaPaz', 283]]
    TT['PzaLaPaz'] = [['UPEA', 283], ['PzaLaLibertad', 258]]
    TT['PzaLaLibertad'] = [['PzaLaPaz', 258], ['16deJulio', 268]]
    TT['16deJulio'] = [['PzaLaLibertad', 268], ['Cementerio', 338], ['FaroMurillo', 516]]
    TT['Cementerio'] = [['16deJulio', 338], ['Central', 309]]
    TT['Central'] = [['Cementerio', 309], ['Armentia', 239]]
    TT['Armentia'] = [['Central', 239], ['Periferica', 227]]
    TT['Periferica'] = [['Armentia', 227], ['Villarroel', 274]]
    TT['Villarroel'] = [['Periferica', 274], ['Busch', 237]]
    TT['Busch'] = [['Villarroel', 237], ['Triangular', 288], ['LasVillas', 227]]
    TT['Triangular'] = [['Busch', 288], ['DelPoeta', 196]]
    TT['DelPoeta'] = [['Triangular', 196], ['TeatroAlAireLibre', 210], ['Libertador', 190]]
    TT['LasVillas'] = [['Busch', 227]]
    TT['TeatroAlAireLibre'] = [['DelPoeta', 210], ['Prado', 220]]
    TT['Prado'] = [['TeatroAlAireLibre', 220]]
    TT['Libertador'] = [['DelPoeta', 190], ['AltoObrajes', 205], ['Sopocachi', 397]]
    TT['AltoObrajes'] = [['Libertador', 205], ['Obrajes', 309]]
    TT['Obrajes'] = [['AltoObrajes', 309], ['Irpavi', 467]]
    TT['Irpavi'] = [['Obrajes', 467]]
    TT['Sopocachi'] = [['Libertador', 397], ['BuenosAires', 375]]
    TT['BuenosAires'] = [['Sopocachi', 375], ['Mirador', 240]]
    TT['Mirador'] = [['BuenosAires', 240], ['FaroMurillo', 246]]
    TT['FaroMurillo'] = [['Mirador', 246], ['Obelisco', 480], ['6deMarzo', 487], ['16deJulio', 516]]
    TT['Obelisco'] = [['FaroMurillo', 480]]
    TT['6deMarzo'] = [['FaroMurillo', 487]]


    TP['Azul'] = [['Roja', precio_teleferico], ['Plateada', precio_teleferico]]
    TP['Plateada'] = [['Roja', precio_teleferico], ['Amarilla', precio_teleferico], ['Morada', precio_teleferico]]
    TP['Naranja'] = [['Roja', precio_teleferico], ['Blanca', precio_teleferico]]
    TP['Roja'] = [['Naranja', precio_teleferico], ['Azul', precio_teleferico], ['Plateada', precio_teleferico]]
    TP['Verde'] = [['Celeste', precio_teleferico], ['Amarilla', precio_teleferico]]
    TP['Celeste'] = [['Blanca', precio_teleferico], ['Amarilla', precio_teleferico], ['Verde', precio_teleferico]]
    TP['Blanca'] = [['Naranja', precio_teleferico], ['Cafe', precio_teleferico], ['Celeste', precio_teleferico]]
    TP['Amarilla'] = [['Plateada', precio_teleferico], ['Verde', precio_teleferico], ['Celeste', precio_teleferico]]
    TP['Morada'] = [['Plateada', precio_teleferico]]
    TP['Cafe'] = [['Blanca', precio_teleferico]]


    R2P['Roja'] = ['Central', 'Cementerio', '16deJulio']
    R2P['Azul'] = ['RioSeco', 'UPEA', 'PzaLaPaz', 'PzaLaLibertad', '16deJulio']
    R2P['Naranja'] = ['Central', 'Armentia', 'Periferica', 'Villarroel']
    R2P['Blanca'] = ['Villarroel', 'Busch', 'Triangular', 'DelPoeta']
    R2P['Cafe'] = ['Busch', 'LasVillas']
    R2P['Celeste'] = ['Prado', 'TeatroAlAireLibre', 'DelPoeta', 'Libertador']
    R2P['Verde'] = ['Libertador', 'AltoObrajes', 'Obrajes', 'Irpavi']
    R2P['Amarilla'] = ['Libertador', 'Sopocachi', 'BuenosAires', 'Mirador']
    R2P['Plateada'] = ['Mirador', 'FaroMurillo', '16deJulio']
    R2P['Morada'] = ['Obelisco', 'FaroMurillo', '6deMarzo']

    P2R = {'RioSeco': ['Azul'], 'UPEA': ['Azul'], 'PzaLaPaz': ['Azul'], 'PzaLaLibertad': ['Azul'],
            '16deJulio': ['Roja', 'Azul', 'Plateada'], 'Cementerio': ['Roja'], 'Central': ['Roja', 'Naranja'],
            'Armentia': ['Naranja'], 'Periferica': ['Naranja'], 'Villarroel': ['Naranja', 'Blanca'], 'Busch':
                ['Blanca', 'Cafe'], 'Triangular': ['Blanca'], 'DelPoeta': ['Blanca', 'Celeste'],
            'LasVillas': ['Cafe'],
            'TeatroAlAireLibre': ['Celeste'], 'Prado': ['Celeste'], 'Libertador': ['Celeste', 'Verde', 'Amarilla'],
            'AltoObrajes': ['Verde'], 'Obrajes': ['Verde'], 'Irpavi': ['Verde'], 'Sopocachi': ['Amarilla'],
            'BuenosAires': ['Amarilla'], 'Mirador': ['Amarilla', 'Plateada'], 'FaroMurillo': ['Plateada', 'Morada'],
            'Obelisco': ['Morada'], '6deMarzo': ['Morada']}

    paradas = list()
    for lindesab in lineas:
        for i in R2P[lindesab]:
            paradas.append(i)  # Todas las paradas que pertenecen a una linea deshabilitada

    for lindesab in lineas:
        # Deshabilitar en TT
        for pardesab in R2P[lindesab]:  # Para todas las paradas que pertezcan a una linea deshabilitada
            for vecino in TT[pardesab]:  # Revisa todos sus vecinos
                if vecino[0] in paradas:  # Si tiene una conexión con una parada por medio de una linea deshabilitada
                    vecino[1] = 1e8  # Su costo en INF

        # Deshabilitar en TP
        TP[lindesab] = []  # La linea se queda sin conexiones
        for linea in TP.keys():  # para todas las otras lineas
            for conexion in TP[linea]:  # Revisa todas sus conexiones
                if lindesab == conexion[0]:  # Si tenías una conexión con la linea a deshabilitar
                    conexion[1] = 1e8  # Su costo es INF

        # Deshabilitar en R2P
        R2P[lindesab] = []
        # Deshabilitar en P2R
        for parada in P2R.keys():
            if lindesab in P2R[parada]:
                P2R[parada].remove(lindesab)


def printruta(desde, ruta):
    r = list()
    r.insert(0, desde)
    while ruta[desde] != 0:
        desde = ruta[desde]
        r.insert(0, desde)
    return r


def rutaminima(ini, fin, grafo, k):
    pq = list()
    ruta = dict()
    dist = dict()

    for v in grafo.keys():
        if v == ini:
            dist[v] = k
            ruta[v] = 0
        else:
            dist[v] = 1e8
            ruta[v] = 0

    pq.insert(0, ini)
    while pq:
        v = pq.pop(0)
        for vecino, t in grafo[v]:
            if dist[vecino] > dist[v] + t:
                if dist[vecino] == 1e8:
                    pq.append(vecino)
                else:
                    pq.insert(0, vecino)
                dist[vecino] = dist[v] + t
                ruta[vecino] = v

    return printruta(fin, ruta), dist[fin]


def costomin(origen, destino, k):
    rutamin = list()
    distprev = 1e8

    for o in P2R[origen]:
        for d in P2R[destino]:
            # print(origen, destino)
            ruta, dist = rutaminima(o, d, TP, k)
            if ruta and dist < distprev:
                rutamin = ruta
                distprev = dist
    return rutamin, distprev


def tiempomin(origen, destino, k=0):
    # for p in TT.keys():
    #     print(p," : ", TT[p])

    # print("---------------------")
    return rutaminima(origen, destino, TT, k)


def trazarRutaLineas(origen, destino, lineas):
    paradasparaverificar = list()
    for linea in lineas:
        for parada in R2P[linea]:
            paradasparaverificar.append(parada)
    ruta = dict()
    for parada in TT.keys():
        ruta[parada] = 0

    q = list()
    q.append(origen)
    v = ""
    while q:
        v = q.pop(0)
        for vecino, t in TT[v]:
            if vecino in paradasparaverificar and ruta[vecino] == 0 and vecino != origen:
                ruta[vecino] = v
                q.append(vecino)
        if ruta[destino] != 0:
            break
    return printruta(destino, ruta)


def trazarRutaParadas(origen, destino, paradas):
    i = 0
    ruta = list()
    while i < len(paradas) - 1:
        for linea in P2R[paradas[i]]:
            if linea in P2R[paradas[i + 1]] and linea not in ruta:
                ruta.append(linea)
                break
        i += 1
    return ruta


def calcprecio(r, k):
    p = k
    for i in range(len(r) - 1):
        for vecino, time in TP[r[i]]:
            if vecino == r[i + 1]:
                p += time
    return p


def calctiempo(r, k=0):
    t = k
    for i in range(len(r) - 1):
        for vecino, time in TT[r[i]]:
            if vecino == r[i + 1]:
                t += time
    return t


@app.route('/', methods=["GET", "POST"])
def home():
    lineas = []
    destinos = []
    rutamin = dict()
    tiempo = 0
    t = ''
    cp = 0
    rutaPosible = True
    lineas_deshabilitadas = []
    opt=''
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

    if request.method == 'POST':
        tarjeta = request.form['tarjeta']
        if tarjeta == '1':
            precio = 2
            tarjeta_k = 3
        elif tarjeta == '2' or tarjeta == '3':
            precio = 1
            tarjeta_k = 1.5
        org1 = request.form['org1']
        org2 = request.form['org2']
        opt = request.form['opt']
        lineas_deshabilitadas = []
        lineas = []
        destinos = []
        rutamin = dict()
        tiempo = 0
        t = ''
        cp = 0
        rutaPosible = True
        if request.form.get('Azul'):
            lineas_deshabilitadas.append('Azul')
        if request.form.get('Cafe'):
            lineas_deshabilitadas.append('Cafe')
        if request.form.get('Plateada'):
            lineas_deshabilitadas.append('Plateada')
        if request.form.get('Naranja'):
            lineas_deshabilitadas.append('Naranja')
        if request.form.get('Roja'):
            lineas_deshabilitadas.append('Roja')
        if request.form.get('Verde'):
            lineas_deshabilitadas.append('Verde')
        if request.form.get('Celeste'):
            lineas_deshabilitadas.append('Celeste')
        if request.form.get('Blanca'):
            lineas_deshabilitadas.append('Blanca')
        if request.form.get('Amarilla'):
            lineas_deshabilitadas.append('Amarilla')
        if request.form.get('Morada'):
            lineas_deshabilitadas.append('Morada')
        print('lienas des: ', lineas_deshabilitadas)

        '''
        if org1!="invalid" and org2!="invalid" :
            destinos = [org1,org2]
            lineas = [dict_estacion_linea[org1], dict_estacion_linea[org2]]
            #parte de calculo:

            rutamin['ruta'], distmin = rutaminima(org1, org2, TT, 0)
            a=distmin//60
            b=distmin%60
            tiempo=[a,b]
            tam=len(rutamin['ruta'])
        '''

        desde = org1
        hasta = org2

        # timeormoney = input("Tiempo o dinero? (t/d): ")
        timeormoney = "t"

        if opt == 'Tiempo':
            timeormoney = "t"
        else:
            timeormoney = "d"

        deshabilitarlineas(lineas_deshabilitadas, precio) # precio 
        #print(lineas_deshabilitadas)
        destinos = [org1, org2]
        if timeormoney == 't':
            rutamin, t = tiempomin(desde, hasta)
            print('rutamin: ', rutamin)
            print('lineas: ', lineas)
            cp=calcprecio(trazarRutaParadas(desde, hasta, rutamin), tarjeta_k) # tarjeta_k
            print(t)
            a = t // 60
            b = t % 60
            tiempo = [a, b]
        else:
            rutamin, p = costomin(desde, hasta, tarjeta_k) # tarjeta_k
            cp=p
            print(cp)
            t=calctiempo(trazarRutaLineas(desde, hasta, rutamin))
            print(t)
            a = t // 60
            b = t % 60
            tiempo = [a, b]
            rutamin = trazarRutaLineas(desde, hasta, rutamin)

        rutaPosible = True
        if cp>10000 or t>10000:
            rutaPosible=False


    return render_template('index.html', destinos=destinos, lineas=lineas, estacionLinea=dict_estacion_linea,
                            rutamin=rutamin, tiempo=tiempo, precio=cp, lineas_deshabilitadas=lineas_deshabilitadas, rutaPosible=rutaPosible, opt=opt)


if __name__ == '__main__':
    app.run(debug=True)
