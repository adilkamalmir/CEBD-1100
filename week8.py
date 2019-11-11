from sklearn.datasets import load_wine
import matplotlib.pyplot as plt
import numpy as np
import os
from collections import Counter


# function for creating pairs plots
def plot (output_dict, color_column, size_column, size_scale=None, size_min=None):
    if not os.path.exists("figures/color_{0}_size_{1}".format(color_column, size_column)):
        os.mkdir("figures/color_{0}_size_{1}".format(color_column, size_column))
    color = output_dict[color_column]
    unique_color = Counter(color)
    size = output_dict[size_column]
    if size_min:
        min_size = np.min(size)
        size = [(x-min_size) for x in size]
    if size_scale:
        size = [size_scale*x**x for x in size]
    else:
        size = [25*x for x in size]
    for idx_col1, column1 in enumerate(output_dict.keys()):
        for idx_col2, column2 in enumerate(output_dict.keys()):
            x = output_dict[column1]
            y = output_dict[column2]
            plt.figure()
            scatter = plt.scatter(x, y, c=color, s=size)
            # polynomial 1
            coefs = np.polyfit(x, y, 1)
            xs, new_line = generate_points(coefs, min(x), max(x))
            l1 = plt.plot(xs, new_line, 'tab:red', label='Order 1')
            # polynomial 2
            coefs = np.polyfit(x, y, 2)
            xs, new_line = generate_points(coefs, min(x), max(x))
            l2 = plt.plot(xs, new_line, 'tab:blue', label='Order 2')
            # polynomial 3
            coefs = np.polyfit(x, y, 3)
            xs, new_line = generate_points(coefs, min(x), max(x))
            l3 = plt.plot(xs, new_line, 'tab:green', label='Order 3')
            # polynomial 4
            coefs = np.polyfit(x, y, 4)
            xs, new_line = generate_points(coefs, min(x), max(x))
            l4 = plt.plot(xs, new_line, 'tab:orange', label='Order 4')
            plt.xlabel(column1)
            plt.ylabel(column2)
            plt.title("{0} x {1}".format(column1, column2))
            lg1 = plt.legend([l1[0], l2[0], l3[0], l4[0]], ['Order 1', 'Order 2', 'Order 3', 'Order 4'], loc="upper right", title="Polynomial Order")
            lg2 = plt.legend(handles=scatter.legend_elements()[0], labels=unique_color.keys(), loc="upper left", title=color_column)
            plt.gca().add_artist(lg1)
            plt.savefig("figures/color_{0}_size_{1}/{2}_x_{3}.png".format(color_column, size_column, column1.replace('/', '_'), column2.replace('/', '_')))
            plt.close()


# function for generating points to plot coefs line
def generate_points(coefs, min_val, max_val):
    xs = np.arange(min_val, max_val, (max_val-min_val)/100)
    return xs, np.polyval(coefs, xs)


def main():
    wine = load_wine()
    # load column headers, and add heading for cultivars
    list_of_col_names = wine.feature_names
    list_of_col_names.insert(0, "cultivars")
    # load data
    target = wine.target
    target = target.tolist()
    # add 1 to all target to make it like the .data file
    target = [x+1 for x in target]
    data = wine.data
    data = data.tolist()
    # combine target as column in data
    [data[idx].insert(0, target[idx]) for idx, item in enumerate(target)]
    # convert to dictionary
    output_dict = [[row[i] for row in data] for i in range(len(list_of_col_names))]
    output_dict = {list_of_col_names[idx]: item for idx, item in enumerate(output_dict)}

    # plotting
    plot(output_dict, "cultivars", "alcohol", 5, True)
    # plot(output_dict, "cultivars", "color_intensity")

if __name__ == "__main__":
    main()








