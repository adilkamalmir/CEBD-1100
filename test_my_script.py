import my_script
import os

def test_my_script():
    output_dict, output_dict_csv = my_script.main("hwk4_data/diabetes.data", None)
    num_lines = sum(1 for line in open('hwk4_data/diabetes.data'))
    # test 1: verify that both manually create dictionary and from csv library are same
    assert output_dict_csv == output_dict
    # test 2: verify output dictionary has the same number of items as input data file
    for item in output_dict.keys():
        assert len(output_dict[item]) == num_lines-1
    # test 3: verify that the output figure is created
    # assert os.path.exists('myfigure.png')
