import matplotlib.pyplot as plt
import numpy as np

def addPoints(ruta,puntaje):
    puntajes = []
    archivo = open(ruta, "r")
    for line in archivo:
        lines = eval(line.rstrip("\n"))
        puntajes.append(lines)
    archivo.close()
    puntajes.append(puntaje)
    while len(puntajes) > 5:
        del puntajes[0]
    archivo = open(ruta,'w')
    for e in range(len(puntajes)):
        d = str(puntajes[e])
        if e == 0:
            archivo.write(d)
        else:
            archivo.write("\n"+d)
    archivo.close()

def graphScore(ruta):
    f = open(ruta, "r")
    i = 1
    xarray = []
    yarray = []
    for line in f:
        xvalue = "Player " + str(i)
        yvalue = eval(line.rstrip("\n"))
        yarray.append(yvalue)
        xarray.append(xvalue)
        i += 1
    f.close()
    x = np.array(xarray)
    y = np.array(yarray)
    
    plt.bar(x,y, color='green')
    plt.show()
