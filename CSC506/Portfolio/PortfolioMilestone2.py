from DynamicTimeWarping import *
import matplotlib.pyplot as plt
import time
from fastdtw import fastdtw
from scipy.spatial.distance import euclidean
import seaborn as sbn
import matplotlib as mpl

# time1 = np.linspace(start=0, stop=1, num=50)
# time2 = time1[0:40]
# a = 3 * np.sin(np.pi * time1) + 1.5 * np.sin(4*np.pi * time1)
# b = 3 * np.sin(np.pi * time2 + 0.5) + 1.5 * np.sin(4*np.pi * time2 + 0.5) 
main_sample = [7, 1, 2, 5, 9]
b = [1, 8, 0, 4, 4, 2, 0]
c = [1, 5, 3, 6, 2, 2, 3, 2, 2]
d = [7, 7, 2, 2, 5, 10] 
e = [6, 7, 2, 1, 5, 8, 8]
f = [8, 2, 3, 6, 10]
g = [7, 7, 1, 1, 2, 2, 5, 5, 9, 9]
h = [6, 7, 1, 2, 2, 3, 5, 6, 9, 10]


samples = [b, c, d, e, f, g, h]
fig, axs = plt.subplots(len(samples))

for i in range(len(samples)):

    start = time.time()
    cost_cos, path = cost(main_sample, samples[i])
    end = time.time()

    print("Time to run: " + str(end - start))
    print("DTW Cost: " + str(cost_cos))

    fig.subplots_adjust(hspace= 0.5)

    main_sample_time = np.arange(0, len(main_sample))
    sample_time = np.arange(0, len(samples[i]))

    #DTW
    samples[i] = np.array(samples[i])
    axs[i].plot(main_sample_time, main_sample)
    axs[i].plot(sample_time, samples[i] + max(main_sample) + 1)
    axs[i].set_title("Dynamic Time Warping Mapping")

    for j in range(1, len(path)-1):
        axs[i].plot([path[j][0]-1, path[j][1]-1], [main_sample[path[j][0]-1], samples[i][path[j][1]-1] + max(main_sample) + 1],'-k')

#Euclidean distance
# axs[1].plot(d, b)
# axs[1].plot(c, a)
# axs[1].set_title("Euclidean Mapping")
# for i in range(min(len(a), len(b))):
#     axs[1].plot([i, i],[a[i], b[i]], 'k-')





# cost_matrix = gen_cost_matrix(b, a)

# fig, ax = plt.subplots(figsize=(6, 4))
# ax = sbn.heatmap(cost_matrix, annot=True, square=True, linewidths=0.1, cmap="YlGnBu", ax=ax, vmin=0, vmax=200)
# ax.invert_yaxis()

# # Get the warp path in x and y directions
# path_x = [p[0] for p in warp_path]
# path_y = [p[1] for p in warp_path]

# # Align the path from the center of each cell
# path_xx = [x+0.5 for x in path_x]
# path_yy = [y+0.5 for y in path_y]

# ax.plot(path_xx, path_yy, color='blue', linewidth=1, alpha=0.2)
#     
plt.show()