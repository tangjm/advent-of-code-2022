from collections import namedtuple 

Point = namedtuple('Point', ['x', 'y'])

def manhatten_distance(p1, p2):
  return abs(p1.x - p2.x) + abs(p1.y - p2.y)

def northern_most_point(sensor, distance):
  return Point(sensor.x, sensor.y - distance)

def southern_most_point(sensor, distance):
  return Point(sensor.x, sensor.y + distance)

def overlaps_with(interval1, interval2):
  return not (interval1[0] > interval2[1] or interval2[0] > interval1[1])

def is_continuous(interval1, interval2):
  if interval1[0] == interval2[1] + 1:
    return True
  if interval2[0] == interval1[1] + 1:
    return True
  return False

def count_visible_points(merged):
  """
  It is guaranteed that given an interval [start, end] that start <= end.
  We (+ 1) to account for the end point itself.
  """
  visible_points = 0
  for interval in merged:
    visible_points += interval[1] - interval[0] + 1 
  return visible_points

def get_relevant_sensors(designated_y, sensor_to_closest_beacon, sensor_to_vertical_perimeters):
  """
  Filter sensors by those whose vertical diameter intersects with
  the horizontal line y=designated_y
  """
  relevant_sensors = []
  for sensor in sensor_to_closest_beacon:
    top, bottom = sensor_to_vertical_perimeters[sensor]
    if not (top.y > designated_y or bottom.y < designated_y):
      relevant_sensors.append(sensor)
  return relevant_sensors

def beacon_scan(sensor_to_closest_beacon, designated_y):
  """
  If any point on our designated_y already has a discovered beacon and is within the perimeter of some sensor, we don't want to treat it as an impossible point for a beacon. (Since it already holds a beacon, it's not true that it cannot hold a beacon.) 
  We use a set because the mapping of sensors to beacons may not be injective.
  """
  discovered_beacons = 0
  for beacon in set(sensor_to_closest_beacon.values()):
    if beacon.y == designated_y:
      discovered_beacons += 1
  return discovered_beacons


def compute_tuning_frequency(x, y):
  return x * 4_000_000 + y

