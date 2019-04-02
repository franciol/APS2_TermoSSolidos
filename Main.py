import matTrelicas as mt
import leitor
import numpy as np
import escritor


def main():
#   |    a      |    b      |    c   |   d    |    e     |    f  |  g  |
    coordernadas, elementos, indices, material, geometria, nodes, loads = leitor.entradas()
    numbOrNot = input("Calculo numérico pelo método de Jacobi?  sim(1)  não(0) ")

    for i in range(len(coordernadas)):
        #print(int(coordernadas[i][0]))
        #print(int(coordernadas[i][1]))
        mt.newNode(coordernadas[i][0], coordernadas[i][1])
    
    for i in range(len(indices)):
        #print(int(indices[i][1]-1))
        #print(int(indices[i][2]-1))
        #print(geometria)
        #print(geometria[0])
        mt.newElement(int(indices[i][1]-1), int(indices[i][2]-1), geometria[0])
    
    for i in range(len(indices)):
        #print(material[0][0])
        #print(material[0][1])
        #print(material[0][2])
        mt.newMaterial(material[0][0], material[0][1], material[0][2])

    for i in range(len(nodes)):
        #print(int(nodes[i][0]-1))
        #print(int(nodes[i][1]-1))
        mt.newRestriction(int(nodes[i][0]-1), int(nodes[i][1]-1))

    for i in range(len(loads)):
        #print(int(loads[i][0]-1))
        #print(int(loads[i][1]-1))
        #print(int(loads[i][2]-1))
        mt.newLoad(int(loads[i][0]-1), int(loads[i][1]-1), int(loads[i][2]-1))
    displacement,reaction,deformations,stress = mt.calcFinal(numbOrNot)
    escritor.saidas(displacement,reaction,deformations,stress)

    tensAd = float(input("Tensão Admissível: "))
    isOk,red = mt.redimencionamento(tensAd)
    
    try:
        if(not isOk):    
            for maxInt in range(800):
                displacement2,reaction2,deformations2,stress2 = mt.calcFinal(numbOrNot)
                isOk,red = mt.redimencionamento(tensAd)
                if(isOk):
                    print("isOK")
                    break
            
        if(not isOk):
            print("Não foi possivel recalcular as áreas de forma completa")

    finally:
        if(isOk):
            for reds in range(len(red)):
                if red[reds] != 0:
                    print("Para o elemento de id ",reds+1," a área transversal da barra deveria redimencionar para ",red[reds]," m^2")
        
    #mt.printAndPlot(displacement,reaction,deformations,stress)

    

main()