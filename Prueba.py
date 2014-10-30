import urllib2



def sumaDos():
    print 10*20

def division(a,b):
    result=a/b
    print result

def cast():
    i=10
    f=10.5
    
    int(10.6)
    print "Funcion: "



def main():
    sumaDos()
    division(10, 20)

class Estudiante(object):
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
    def hola(self):
        return self.nombre
    def esMayor(self):
        if self.edad>=18:
            return True
        else:
            return False

def EXCEPTION():
    try:
        3/0
    except Exception:
        print "Error"

def main():
    e=Estudiante("K", 20)
    print "Hola %s" % e.hola()
    if e.esMayor():
        print "Es mayor de edad"
    else:
        print "No es mayor de edad"

    contador=0
    while contador<=10:
        print contador
        contador +=1

    EXCEPTION()



def getWeb():
    try:
        web = urllib2.urlopen("http://itjiquilpan.edu.mx/")
        print web.read()
        web.close()
    except urllib2.HTTPError, e:
        print e
    except urllib2.URLError as e:
        print e

def main():
    getWeb()

if __name__ == "__main__":
    main()



