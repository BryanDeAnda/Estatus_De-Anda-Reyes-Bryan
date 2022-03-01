# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interfaz.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import pickle
import threading
import time

class Peliculas:
    def __init__(self, nombre, genero, director):
        self.nombre = nombre
        self.genero = genero
        self.director = director
        print("\nSe a agregado una pelicula nueva con el nombre de: ", self.nombre, "\n")
        
    def __str__(self):
        return "{} {} {}".format(self.nombre, self.genero, self.director)
    
    
class ListaPeliculas:
    
    peliculas = []
    
    def __init__(self):
        listaDePeliculas = open("ficheroExterno", "ab+")
        listaDePeliculas.seek(0)
        
        try:
            self.peliculas=pickle.load(listaDePeliculas)
        except:
            print("El fichero esta vacio")
        finally:
            listaDePeliculas.close()
            del(listaDePeliculas)
    
    def AgregarPeliculas(self, p):
        self.peliculas.append(p)
        self.GuardarPeliculasExterno()
        
    def MostrarPeliculas(self):
        for p in self.peliculas:
            print(p)
        
    def GuardarPeliculasExterno(self):
        listaDePeliculas = open("FicheroExterno", "wb")
        pickle.dump(self.peliculas, listaDePeliculas)
        del(listaDePeliculas)
    
    def MostrarInfoFicheroExterno(self):
        print("\nLa información de las peliculas almacenadas es: \n")
        for p in self.peliculas:
            print("Nombre: ", p.nombre)
            print("Genero: ", p.genero)
            print("Director: ", p.director)
    
    def BuscarPeliculaEnElFichero(self, nom):
        for p in self.peliculas:
            if p.nombre == nom:
                print("\nPelicula encontrada: ")
                print("Nombre: ", p.nombre)
                print("Genero: ", p.genero)
                print("Director: ", p.director)
                break
                       
miLista = ListaPeliculas() 

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1014, 607)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(290, 40, 471, 41))
        self.label.setStyleSheet("font: 22pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(170, 120, 200, 50))
        self.label_2.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(110, 180, 271, 41))
        self.lineEdit.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(20, 180, 81, 41))
        self.label_3.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 240, 71, 41))
        self.label_4.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(Form)
        self.lineEdit_2.setGeometry(QtCore.QRect(110, 240, 271, 41))
        self.lineEdit_2.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit_3 = QtWidgets.QLineEdit(Form)
        self.lineEdit_3.setGeometry(QtCore.QRect(110, 300, 271, 41))
        self.lineEdit_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_3.setText("")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 300, 71, 41))
        self.label_5.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(130, 360, 141, 41))
        self.pushButton.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.agregar_pelicula)
        
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(100, 440, 221, 31))
        self.label_6.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 490, 81, 41))
        self.label_7.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.label_7.setObjectName("label_7")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(110, 490, 271, 41))
        self.lineEdit_4.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.lineEdit_4.setText("")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(130, 550, 141, 41))
        self.pushButton_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Buscar_Pelicula)

        
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(660, 110, 141, 41))
        self.label_8.setStyleSheet("font: 20pt \"MS Shell Dlg 2\";")
        self.label_8.setObjectName("label_8")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(450, 180, 541, 351))
        self.tableWidget.setStyleSheet("font: 12pt \"MS Shell Dlg 2\";")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(630, 550, 141, 41))
        self.pushButton_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.clicked.connect(self.mostrar_pelicula)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Almacenamiento de peliculas"))
        self.label_2.setText(_translate("Form", "Agregar"))
        self.label_3.setText(_translate("Form", "Nombre"))
        self.label_4.setText(_translate("Form", "Genero"))
        self.label_5.setText(_translate("Form", "Director"))
        self.pushButton.setText(_translate("Form", "Agregar"))
        self.label_6.setText(_translate("Form", "Buscar Pelicula"))
        self.label_7.setText(_translate("Form", "Nombre"))
        self.pushButton_2.setText(_translate("Form", "Buscar"))
        self.label_8.setText(_translate("Form", "Peliculas"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Nombre"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Genero"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Director"))
        self.pushButton_3.setText(_translate("Form", "Mostrar"))
    
    def agregar_pelicula(self):
        nombre = self.lineEdit.text()
        genero = self.lineEdit_2.text()
        director = self.lineEdit_3.text()
        
        peli = Peliculas(nombre, genero, director)
        miLista.AgregarPeliculas(peli)
        contador = 0
        lista = []
        for p in miLista.peliculas:
            lista1 = ()
            lista1 = (p.nombre, p.genero, p.director)
            lista.append(lista1)
        self.tableWidget.setRowCount(len(lista))
        for p in lista:
            self.tableWidget.setItem(contador, 0, QtWidgets.QTableWidgetItem(p[0]))
            self.tableWidget.setItem(contador, 1, QtWidgets.QTableWidgetItem(str(p[1])))
            self.tableWidget.setItem(contador, 2, QtWidgets.QTableWidgetItem(str(p[2])))
            contador += 1
            
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.setText(_translate("Dialog", ""))
        self.lineEdit_2.setText(_translate("Dialog", ""))
        self.lineEdit_3.setText(_translate("Dialog", ""))
        
    def mostrar_pelicula(self):
        contador = 0
        lista = []
        for p in miLista.peliculas:
            lista1 = ()
            lista1 = (p.nombre, p.genero, p.director)
            lista.append(lista1)
        self.tableWidget.setRowCount(len(lista))
        for p in lista:
            self.tableWidget.setItem(contador, 0, QtWidgets.QTableWidgetItem(p[0]))
            self.tableWidget.setItem(contador, 1, QtWidgets.QTableWidgetItem(str(p[1])))
            self.tableWidget.setItem(contador, 2, QtWidgets.QTableWidgetItem(str(p[2])))
            contador += 1
    
    def Buscar_Pelicula(self):
        nom = self.lineEdit_4.text()
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit_4.setText(_translate("Dialog", ""))
        contador = 0
        lista = []
        for p in miLista.peliculas:
            lista1 = ()
            lista1 = (p.nombre, p.genero, p.director)
            lista.append(lista1)
        self.tableWidget.setRowCount(1)
        for p in lista:
            if p[0] == nom:
                self.tableWidget.setItem(contador, 0, QtWidgets.QTableWidgetItem(p[0]))
                self.tableWidget.setItem(contador, 1, QtWidgets.QTableWidgetItem(str(p[1])))
                self.tableWidget.setItem(contador, 2, QtWidgets.QTableWidgetItem(str(p[2])))
                break
            

    def Guardar(self):
        '''Contar hasta cien'''
        while True:
            time.sleep(3)
            try:
                nombre = self.lineEdit.text()
                genero = self.lineEdit_2.text()
                director = self.lineEdit_3.text()
                archivo = open('nombre.txt', 'w')
                archivo2 = open('genero.txt', 'w')
                archivo3 = open('director.txt', 'w')
                archivo.write(nombre)
                archivo2.write(genero)
                archivo3.write(director)
            except Exception as e:
                print(e)
            finally:
                archivo.close()
                archivo2.close()
                archivo3.close()
                
    def Recuperar(self):
        archivo = open("nombre.txt", "r")
        nombre = archivo.read()
        archivo2 = open("genero.txt", "r")
        genero = archivo2.read()
        archivo3 = open("director.txt", "r")
        director = archivo3.read()
        _translate = QtCore.QCoreApplication.translate
        self.lineEdit.setText(_translate("Dialog", nombre))
        self.lineEdit_2.setText(_translate("Dialog", genero))
        self.lineEdit_3.setText(_translate("Dialog", director))
        archivo.close()
        archivo2.close()
        archivo3.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    ui.Recuperar()
    hilo1 = threading.Thread(target=ui.Guardar, daemon=True)
    hilo1.start()
    sys.exit(app.exec_()) 
          