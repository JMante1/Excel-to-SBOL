import utils.converter_function as cf
import os

cwd = os.getcwd()
file_name = 'CIDAR_extension_kit_vol1_KWK_v005tem_v002'
file_path_in = os.path.join(cwd, 'excel2sbol', 'tests', 'test_files',
                            f'{file_name}.xlsx')
file_path_out = os.path.join(cwd, 'excel2sbol', 'tests', 'test_files',
                             f'{file_name}.xml')

cf.converter('excel2bol_darpa_template_blank_v006_20210405.xlsx',
             file_path_in, file_path_out)