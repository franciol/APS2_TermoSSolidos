#def da função
def saidas(disp,rea,stra,stre):
    saida= open("arquivoSaida.out","w+")
    saida.write("*DISPLACEMENTS\n")
    for i in range(int(len(disp)/2)):
        a=str(i+1) + " " + str(disp[i*2]) + " " + str(disp[i*2+1]) + "\n"
        saida.write(a)
    saida.write("\n")
    saida.write("*REACTION_FORCES\n")
    for i in range(len(rea)):
        if rea[i][0] == 0:
            b="FX"
        else:
            b="FY"
        a=str(i+1) + " " + b + " " + str(rea[i][1]) + "\n"
        saida.write(a)
    saida.write("\n")
    for i in range(len(stra)):
        a=str(i+1) + " " + str(float(stra[i][0])) + "\n"
        saida.write(a)
    saida.write("\n")
    for i in range(len(stre)):
        a=str(i+1) + " " + str(float(stre[i][0])) + "\n"
        saida.write(a)
    saida.write("\n")


    saida.close()
