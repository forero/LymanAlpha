from numpy import *
from scipy.interpolate import interp1d
import read_LyaRT

#Importo datos del triple pico
datos=loadtxt("./data/V150OC075.dat")
#Importo wl_in, wl_out
wl_in, wl_out = read_LyaRT.wls()

#Defino la interpolacion lineal
velocidades=datos[:,0]
intensidades=datos[:,1]
interpolacion = interp1d(velocidades, intensidades)

#Se hace la interpolacion para tener la misma cantidad de datos que con wl
velocidades_interpoladas = linspace(velocidades[0], velocidades[len(velocidades)-1], len(wl_out))
intensidades_interpoladas = interpolacion(velocidades_interpoladas)

#Entrada wl_in
peso_entrada_codigo=histogram(wl_in, nbins=20,normed=False, weights=intensidades_interpoladas)

#Salida wl_out
espectro_final=histogram(wl_out, nbins=20, normed=False, weights=peso_entrada_codigo)

#Guardar en archivo
datos[:,0]=velocidades_interpoladas
datos[:,1]=espectro_final
filename="prueba.dat"
savetxt(filename,datos) 

print "termin� :)"

##CORREO DE JULIAN
##
##Lo que tienes que hacer es 
##
##1) interpolar los datos de Jaime a una funci�n (interp1d de scipy.interpolate por ejemplo puede servirte link) y evalular el arreglo de wl_in en ese funci�n
##interpolada para obtener el arreglo wegihts.
##
##2)Los valores de esa evaluaci�n (weights) se los pasa como pesos a  la funci�n histogram de numpy para el arreglo wl_out
##
##
##B�sicamente lo que est�s es haciendo:  
##
##1) Evaluando la nueva contribuci�n (o peso) que tiene cada fot�n si el espectro de entrada es el de Jaime
##
##2) Entregarle ese peso calculado a arreglo de salida LyRT (wl_out) para que reajuste la forma del espectro dado el espectro de Jaime como entrada en
##vez de la distribuci�n plana inicial
##
##
##La raz�n por que lo que te hab�a dicho no funciona es porque el arreglo weights que se le debe pasar a la funci�n histogram debe ser de la misma
##longitud que el arreglo al que se le va a hacer el histograma (wl_out)  de modo que el c�digo internamente peuda saber cuanto eso tiene cada fot�n.
