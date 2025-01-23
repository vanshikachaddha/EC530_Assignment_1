# EC530_Assignment_1
The Geo Location Matcher is a Python module designed to efficiently match points between two arrays of geographic coordinates. Given two arrays of GPS locations, the module computes the shortest distance between each point in the first array and the closest point in the second array. 

## Sample Implementation
```
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
```
