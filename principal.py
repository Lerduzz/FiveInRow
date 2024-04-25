from PyQt5 import QtWidgets
from ventana import Ui_VentanaJuego
import sys, random, qdarkstyle

class VentanaJuego(QtWidgets.QMainWindow):
    def __init__(self):
        super(VentanaJuego, self).__init__()
        self.ui = Ui_VentanaJuego() 
        self.ui.setupUi(self)

        self.juegoIniciado = False
        self.numeroJugadores = 2
        self.jugadorActual = 0

        self.simbolos = ['X', 'O', 'Z', 'P']

        self.botones = [
            [self.ui.b00, self.ui.b01, self.ui.b02, self.ui.b03, self.ui.b04, self.ui.b05, self.ui.b06, self.ui.b07, self.ui.b08, self.ui.b09],
            [self.ui.b10, self.ui.b11, self.ui.b12, self.ui.b13, self.ui.b14, self.ui.b15, self.ui.b16, self.ui.b17, self.ui.b18, self.ui.b19],
            [self.ui.b20, self.ui.b21, self.ui.b22, self.ui.b23, self.ui.b24, self.ui.b25, self.ui.b26, self.ui.b27, self.ui.b28, self.ui.b29],
            [self.ui.b30, self.ui.b31, self.ui.b32, self.ui.b33, self.ui.b34, self.ui.b35, self.ui.b36, self.ui.b37, self.ui.b38, self.ui.b39],
            [self.ui.b40, self.ui.b41, self.ui.b42, self.ui.b43, self.ui.b44, self.ui.b45, self.ui.b46, self.ui.b47, self.ui.b48, self.ui.b49],
            [self.ui.b50, self.ui.b51, self.ui.b52, self.ui.b53, self.ui.b54, self.ui.b55, self.ui.b56, self.ui.b57, self.ui.b58, self.ui.b59],
            [self.ui.b60, self.ui.b61, self.ui.b62, self.ui.b63, self.ui.b64, self.ui.b65, self.ui.b66, self.ui.b67, self.ui.b68, self.ui.b69],
            [self.ui.b70, self.ui.b71, self.ui.b72, self.ui.b73, self.ui.b74, self.ui.b75, self.ui.b76, self.ui.b77, self.ui.b78, self.ui.b79],
            [self.ui.b80, self.ui.b81, self.ui.b82, self.ui.b83, self.ui.b84, self.ui.b85, self.ui.b86, self.ui.b87, self.ui.b88, self.ui.b89],
            [self.ui.b90, self.ui.b91, self.ui.b92, self.ui.b93, self.ui.b94, self.ui.b95, self.ui.b96, self.ui.b97, self.ui.b98, self.ui.b99]
        ]

        self.funciones = [
            [self.clicBoton00, self.clicBoton01, self.clicBoton02, self.clicBoton03, self.clicBoton04, self.clicBoton05, self.clicBoton06, self.clicBoton07, self.clicBoton08, self.clicBoton09],
            [self.clicBoton10, self.clicBoton11, self.clicBoton12, self.clicBoton13, self.clicBoton14, self.clicBoton15, self.clicBoton16, self.clicBoton17, self.clicBoton18, self.clicBoton19],
            [self.clicBoton20, self.clicBoton21, self.clicBoton22, self.clicBoton23, self.clicBoton24, self.clicBoton25, self.clicBoton26, self.clicBoton27, self.clicBoton28, self.clicBoton29],
            [self.clicBoton30, self.clicBoton31, self.clicBoton32, self.clicBoton33, self.clicBoton34, self.clicBoton35, self.clicBoton36, self.clicBoton37, self.clicBoton38, self.clicBoton39],
            [self.clicBoton40, self.clicBoton41, self.clicBoton42, self.clicBoton43, self.clicBoton44, self.clicBoton45, self.clicBoton46, self.clicBoton47, self.clicBoton48, self.clicBoton49],
            [self.clicBoton50, self.clicBoton51, self.clicBoton52, self.clicBoton53, self.clicBoton54, self.clicBoton55, self.clicBoton56, self.clicBoton57, self.clicBoton58, self.clicBoton59],
            [self.clicBoton60, self.clicBoton61, self.clicBoton62, self.clicBoton63, self.clicBoton64, self.clicBoton65, self.clicBoton66, self.clicBoton67, self.clicBoton68, self.clicBoton69],
            [self.clicBoton70, self.clicBoton71, self.clicBoton72, self.clicBoton73, self.clicBoton74, self.clicBoton75, self.clicBoton76, self.clicBoton77, self.clicBoton78, self.clicBoton79],
            [self.clicBoton80, self.clicBoton81, self.clicBoton82, self.clicBoton83, self.clicBoton84, self.clicBoton85, self.clicBoton86, self.clicBoton87, self.clicBoton88, self.clicBoton89],
            [self.clicBoton90, self.clicBoton91, self.clicBoton92, self.clicBoton93, self.clicBoton94, self.clicBoton95, self.clicBoton96, self.clicBoton97, self.clicBoton98, self.clicBoton99]
        ]

        for i in range(10):
            for j in range(10):
                self.botones[i][j].clicked.connect(self.funciones[i][j])
                self.botones[i][j].setEnabled(False)

        self.ui.accionIniciarPartida.triggered.connect(self.accionIniciarPartida)
        self.ui.accionDosJugadores.triggered.connect(self.seleccionarDosJugadores)
        self.ui.accionTresJugadores.triggered.connect(self.seleccionarTresJugadores)
        self.ui.accionCuatroJugadores.triggered.connect(self.seleccionarCuatroJugadores)
        self.ui.accionSalir.triggered.connect(self.accionSalir)
        self.ui.accionInformacion.triggered.connect(self.accionInformacion)
        self.ui.accionCreditos.triggered.connect(self.accionCreditos)

    def accionSalir(self):
        sys.exit(0)

    def accionIniciarPartida(self):
        self.jugadorActual = 0
        self.setWindowTitle('FiveRow por Lerduzz | Turno del jugador # ' + str(self.jugadorActual + 1) + ' (' + self.simbolos[self.jugadorActual] + ').')
        for i in range(10):
            for j in range(10):
                self.botones[i][j].setText('')
                self.botones[i][j].setStyleSheet('')
                self.botones[i][j].setEnabled(True)
        QtWidgets.QMessageBox.warning(
            self,
            'Partida iniciada',
            '¡Es hora de JUGAR!',
        )
    
    def accionInformacion(self):
        QtWidgets.QMessageBox.information(
            self,
            'Información',
            'Este juego consiste en ir marcando las casillas hasta lograr hacer una fila de cinco casillas consecutivas. Puede ser de manera horizontal, vertical o diagonal.\n\nPueden jugar de dos a cuatro jugadores en una misma computadora.\nPara comenzar has clic en el menu (Juego/Iniciar partida).',
        )

    def accionCreditos(self):
        QtWidgets.QMessageBox.information(
            self,
            'Creditos',
            'Desarrollado por Lerduzz\nhttps://youtube.com/@lerduzz\n\nDesarrollado con Python 3.8 + PyQt5.',
        )

    def seleccionarDosJugadores(self):
        self.ui.accionDosJugadores.setEnabled(False)
        self.ui.accionTresJugadores.setEnabled(True)
        self.ui.accionCuatroJugadores.setEnabled(True)
        self.ui.accionDosJugadores.setChecked(True)
        self.ui.accionTresJugadores.setChecked(False)
        self.ui.accionCuatroJugadores.setChecked(False)
        self.numeroJugadores = 2
        for i in range(10):
            for j in range(10):
                self.botones[i][j].setEnabled(False)
        self.setWindowTitle('FiveRow por Lerduzz | ¡Juego no iniciado!')

    def seleccionarTresJugadores(self):
        self.ui.accionDosJugadores.setEnabled(True)
        self.ui.accionTresJugadores.setEnabled(False)
        self.ui.accionCuatroJugadores.setEnabled(True)
        self.ui.accionDosJugadores.setChecked(False)
        self.ui.accionTresJugadores.setChecked(True)
        self.ui.accionCuatroJugadores.setChecked(False)
        self.numeroJugadores = 3
        for i in range(10):
            for j in range(10):
                self.botones[i][j].setEnabled(False)
        self.setWindowTitle('FiveRow por Lerduzz | ¡Juego no iniciado!')

    def seleccionarCuatroJugadores(self):
        self.ui.accionDosJugadores.setEnabled(True)
        self.ui.accionTresJugadores.setEnabled(True)
        self.ui.accionCuatroJugadores.setEnabled(False)
        self.ui.accionDosJugadores.setChecked(False)
        self.ui.accionTresJugadores.setChecked(False)
        self.ui.accionCuatroJugadores.setChecked(True)
        self.numeroJugadores = 4
        for i in range(10):
            for j in range(10):
                self.botones[i][j].setEnabled(False)
        self.setWindowTitle('FiveRow por Lerduzz | ¡Juego no iniciado!')

    def clicBoton00(self):
        self.procesarClic(0, 0)

    def clicBoton01(self):
        self.procesarClic(0, 1)

    def clicBoton02(self):
        self.procesarClic(0, 2)

    def clicBoton03(self):
        self.procesarClic(0, 3)

    def clicBoton04(self):
        self.procesarClic(0, 4)

    def clicBoton05(self):
        self.procesarClic(0, 5)

    def clicBoton06(self):
        self.procesarClic(0, 6)

    def clicBoton07(self):
        self.procesarClic(0, 7)

    def clicBoton08(self):
        self.procesarClic(0, 8)

    def clicBoton09(self):
        self.procesarClic(0, 9)

    def clicBoton10(self):
        self.procesarClic(1, 0)

    def clicBoton11(self):
        self.procesarClic(1, 1)

    def clicBoton12(self):
        self.procesarClic(1, 2)

    def clicBoton13(self):
        self.procesarClic(1, 3)

    def clicBoton14(self):
        self.procesarClic(1, 4)

    def clicBoton15(self):
        self.procesarClic(1, 5)

    def clicBoton16(self):
        self.procesarClic(1, 6)

    def clicBoton17(self):
        self.procesarClic(1, 7)

    def clicBoton18(self):
        self.procesarClic(1, 8)

    def clicBoton19(self):
        self.procesarClic(1, 9)

    def clicBoton20(self):
        self.procesarClic(2, 0)

    def clicBoton21(self):
        self.procesarClic(2, 1)

    def clicBoton22(self):
        self.procesarClic(2, 2)

    def clicBoton23(self):
        self.procesarClic(2, 3)

    def clicBoton24(self):
        self.procesarClic(2, 4)

    def clicBoton25(self):
        self.procesarClic(2, 5)

    def clicBoton26(self):
        self.procesarClic(2, 6)

    def clicBoton27(self):
        self.procesarClic(2, 7)

    def clicBoton28(self):
        self.procesarClic(2, 8)

    def clicBoton29(self):
        self.procesarClic(2, 9)

    def clicBoton30(self):
        self.procesarClic(3, 0)
    
    def clicBoton31(self):
        self.procesarClic(3, 1)
    
    def clicBoton32(self):
        self.procesarClic(3, 2)
    
    def clicBoton33(self):
        self.procesarClic(3, 3)
    
    def clicBoton34(self):
        self.procesarClic(3, 4)
    
    def clicBoton35(self):
        self.procesarClic(3, 5)
    
    def clicBoton36(self):
        self.procesarClic(3, 6)
    
    def clicBoton37(self):
        self.procesarClic(3, 7)
    
    def clicBoton38(self):
        self.procesarClic(3, 8)
    
    def clicBoton39(self):
        self.procesarClic(3, 9)
    
    def clicBoton40(self):
        self.procesarClic(4, 0)

    def clicBoton41(self):
        self.procesarClic(4, 1)
    
    def clicBoton42(self):
        self.procesarClic(4, 2)
    
    def clicBoton43(self):
        self.procesarClic(4, 3)
    
    def clicBoton44(self):
        self.procesarClic(4, 4)
    
    def clicBoton45(self):
        self.procesarClic(4, 5)
    
    def clicBoton46(self):
        self.procesarClic(4, 6)
    
    def clicBoton47(self):
        self.procesarClic(4, 7)
    
    def clicBoton48(self):
        self.procesarClic(4, 8)
    
    def clicBoton49(self):
        self.procesarClic(4, 9)
    
    def clicBoton50(self):
        self.procesarClic(5, 0)

    def clicBoton51(self):
        self.procesarClic(5, 1)
    
    def clicBoton52(self):
        self.procesarClic(5, 2)
    
    def clicBoton53(self):
        self.procesarClic(5, 3)
    
    def clicBoton54(self):
        self.procesarClic(5, 4)
    
    def clicBoton55(self):
        self.procesarClic(5, 5)
    
    def clicBoton56(self):
        self.procesarClic(5, 6)
    
    def clicBoton57(self):
        self.procesarClic(5, 7)
    
    def clicBoton58(self):
        self.procesarClic(5, 8)
    
    def clicBoton59(self):
        self.procesarClic(5, 9)

    def clicBoton60(self):
        self.procesarClic(6, 0)

    def clicBoton61(self):
        self.procesarClic(6, 1)

    def clicBoton62(self):
        self.procesarClic(6, 2)

    def clicBoton63(self):
        self.procesarClic(6, 3)

    def clicBoton64(self):
        self.procesarClic(6, 4)

    def clicBoton65(self):
        self.procesarClic(6, 5)

    def clicBoton66(self):
        self.procesarClic(6, 6)

    def clicBoton67(self):
        self.procesarClic(6, 7)

    def clicBoton68(self):
        self.procesarClic(6, 8)

    def clicBoton69(self):
        self.procesarClic(6, 9)

    def clicBoton70(self):
        self.procesarClic(7, 0)

    def clicBoton71(self):
        self.procesarClic(7, 1)

    def clicBoton72(self):
        self.procesarClic(7, 2)

    def clicBoton73(self):
        self.procesarClic(7, 3)

    def clicBoton74(self):
        self.procesarClic(7, 4)

    def clicBoton75(self):
        self.procesarClic(7, 5)

    def clicBoton76(self):
        self.procesarClic(7, 6)

    def clicBoton77(self):
        self.procesarClic(7, 7)

    def clicBoton78(self):
        self.procesarClic(7, 8)

    def clicBoton79(self):
        self.procesarClic(7, 9)

    def clicBoton80(self):
        self.procesarClic(8, 0)

    def clicBoton81(self):
        self.procesarClic(8, 1)

    def clicBoton82(self):
        self.procesarClic(8, 2)

    def clicBoton83(self):
        self.procesarClic(8, 3)

    def clicBoton84(self):
        self.procesarClic(8, 4)

    def clicBoton85(self):
        self.procesarClic(8, 5)

    def clicBoton86(self):
        self.procesarClic(8, 6)

    def clicBoton87(self):
        self.procesarClic(8, 7)

    def clicBoton88(self):
        self.procesarClic(8, 8)

    def clicBoton89(self):
        self.procesarClic(8, 9)

    def clicBoton90(self):
        self.procesarClic(9, 0)

    def clicBoton91(self):
        self.procesarClic(9, 1)

    def clicBoton92(self):
        self.procesarClic(9, 2)

    def clicBoton93(self):
        self.procesarClic(9, 3)

    def clicBoton94(self):
        self.procesarClic(9, 4)

    def clicBoton95(self):
        self.procesarClic(9, 5)

    def clicBoton96(self):
        self.procesarClic(9, 6)

    def clicBoton97(self):
        self.procesarClic(9, 7)

    def clicBoton98(self):
        self.procesarClic(9, 8)

    def clicBoton99(self):
        self.procesarClic(9, 9)
    
    def procesarClic(self, i, j):
        self.botones[i][j].setText(self.simbolos[self.jugadorActual])
        self.botones[i][j].setEnabled(False)
        if self.verificarVictoria():
            for i in range(10):
                for j in range(10):
                    self.botones[i][j].setEnabled(False)
            self.setWindowTitle('FiveRow por Lerduzz | ¡Juego no iniciado!')
            QtWidgets.QMessageBox.information(
                self,
                'Fin de la partida',
                'Ha ganado el jugador # ' + str(self.jugadorActual + 1) + ' (' + self.simbolos[self.jugadorActual] + ').',
            )
        else:
            self.jugadorActual += 1
            if self.jugadorActual == self.numeroJugadores:
                self.jugadorActual = 0
            self.setWindowTitle('FiveRow por Lerduzz | Turno del jugador # ' + str(self.jugadorActual + 1) + ' (' + self.simbolos[self.jugadorActual] + ').')

    def verificarVictoria(self):
        if self.verificarHorizontal():
            return True
        if self.verificarVertical():
            return True
        if self.verificarDiagonalAscendente():
            return True
        if self.verificarDiagonalDescendente():
            return True
        return False

    def verificarHorizontal(self):
        ganadores = [None, None, None, None, None]
        actual = ''
        contador = 0
        for i in range(10):
            actual = ''
            contador = 0
            for j in range(10):
                simbolo = self.botones[i][j].text()
                if simbolo != '':
                    if actual != simbolo:
                        actual = simbolo
                        contador = 1
                        ganadores[0] = self.botones[i][j]
                    else:
                        ganadores[contador] = self.botones[i][j]
                        contador += 1
                        if contador == 5:
                            break
                else:
                    actual = ''
                    contador = 0
            if contador == 5:
                break
        if contador == 5:
            for ganador in ganadores:
                ganador.setStyleSheet('color: green;')
            return True
        return False

    def verificarVertical(self):
        ganadores = [None, None, None, None, None]
        actual = ''
        contador = 0
        for i in range(10):
            actual = ''
            contador = 0
            for j in range(10):
                simbolo = self.botones[j][i].text()
                if simbolo != '':
                    if actual != simbolo:
                        actual = simbolo
                        contador = 1
                        ganadores[0] = self.botones[j][i]
                    else:
                        ganadores[contador] = self.botones[j][i]
                        contador += 1
                        if contador == 5:
                            break
                else:
                    actual = ''
                    contador = 0
            if contador == 5:
                break
        if contador == 5:
            for ganador in ganadores:
                ganador.setStyleSheet('color: green;')
            return True
        return False

    def verificarDiagonalAscendente(self):
        ganadores = [None, None, None, None, None]
        actual = ''
        contador = 0
        sI = 4
        sJ = 0
        i = sI
        j = sJ
        diagonales = 0
        while diagonales < 12:
            simbolo = self.botones[i][j].text()
            if simbolo != '':
                if actual != simbolo:
                    actual = simbolo
                    contador = 1
                    ganadores[0] = self.botones[i][j]
                else:
                    ganadores[contador] = self.botones[i][j]
                    contador += 1
                    if contador == 5:
                        break
            else:
                actual = ''
                contador = 0
            i -= 1
            j += 1
            if i < 0 or j > 9:
                if sI < 9:
                    sI += 1
                else:
                    sJ += 1
                    if sJ > 5:
                        break
                diagonales += 1
                actual = ''
                contador = 0
                i = sI
                j = sJ
        if contador == 5:
            for ganador in ganadores:
                ganador.setStyleSheet('color: green;')
            return True
        return False

    def verificarDiagonalDescendente(self):
        ganadores = [None, None, None, None, None]
        actual = ''
        contador = 0
        sI = 5
        sJ = 0
        i = sI
        j = sJ
        diagonales = 0
        while diagonales < 12:
            simbolo = self.botones[i][j].text()
            if simbolo != '':
                if actual != simbolo:
                    actual = simbolo
                    contador = 1
                    ganadores[0] = self.botones[i][j]
                else:
                    ganadores[contador] = self.botones[i][j]
                    contador += 1
                    if contador == 5:
                        break
            else:
                actual = ''
                contador = 0
            i += 1
            j += 1
            if i > 9 or j > 9:
                if sI > 0:
                    sI -= 1
                else:
                    sJ += 1
                    if sJ > 5:
                        break
                diagonales += 1
                actual = ''
                contador = 0
                i = sI
                j = sJ
        if contador == 5:
            for ganador in ganadores:
                ganador.setStyleSheet('color: green;')
            return True
        return False

app = QtWidgets.QApplication([])
app.setStyleSheet(qdarkstyle.load_stylesheet(qt_api='pyqt5'))
application = VentanaJuego()
application.show()
sys.exit(app.exec())