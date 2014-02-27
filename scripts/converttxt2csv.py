#convert txt files to consistent csv files
import glob

class Votante:
    def __init__(self):
        self.nombre = ''
        self.rut = 0
        self.dv = ''
        self.sexo = ''
        self.direccion = ''
        self.circunscripcion = ''
        self.mesa = ''
        self.region = ''
        self.comuna = ''

    def __str__(self):
        return '%s;%i;%s;%s;%s;%s;%s;%s;%s' % (self.nombre, self.rut , self.dv, self.sexo, self.direccion, self.circunscripcion, self.mesa, self.region, self.comuna)


#for file in txt folder
for filepath in glob.glob('txts/txtsample/*.txt'):
    f = open(filepath)
    for line in f:
        print line







