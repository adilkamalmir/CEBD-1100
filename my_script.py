import sys


def convert(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return s


def check_for_headers (input_list):
    count = 0
    for item in input_list[0]:
        if type(item) == str:
            count += 1
    if count != len(input_list[0]):
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

# name_file = "housing.names"
# names = open(name_file, 'r')
# count = 0
# for line in names:
#     if line.find("Attribute Information") > -1 or line.find("Attribute information") > -1:
#         next(names)
#         for item in names:
#             # print (item.split())
#             if item.split() == [] and count > 0:
#                 break
#             elif item.split() == []:
#                 count += 1
#                 continue
#             elif item.split() == [] and count > 0:
#                 break
#             elif item.split()[0].find(".") > -1:
#                 print(item.split()[1])
#             elif item.split()[0].find(")") > -1:
#                 print(item.split()[1])
