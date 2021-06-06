import sys, os

for p in sys.path:
    print(p)
    if 'Documentos' in p:
        path = p
    
print(path)