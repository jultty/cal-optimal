import sys
from PySide6.QtGui import QDoubleValidator
from PySide6.QtWidgets \
  import QApplication, QDialog, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from optimal.algo import *
from optimal.constants import assignment_error_message
from typing import Dict

class Form(QDialog):

  def __init__(self, parent=None):
    super(Form, self).__init__(parent)
    self.setWindowTitle("TAMC Optimal")

    layout = QVBoxLayout(self)
    validator = QDoubleValidator()
    validator.setBottom(0)

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

    if self.river_width.text() == '' or self.factory_distance.text() == '' \
      or self.river_cost.text() == '' or self.land_cost.text() == '':
      msgBox = QMessageBox()
      msgBox.setText(assignment_error_message)
      msgBox.exec()
      return

    dict: Dict[str, float] = {
      'river_width': float(self.river_width.text()),
      'factory_distance': float(self.factory_distance.text()),
      'river_cost': float(self.river_cost.text()),
      'land_cost': float(self.land_cost.text()),
    }

    river_distance = None
    land_distance = None
    minimal_cost = None
    mixed_cost = 'Indeterminado'
    minimal_cost_label = 'Indefinido'

    land_only_cost = get_land_only_cost(
      river_cost = dict['river_cost'],
      river_width = dict['river_width'],
      land_cost = dict['land_cost'],
      factory_distance = dict['factory_distance'],
    )

    river_only_cost = get_river_only_cost(
      river_cost = dict['river_cost'],
      river_width = dict['river_width'],
      land_cost = dict['land_cost'],
      factory_distance = dict['factory_distance'],
    )

    critical_point = get_critical_point(
      river_cost=dict['river_cost'],
      river_width=dict['river_width'],
      land_cost=dict['land_cost']
    )

    mixed_cost = get_mixed_cost(
      dict['river_cost'],
      dict['river_width'],
      dict['land_cost'],
      dict['factory_distance'],
      critical_point
    )

    minimal_cost = get_minimal_cost(
      land_only_cost=land_only_cost,
      river_only_cost=river_only_cost,
      mixed_cost=mixed_cost,
      critical_point=critical_point
    )

    minimal_cost_label = get_minimal_cost_label(
      river_cost=dict['river_cost'],
      land_cost=dict['land_cost'],
      factory_distance=dict['factory_distance'],
      river_width=dict['river_width'],
      critical_point=critical_point
    )

    river_distance = get_river_distance(
      river_width=dict['river_width'],
      factory_distance=dict['factory_distance'],
      river_cost=dict['river_cost'],
      land_cost=dict['land_cost'],
      critical_point=critical_point
    )

    land_distance = get_land_distance(
      river_width=dict['river_width'],
      factory_distance=dict['factory_distance'],
      river_cost=dict['river_cost'],
      land_cost=dict['land_cost'],
      critical_point=critical_point
    )

    # Output

    msgBox = QMessageBox()
    msgBox.setText(
      'Custo mínimo: ' + str(minimal_cost) + ' (' + minimal_cost_label + ')' + \
      '\n' + 'Distância percorrida pelo rio: ' + str(river_distance) + \
      '\n' + 'Distância percorrida pela terra: ' + str(land_distance)
    )
    msgBox.exec()

def launch():
  app = QApplication(sys.argv)
  form = Form()
  form.show()
  sys.exit(app.exec())
