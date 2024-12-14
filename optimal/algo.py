from math import sqrt

def get_cost(
  river_cost,
  river_width,
  land_cost,
  factory_distance,
  non_land_distance
):
  return river_cost * sqrt(river_width**2 + non_land_distance**2) + \
    land_cost * (factory_distance - non_land_distance)

def get_mixed_cost(river_cost, river_width, land_cost, factory_distance, critical_point):
    if critical_point != None:
      return get_cost(
        river_cost=river_cost,
        river_width=river_width,
        land_cost=land_cost,
        factory_distance=factory_distance,
        non_land_distance=critical_point
    )
    else:
      return None

def get_land_only_cost(
  river_cost,
  river_width,
  land_cost,
  factory_distance
): return get_cost(
        river_cost=river_cost,
        river_width=river_width,
        land_cost=land_cost,
        factory_distance=factory_distance,
        non_land_distance=0)

def get_river_only_cost(
  river_cost,
  river_width,
  land_cost,
  factory_distance
): return get_cost(
        river_cost=river_cost,
        river_width=river_width,
        land_cost=land_cost,
        factory_distance=factory_distance,
        non_land_distance=factory_distance)

def get_critical_point(river_cost, river_width, land_cost):
  if land_cost >= river_cost:
    return None
  return sqrt((land_cost**2 * river_width**2) / (river_cost**2 - land_cost**2)
)

def get_river_distance(river_width, factory_distance, river_cost, land_cost, critical_point):
  river_only_cost = get_cost(river_cost=river_cost, river_width=river_width, land_cost=land_cost, factory_distance=factory_distance, non_land_distance=factory_distance)
  land_only_cost = get_cost(river_cost=river_cost, river_width=river_width, land_cost=land_cost, factory_distance=factory_distance, non_land_distance=0)

  if critical_point != None:
    return sqrt(river_width**2 + critical_point**2)
  else:
    if river_only_cost < land_only_cost:
      return sqrt(river_width**2 + factory_distance**2)
    elif land_only_cost < river_only_cost:
      return river_width

def get_land_distance(river_width, factory_distance, river_cost, land_cost, critical_point):
  river_only_cost = get_cost(river_cost=river_cost, river_width=river_width, land_cost=land_cost, factory_distance=factory_distance, non_land_distance=factory_distance)
  land_only_cost = get_cost(river_cost=river_cost, river_width=river_width, land_cost=land_cost, factory_distance=factory_distance, non_land_distance=0)

  if critical_point != None:
    return factory_distance - critical_point
  else:
    if river_only_cost < land_only_cost:
      return 0
    elif land_only_cost < river_only_cost:
      return factory_distance

def get_minimal_cost(land_only_cost, river_only_cost, mixed_cost, critical_point):
  if critical_point != None:
    return min([land_only_cost, river_only_cost, mixed_cost])
  else:
    return min([land_only_cost, river_only_cost])


def get_minimal_cost_label(river_cost, land_cost, river_width, factory_distance, critical_point) -> str:
  river_only_cost = get_cost(river_cost=river_cost, river_width=river_width, land_cost=land_cost, factory_distance=factory_distance, non_land_distance=factory_distance)
  land_only_cost = get_cost(river_cost=river_cost, river_width=river_width, land_cost=land_cost, factory_distance=factory_distance, non_land_distance=0)

  if critical_point != None:
    return 'por rio e terra'
  elif river_only_cost < land_only_cost:
    return 'apenas pelo rio'
  elif land_only_cost < river_only_cost:
    return 'majoritariamente por terra'
  else:
    return 'Indefinido'

