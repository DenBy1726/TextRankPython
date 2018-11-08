import pytextrank
from pytextrank import normalize_key_phrases, pretty_print, render_ranks, text_rank
import sys
import numpy as np

if(len(sys.argv) < 2):
    path_stage0 = "data/input.json"
else:
    path_stage0 = sys.argv[1]

path_stage1 = "output/o1.json"
path_stage2 = "output/o2.json"
path_graph_dot = "output/graph.dot"

def graph_from_object(obj):
    arr = []
    for graf in pytextrank.parse_doc(obj):
        arr.append(graf)
    return arr

def graph_dict(graphs):
    arr = []
    for graph in graphs:
        arr.append(graph._asdict())
    return arr

def graph_dict_to_keywords(dicts,ranks):
    arr = []
    for rl in pytextrank.normalize_key_phrases(dicts, ranks):
        arr.append(rl._asdict())
    return arr
    

def obj_to_keywords(obj):
    if isinstance(obj, list) == False:
        obj = [obj]
    graphs = graph_from_object(obj)
    dicts = graph_dict(graphs)
    graph, ranks = text_rank(path_stage1)
    keywords = graph_dict_to_keywords(dicts,ranks)
    return keywords

obj = {'id':1,'text':"Compatibility of systems of linear constraints over the set of natural numbers. Criteria of compatibility of a system of linear Diophantine equations, strict inequations, and nonstrict inequations are considered. Upper bounds for components of a minimal set of solutions and algorithms of construction of minimal generating sets of solutions for all types of systems are given. These criteria and the corresponding algorithms for constructing a minimal supporting set of solutions can be used in solving all the considered types systems and systems of mixed types."}
obj_to_keywords(obj)

# obj = pytextrank.json_iter(path_stage0)
# graphs = graph_from_object(obj)
# with open(path_stage1, 'w') as f:
#     for graph in graphs:
#         #итерируем по предложениям, сохраняем граф каждого предложениям.
#         f.write("%s\n" % pytextrank.pretty_print(graph._asdict()))

# graph, ranks = text_rank(path_stage1)
# render_ranks(graph,ranks,path_graph_dot)

# with open(path_stage2, 'w') as f:
#     for rl in pytextrank.normalize_key_phrases(path_stage1, ranks):
#         f.write("%s\n" % pytextrank.pretty_print(rl._asdict()))
