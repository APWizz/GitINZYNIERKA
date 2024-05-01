import vtk

# Ścieżka do pliku OBJ
obj_file_path = r"C:\Users\adria\Desktop\Git\output.obj"

# Wczytaj plik OBJ
reader = vtk.vtkOBJReader()
reader.SetFileName(obj_file_path)
reader.Update()

# Utwórz aktora na podstawie wczytanych danych
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputData(reader.GetOutput())

actor = vtk.vtkActor()
actor.SetMapper(mapper)

# Utwórz renderer i dodaj aktora do niego
renderer = vtk.vtkRenderer()
renderer.AddActor(actor)

# Utwórz okno renderowania
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

# Utwórz interakcję
render_window_interactor = vtk.vtkRenderWindowInteractor()
render_window_interactor.SetRenderWindow(render_window)

# Uruchom interakcję
render_window.Render()
render_window_interactor.Start()
