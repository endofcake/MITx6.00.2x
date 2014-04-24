from ps5 import *

def test_load_map():
    mapFilename = 'mit_map.txt'
    mitMap = load_map(mapFilename)
    print(mitMap)
    print isinstance(mitMap, Digraph)
    print isinstance(mitMap, WeightedDigraph)

test_load_map()