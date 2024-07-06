from PyQt5 import uic, QtWidgets
from service import ServiceEjercicio1

class Ejercicio1:
    
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.prom = uic.loadUi("view/frm_calc.ui")
        self.prom.calcular.clicked.connect(self.primera)
        self.prom.show()
        app.exec()
        
    def primera(self):
        comprob = False
        txt = ""
        
        try:
            nota1 = float(self.prom.n1.text())
            nota2 = float(self.prom.n2.text())
            nota3 = float(self.prom.n3.text())
            nota4 = float(self.prom.n4.text())
            pr = ServiceEjercicio1.PromNota(nota1,nota2,nota3,nota4)
            comprob = True
            txt = "Tu promedio es: "
            
        except:
            txt = "¡Solo se aceptan valores numericos!"
        
        finally:
            
            if comprob == True:
                self.prom.resultado.setText(txt + str(round(pr, 2)))
            else:
                self.prom.resultado.setText(txt)
