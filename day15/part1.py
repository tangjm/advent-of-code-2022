#!/usr/bin/python3
import sys
import re
from typing import *
from collections import namedtuple
from logger import log
from helpers import * 

filename = './puzzle_input.txt' if len(sys.argv) < 2 else sys.argv[1]

sensor_to_closest_beacon = {}
distance_to_closest_beacon = {}

with open(filename, 'rt') as f: 
  lines = f.read().rstrip().split('\n')
  pattern = 'x=(\-?\d+), y=(\-?\d+)'

  for line in lines:
    matches = re.findall(pattern, line)
    sensor, beacon = tuple(map(lambda pair : Point(int(pair[0]), int(pair[1])), matches))
    sensor_to_closest_beacon[sensor] = beacon
    distance_to_closest_beacon[sensor] = manhatten_distance(sensor, beacon)

def part_one(designated_y):
  sensor_to_vertical_perimeters = {}

  # Construct the northern and southern most points for each sensor 
  # given the manhatten distance to their closest beacon.
  for sensor in sensor_to_closest_beacon:
    d = distance_to_closest_beacon[sensor]
    northern_perimeter = northern_most_point(sensor, d) 
    southern_perimeter = southern_most_point(sensor, d) 
    sensor_to_vertical_perimeters[sensor] = [northern_perimeter, southern_perimeter]
  
  # Sensors that intersect vertically with the designated line.
  relevant_sensors = get_relevant_sensors(designated_y, sensor_to_closest_beacon, sensor_to_vertical_perimeters)
  
  # Breadth of points on designated line
  # within the manhatten distance from the sensor
  sensor_to_breadth = {}
  for sensor in relevant_sensors:
    radius = distance_to_closest_beacon[sensor]
    distance_from_designated_y = abs(designated_y - sensor.y) 
    new_radius = radius - distance_from_designated_y

    left_most_point = sensor.x - new_radius 
    right_most_point = sensor.x + new_radius 
    sensor_to_breadth[sensor] = [left_most_point, right_most_point]
  
  # Merge any overlapping intervals
  sorted_intervals = sorted(sensor_to_breadth.values(), key=lambda pair:pair[0])

  log('sorted_intervals', sorted_intervals)
  
  merged = [sorted_intervals[0]]
  for i in range(1, len(sorted_intervals)):
    if overlaps_with(merged[-1], sorted_intervals[i]):
      merged[-1][0] = min(merged[-1][0], sorted_intervals[i][0]) 
      merged[-1][1] = max(merged[-1][1], sorted_intervals[i][1]) 
    else: 
      merged.append(sorted_intervals[i])
    
  log('merged', merged)

  visible_points = count_visible_points(merged)
  discovered_beacons = beacon_scan(sensor_to_closest_beacon, designated_y)
  
  impossible_points = visible_points - discovered_beacons

  log('discovered beacons', discovered_beacons)
  log('impossible_points', impossible_points)

  print('Part One:', impossible_points)

    
# sample_y = 10
# part_one(sample_y)

actual_y = 2_000_000
part_one(actual_y)
