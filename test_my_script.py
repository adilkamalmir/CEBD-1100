import my_script
import os

def test_my_script():
    output_dict, output_dict_csv = my_script.main("hwk4_data/diabetes.data", None)
    assert output_dict_csv == output_dict
    assert os.path.exists('myfigure.png')
