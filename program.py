"""
@author: Budzyńska Justyna, Sidor Aleksandra 

"""
import sys
from PySide2 import QtCore
from PySide2 import *
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtWidgets import QHBoxLayout
import matplotlib
matplotlib.use('Qt5Agg')
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg 
from matplotlib.figure import Figure
import nibabel as nib



class ImageDisplay(FigureCanvasQTAgg):
    """Klasa obsługująca wyświetlanie obrazu za pomocą biblioteki
    wbudowanej matplotlib.

    Args:
        FigureCanvasQTAgg ([class 'Shiboken.ObjectType']): pole, w którym będzie 
        wyświetlany obraz
    """

    def __init__(self, width=4, height=4, dpi=100):
        """Konstruktor klasy ImageDisplay

        Args:
            width (int, optional): Określa szerokośc pola. Defaults to 4.
            height (int, optional): Określa wysokość pola. Defaults to 4.
            dpi (int, optional): Rozdzielczość. Defaults to 100.
        """

        fig = Figure(figsize=(width, height), dpi=dpi, facecolor = '#eae3e1')
        self.axes = fig.add_subplot(111)
        self.axes.set_aspect('auto') 
        self.canvas = FigureCanvasQTAgg(fig)
        self.mc = fig.canvas.mpl_connect('button_press_event', self.onclick)
        super().__init__(fig)

    def onclick(self, event):
        """Deklaracja metody obsługującej pobieranie współrzędnych
        kliknięcia myszy.

        Args:
            event ([class 'matplotlib.backend_bases.MouseEvent']): 
            Reprezentuje zdarzenie kliknięcia myszy.
        """
        pass


class MainWindow(QMainWindow):
    """Klasa główna programu odpowiadająca za wyświetlanie głównego
    okna i jego oprawę graficzną. 

    Args:
        QMainWindow ([class PySide2.QtGui.QMainWindow]): Reprezentuje
        główne okno programu.
    """

    def __init__(self):
        """Konstruktor klasy MainWindow
        """
        super().__init__()

        self.num = 0
        self.num2 = 0
        self.num3 = 0
        self.tmp3 = 0
        self.image = None
        self.counter = 0

        self.setWindowTitle("Rekonstrukcja multiplanarna obrazu 3D CT")
        button1 = QPushButton('Wybierz obraz')
        button1.setFixedSize(150,40)
        button1.clicked.connect(self.openImage)
        button1.setStyleSheet("background-color: #d7c0b6")

        
#########################################################
        prev1 = QPushButton()
        prev1.setFixedSize(80,30)
        prev1.setIcon(QPixmap('strzałka2.png'))
        prev1.setStyleSheet("background-color: #eae3e1")

        next1 = QPushButton()
        next1.setFixedSize(80,30)
        next1.setIcon(QPixmap('strzałka.png'))
        next1.setStyleSheet("background-color: #eae3e1")

##########################################################
        prev2 = QPushButton()
        prev2.setFixedSize(80,30)
        prev2.setIcon(QPixmap('strzałka2.png'))
        prev2.setStyleSheet("background-color: #eae3e1")

        next2 = QPushButton()
        next2.setFixedSize(80,30)
        next2.setIcon(QPixmap('strzałka.png'))
        next2.setStyleSheet("background-color: #eae3e1")
##########################################################
        prev3 = QPushButton()
        prev3.setFixedSize(80,30)
        prev3.setIcon(QPixmap('strzałka2.png'))
        prev3.setStyleSheet("background-color: #eae3e1")

        next3 = QPushButton()
        next3.setFixedSize(80,30)
        next3.setIcon(QPixmap('strzałka.png'))
        next3.setStyleSheet("background-color: #eae3e1")
##########################################################



        self.slider = QSlider(Qt.Horizontal)
        self.slider.setMinimum(0)

        self.slider2 = QSlider(Qt.Horizontal)
        self.slider2.setMinimum(0)

        self.slider3 = QSlider(Qt.Horizontal)
        self.slider3.setMinimum(0)
        
        self.center = QLabel()
        self.center.setFixedSize(90,30)

        self.center2 = QLabel()
        self.center2.setFixedSize(90,30)

        self.center3 = QLabel()
        self.center3.setFixedSize(90,30)

        self.figure1 = ImageDisplay()
        self.figure2 = ImageDisplay()
        self.figure3 = ImageDisplay()
    
        next1.clicked.connect(self.updateNext)
        prev1.clicked.connect(self.updatePrev)

        next2.clicked.connect(self.updateNext2)
        prev2.clicked.connect(self.updatePrev2)

        next3.clicked.connect(self.updateNext3)
        prev3.clicked.connect(self.updatePrev3)

        self.slider.valueChanged.connect(self.updateSlider)
        self.slider2.valueChanged.connect(self.updateSlider2)
        self.slider3.valueChanged.connect(self.updateSlider3)

        arrows1 = QHBoxLayout()
        arrows1.addWidget(self.slider)
        arrows1.addWidget(prev1, alignment=QtCore.Qt.AlignHCenter)
        arrows1.addWidget(next1, alignment=QtCore.Qt.AlignHCenter)
        arrows1.addWidget(self.center)


        layout2 = QVBoxLayout()
        layout2.addLayout(arrows1, stretch=1)
        layout2.addWidget(self.figure1)
        layout2.addWidget(button1)

        arrows2 = QHBoxLayout()
        arrows2.addWidget(self.slider2)
        arrows2.addWidget(prev2, alignment=QtCore.Qt.AlignCenter)
        arrows2.addWidget(next2, alignment=QtCore.Qt.AlignCenter)
        arrows2.addWidget(self.center2, alignment=QtCore.Qt.AlignRight)

        arrows3 = QHBoxLayout()
        arrows3.addWidget(self.slider3)
        arrows3.addWidget(prev3, alignment=QtCore.Qt.AlignHCenter)
        arrows3.addWidget(next3, alignment=QtCore.Qt.AlignHCenter)
        arrows3.addWidget(self.center3, alignment=QtCore.Qt.AlignRight)

        layout3 = QVBoxLayout()
        layout3.addLayout(arrows2, stretch=1)
        layout3.addWidget(self.figure2)
        layout3.addLayout(arrows3, stretch=1)
        layout3.addWidget(self.figure3)

        mainlayout =QHBoxLayout()
        mainlayout.addLayout(layout2, stretch=1)
        mainlayout.addLayout(layout3, stretch=1)

        widget = QWidget()
        widget.setLayout(mainlayout)
        self.setCentralWidget(widget)
        widget.setStyleSheet("background-color: #FEFEFE")
        self.showMaximized()
        

    def onclick1(self, event):
        """Metoda, która po kliknięciu myszką w przestrzeni pierwszego rzutu
        (po lewej stronie) pobiera współrzędne kliknięcia. 
        Wywołuje funkcję updateCoor1().

        Args:
            event (class 'matplotlib.backend_bases.MouseEvent'): 
            Reprezentuje zdarzenie kliknięcia myszy.
        """
        self.x1 = event.xdata
        self.y1 = event.ydata
 
        self.updateCoor1()
        

    def onclick2(self, event):
        """Metoda, która po kliknięciu myszką w przestrzeni drugiego rzutu 
        (u góry po prawej stronie) pobiera współrzędne kliknięcia. 
        Wywołuje funkcję updateCoor1().

        Args:
            event (class 'matplotlib.backend_bases.MouseEvent'): 
            Reprezentuje zdarzenie kliknięcia myszy.
        """
        self.x1 = event.xdata
        self.z1 = event.ydata

        self.updateCoor1()

    def onclick3(self, event):
        """Metoda, która po kliknięciu myszką w przestrzeni trzeciego rzutu
        (na dole po prawej stronie) pobiera współrzędne kliknięcia.
        Wywołuje funkcję updateCoor1().

        Args:
            event (class 'matplotlib.backend_bases.MouseEvent'): 
            Reprezentuje zdarzenie kliknięcia myszy.
        """
        self.y1 = event.xdata
        self.z1 = event.ydata

        self.updateCoor1()
    

    def updateCoor1(self):
        """Metoda, która uaktualnia poszczególne rzuty i linie
        reprezentujące położenie pozostałych dwóch rzutów względem
        danego rzutu.
        """
        self.vline1.remove()
        self.hline1.remove()
        self.vline1 = self.figure1.axes.vlines(self.x1, 0, self.tmp2-1, colors = 'blue')
        self.hline1 = self.figure1.axes.hlines(self.y1, 0, self.tmp1-1, colors = 'yellow')
        

        self.vline2.remove()
        self.hline2.remove()
        self.vline2 = self.figure2.axes.vlines(self.x1, 0, self.tmp3-1, colors = 'blue')
        self.hline2 = self.figure2.axes.hlines(self.z1, 0, self.tmp1-1, colors = 'deeppink')


        self.vline3.remove()
        self.hline3.remove()
        self.vline3 = self.figure3.axes.vlines(self.y1, 0, self.tmp3-1, colors = 'yellow')
        self.hline3 = self.figure3.axes.hlines(self.z1, 0, self.tmp2-1, colors = 'deeppink')
  

        self.num = int(self.z1)
        self.num2 = int(self.y1)
        self.num3 = int(self.x1)

        self.figure1.axes.imshow(self.img_data[:, :, self.num].T, origin = 'lower', cmap = 'gray')
        self.figure1.axes.set_aspect('auto')
        self.center.setText('Wolumen: ' + str(self.num))
        self.slider.setValue(self.num)
        self.figure1.draw()

        self.figure2.axes.imshow(self.img_data[:, self.num2, :].T, origin = 'lower', cmap = 'gray')
        self.figure2.axes.set_aspect('auto')
        self.center2.setText('Wolumen: ' + str(self.num2))
        self.slider2.setValue(self.num2)
        self.figure2.draw()

        self.figure3.axes.imshow(self.img_data[self.num3, :, :].T, origin = 'lower', cmap = 'gray')
        self.figure3.axes.set_aspect('auto')
        self.center3.setText('Wolumen: ' + str(self.num3))
        self.slider3.setValue(self.num3)
        self.figure3.draw()



    def showImage(self):
        """Metoda wyświetlająca trzy rzuty i ustawiająca
        ich początkowy stan.
        """
        self.counter += 1
        if (self.counter>1):
            self.figure1.axes.clear()
            self.figure2.axes.clear()
            self.figure3.axes.clear()

        mri_file = self.image
        img = nib.load(mri_file)
        hdr = img.header

        self.img_data = img.get_fdata()

        self.tmp1 = self.img_data.shape[0]
        self.tmp2 = self.img_data.shape[1]
        self.tmp3 = self.img_data.shape[2]


        self.x1 = self.tmp1/2
        self.y1 = self.tmp2/2
        self.z1 = self.tmp3/2

        self.num = int(self.tmp3/2)
        self.num2 = int(self.tmp2/2)
        self.num3 = int(self.tmp1/2)

        self.center.setText('Wolumen: ' + str(self.num))
        self.center2.setText('Wolumen: ' + str(self.num2))
        self.center3.setText('Wolumen: ' + str(self.num3))


 
        self.figure1.axes.imshow(self.img_data[:, :, self.num].T, origin = 'lower', cmap = 'gray')
        self.vline1 = self.figure1.axes.vlines(self.x1, 0,self.tmp2-1, colors = 'blue')
        self.hline1 = self.figure1.axes.hlines(self.y1, 0, self.tmp1-1, colors = 'yellow')
        self.figure1.axes.set_aspect('auto')
        self.figure1.draw()
        self.figure1.canvas.mpl_connect('button_press_event', self.onclick1)
        
        
        self.figure2.axes.imshow(self.img_data[:, self.num2, :].T, origin = 'lower', cmap = 'gray')
        self.vline2 = self.figure2.axes.vlines(self.x1, 0, self.tmp3-1, colors = 'blue')
        self.hline2 = self.figure2.axes.hlines(self.z1, 0, self.tmp1-1, colors = 'deeppink')
        self.figure2.axes.set_aspect('auto')
        self.figure2.draw()
        self.figure2.canvas.mpl_connect('button_press_event', self.onclick2)
        
        
        self.figure3.axes.imshow(self.img_data[self.num3, :, :].T, origin = 'lower', cmap = 'gray')
        self.vline3 = self.figure3.axes.vlines(self.y1, 0, self.tmp3-1, colors = 'yellow')
        self.hline3 = self.figure3.axes.hlines(self.z1, 0, self.tmp2-1, colors = 'deeppink')
        self.figure3.axes.set_aspect('auto')
        self.figure3.draw()
        self.figure3.canvas.mpl_connect('button_press_event', self.onclick3)

        self.slider.setMaximum(self.tmp3-1)
        self.slider.setValue(self.num)

        self.slider2.setMaximum(self.tmp2-1)
        self.slider2.setValue(self.num2)

        self.slider3.setMaximum(self.tmp1-1)
        self.slider3.setValue(self.num3)


    def openImage(self):
        """Metoda obsługująca otwarcie pliku .nii.gz. Otwiera okno dialogowe
        umożliwiające wybór pliku. Wywołuje metodę showImage().
        """
        self.num = int(self.tmp3/2)
        self.center.setText('Wolumen: ' + str(self.num))
        self.center2.setText('Wolumen: ')
        self.center3.setText('Wolumen: ')
        path = QFileDialog.getOpenFileName(self,"Wybierz plik", filter="NIFTI files (*.nii, *.nii.gz, *.gz)")

        if path[0]=="":
            return
        self.image = path[0]

        if self.image is None:
            QMessageBox.warning(self,"Warning",f"Cannot open file {path}")
            return
            
        self.showImage()


    def updatePrev(self):
        """Metoda obsługująca przycisk strzałki w lewo w pierwszym rzucie.
        Każde naciśnięcie przycisku zmniejsza indeks wyświetlanego obrazu
        w pierwszym rzucie. 
        Pośrednio wywołuje metodę updateSlider() poprzez zmianę wartości
        suwaka.
        """
        tmp3 = 0

        self.num -= 1
        if self.num < tmp3:
            self.num = tmp3

        self.center.setText('Wolumen: ' + str(self.num))
        self.slider.setValue(self.num)



    def updateNext(self): 
        """Metoda obsługująca przycisk strzałki w prawo w pierwszym rzucie.
        Każde naciśnięcie przycisku zwiększa indeks wyświetlanego obrazu
        w pierwszym rzucie. 
        Pośrednio wywołuje metodę updateSlider() poprzez zmianę wartości
        suwaka.
    
        """

        tmp3 = self.img_data.shape[2] 

        self.num += 1
        if self.num >= tmp3:
            self.num = tmp3-1

        self.center.setText('Wolumen: ' + str(self.num))
        self.slider.setValue(self.num)


    
    def updateSlider(self, value):
        """Metoda obsługująca suwak pierwszego rzutu.
        Aktualizuje rzut Z: w pierwszym rzucie aktualizuje slice, 
        a w pozostałych dwóch rzutach - położenie linii reprezentującej
        rzut Z.

        Args:
            value (class int): Reprezentuje wartości na suwaku.
        """
        self.num = value

        tmp3 = self.img_data.shape[2] 
        self.slider.setMaximum(tmp3-1)

        self.figure1.axes.imshow(self.img_data[:, :, self.num].T, origin = 'lower', cmap = 'gray')
        self.figure1.axes.set_aspect('auto')
        self.z1 = self.num
        self.hline2.remove()
        self.hline3.remove()
  
        self.hline2 = self.figure2.axes.hlines(self.z1, 0, self.tmp1-1, colors = 'deeppink')
        self.hline3 = self.figure3.axes.hlines(self.z1, 0, self.tmp2-1, colors = 'deeppink')
        self.center.setText('Wolumen: ' + str(self.num))
        self.figure1.draw()
        self.figure2.draw()
        self.figure3.draw()
        

    def updatePrev2(self):
        """Metoda obsługująca przycisk strzałki w lewo w drugim rzucie.
        Każde naciśnięcie przycisku zmniejsza indeks wyświetlanego obrazu
        w drugim rzucie. 
        Pośrednio wywołuje metodę updateSlider2() poprzez zmianę wartości
        suwaka.
        """
        tmp2 = 0

        self.num2 -= 1
        if self.num2 < tmp2:
            self.num2 = tmp2

        self.center2.setText('Wolumen: ' + str(self.num2))
        self.slider2.setValue(self.num2)



    def updateNext2(self):
        """Metoda obsługująca przycisk strzałki w prawo w drugim rzucie.
        Każde naciśnięcie przycisku zwiększa indeks wyświetlanego obrazu
        w drugim rzucie. 
        Pośrednio wywołuje metodę updateSlider2() poprzez zmianę wartości
        suwaka.
        """

        tmp2 = self.img_data.shape[1] 

        self.num2 += 1
        if self.num2 >= tmp2:
            self.num2 = tmp2-1

        self.center2.setText('Wolumen: ' + str(self.num2))
        self.slider2.setValue(self.num2)

    def updateSlider2(self, value):
        """Metoda obsługująca suwak drugiego rzutu.
        Aktualizuje rzut Y: w drugim rzucie aktualizuje slice, 
        a w pozostałych dwóch rzutach - położenie linii reprezentującej
        rzut Y.

        Args:
            value (class int): Reprezentuje wartości na suwaku.
        """
        self.num2 = value

        tmp2 = self.img_data.shape[1] 
        self.slider2.setMaximum(tmp2-1)

        self.figure2.axes.imshow(self.img_data[:, self.num2, :].T, origin = 'lower', cmap = 'gray')
        self.figure2.axes.set_aspect('auto')
        self.y1 = self.num2
        self.hline1.remove()
        self.vline3.remove()

        self.hline1 = self.figure1.axes.hlines(self.y1, 0, self.tmp1-1, colors = 'yellow')
        self.vline3 = self.figure3.axes.vlines(self.y1, 0, self.tmp3-1, colors = 'yellow')
        self.center2.setText('Wolumen: ' + str(self.num2))
        self.figure2.draw()
        self.figure1.draw()
        self.figure3.draw()


    def updatePrev3(self):
        """Metoda obsługująca przycisk strzałki w lewo w trzecim rzucie.
        Każde naciśnięcie przycisku zmniejsza indeks wyświetlanego obrazu
        w trzecim rzucie. 
        Pośrednio wywołuje metodę updateSlider3() poprzez zmianę wartości
        suwaka.
        """        
        tmp1 = 0

        self.num3 -= 1
        if self.num3 < tmp1:
            self.num3 = tmp1

        self.center3.setText('Wolumen: ' + str(self.num3))
        self.slider3.setValue(self.num3)


    def updateNext3(self):
        """Metoda obsługująca przycisk strzałki w prawo w trzecim rzucie.
        Każde naciśnięcie przycisku zwiększa indeks wyświetlanego obrazu
        w trzecim rzucie. 
        Pośrednio wywołuje metodę updateSlider3() poprzez zmianę wartości
        suwaka.
        """

        tmp1 = self.img_data.shape[0] 

        self.num3 += 1
        if self.num3 >= tmp1:
            self.num3 = tmp1-1

        self.center3.setText('Wolumen: ' + str(self.num3))
        self.slider3.setValue(self.num3)



    def updateSlider3(self, value):
        """Metoda obsługująca suwak trzeciego rzutu.
        Aktualizuje rzut X: w trzecim rzucie aktualizuje slice, 
        a w pozostałych dwóch rzutach - położenie linii reprezentującej
        rzut X.

        Args:
            value (class int): Reprezentuje wartości na suwaku.
        """
        self.num3 = value

        tmp1 = self.img_data.shape[0] 
        self.slider3.setMaximum(tmp1-1)

        self.figure3.axes.imshow(self.img_data[self.num3, :, :].T, origin = 'lower', cmap = 'gray')
        self.figure3.axes.set_aspect('auto')
        self.x1 = self.num3
        self.vline1.remove()
        self.vline2.remove()

        self.vline1 = self.figure1.axes.vlines(self.x1, 0, self.tmp2-1, colors = 'blue')
        self.vline2 = self.figure2.axes.vlines(self.x1, 0, self.tmp3-1, colors = 'blue')
        self.center3.setText('Wolumen: ' + str(self.num3))
        self.figure3.draw()
        self.figure1.draw()
        self.figure2.draw()


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()