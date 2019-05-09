from Tkinter import *
from threading import *
from figura import *
from circulo import *
from cuadrado import *
from rectangulo import *
from triangulo import *
from puntos import *

class interfacefigura():

    def __init__(self):
        self.root = Tk()
        

        self.cadena = StringVar(self.root)
        self.display = Label(self.root, textvariable=self.cadena, font=("Helvetica", 30))
        self.display.pack(padx=10,pady=10)
        
        self.buttoncirculo = Button(self.root, text="circulo", command=self.codfigura)
        self.buttoncirculo.pack()
       
        self.buttoncuadrado = Button(self.root, text="cuadrado", command=self.codfigura2)
        self.buttoncuadrado.pack()
        

        self.buttonrectangulo = Button(self.root, text="rectangulo", command=self.codfigura4)
        self.buttonrectangulo.pack()
        

        self.buttontriangulo = Button(self.root, text="triangulo", command=self.codfigura3)
        self.buttontriangulo.pack()
        

        self.inf = StringVar(self.root)
        
        self.entry1 = Entry(self.root, textvariable=self.inf)
        self.entry1.pack()
        self.inf2 = StringVar(self.root)
        self.label1 = Label(self.root, textvariable=self.inf2)
        self.label1.pack()

        self.inf3 = StringVar(self.root)
        self.label2 = Label(self.root, textvariable=self.inf3)
        self.label2.pack()

        self.root.mainloop()

        

    def codfigura(self):
        self.p = punto()
        self.q = punto()
        valores = [int (p) for p in self.inf.get().split()]
        self.p.x=valores[0]
        self.p.y=valores[1]
        self.q.x=valores[2]
        self.q.y=valores[3]
        self.f = circulo()
        self.f.setPuntos(self.p,self.q)
        self.f.calcularArea()
        self.f.calperimetro()
        
        self.inf2.set("el area es " + str (self.f.area))
        self.inf3.set("el perimetro es " + str (self.f.perimetro))
        
    def codfigura2(self):
        self.p = punto()
        self.q = punto()
        valores = [int (p) for p in self.inf.get().split()]
        self.p.x=valores[0]
        self.p.y=valores[1]
        self.q.x=valores[2]
        self.q.y=valores[3]
        self.f = cuadrado()
        self.f.setPuntos(self.p,self.q)
        self.f.calcularArea()
        self.f.calperimetro()
        
        self.inf2.set("el area es " + str (self.f.area))
        self.inf3.set("el perimetro es " + str (self.f.perimetro))
        
  
    def codfigura3(self):
        self.p = punto()
        self.q = punto()
        valores = [int (p) for p in self.inf.get().split()]
        self.p.x=valores[0]
        self.p.y=valores[1]
        self.q.x=valores[2]
        self.q.y=valores[3]
        self.f = triangulo()
        self.f.setPuntos(self.p,self.q)
        self.f.calcularArea()
        self.f.calperimetro()
        
        self.inf2.set("el area es " + str (self.f.area))
        self.inf3.set("el perimetro es " + str (self.f.perimetro))

    def codfigura4(self):
        self.p = punto()
        self.q = punto()
        valores = [int (p) for p in self.inf.get().split()]
        self.p.x=valores[0]
        self.p.y=valores[1]
        self.q.x=valores[2]
        self.q.y=valores[3]
        self.f = rectangulo()
        self.f.setPuntos(self.p,self.q)
        self.f.calcularArea()
        self.f.calperimetro()
        
        self.inf2.set("el area es " + str (self.f.area))
        self.inf3.set("el perimetro es " + str (self.f.perimetro))
        
            


x = interfacefigura()
