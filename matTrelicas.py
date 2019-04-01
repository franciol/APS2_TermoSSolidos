import numpy as np
import matplotlib.pyplot as plt

#Deslocamento           [m] metro
#Comprimento            [m] metro
#Forças/Reação          [N] Newton
#Tensão                 [Pa] Pascal
#Módulo de elasticidade [Pa] Pascal
#Área                   [m²] metro quadrado

nodes = []
elements = []
materials = []
restrictions = []
loads = []
deformations = []
tensions = []
ksElements = []
peFinal = []


def transposeMatrix(matrix):
    arrayCoordenates = 2*len(nodes)
    result = np.zeros((arrayCoordenates,arrayCoordenates))    
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            result[j][i] = matrix[i][j]
    return result

def calcDistNodes(node1,node2):
    xs = ((nodes[node1][0]-nodes[node2][0]))**2
    ys = ((nodes[node1][1]-nodes[node2][1]))**2
    return (xs+ys)**(1/2)

def cos(node1,node2):
    xs = ((nodes[node2][0]-nodes[node1][0]))
    l = calcDistNodes(node1,node2)
    return xs/l

def sen(node1,node2):
    ys = ((nodes[node2][1]-nodes[node1][1]))
    l = calcDistNodes(node1,node2)
    return ys/l


def newNode(x,y):
    nodes.append([x,y])

def newElement(inc1,inc2,area):
    elements.append([[inc1,inc2],calcDistNodes(inc1,inc2),area,cos(inc1,inc2),sen(inc1,inc2)])

def newMaterial(elasticidade,tracao,compressao):
    materials.append([elasticidade,tracao,compressao])

def newRestriction(node,restric):
    restrictions.append([node,restric])

def newLoad(node,direction,value):
    loads.append([node,direction,value])


def createKs():
    arrayCoordenates = 2*len(nodes)

    for actual in range(0,len(elements)):
        thisMatrix = np.zeros((arrayCoordenates,arrayCoordenates))

        node1 = elements[actual][0][0]
        node2 = elements[actual][0][1]

        freedom0 = node1*2
        freedom1 = node1*2+1
        freedom2 = node2*2
        freedom3 = node2*2+1
        free = [freedom0,freedom1,freedom2,freedom3]

        sin = elements[actual][3]
        cos = elements[actual][4]

        for xline in free:
            for yline in free:
                if(xline == yline and (xline == freedom0 or xline == freedom2) ):
                    thisMatrix[yline][xline] = sin**2

                elif(xline == yline and (xline == freedom1 or xline == freedom3) ):
                    thisMatrix[yline][xline] = cos**2

                elif( (xline==freedom0 and yline==freedom1) or (xline==freedom1 and yline==freedom0) or (xline==freedom3 and yline==freedom2) or (xline==freedom2 and yline==freedom3)):
                    thisMatrix[yline][xline] = cos*sin
                
                elif( (xline==freedom0 and yline==freedom2) or (xline==freedom2 and yline==freedom0) ):
                    thisMatrix[yline][xline] = (-1)*(sin**2)
                
                elif( (xline==freedom0 and yline==freedom3) or (xline==freedom3 and yline==freedom0) or (xline==freedom1 and yline==freedom2) or (xline==freedom2 and yline==freedom1)):
                    thisMatrix[yline][xline] = (-1)*(cos*sin)
                
                elif( (xline==freedom1 and yline==freedom3) or (xline==freedom3 and yline==freedom1) ):
                    thisMatrix[yline][xline] = (-1)*(cos**2)

        thisMatrix *= (materials[actual][0]*elements[actual][2]/elements[actual][1])

        ksElements.append(thisMatrix)
    

def calcMainMatrix():
    arrayCoordenates = 2*len(nodes)
    mainMatrix = np.zeros((arrayCoordenates,arrayCoordenates))
    
    for mat in ksElements:
        mainMatrix+=mat

    return mainMatrix


def globalVectorForces():
    arrayCoordenates = 2*len(nodes)
    pgzao = np.zeros((arrayCoordenates,1))
    listIdx = []


    for lod in loads:
        idx = 2*lod[0]+lod[1]
        pgzao[idx][0] = lod[2]
    

    for i in range(0,arrayCoordenates):
        a = 0
        for restrict in restrictions:
            if(restrict[0]*2+restrict[1]==i):
                a = 1
        if(a==0):
            listIdx.append(i)


    return pgzao,listIdx
                
def calcU(pg,idxs,matrix,numbOrNot):
    arrayCoordenates = 2*len(nodes)
    ixnbs = len(idxs)
    endMatrix = np.zeros((ixnbs,ixnbs))
    endPg = np.zeros((ixnbs,1))


    for i in range(0,ixnbs):
        endPg[i][0] = pg[idxs[i]][0]
        for j in range(0,ixnbs):
            endMatrix[i][j] = matrix[idxs[i]][idxs[j]]

    uJacobs,erro = jacobi(1000,0.01,endMatrix,endPg)
    
    endMatrix = np.matrix(endMatrix)
    endMatrix2 = np.linalg.pinv(endMatrix)
    
    
    u = endMatrix2 * endPg
    endU = np.zeros((len(pg),1))

    if(numbOrNot == 1):
        u = uJacobs

    for val in range(0,ixnbs):
        endU[idxs[val]] = u[val]
    
    pfinal = matrix * np.matrix((endU)) 

    #deformação
    for ele in range(0,len(elements)):
        u1 = endU[elements[ele][0][0]*2]
        u2 = endU[elements[ele][0][0]*2+1]
        u3 = endU[elements[ele][0][1]*2]
        u4 = endU[elements[ele][0][1]*2+1]
        lis = [u1,u2,u3,u4]
        preU = np.zeros((4,1))
        for ina in range(0,4):
            preU[ina][0] = lis[ina]



        preDef = np.matrix([-elements[ele][3],-elements[ele][4],elements[ele][3],elements[ele][4]]) * preU 
        pe = np.zeros((4,1))
        for js in range(0,4):    
            if(js%2==0):
                pe[js][0] = pfinal[elements[ele][0][js//2]*2]
            else:
                pe[js][0] = pfinal[(elements[ele][0][js//2]*2)+1]
        peFinal.append(pe)

        deformation = (1/elements[ele][1])*preDef
        tension = materials[ele][0]*deformation

        deformations.append([deformation])
        tensions.append([tension])

    reaction_forces = []
    for i in range(0,arrayCoordenates):
        a = 0
        for restrict in restrictions:
            if(restrict[0]*2+restrict[1]==i):
                a = 1
        if(a==1):
            reaction_forces.append([pfinal[i][0],i%2])

    return endU,reaction_forces, deformations, tensions

def calcFinal(numbOrNot):
    createKs()

    matrix = calcMainMatrix()
    pg,listIdx = globalVectorForces()   


    return calcU(pg,listIdx,matrix,numbOrNot)



def jacobi(ite,tol,K,F):
    x = np.zeros((len(K),1))
    for alter in range(len(K)):
        x[alter][0] = np.random.randint(0,1000)
    x1 = np.zeros((len(K),1))
    for interacoes in range(0,ite):
        soma = np.dot(K,x)
        erroMax = 0
        
        deltaEXTERNO = 0
        deltaIdx = 0

        for lines in range(0,len(K)):
            x1[lines] = (F[lines] - (soma[lines]-(x[lines]*K[lines][lines]) ) )/K[lines][lines]
            if(deltaEXTERNO < np.abs(x1[lines]-x[lines])):
                deltaIdx = lines
                deltaEXTERNO = np.abs(x1[lines]-x[lines])
        
        erroMax = np.abs((deltaEXTERNO)/x1[lines])
        for ksk in range(0,len(x)):
            x[ksk] = x1[ksk]
        if (erroMax<=tol):
            print("Interações: ",interacoes)
            print("Erro max = ",float(erroMax))
            return x,erroMax
    return x,erroMax





def printAndPlot(displacement,reaction,deformations,stress):
    print("-------------------------------------")
    print("Vetor de Deslocamento Nodal [m]")
    for i in range(0,len(nodes)):
        print(i+1,float(displacement[i*2][0]),float(displacement[i*2+1][0]))
    print("-------------------------------------")
    for j in range(0,len(reaction)):
        print("Reação de apoio no nó ",j+1," [N]")
        print(float(reaction[j][0]),int(reaction[j][1]))
    print("-------------------------------------")
    print("Tensão em cada elemento [Pa]")
    for ji in range(0,len(stress)):
        print(ji+1,float(stress[ji][0]))
    print("-------------------------------------")
    print("Deformação longitudinal específica de cada elemento")
    for ij in range(0,len(deformations)):
        print(ij+1,float(deformations[ij][0]))
