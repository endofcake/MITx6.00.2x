from ps5 import *

mapFilename = 'mit_map.txt'

def test_load_map():
    mitMap = load_map(mapFilename)
    print(mitMap)
    print isinstance(mitMap, Digraph)
    print isinstance(mitMap, WeightedDigraph)

def test_set_of_nodes():
    mitMap = load_map(mapFilename)
    nodes = mitMap.nodes
    print(nodes)

def test_map_edges():
    mitMap = load_map(mapFilename)
    print mitMap.edges

#test_load_map()
# test_set_of_nodes()
test_map_edges()