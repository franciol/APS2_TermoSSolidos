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

    kk = (10^8) * np.array([
    [1.59,-0.4,-0.54],
    [-0.4,1.7,0.4],
    [-0.54,0.4,0.54]
    ])


    Fs =np.array([[0],[150],[-100]])

    jac = mt.jacobi(10000000000,0.0000001,kk,Fs)

    print("Erro Calculado: ",jac[1],"\n")
    print("U = ",jac[0])

    
teste2()