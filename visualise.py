from matplotlib_venn import venn3
import matplotlib.pyplot as plt
import os
print("cwd:", os.getcwd())

set_a = {1, 2, 3, 4, 5}
set_b = {3, 4, 5, 6, 7}
set_c = {5, 6, 7, 8, 9}

venn3([set_a, set_b, set_c], set_labels=('Desirable', 'Viable & Feasible', 'Responsible'))
plt.savefig("venn.png")

print("ran")