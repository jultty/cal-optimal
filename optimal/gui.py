import sys
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets \
  import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout
from optimal.render import render

class Form(QDialog):

  def __init__(self, parent=None):
    super(Form, self).__init__(parent)
    self.setWindowTitle("TAMC Optimal")

    layout = QVBoxLayout(self)
    validator = QDoubleValidator()

    self.river_width = QLineEdit()
    self.river_width.setValidator(validator)
    self.river_width.setPlaceholderText("Largura do rio")
    layout.addWidget(self.river_width)

    self.factory_distance = QLineEdit()
    self.factory_distance.setValidator(validator)
    self.factory_distance.setPlaceholderText("Distância até a fábrica")
    layout.addWidget(self.factory_distance)

    self.river_cost = QLineEdit()
    self.river_cost.setValidator(validator)
    self.river_cost.setPlaceholderText("Custo pelo rio")
    layout.addWidget(self.river_cost)

    self.land_cost = QLineEdit()
    self.land_cost.setValidator(validator)
    self.land_cost.setPlaceholderText("Custo pela terra")
    layout.addWidget(self.land_cost)

    self.submit_button = QPushButton("Calcular")
    self.submit_button.clicked.connect(self.submit_handler)
    layout.addWidget(self.submit_button)

    self.setLayout(layout)

  def submit_handler(self):

    render({
      'river_width': float(self.river_width.text()),
      'factory_distance': float(self.factory_distance.text()),
      'river_cost': float(self.river_cost.text()),
      'land_cost': float(self.land_cost.text()),
    })

def launch():
  app = QApplication(sys.argv)
  form = Form()
  form.show()
  sys.exit(app.exec())
