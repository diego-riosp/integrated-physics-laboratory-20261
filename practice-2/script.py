#Run in https://www.programiz.com/python-programming/online-compiler/
import numpy as np

class Lab:
  def __init__(self,gravity):
    self.g = gravity

  def x(self,t,v,phi,t0):
    return v*np.cos(phi)*(t-t0)

  def y(self,t,y0,v,phi,t0):
    return y0+v*np.sin(phi)*(t-t0)-0.5*self.g*(t-t0)**2

  def X(self,t,X0,Phi):
    return X0-0.25*self.g*np.sin(2*Phi)*t**2

  def Y(self,t,Y0,Phi):
    return Y0-0.5*self.g*np.sin(Phi)**2*t**2

  def tX0(self,v,y0,phi,Y0,Phi,t0):
    a=0.5*self.g*np.cos(Phi)**2
    b=-(v*np.sin(phi) + self.g*t0*np.sin(Phi)**2)
    c=Y0-y0-0.5*self.g*t0**2*np.sin(Phi)**2
    t = t0 + (-b + np.sqrt(b**2-4*a*c)) / (2*a)
    X0 = (v*np.cos(phi)+0.5*self.g*t0*np.sin(2*Phi))*(t-t0) \
    + 0.25*self.g*np.sin(2*Phi)*(t-t0)**2 \
    + 0.25*self.g*np.sin(2*Phi)*t0**2
    return t, X0

if __name__ == "__main__":

  v = float(input("Ingrese la velocidad inicial v (m/s): "))
  phi = np.deg2rad(float(input("Ingrese el ángulo phi (grados): ")))
  y0 = float(input("Ingrese la altura inicial y0 (m): "))
  L = float(input("Ingrese la longitud L (m): "))
  Y0 = float(input("Ingrese la altura Y0 (m): "))

  resp = input("¿El carro se dejó caer antes que la esfera? (s/n): ").strip().lower()

  if resp == "s":
      t0 = float(input("Ingrese el tiempo t0 (s): "))
  else:
      t0 = 0

  Phi = np.arcsin(Y0/L)

  lb = Lab(9.76)

  t, X0 = lb.tX0(v, y0, phi, Y0, Phi, t0)
  x = lb.x(t, v, phi, t0)
  y = lb.y(t, y0, v, phi, t0)
  X = lb.X(t, X0, Phi)
  Y = lb.Y(t, Y0, Phi)

  print(f"\nDebe posicionar el carro a {X0:.2f} m")
  print(f"Se espera que los objetos interactúen pasados {t:.2f} s")
  print(f"Interactuarán en el punto de coordenadas de la esfera (x,y)= ({x:.2f}, {y:.2f})")
  print(f"Interactuarán en el punto de coordenadas del carro (X,Y)= ({X:.2f}, {Y:.2f})")
