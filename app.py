from wit_fwi import WIT_FWI
from wit_fwi_diff import WIT_FWI_DIFF
from wis import generate_frequent_itemsets
import timeit
from read_data import read_data, transform_to_data

min_support = [1, 2, 3, 4, 5]
database = [
    {'Beer': 3, 'Sausage': 2, 'Egg': 1},
    {'Beer': 1, 'Durian': 2, 'Yaourt': 2},
    {'Beer': 2, 'Durian': 3, 'Yaourt': 2, 'Beef': 1},
    {'Durian': 1, 'Yaourt': 2, 'Beef': 2}
]

runtime_WITs = []
runtime_WIT_DIFFs = []
runtime_WISs = []
for i in min_support:
    runtime_WIT = timeit.timeit('WIT_FWI(database, i)', globals=globals(), number=1)
    runtime_WIT_DIFF = timeit.timeit('WIT_FWI_DIFF(database, i)', globals=globals(), number=1)
    runtime_WIS = timeit.timeit('generate_frequent_itemsets(database, i)', globals= globals(), number=1)

    runtime_WITs.append(runtime_WIT)
    runtime_WIT_DIFFs.append(runtime_WIT_DIFF)
    runtime_WISs.append(runtime_WIS)


import matplotlib.pyplot as plt
plt.plot(min_support, runtime_WITs, 'red')
plt.plot(min_support, runtime_WIT_DIFFs, 'blue')
plt.plot(min_support, runtime_WISs, 'yellow')
plt.xlabel('min_supports')
plt.ylabel('Runtimes')
plt.title('Compare Algorithms')
plt.legend()
plt.show()

