# The same is also available on GitHub at: https://github.com/adilkamalmir/python/blob/master/my_script.py
# The script takes the .data file as input in the first argument, you can optionally pass a .names file as a second
# argument but that only works for housing and breast-cancer-wisconsin data as best effort. In all other cases,
# the headers either come from .data file itself (if available) or just the column numbers are used
# (if headers not available in the data)

# Libraries
import argparse
import os
import sys
import csv
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter


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


# function for creating pairs plots
def pairsplot (output_dict):
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


# Function to check if given data is discrete or not
def check_if_discrete(data):
    discrete_percentage = 0.10
    total_number = len(data)
    unique_data = Counter(data)
    unique_number = len(unique_data.keys())
    unique_percentage = unique_number/total_number
    return True if unique_percentage <= discrete_percentage else False


# Function to compile summary of given data
def summary(output_dict, column):
    try:
        data = output_dict[column]
        print("Summary for %s:" % column)
        min = np.min(data)
        print("Min: %s" % min)
        max = np.max(data)
        print("Max: %s" % max)
        mean = np.mean(data)
        print("Mean: %s" % mean)
        sd = np.std(data)
        print("Standard Deviation: %s" % sd)
        check_if_discrete(data)
        discrete = check_if_discrete(data)
        print("Discrete Data: %s" % discrete)
        return min, max, mean, sd

    except KeyError:
        print("Oops! %s is not a valid column name for this data set" % column)
        exit(1)


# Function to check if given headers is in data
def is_column(data, column):
    try:
        data[column]
        return True
    except KeyError:
        return False


# Function for interpolation
def interpolate(output_dict, column1, column2, column1_val):
    if column1 == column2:
        print("Hey! You provided the same column name twice!")
        exit(1)
    elif not is_column(output_dict, column1) or not is_column(output_dict, column2):
        print("Hey! One of your columns names is not valid!")
        exit(1)
    elif type(convert(column1_val)) != type(output_dict[column1][0]):
        print("Hey! the value your provided is not the same type as \'%s\' data" % column1)
        exit(1)
    elif convert(column1_val) < np.min(output_dict[column1]) or convert(column1_val) > np.max(output_dict[column1]):
        print("Hey! the value your provided is not within range of \'%s\', try using the --summary option" % column1)
        exit(1)
    elif check_if_discrete(output_dict[column1]) or check_if_discrete(output_dict[column2]):
        print("Hey! One of your provided columns does not have continuous data therefore can not interpolate")
        exit(1)
    else:
        print("Interpolation Result:")
        x = output_dict[column1]
        y = output_dict[column2]
        # polynomial 1
        l1 = np.polyfit(x, y, 1)
        l1_val = np.polyval(l1, convert(column1_val))
        print("Order 1 value: %s" %l1_val)
        # polynomial 2
        l2 = np.polyfit(x, y, 2)
        l2_val = np.polyval(l2, convert(column1_val))
        print("Order 2 value: %s" %l2_val)
        # polynomial 3
        l3 = np.polyfit(x, y, 3)
        l3_val = np.polyval(l3, convert(column1_val))
        print("Order 3 value: %s" %l3_val)


def main():
    # Argument Parsing
    parser = argparse.ArgumentParser(description='Process provided data files')

    parser.add_argument('input_data_file', type=str,
                       help='an input data file')

    parser.add_argument('--input_names_file', '-n', type=str,
                       help='an input names file')

    parser.add_argument('--summary', '-s', type=str,
                        help='provide a column name to generate summary')

    parser.add_argument('-i', '--interpolate', nargs='+', help='to interpolate, provide two column names and a value for the first column (in this order)')

    parser.add_argument('--plot', '-p', action='store_true', help='set flag to generate pairs plot')

    args = parser.parse_args()

    if not os.path.exists(args.input_data_file):
        print("Input data file does not exist")
        exit()

    if args.input_names_file:
        if not os.path.exists(args.input_names_file):
            print("Input name file does not exist")
            exit()

    ############################################################################
    # parsing data without libraries
    input_file = (args.input_data_file)
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

    if args.input_names_file:
        list_of_col_names = get_headers(args.input_names_file)

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

    ############################################################################
    # plotting
    if args.plot:
        pairsplot(output_dict)

    ############################################################################
    # column summary
    if args.summary:
        summary(output_dict, args.summary)
    ############################################################################
    # interpolate
    if args.interpolate:
        try:
            if len(args.interpolate) != 3:
                print("Bummer! For interpolate you need to provide exactly 3 arguments, check help!")
                exit(1)
            else:
                interpolate(output_dict, args.interpolate[0], args.interpolate[1], args.interpolate[2])
        except IndexError:
            print("Bummer! For interpolate you need to provide exactly 3 arguments, check help!")
            exit(1)


    return output_dict, output_dict_csv


if __name__ == "__main__":
    main()
