import types
class C:
    def x():
        return 1
    def y():
        return 1    
        
def b():
    return 2

print(isinstance(C().x, types.MethodType))
print(isinstance(C().y, types.MethodType))
print(isinstance(b, types.MethodType))
print(isinstance(max, types.MethodType))
print(isinstance(abs, types.MethodType))
print(isinstance(b,types.FunctionType))
print(isinstance(lambda x : x , types.FunctionType))
print(isinstance(lambda x : x , types.LambdaType))
print(isinstance(max,types.FunctionType))
print(isinstance(max,types.LambdaType))

