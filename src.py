import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
t= np.linspace(0,3,num=(12*1024))
N=5 #number of notes
t1=[0,0.7,1.3,1.9,2.4]
T=[0.5,0.5,0.3,0.3,0.1]
#left=abefc from the 3rd octave
#right=dgfac from the 4th octave
F=[130.81,196,174.61,220,196] #freq for the left hand notes
f=[349.23,440,293.66,261.63,329.63] # freq for the right hand notes
x=0
for ti,Ti,fi,Fi in zip(t1,T,f,F):
    x1 = np.where(np.logical_and(t>=ti,t<=(Ti+ti)),np.sin(2*np.pi*fi*t),0)
    x1_new = np.reshape(x1,np.shape(t))
    x2 = np.where(np.logical_and(t>=ti,t<=(Ti+ti)),np.sin(2*np.pi*Fi*t),0)
    x2_new=np.reshape(x2,np.shape(t))
    x+= x1_new + x2_new
plt.plot(t,x)
sd.play(x,3*1024)