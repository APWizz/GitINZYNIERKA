import meshio

input_stl_file = r"C:\Users\adria\Desktop\Inzynierka\Pręt_test.stl"
output_obj_file = 'nowy.obj'

mesh = meshio.read(input_stl_file)
meshio.write(output_obj_file, mesh, file_format='obj')
