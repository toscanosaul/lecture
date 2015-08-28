import numpy as np
from matplotlib import pyplot as plt
import sys


def idealizedSpeedUp(NumberCores,serialFraction):
    x=np.linspace(1,NumberCores,NumberCores)
    y=1.0/(serialFraction+(1.0-serialFraction)/x)
    fig=plt.figure()
    plt.plot(x,y)
    plt.title("Idealized Speed Up")
    plt.xlabel('Number of Cores')
    plt.ylabel('Idealized Speedup')
    plt.savefig("idealizedSpeedUp.pdf")
    plt.close(fig)
    
def parallelEfficiency(NumberCores,serialFraction):
    x=np.linspace(1,NumberCores,NumberCores)
    y=1.0/(x*serialFraction+(1.0-serialFraction))
    fig=plt.figure()
    plt.plot(x,y)
    plt.title("Parallel Efficiency")
    plt.xlabel('Number of Cores')
    plt.ylabel('Parallel Efficiency')
    plt.savefig("parallelEfficiency.pdf")
    plt.close(fig)


numberCores=int(sys.argv[1])
serialFraction=float(sys.argv[2])

idealizedSpeedUp(numberCores,serialFraction)
parallelEfficiency(numberCores,serialFraction)















