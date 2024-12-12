from math import sqrt

def get_cost(river_cost, river_width, land_cost, factory_distance, non_land_distance):
  return river_cost * sqrt(river_width**2 + non_land_distance**2) + \
    land_cost * (factory_distance - non_land_distance)

def get_critical_point(river_cost, river_width, land_cost):
  return sqrt((land_cost**2 * river_width**2) / (river_cost**2 - land_cost**2)
)

def get_minimal_cost(river_cost, river_width, land_cost, factory_distance, critical_point):
  get_cost(river_cost, river_width, land_cost, factory_distance, critical_point)

def get_river_distance(river_width, non_land_distance):
  return sqrt(river_width**2 + non_land_distance**2)

def get_land_distance(factory_distance, non_land_distance):
  return factory_distance - non_land_distance
