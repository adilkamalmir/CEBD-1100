import sys


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
        return input_list
    else:
        input_list.insert(0, list(range(len(input_list[0]))))
        return input_list


input_file = (sys.argv[1])
output_file = "output.data"
data = open(input_file, 'r')
output_list = []

# Creating the output list
for line in data:
    line = [convert(x) for x in line.replace(","," ").split()]
    output_list += [line]

# Check if first row items are column headings or data
output_list = check_for_headers(output_list)
list_of_col_names = output_list.pop(0)

# Creating the output dictionary from the output list
output_dict = [[row[i] for row in output_list] for i in range(len(list_of_col_names))]
output_dict = {list_of_col_names[idx]:item for idx, item in enumerate(output_dict)}

# Writing output to file
with open(output_file, 'w') as file_out:
    file_out.write("output_list: %s\r\n output_dict: %s\r\n" % (output_list, output_dict))
    file_out.close()
