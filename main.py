from optimal.algo import *

assignment_message = 'Para todas as entradas, são aceitos apenas valores numéricos e um único ponto para delimitar as casas decimais'
assignment_error_message = 'Valor inválido fornecido: ' + assignment_message

def main():

  river_width = None
  factory_distance = None
  river_cost = None
  land_cost = None

  try:
    print('Digite a largura do rio em metros:')
    river_width = float(input())
    print('Digite a distância até a fábrica em metros')
    factory_distance = float(input())
    print('Digite o custo por metro para estender o cabo pelo rio')
    river_cost = float(input())
    print('Digite o custo por metro para estender o cabo por terra')
    land_cost = float(input())
  except KeyboardInterrupt:
    exit()
  except:
    print(assignment_error_message)
    main()

  if river_width == None or factory_distance == None or river_cost == None or land_cost == None:
    print(assignment_error_message)
    exit(1)

  critical_point = get_critical_point(
    river_cost=river_cost,
    river_width=river_width,
    land_cost=land_cost
  )

  minimal_cost = get_cost(river_cost, river_width, land_cost, factory_distance, critical_point)
  river_distance = get_river_distance(river_width=river_width, non_land_distance=critical_point)
  land_distance = get_land_distance(factory_distance=factory_distance, non_land_distance=critical_point)

  # Output
  print('Custo mínimo: ' + str(minimal_cost))
  print('Distância percorrida pelo rio: ' + str(river_distance))
  print('Distância percorrida pela terra: ' + str(land_distance))

  # render(input_a, input_b, input_c, input_d, input_f)


print(assignment_message)
main()
