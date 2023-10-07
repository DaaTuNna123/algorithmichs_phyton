from PyQt5.QtWidgets import QApplication , QPushButton, QWidget,  QLabel, QHBoxLayout, QVBoxLayout, QListWidget, QFileDialog
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PIL import Image, ImageFilter
import os

app = QApplication([])

window = QWidget()
window.resize(700, 400)

window.setWindowTitle("Easy Editor App")


button_left = QPushButton('Left')
button_Right = QPushButton('Right')
button_Mirror = QPushButton('Mirror')
button_Sharpness = QPushButton('Sharpness')
button_BW = QPushButton('BW')

Button_Folder = QPushButton('Folder')

Label_pic = QLabel("")

List_Widget = QListWidget()
#layout_თან მუშაობა
button_row = QHBoxLayout()

button_row.addWidget(button_left)
button_row.addWidget(button_Right)
button_row.addWidget(button_Mirror)
button_row.addWidget(button_Sharpness)
button_row.addWidget(button_BW)


row = QHBoxLayout()
col1 = QVBoxLayout()
col2 = QVBoxLayout()

col1.addWidget(Button_Folder)
col1.addWidget(List_Widget)

col2.addWidget(Label_pic)
col2.addLayout(button_row)

row.addLayout(col1)
row.addLayout(col2)



window.setLayout(row)
window.show()


workdir = ''

extensions = ['.jpg','.jpeg','.png', '.gif', '.bmp']

def filter(files, extensions):
    results=[]
    for filenames in files:
        for ext in extensions:
            if filenames.endswith(ext):
                results.append(filenames)
    return results


def chooseWorkdir():
    global workdir
    workdir = QFileDialog.getExistingDirectory()


def showFilenamesList():
    extensions = ['.jpg','.jpeg','.png', '.gif', '.bmp']
    chooseWorkdir()
    filtered_list = filter(os.listdir(workdir), extensions)
    List_Widget.clear()
    for i in filtered_list:
        List_Widget.addItem(i)
           
class ImageProcesor():
    def __init__(self):
        self.image=None #აქ იქნება ფოტოს ობიექტი
        self.Filename=None #აქ იქნება ფოტოს სახელი
        self.dir=None #აქ იქნება დირექტორიის მისამართი
        self.save_dir="Modified/" #ფოლდერი სადაც შევინახავთ სახეშეცვლილ ფოტოებს

    ''' LoadImage ფოტოს ჩატვირთვის ფუნქცია'''

    def loadImage(self, filename):
        '''When loading, remember the path and file name '''
        self.filename=filename #გადავცემთ სახელს
        fullname = os.path.join(workdir, filename) #სრული მისამართის ცვლადი
        self.image = Image.open(fullname) #self.image აქ არის უკვე PIL ის ობიექტი

    def SaveImage(self):
        path=os.path.join(workdir, self.save_dir) #ვქმნით შესანახ მისამართს 
        if not (os.path.exists(path) or os.path.isdir(path)):
            os.mkdir(path) #ვქმნით ფოლდერს თუ არ გვაქვს
        fullname = os.path.join(path, self.filename)
        self.image.save(fullname)

        '''showImage გვიჩვენებს ფოტოს ეკრანზე'''

    def showImage(self,path):
        Label_pic.hide() #labelის დაფარვა
        pixmap = QPixmap(path) #Pixmap ის ობიექტი
        w,h = Label_pic.width(),Label_pic.height()
        piximage = pixmap.scaled(w, h, Qt.KeepAspectRatio)
        Label_pic.setPixmap(piximage)
        Label_pic.show()


    def do_bw(self):
        self.image = self.image.convert('L')
        obj = os.path.join(workdir, self.save_dir, self.filename)
        self.SaveImage()
        self.showImage(obj)
        

    def do_button_left(self):
        self.image = self.image.transpose(Image.ROTATE_270)
        obj = os.path.join(workdir,self.save_dir, self.filename )
        self.SaveImage()
        self.showImage(obj)

    
    def do_button_right(self):
        self.image = self.image.transpose(Image.ROTATE_90)
        obj = os.path.join(workdir,self.save_dir, self.filename )
        self.SaveImage()
        self.showImage(obj)

    def do_button_Mirror(self):
        self.image = self.image.transpose(Image.FLIP_LEFT_RIGHT)
        obj = os.path.join(workdir,self.save_dir, self.filename )
        self.SaveImage()
        self.showImage(obj)


    def do_button_Sharpness(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)
        obj = os.path.join(workdir,self.save_dir, self.filename )
        self.SaveImage()
        self.showImage(obj)


def showChoosenImage():
    if List_Widget.currentRow() >=0:
        print(List_Widget.currentRow())
        filename = List_Widget.currentItem().text()
        obj.loadImage(filename)
        obj.showImage(os.path.join(workdir, filename))








Button_Folder.clicked.connect(showFilenamesList)
obj = ImageProcesor()
List_Widget.currentRowChanged.connect(showChoosenImage)
button_BW.clicked.connect(obj.do_bw)
button_left.clicked.connect(obj.do_button_left)
button_Right.clicked.connect(obj.do_button_right)
button_Mirror.clicked.connect(obj.do_button_Mirror)
button_Sharpness.clicked.connect(obj.do_button_Sharpness)
app.exec()



