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
def nanotools_spirals(n, d) -> gf.Component:
    if not n in [1,2,3]:
        raise ValueError("n deve ser um número de 1 a 3")
    if not d in [5,10]:
        raise ValueError("d deve ser 5 ou 10")

    centers_1_d5 = [(-46.500, 22.000),(-42.000, -32.000)]
    centers_2_d5 = [(-57.500,33.000),(-53.000, -43.000)]
    centers_3_d5 = [(-74.000, 49.500), (-69.500, -59.500)]
    centers_1_d10 = [(-66.000, 31.500),(-61.500, -46.500)]
    centers_2_d10 = [(-72.000, 52.500),(-72.500, -62.500)]
    centers_3_d10 = [(-108.000, 73.500), (-103.500, -88.500)]

    centers_d5 = [centers_1_d5, centers_2_d5, centers_3_d5]
    centers_d10 = [centers_1_d10, centers_2_d10, centers_3_d10]

    filename = folder + '/Spirals/spiral_%d_d%d.gds' %(n,d)
    try:
        cellname = 'Square'
        comp = gf.import_gds(filename, cellname=cellname)
    except:
        cellname = 'Square$1'
        comp = gf.import_gds(filename, cellname=cellname)
    if d == 5:
        comp.add_port(name='o1', center=centers_d5[n-1][0], width=0.5, orientation=90, layer=(1,0), port_type='optical')
        comp.add_port(name='o2', center=centers_d5[n-1][1], width=0.5, orientation=180, layer=(1,0), port_type='optical')
    else:
        comp.add_port(name='o1', center=centers_d10[n-1][0], width=0.5, orientation=90, layer=(1,0), port_type='optical')
        comp.add_port(name='o2', center=centers_d10[n-1][1], width=0.5, orientation=180, layer=(1,0), port_type='optical')

    return comp


@gf.cell
def nanotools_gcTE() -> gf.Component:
    filename = folder + '/nanotools_gc_TE_8.gds'
    cellname = 'GratingCoupler_TE_Oxide_8degrees'

    comp = gf.import_gds(filename, cellname=cellname)

    comp.add_port(name='o1', center=(0.000, 0.000), width=0.5, orientation=-90, layer=(1,0), port_type='optical')
    comp.rotate(90)

    return comp