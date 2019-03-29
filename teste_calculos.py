import matTrelicas as mt
import numpy as np

def teste1():
    mt.newNode(0,0)
    mt.newNode(0,0.4)
    mt.newNode(0.3,0.4)

    mt.newElement(0,1,2e-4)
    mt.newElement(1,2,2e-4)
    mt.newElement(2,0,2e-4)

    mt.newMaterial(210e9,1570e6,1570e6)
    mt.newMaterial(210e9,1570e6,1570e6)
    mt.newMaterial(210e9,1570e6,1570e6)

    mt.newRestriction(0,0)
    mt.newRestriction(1,0)
    mt.newRestriction(1,1)

    mt.newLoad(2,0,150)
    mt.newLoad(2,1,-100)

    
    displacement,reaction,deformations,stress = mt.calcFinal()
    mt.printAndPlot(displacement,reaction,deformations,stress)


    
def teste2():
    mt.newNode(0,0)
    mt.newNode(0,21)
    mt.newNode(21,0)
    mt.newNode(21,21)

    mt.newElement(0,1,1)
    mt.newElement(0,2,1)
    mt.newElement(2,3,1)
    mt.newElement(1,3,1)
    mt.newElement(1,2,2**(1/2))
    mt.newElement(0,3,2**(1/2))

    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)

    mt.newLoad(3,1,-9806)

    mt.newRestriction(0,0)
    mt.newRestriction(0,1)
    mt.newRestriction(1,0)
    mt.newRestriction(1,1)
    
    

    displacement,reaction,deformations,stress = mt.calcFinal()
    mt.printAndPlot(displacement,reaction,deformations,stress)


def teste3():
    mt.newNode(0,0)
    mt.newNode(2,0)
    
    mt.newElement(0,1,0.02)
    mt.newMaterial(200e9,1570e6,1570e6)

    mt.newRestriction(0,0)
    mt.newRestriction(0,1)

    mt.newLoad(1,0,50e3)

    displacement,reaction,deformations,stress = mt.calcFinal()
    mt.printAndPlot(displacement,reaction,deformations,stress)

def teste4():

    K = np.array(([[1.59,-0.4,-0.54],[-0.4,1.7,0.4],[-0.54,0.4,0.54]]))


    Fs =np.array(([[0],[150],[-100]]))

    jac = mt.jacobi(1000,0.000001,10e8*K,Fs)

    print("U = \n",jac)

def teste5():
    mt.newNode(0,0)
    mt.newNode(3,0)
    mt.newNode(6,0)
    mt.newNode(9,0)
    mt.newNode(12,0)
    mt.newNode(3,3)
    mt.newNode(6,3)
    mt.newNode(9,3)
    mt.newNode(12,3)
    mt.newNode(6,6)
    mt.newNode(9,6)
    mt.newNode(12,6)
    mt.newNode(9,9)
    mt.newNode(12,9)

    mt.newElement(0,1,0.0225)
    mt.newElement(1,2,0.0225)
    mt.newElement(2,3,0.0225)
    mt.newElement(3,4,0.0225)
    mt.newElement(0,5,0.0225)
    mt.newElement(1,5,0.0225)
    mt.newElement(1,6,0.0225)
    mt.newElement(2,6,0.0225)
    mt.newElement(3,6,0.0225)
    mt.newElement(3,7,0.0225)
    mt.newElement(3,8,0.0225)
    mt.newElement(4,8,0.0225)
    mt.newElement(5,6,0.0225)
    mt.newElement(6,7,0.0225)
    mt.newElement(7,8,0.0225)
    mt.newElement(5,9,0.0225)
    mt.newElement(6,9,0.0225)
    mt.newElement(6,10,0.0225)
    mt.newElement(7,10,0.0225)
    mt.newElement(8,10,0.0225)
    mt.newElement(8,11,0.0225)
    mt.newElement(9,12,0.0225)
    mt.newElement(10,12,0.0225)
    mt.newElement(11,12,0.0225)
    mt.newElement(11,13,0.0225)
    mt.newElement(9,10,0.0225)
    mt.newElement(10,11,0.0225)
    mt.newElement(12,13,0.0225)

    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    mt.newMaterial(2e11,1570e6,1570e6)
    
    mt.newRestriction(0,0)
    mt.newRestriction(0,1)
    mt.newRestriction(1,1)
    mt.newRestriction(2,1)
    mt.newRestriction(3,1)
    mt.newRestriction(4,0)
    mt.newRestriction(4,1)
    

    mt.newLoad(5,1,30000)
    mt.newLoad(9,1,30000)
    mt.newLoad(12,1,30000)
    mt.newLoad(13,1,30000)
    mt.newLoad(5,1,30000)
    mt.newLoad(11,0,24000)
    mt.newLoad(13,0,24000)


    displacement,reaction,deformations,stress = mt.calcFinal()
    mt.printAndPlot(displacement,reaction,deformations,stress)
    

    
teste1()