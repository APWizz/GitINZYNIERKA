import vtk
import meshio

def convert_stl_to_obj(input_stl_file, output_obj_file):                # definiuje funkcje do konwersji formatu pliku
    mesh = meshio.read(input_stl_file)                                  # Wczytaj plik STL
    meshio.write(output_obj_file, mesh, file_format='obj')              # Zapisz siatkę do formatu OBJ


def render_obj_file(output_obj_file):                                     # definiuje funkcje do wyświetlania bryly
    reader = vtk.vtkOBJReader()                                         # Wczytaj plik OBJ
    reader.SetFileName(output_obj_file)
    reader.Update()
    mapper = vtk.vtkPolyDataMapper()                                    # Utwórz aktora na podstawie wczytanych danych
    mapper.SetInputData(reader.GetOutput())
    actor = vtk.vtkActor()
    actor.SetMapper(mapper)
    renderer = vtk.vtkRenderer()                                        # Utwórz renderer i dodaj aktora do niego
    renderer.AddActor(actor)
    render_window = vtk.vtkRenderWindow()                               # Utwórz okno renderowania
    render_window.AddRenderer(renderer)
    render_window_interactor = vtk.vtkRenderWindowInteractor()          # Utwórz interakcję
    render_window_interactor.SetRenderWindow(render_window)
    render_window.Render()                                              # Uruchom interakcję
    render_window_interactor.Start()

input_stl_file = r"C:\Users\adria\Desktop\Inzynierka\Pręt_test.stl"     # Ścieżka do pliku STL wejściowego
output_obj_file = 'output.obj'                                          # Ścieżka do pliku OBJ wyjściowego
convert_stl_to_obj(input_stl_file, output_obj_file)                     # Wywołaj funkcję konwersji
render_obj_file(output_obj_file)                                          # Wywołanie funkcji
