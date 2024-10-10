# import external libraries
import random
# store random value into cube
def iniCubo(cb):
    for fil in range(5):
        for col in range(5):
            for pro in range(5):
                cb[fil][col][pro] = random.randint(1, 100)
# print cube function
def impCubo(cb):
 for fil in range(5):
 for col in range(5):
 print('[F{0}:C{1}] ==> '.format(fil, col), end="")
 for pro in range(5):
 print('[{0:>3}]'.format(cb[fil][col][pro]), end="")
 print()
 print('=====================================')
# declare data cube with format [5,5,5]
cubo = [[[0 for pro in range(5)] for col in range(5)] for fil in range(5)]
# call cube functions
iniCubo(cubo)
impCubo(cubo)