from matplotlib.pylab import *
from matplotlib.pyplot import imshow
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import cm
from calor_de_hidratacion import Calor_de_hidratacion

#Geometria
a = 5.2 #alto del dominio Y
b = 10.4 #ancho del dominio X
ce = 5.2  #profundidad del dominio Z
Nx = 26
Ny = 13
Nz = 13

dx = b/Nx #discreticzacion expacial en x
dy = ce/Ny #discreticzacion expacial en y
dz = a/Nz #discreticzacion expacial en z

if dx != dy:
    print("ERROR! dy != dy")
    exit(-1)

#funcion de cenveniencia para calcular las coordenadas del punto (i,j)

coords = lambda i,j,k:(dx*i, dy*j, dz*k)

x,y,z = coords(4,2,1)
print ("x: ", x)
print ("y: ", y)
print ("z: ", z)


def imshowbienxy(u,r):
    imshow(u.T[Nx::-1,:],cmap=cm.coolwarm,interpolation='bilinear')
    cbar = colorbar(extend = 'both', cmap= cm.coolwarm)
    ticks = np.arange(0,35,5)
    ticks_Text = ["{}°".format(deg) for deg in ticks]
    cbar.set_ticks(ticks)
    cbar.set_ticklabels(ticks_Text)
    clim(0,30)
    xlabel('b(x)')
    ylabel('c(y)')
    xTicks_N= np.arange(0,Nx+1,3)
    yTicks_N= np.arange(0,Ny+1,3)
    xTicks= [coords(i,0,r)[0] for i in xTicks_N]
    yTicks= [coords(0,i,r)[1] for i in yTicks_N]
    xTicks_Text = ["{0:.2f}".format(tick) for tick in xTicks]
    yTicks_Text = ["{0:.2f}".format(tick) for tick in yTicks]
    xticks(xTicks_N,xTicks_Text, rotation='vertical')
    yticks(yTicks_N,yTicks_Text)
    margins(0.2)
    subplots_adjust(bottom=0.15)
    
def imshowbienxz(u,r):
    imshow(u.T[Nx::-1,:],cmap=cm.coolwarm,interpolation='bilinear')
    cbar = colorbar(extend = 'both', cmap= cm.coolwarm)
    ticks = np.arange(0,35,5)
    ticks_Text = ["{}°".format(deg) for deg in ticks]
    cbar.set_ticks(ticks)
    cbar.set_ticklabels(ticks_Text)
    clim(0,30)
    xlabel('b(x)')
    ylabel('a (z)')
    xTicks_N= np.arange(0,Nx+1,3)
    yTicks_N= np.arange(0,Nz+1,3)
    xTicks= [coords(i,r,0)[0] for i in xTicks_N]
    yTicks= [coords(0,r,i)[1] for i in yTicks_N]
    xTicks_Text = ["{0:.2f}".format(tick) for tick in xTicks]
    yTicks_Text = ["{0:.2f}".format(tick) for tick in yTicks]
    xticks(xTicks_N,xTicks_Text, rotation='vertical')
    yticks(yTicks_N,yTicks_Text)
    margins(0.2)
    subplots_adjust(bottom=0.15)
    
def imshowbienyz(u,r):
    imshow(u.T[Nx::-1,:],cmap=cm.coolwarm,interpolation='bilinear')
    cbar = colorbar(extend = 'both', cmap= cm.coolwarm)
    ticks = np.arange(0,35,5)
    ticks_Text = ["{}°".format(deg) for deg in ticks]
    cbar.set_ticks(ticks)
    cbar.set_ticklabels(ticks_Text)
    clim(0,30)
    xlabel('c(y)')
    ylabel('a(z)')
    xTicks_N= np.arange(0,Ny+1,3)
    yTicks_N= np.arange(0,Nz+1,3)
    xTicks= [coords(r,i,0)[0] for i in xTicks_N]
    yTicks= [coords(r,0,i)[1] for i in yTicks_N]
    xTicks_Text = ["{0:.2f}".format(tick) for tick in xTicks]
    yTicks_Text = ["{0:.2f}".format(tick) for tick in yTicks]
    xticks(xTicks_N,xTicks_Text, rotation='vertical')
    yticks(yTicks_N,yTicks_Text)
    margins(0.2)
    subplots_adjust(bottom=0.15)
    
u_k = np.zeros((Nx+1, Ny+1, Nz+1), dtype=np.double)
u_kml = np.zeros((Nx+1, Ny+1, Nz+1), dtype=np.double)

#Condicion de borde inicial
u_k[:,:,:] = 20. # grado inicial en todas partes

# Parametros (fisicos del problema (hierro))
dt = 0.01 #s
K = 79.5 # m2/s
c = 450.
ρ = 7800. # kg/m3
α = K * dt / (c * ρ * dx**2)

#informar cosas interesantes
print(f"dt = {dt}")
print(f"dx = {dx}")
print(f"K = {K}")
print(f"c = {c}")
print(f"ρ = {ρ}")
print(f"α = {α}")

#Loop tiempo
minuto = 60.
hora = 3600.
dia = 24.5 * 3600.

dt = 1.*minuto
dnext_t = 0.5 * hora

next_t = 0
framenum = 0

T = 1.*dia
Days = 1*T #cuantos dias quiero simular

# Vectores para acumular la temperatura en puntos interesantes
s1 = np.zeros(np.int32(Days/dt))
s2 = np.zeros(np.int32(Days/dt))
s3 = np.zeros(np.int32(Days/dt))
s4 = np.zeros(np.int32(Days/dt))
s5 = np.zeros(np.int32(Days/dt))
s6 = np.zeros(np.int32(Days/dt))
s7 = np.zeros(np.int32(Days/dt))
s8 = np.zeros(np.int32(Days/dt))
s9 = np.zeros(np.int32(Days/dt))
s10 = np.zeros(np.int32(Days/dt))
s11 = np.zeros(np.int32(Days/dt))
s12 = np.zeros(np.int32(Days/dt))
s13 = np.zeros(np.int32(Days/dt))
s14 = np.zeros(np.int32(Days/dt))
s15 = np.zeros(np.int32(Days/dt))

def truncate(n,decimales=0):
    multiplier= 10**decimales
    return int(n*multiplier)/multiplier

#Loop de tiempo
for k in range(np.int32(Days/dt)):
    t = dt*(k+1)
    dias = truncate(t/dia, 0)
    horas = truncate((t-dias*dia)/hora, 0)
    minutos = truncate((t-dias*dia-horas*hora)/minuto, 0)
    titulo = "k = {0:05.0f} ".format(k) + " t = {0:02.0f}d {1:02.0f}h {2:02.0f}m".format(dias, horas, minutos)
    print(titulo)
    
    #CB esenciales, se repite en cada iteracion
    u_ambiente = 20. + 10.*np.sin((2*np.pi/T)*t)

    u_k[-1 , : , : ] = u_k[-2 , : , : ]-0*dx   #cara frente yz
    u_k[ 0 , : , : ] = u_k[ -2 , : , : ]-0*dx   #cara atras yz
    u_k[ : ,-1 , : ] = u_k[ : ,-2 , : ]-0*dx   #cara derecha xz
    u_k[ : , 0 , : ] = u_k[ : ,-2 , : ]-0*dx   #cara izquierda xz
    u_k[ : , : , 0 ] = u_k[ : , : ,-2 ]-0*dx   #cara inf xy
    u_k[ : , : ,-1 ] = u_ambiente              #cara sup xy


    #Loop en el espacio i = 1......... n-1
    for i in range (1,Nx):
        for j in range (1,Ny):
            for s in range (1,Nz):

                # Algoritmo de diferencias finitas para 2-D para difusion

                # Laplaciano
                nabla_u_k = (u_k[i-1,j,s] + u_k[i+1,j,s] + u_k[i,j-1,s] + u_k[i,j+1,s] + u_k[i,j,s-1] + u_k[i,j,s+1] - 6 * u_k[i,j,s])

                #Fordwar Euler
                u_kml[i,j,s] = u_k[i,j,s] + α*nabla_u_k + Calor_de_hidratacion(t)*dt/(c*ρ)*1000.

    #Avanzar la solucion a k+1
    u_k = u_kml
#CB esenciales, se repite en cada iteracion
    u_ambiente = 20. + 10.*np.sin((2*np.pi/T)*t)

    u_k[-1 , : , : ] = u_k[-2 , : , : ]-0*dx   #cara frente yz
    u_k[ 0 , : , : ] = u_k[-2 , : , : ]-0*dx   #cara atras yz
    u_k[ : ,-1 , : ] = u_k[ : ,-2 , : ]-0*dx   #cara derecha xz
    u_k[ : , 0 , : ] = u_k[ : ,-2 , : ]-0*dx   #cara izquierda xz
    u_k[ : , : , 0 ] = u_k[ : , : ,-2 ]-0*dx   #cara inf xy
    u_k[ : , : ,-1 ] = u_ambiente              #cara sup xy
    
    
    #Escribiendo Puntos Interesantes
    s1[k]  = u_k[int(Nx/2),int(Ny*765/1040),int(Nz/2)]   #1
    s2[k]  = u_k[int(Nx/2),int(Ny/2),int(Nz/2)]          #2
    s3[k]  = u_k[int(Nx*510/540),int(Ny/2),int(Nz/2)]    #3
    s4[k] = u_k[int(Nx/2),int(Ny/2),int(Nz*470/500)]    #4
    s5[k]  = u_k[int(Nx/2),int(Ny*30/1040),int(Nz/2)]    #5
    s6[k]  = u_k[int(Nx*30/540),int(Ny/2),int(Nz/2)]     #6
    s7[k]  = u_k[int(Nx/2),int(Ny/2),int(Nz*360/500)]    #7
    s8[k]  = u_k[int(Nx/2),int(Ny/2),int(Nz*140/500)]    #8
    s9[k]  = u_k[int(Nx*150/540),int(Ny/2),int(Nz/2)]    #9
    s10[k] = u_k[int(Nx/2),int(Ny*1010/1040),int(Nz/2)]  #10
    s11[k] = u_k[int(Nx/2),int(Ny/2),int(Nz*30/500)]     #11
    s12[k]  = u_k[int(Nx/2),int(Ny*275/1040),int(Nz/2)]   #12
    s13[k] = u_k[int(Nx/2),int(Ny/2),int(Nz)]            #13
    s14[k]  = u_k[int(Nx*390/540),int(Ny/2),int(Nz/2)]    #14
    s15[k] = u_k[int(Nx/2),int(Ny),int(Nz/2)]            #15
    
    #grafico en d_next
    if t> next_t:
        plt.figure(1)
        imshowbienxy(u_k[:,:,int(Nz/2)],int(Nz/2))
        plt.title(titulo)
        plt.savefig("fig/caso_xy_{0:04.0f}.png".format(framenum))
        framenum+=1
        next_t+= dnext_t
        plt.close(1)
        plt.figure(2)
        imshowbienxz(u_k[:,int(Ny/2),:],int(Ny/2))
        plt.title(titulo)
        plt.savefig("fig/caso_xz_{0:04.0f}.png".format(framenum))
        framenum+=1
        next_t+= dnext_t
        plt.close(2)
        plt.figure(3)
        imshowbienyz(u_k[int(Nx/2),:,:],int(Nx/2))
        plt.title(titulo)
        plt.savefig("fig/caso_yz_{0:04.0f}.png".format(framenum))
        framenum+=1
        next_t+= dnext_t
        plt.close(3)
        
#Ploteo puntos
plt.figure(4)

plt.plot(range(np.int32(Days / dt)), s1, label='Sensor 1')
plt.plot(range(np.int32(Days / dt)), s2, label='Sensor 2')
plt.plot(range(np.int32(Days / dt)), s3, label='Sensor 3')
plt.plot(range(np.int32(Days / dt)), s4, label='Sensor 4')
plt.plot(range(np.int32(Days / dt)), s5, label='Sensor 5')
plt.plot(range(np.int32(Days / dt)), s6, label='Sensor 6')
plt.plot(range(np.int32(Days / dt)), s7, label='Sensor 7')
plt.plot(range(np.int32(Days / dt)), s8, label='Sensor 8')
plt.plot(range(np.int32(Days / dt)), s9, label='Sensor 9')
plt.plot(range(np.int32(Days / dt)), s10, label='Sensor 10')
plt.plot(range(np.int32(Days / dt)), s11, label='Sensor 11')
plt.plot(range(np.int32(Days / dt)), s12, label='Sensor 12')
plt.plot(range(np.int32(Days / dt)), s13, label='Sensor 13')
plt.plot(range(np.int32(Days / dt)), s14, label='Sensor 14')
plt.plot(range(np.int32(Days / dt)), s15, label='Sensor 15')
plt.title("Evolucion de temperatura")
plt.legend()
plt.savefig("EvolucionT_caso_1.png")
plt.show()
