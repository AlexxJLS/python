import numpy as np

carros = np.array(["VW","Ford","Ferrari"])

tuplos = (carros,)
print(type(tuplos))
print(tuplos[0][2])
print(tuplos)