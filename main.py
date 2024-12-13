import sys
from optimal.render import render
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
      main(textual=True)

    if dict['river_width'] == None or dict['factory_distance'] == None \
      or dict['river_cost'] == None or dict['land_cost'] == None:
      print(assignment_error_message)
      exit(1)

    critical_point = get_critical_point(
      river_cost=dict['river_cost'],
      river_width=dict['river_width'],
      land_cost=dict['land_cost']
    )

    minimal_cost = get_cost(
      dict['river_cost'],
      dict['river_width'],
      dict['land_cost'],
      dict['factory_distance'],
      critical_point
    )

    river_distance = get_river_distance(
      river_width=dict['river_width'],
      non_land_distance=critical_point
    )

    land_distance = get_land_distance(
      factory_distance=dict['factory_distance'],
      non_land_distance=critical_point
    )

    # Output
    print('Custo mínimo: ' + str(minimal_cost))
    print('Distância percorrida pelo rio: ' + str(river_distance))
    print('Distância percorrida pela terra: ' + str(land_distance))
  else:
    gui.launch()

print(assignment_message)
if len(sys.argv) > 1:
  session_is_textual = sys.argv[1] == '--text' or sys.argv[1] == '-t'
else:
  session_is_textual = False

main(textual=session_is_textual)
