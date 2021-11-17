f = open("listsaham.txt", "r")
content = f.read()

#import ast
#listsaham = ast.literal_eval(content)

import json
listsaham = json.loads(content)
