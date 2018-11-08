import pytextrank
import sys

if(len(sys.argv) < 2):
    path_stage0 = "data/input.json"
else:
    path_stage0 = sys.argv[1]
path_stage1 = "o1.json"

with open(path_stage1, 'w') as f:
    for graf in pytextrank.parse_doc(pytextrank.json_iter(path_stage0)):
        f.write("%s\n" % pytextrank.pretty_print(graf._asdict()))