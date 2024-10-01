import os
from openpyxl import load_workbook

filePath = '/Users/davidgarcia/Desktop/Test Copy'

cluster_length = 2
cluster_size = 8
spf = 4
ehd = 0.45
np = 42
phasing = 120
orientation = '90 deg & 270 deg'

plug_length = 2
plug_od = 4.38
plug_id = 1.25
make = "SLB"
model = "FRACXION"

for x in os.listdir(filePath):
    # print(x)
    wb = load_workbook(filename=f'{filePath}/{x}')
    perf_sheet = wb["WellView Perf Template"]
    stages_cells_range = perf_sheet["B21:B2022"]
    perf_row_counter = 20
    stage_counter = 0
    plug_sheet = wb["WellView Plug Template"]

    for row in stages_cells_range:
        stage_counter += 1
        for cell in row:
            if cell.value is None:
                break
            else:
                perf_row_counter += 1

    print(perf_row_counter)

    print(f'{x} has {perf_row_counter / cluster_size} stages')

    # print(perf_sheet["B21"].value)
