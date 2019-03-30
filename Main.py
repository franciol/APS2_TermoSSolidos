import matTrelicas as mt
import leitor
import numpy as np


def main():
#   |    a      |    b      |    c   |   d    |    e     |    f  |  g  |
    coordernadas, elementos, indices, material, geometria, nodes, loads = leitor.entradas()

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

    displacement,reaction,deformations,stress = mt.calcFinal()
    mt.printAndPlot(displacement,reaction,deformations,stress)


main()