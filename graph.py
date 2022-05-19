from PyQt6 import QtWidgets
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication

pg.setConfigOptions(antialias=True)  # anti-aliasing


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.graphWidget = pg.PlotWidget()  # create graph widget
        self.setCentralWidget(self.graphWidget)  # place it inside anothe widget

        hour = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12]
        temperature = [30, 32, 34, 32, 33, 31, 29, 32, 35, 45, 0]

        # plot data: x, y values
        self.graphWidget.plot(hour, temperature, pen=pg.mkPen(color=(255, 255, 255)))

        self.graphWidget.setBackground((38, 38, 38))  # change background


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec())
