# from PyQt5.QtWidgets import QApplication , QPushButton, QWidget,  QLabel, QHBoxLayout, QVBoxLayout, QListWidget


# app = QApplication([])

# window = QWidget()
# window.resize(700, 400)

# window.setWindowTitle("Easy Editor App")


# button_left = QPushButton('Left')
# button_Right = QPushButton('Right')
# button_Mirror = QPushButton('Mirror')
# button_Sharpness = QPushButton('Sharpness')
# button_BW = QPushButton('BW')

# Button_Folder = QPushButton('Folder')

# Label_pic = QLabel("")

# List_Widget = QListWidget()
# #layout_თან მუშაობა
# button_row = QHBoxLayout()

# button_row.addWidget(button_left)
# button_row.addWidget(button_Right)
# button_row.addWidget(button_Mirror)
# button_row.addWidget(button_Sharpness)
# button_row.addWidget(button_BW)


# row = QHBoxLayout()
# col1 = QVBoxLayout()
# col2 = QVBoxLayout()

# col1.addWidget(Button_Folder)
# col1.addWidget(List_Widget)

# col2.addWidget(Label_pic)
# col2.addLayout(button_row)

# row.addLayout(col1)
# row.addLayout(col2)



# window.setLayout(row)
# window.show()
# app.exec()



from PyQt5.QtWidgets import QApplication , QPushButton, QWidget,  QLabel, QHBoxLayout, QVBoxLayout, QListWidget


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

col2.addWidget(Button_Folder)
col2.addWidget(List_Widget)

col1.addWidget(Label_pic)
col1.addLayout(button_row)

row.addLayout(col1)
row.addLayout(col2)



window.setLayout(row)
window.show()
app.exec()


