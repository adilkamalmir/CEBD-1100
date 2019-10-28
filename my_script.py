# The same is also available on GitHub at: https://github.com/adilkamalmir/python/blob/master/my_script.py
# The script takes the .data file as input in the first argument, you can optionally pass a .names file as a second
# argument but that only works for housing and breast-cancer-wisconsin data as best effort. In all other cases,
# the headers either come from .data file itself (if available) or just the column numbers are used
# (if headers not available in the data)

# Libraries
import argparse
import os
import csv
import matplotlib.pyplot as plt
import numpy as np
# from collections import Counter
# import seaborn as sns
# import pandas as pd


# setting appropriate data type
def convert(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s


# assuming if only first row is unique, they are headers
def check_for_headers (input_list):
    headers = 0
    first_row = [type(item) for item in input_list[0]]
    for cur_row in input_list:
        cur_row = [type(item) for item in cur_row]
        if cur_row == first_row:
            headers += 1
    if headers == 1:
        return input_list, headers
    else:
        input_list.insert(0, [str(x) for x in range(len(input_list[0]))])
        return input_list, headers


# Get headers from .names files (works only for housing and breast-cancer-wisconsin data)
def get_headers(headers_file):
    names = open(headers_file, 'r')
    count = 0
    headers_list = []
    for line in names:
        if line.find("Attribute Information") > -1 or line.find("Attribute information") > -1:
            next(names)
            for item in names:
                if item.split() == [] and count > 0:
                    break
                elif item.split() == []:
                    count += 1
                    if item.split() == [] and count > 0:
                        break
                    else:
                        continue
                elif item.split()[0].find(".") > -1:
                    headers_list += [item.split()[1]]
                elif item.split()[0].find(")") > -1:
                    headers_list += item.split()[1]
    return headers_list


# function for generating points to plot coefs line
def generate_points(coefs, min_val, max_val):
    xs = np.arange(min_val, max_val, (max_val-min_val)/100)
    return xs, np.polyval(coefs, xs)


def main(input_data_file, input_names_file):
    ############################################################################
    # parsing data without libraries
    input_file = (input_data_file)
    output_file = "output.tmp"
    data = open(input_file, 'r')
    output_list = []

    # Creating the output list
    for line in data:
        line = [convert(x) for x in line.replace(","," ").split()]
        output_list += [line]

    # Check if first row items are column headings or data
    output_list, headers = check_for_headers(output_list)
    list_of_col_names = output_list.pop(0)

    if input_names_file:
        list_of_col_names = get_headers(input_names_file)

    # Creating the output dictionary from the output list
    output_dict = [[row[i] for row in output_list] for i in range(len(list_of_col_names))]
    output_dict = {list_of_col_names[idx]:item for idx, item in enumerate(output_dict)}

    # Writing output to file
    with open(output_file, 'w') as file_out:
        file_out.write("output_list: %s\r\n output_dict: %s\r\n" % (output_list, output_dict))

    ############################################################################
    # using csv library
    with open('out.csv', 'w+') as output:
        data = open(input_file, 'r')
        if headers == 1:
            next(data)
        for line in data:
            output.write(','.join(line.split()))
            output.write("\n")
    output_dict_csv={}
    with open('out.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file, fieldnames=list_of_col_names)
        for row in csv_reader:
            for column, value in row.items():
                output_dict_csv.setdefault(column, []).append(convert(value))
    assert output_dict_csv == output_dict

    ############################################################################
    # plotting
    fig, axs = plt.subplots(len(output_dict.keys()), len(output_dict.keys()), figsize=(50,50))
    for idx_col1, column1 in enumerate(output_dict.keys()):
        for idx_col2, column2 in enumerate(output_dict.keys()):
            x = output_dict[column1]
            y = output_dict[column2]
            axs[idx_col1, idx_col2].scatter(x, y)
            axs[idx_col1, idx_col2].set(title="{0} x {1}".format(column1, column2), xlabel=column1, ylabel=column2)
            # polynomial 1
            coefs = np.polyfit(x, y, 1)
            xs, new_line = generate_points(coefs, min(x), max(x))
            l1 = axs[idx_col1, idx_col2].plot(xs, new_line, 'tab:red')
            # polynomial 2
            coefs = np.polyfit(x, y, 2)
            xs, new_line = generate_points(coefs, min(x), max(x))
            l2 = axs[idx_col1, idx_col2].plot(xs, new_line, 'tab:blue')
            # polynomial 3
            coefs = np.polyfit(x, y, 3)
            xs, new_line = generate_points(coefs, min(x), max(x))
            l3 = axs[idx_col1, idx_col2].plot(xs, new_line, 'tab:green')
            # polynomial 4
            coefs = np.polyfit(x, y, 4)
            xs, new_line = generate_points(coefs, min(x), max(x))
            l4 = axs[idx_col1, idx_col2].plot(xs, new_line, 'tab:cyan')
            # formatting
            box = axs[idx_col1, idx_col2].get_position()
            axs[idx_col1, idx_col2].set_position([box.x0, box.y0, box.width * 1.2 , box.height * 1.2])
    plt.tight_layout()
    fig.legend((l1[0], l2[0], l3[0], l4[0]), ('Order 1', 'Order 2', 'Order 3', 'Order 4'), 'upper left')
    plt.savefig("myfigure.png")

    # seaborne option
    # output_df = pd.DataFrame.from_dict(output_dict)
    # sns.pairplot(output_df, kind="reg")
    # plt.savefig("myfigure.png")

    return output_dict, output_dict_csv


if __name__ == "__main__":
    # Argument Parsing
    parser = argparse.ArgumentParser(description='Process provided data files')
    parser.add_argument('input_data_file', type=str,
                       help='an input data file')
    parser.add_argument('--input_names_file', '-n', type=str,
                       help='an input names file')
    args = parser.parse_args()

    if not os.path.exists(args.input_data_file):
        print("Input data file does not exist")
        exit()

    if args.input_names_file:
        if not os.path.exists(args.input_names_file):
            print("Input name file does not exist")
            exit()

    main(args.input_data_file, args.input_names_file)
