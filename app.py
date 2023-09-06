from wit_fwi import WIT_FWI
from wit_fwi_diff import WIT_FWI_DIFF
from wis import wis_algorithm
from warm import generate_association_rules
from read_data import read_data, transform_to_data
import timeit

# min_support = [0.5, 1, 1.5, 2, 2.5, 3]
min_support = [150, 160, 170, 180, 190]
min_confidence = 1
# database = [
#     {'Beer': 3, 'Sausage': 2, 'Egg': 1},
#     {'Beer': 1, 'Durian': 2, 'Yaourt': 2},
#     {'Beer': 2, 'Durian': 3, 'Yaourt': 2, 'Beef': 1},
#     {'Durian': 1, 'Yaourt': 2, 'Beef': 2}
# ]

from sklearn.model_selection import train_test_split
data = read_data('./data/chess.dat.txt')
database = transform_to_data(data)
train_data, test_data = train_test_split(database, test_size=0.01)

runtime_WITs = []
runtime_WIT_DIFFs = []
runtime_WISs = []
runtime_WARMs = []
for i in min_support:
    runtime_WIT = timeit.timeit('WIT_FWI(test_data, i)', globals=globals(), number=1)
    runtime_WIT_DIFF = timeit.timeit('WIT_FWI_DIFF(test_data, i)', globals=globals(), number=1)
    runtime_WIS = timeit.timeit('wis_algorithm(test_data, i)', globals= globals(), number=1)
    runtime_WARM = timeit.timeit('generate_association_rules(test_data, i, min_confidence)', globals=globals(), number=1)

    runtime_WITs.append(runtime_WIT)
    runtime_WIT_DIFFs.append(runtime_WIT_DIFF)
    runtime_WISs.append(runtime_WIS)
    runtime_WARMs.append(runtime_WARM)


import matplotlib.pyplot as plt
plt.plot(min_support, runtime_WITs, 'red', marker='o', label='WIT')
plt.plot(min_support, runtime_WIT_DIFFs, 'blue', marker='o', label='WIT-DIFF')
plt.plot(min_support, runtime_WISs, 'yellow', marker='o',label='WIS')
plt.plot(min_support, runtime_WARMs, 'black', marker='o' ,label='WARM')
plt.xlabel('min_supports')
plt.ylabel('Runtimes')
plt.title('Compare Algorithms with Chess Data')
plt.legend()
plt.show()

