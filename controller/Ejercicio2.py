from PyQt5 import uic, QtWidgets
from service import ServiceEjercicio2

class Ejercicio2:
    
    def __init__(self):
        app = QtWidgets.QApplication([])
        self.clc = uic.loadUi("view/frm_ope.ui")
        self.clc.calcular2.clicked.connect(self.segunda)
        self.clc.show()
        app.exec()
        
    def segunda(self):
        comprob = False
        
        try:
            nrt1 = float(self.clc.num1.text())
            nrt2 = float(self.clc.num2.text())
            funcionC1 = ServiceEjercicio2.fcForm1(nrt1, nrt2)
            funcionC2 = ServiceEjercicio2.fcForm2(nrt1, nrt2)
            comprob = True

        except:
            txt = "¡Solo se aceptan valores numericos!"
        
        finally:
            
            if comprob == True:
                self.clc.resultado1.setText(funcionC2)
                self.clc.resultado2.setText(str(funcionC1))
            else:
                self.clc.resultado1.setText(txt)
