#def da funcao
def entradas():
    filename=input("nome do arquivo: ")
    file=open(filename,"r+")
    linhas=file.readlines()
    arquivo=file.read()

    filename="variaveis.fem"
    file=open(filename,"r+")
    tipos=file.readlines()
    t=range(len(linhas))
    contador=0
    cord,ele,inc,mat,geo,bcn,loads=[],[],[],[],[],[],[]

    #for *COORDINATES
    for i in t:
        if linhas[i] == tipos[0]:
            x=int(linhas[i+1])
            for j in range(x):
                y=linhas[i+2+j]
                a=y.split()
                ponto=[]
                ponto.append(float(a[1]))
                ponto.append(float(a[2]))
                cord.append(ponto)
    #for *ELEMENT_GROUPS
    for i in t:
        if linhas[i] == tipos[1]:
            x=int(linhas[i+1])
            for j in range(x):
                y=linhas[i+2+j]
                a=y.split()
                ponto=[]
                ponto.append(float(a[0]))
                ponto.append(float(a[1]))
                ponto.append(a[2])
                ele.append(ponto)
                contador+=(int(a[1]))
    #for *INCIDENCES
    for i in t:
        if linhas[i] == tipos[2]:
            for j in range(contador):
                y=linhas[i+1+j]
                a=y.split()
                ponto=[]
                ponto.append(float(a[0]))
                ponto.append(float(a[1]))
                ponto.append(float(a[2]))
                inc.append(ponto)
    #for *MATERIALS
    for i in t:
        if linhas[i] == tipos[3]:
            x=int(linhas[i+1])
            for j in range(x):
                y=linhas[i+2+j]
                a=y.split()
                ponto=[]
                ponto.append(float(a[0]))
                ponto.append(float(a[1]))
                ponto.append(float(a[2]))
                mat.append(ponto)
    #for *GEOMETRIC_PROPERTIES
    for i in t:
        if linhas[i] == tipos[4]:
            x=int(linhas[i+1])
            for j in range(x):
                y=linhas[i+2+j]
                geo.append(float(y))
    #for *BCNODES
    for i in t:
        if linhas[i] == tipos[5]:
            x=int(linhas[i+1])
            for j in range(x):
                y=linhas[i+2+j]
                a=y.split()
                ponto=[]
                ponto.append(float(a[0]))
                ponto.append(float(a[1]))
                bcn.append(ponto)
    #for *LOADS
    for i in t:
        if linhas[i] == tipos[6]:
            x=int(linhas[i+1])
            for j in range(x):
                y=linhas[i+2+j]
                a=y.split()
                ponto=[]
                ponto.append(float(a[0]))
                ponto.append(float(a[1]))
                ponto.append(float(a[2]))
                loads.append(ponto)

    return cord,ele,inc,mat,geo,bcn,loads

#teste da funcao
"""a,b,c,d,e,f,g=entradas()
#print(f)
print("A--------------")
print(a)
print("B--------------")
print(b)
print("C--------------")
print(c)
print("D--------------")
print(d)
print("E--------------")
print(e)
print("F--------------")
print(f)
print("G--------------")
print(g)"""