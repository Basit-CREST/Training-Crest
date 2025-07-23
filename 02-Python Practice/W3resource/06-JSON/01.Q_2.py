object = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}

import json

dic = json.dumps(object)
print(dic)
print(type(dic))