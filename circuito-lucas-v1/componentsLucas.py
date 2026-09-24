import gdsfactory as gf
from pathlib import Path

folder = str(Path(__file__).resolve().parent / "Components_Lucas")

@gf.cell
def yEbeam() -> gf.Component:
    filename = folder + '/ebeam_y_te1550.gds'
    cellname = 'ebeam_y_1550'

    comp = gf.import_gds(filename, cellname=cellname)

    comp.add_port(name='o1', center=(-7.4,0), width=0.5, orientation=180, layer=(1,0), port_type='optical')
    comp.add_port(name='o2', center=(7.4, -2.75), width=0.5, orientation=0, layer=(1,0), port_type='optical')
    comp.add_port(name='o3', center=(7.4, 2.75), width=0.5, orientation=0, layer=(1,0), port_type='optical')

    return comp

@gf.cell
def dcEbeam_13() -> gf.Component:
    filename = folder + '/ebeam_dc_te1550_13.gds'
    cellname = 'ebeam_dc_te1550$1'

    comp = gf.import_gds(filename, cellname=cellname)

    comp.add_port(name='o1', center=(-10.178, -2.35), width=0.5, orientation=180, layer=(1,0), port_type='optical')
    comp.add_port(name='o2', center=(-10.178, 2.35), width=0.5, orientation=180, layer=(1,0), port_type='optical')
    comp.add_port(name='o3', center=(10.178, -2.35), width=0.5, orientation=0, layer=(1,0), port_type='optical')
    comp.add_port(name='o4', center=(10.178, 2.35), width=0.5, orientation=0, layer=(1,0), port_type='optical')

    return comp

@gf.cell
def dcEbeam_12() -> gf.Component:
    filename = folder + '/ebeam_dc_te1550_12.gds'
    cellname = 'ebeam_dc_te1550$1'

    comp = gf.import_gds(filename, cellname=cellname)

    comp.add_port(name='o1', center=(-9.968, -2.35), width=0.5, orientation=180, layer=(1,0), port_type='optical')
    comp.add_port(name='o2', center=(-9.968, 2.35), width=0.5, orientation=180, layer=(1,0), port_type='optical')
    comp.add_port(name='o3', center=(9.968, -2.35), width=0.5, orientation=0, layer=(1,0), port_type='optical')
    comp.add_port(name='o4', center=(9.968, 2.35), width=0.5, orientation=0, layer=(1,0), port_type='optical')

    return comp

@gf.cell
def dcEbeam_50() -> gf.Component:
    filename = folder + '/ebeam_dc_te1550_50.gds'
    cellname = 'ebeam_dc_te1550$1'

    comp = gf.import_gds(filename, cellname=cellname)

    comp.add_port(name='o1', center=(-16.232, -2.35), width=0.5, orientation=180, layer=(1,0), port_type='optical')
    comp.add_port(name='o2', center=(-16.232, 2.35), width=0.5, orientation=180, layer=(1,0), port_type='optical')
    comp.add_port(name='o3', center=(16.232, -2.35), width=0.5, orientation=0, layer=(1,0), port_type='optical')
    comp.add_port(name='o4', center=(16.232, 2.35), width=0.5, orientation=0, layer=(1,0), port_type='optical')

    return comp

@gf.cell
def dcEbeam_25() -> gf.Component:
    filename = folder + '/ebeam_dc_te1550_25.gds'
    cellname = 'ebeam_dc_te1550$1'

    comp = gf.import_gds(filename, cellname=cellname)

    comp.add_port(name='o1', center=(-12.481, -2.35), width=0.5, orientation=180, layer=(1,0), port_type='optical')
    comp.add_port(name='o2', center=(-12.481, 2.35), width=0.5, orientation=180, layer=(1,0), port_type='optical')
    comp.add_port(name='o3', center=(12.481, -2.35), width=0.5, orientation=0, layer=(1,0), port_type='optical')
    comp.add_port(name='o4', center=(12.481, 2.35), width=0.5, orientation=0, layer=(1,0), port_type='optical')

    return comp

@gf.cell
def nanotoolsSpiralPaperclip(length) -> gf.Component:
    length_array = [193.597, 890.327, 1608.635, 3028.174]
    if not length in length_array:
        raise ValueError(f'Error! length must be in the array: {length_array}')
    else:
        n = length_array.index(length)

    centers_193 = [(-26.500, 5.000), (-21.000, -13.000)]
    centers_890 = [(-49.000, 12.500), (-38.500, -25.500)]
    centers_1608 = [(-54.200, 20.800), (-44.800, -32.800)]
    centers_3028 = [(-61.800, 31.200), (-53.200, -42.200)]

    centers_matrix = [centers_193, centers_890, centers_1608, centers_3028]

    filename = folder + '/nanotools_paperclip_%.3f.gds' %length
    cellname = 'Square'

    comp = gf.import_gds(filename, cellname=cellname)

    comp.add_port(name='o1', center=centers_matrix[n][0], width=0.5, orientation=90, layer=(1,0), port_type='optical')
    comp.add_port(name='o2', center=centers_matrix[n][1], width=0.5, orientation=180, layer=(1,0), port_type='optical')

    return comp

@gf.cell
def nanotools_gcTE() -> gf.Component:
    filename = folder + '/nanotools_gc_TE_8.gds'
    cellname = 'GratingCoupler_TE_Oxide_8degrees'

    comp = gf.import_gds(filename, cellname=cellname)

    comp.add_port(name='o1', center=(0.000, 0.000), width=0.5, orientation=-90, layer=(1,0), port_type='optical')
    comp.rotate(90)

    return comp