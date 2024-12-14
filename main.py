import sys

from optimal.constants import assignment_message, assignment_error_message
from optimal.algo import *
from optimal import gui
from typing import Dict

def main(textual : bool):

  dict: Dict[str, float | None] = {
    'river_width': None,
    'factory_distance': None,
    'river_cost': None,
    'land_cost': None,
  }

  if textual:

    # Input

    try:
      print('Digite a largura do rio em metros:')
      dict['river_width'] = float(input())
      print('Digite a distância até a fábrica em metros')
      dict['factory_distance'] = float(input())
      print('Digite o custo por metro para estender o cabo pelo rio')
      dict['river_cost'] = float(input())
      print('Digite o custo por metro para estender o cabo por terra')
      dict['land_cost'] = float(input())
    except KeyboardInterrupt:
      exit()
    except:
      print(assignment_error_message)
      exit(1)

    if dict['river_width'] == None or dict['factory_distance'] == None \
      or dict['river_cost'] == None or dict['land_cost'] == None:
      print(assignment_error_message)
      exit(1)

    # Processing

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

    river_distance = None
    land_distance = None
    minimal_cost = None
    mixed_cost = 'Indeterminado'
    minimal_cost_label = 'Indefinido'

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

    print('Custo mínimo: ' + str(minimal_cost) + ' (' + minimal_cost_label + ')')
    print('Distância percorrida pelo rio: ' + str(river_distance))
    print('Distância percorrida pela terra: ' + str(land_distance))
  else:
    gui.launch()

has_textual_flag = False

if len(sys.argv) > 1:
  has_textual_flag = '--text' in sys.argv or '-t' in sys.argv

else:
  session_is_textual = False

print(assignment_message)
main(textual=has_textual_flag)
