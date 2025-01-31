# -*- coding: utf-8 -*-
"""EC 530 - Assignment 1.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1t6kWjf8r2yoXnkeYTa0IrDpE4jS1SSx1
"""

import math
import pandas as pd

# Checking if DMS
def check_DMS(value):
  return isinstance(value, str) and " " in value

# Convert from DMS to DD
def convert_dms(dms):

  if check_DMS(dms):
    deg_form = dms.split()
    return round(float(deg_form[0]) + (float(deg_form[1]) / 60), 6)
  else:
    return dms

# Reading a CSV File

def tuple_list(a,b):
  return list(map(lambda x, y:(x,y), a, b))


def read_csv(name, lat_col, long_col):
  dataset = pd.read_csv(name)
  latitude = dataset.iloc[:, lat_col].values
  longitude = dataset.iloc[:, long_col].values

  return tuple_list(latitude, longitude)

# Precompute radians
def convert_radians(arr):

  new_arr = []
  for (lat, long) in arr:

    if check_DMS(lat):
      lat = convert_dms(lat)

    if check_DMS(long):
      long = convert_dms(long)

    new_arr.append((math.radians(lat), math.radians(long)))

  return new_arr

# Calculate distance between two points
def distance(lon1, lon2, lat1, lat2):

  distance = 3963.0 * math.acos(math.sin(lat1) * math.sin(lat2) + math.cos(lat1) * math.cos(lat2) * math.cos(lon2-lon1))

  return distance


# Find the shortest distance
def shortest_match(arr1, arr2):
  i = 0

  shortest_match = []
  rad_arr1 = convert_radians(arr1)
  rad_arr2 = convert_radians(arr2)

  for lat1, lon1 in rad_arr1:
      distances = []
      for lat2, lon2 in rad_arr2:
        distances.append(distance(lon1, lon2, lat1, lat2))

      min_value = min(distances)
      min_index = distances.index(min_value)
      closest_point = arr2[min_index]
      shortest_match.append((arr1[i], closest_point))
      i = i+1


  return shortest_match

# Test 1

current_GPS = [(42.361145, -71.057083)]

arr_2 = read_csv('/content/Boston 311 012225.csv',27,28)

result = shortest_match(current_GPS, arr_2)

print(result)

# Test 2 (not efficient - 11 min to execute)

major_cities = read_csv('/content/world_cities.csv', 2, 3)
airports = read_csv('/content/iata-icao.csv', 5, 6)

result = shortest_match(major_cities, airports)

print(result)

# Test 3

cities = read_csv('/content/Cities - Sheet1.csv', 1, 2)
airports = read_csv('/content/iata-icao.csv', 5, 6)

result = shortest_match(cities, airports)

print(result)

# Example implementation

array1 = [
    (42.3601, -71.0589),
    (34.0522, -118.2437)
]

array2 = [
    (40.7128, -74.0060),
    (36.7783, -119.4179),
    (41.8781, -87.6298)
]

result = shortest_match(array1, array2)
print(result)