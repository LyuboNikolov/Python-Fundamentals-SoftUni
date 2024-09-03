cells = input().split("#")
water = int(input())

total_effort = 0
put_out_cells = []

for cell in cells:
    current_cell = cell.split()
    fire_type = current_cell[0]
    cell_value = int(current_cell[2])
    if (fire_type == "High" and 81 <= cell_value <= 125) or \
            (fire_type == "Medium" and 51 <= cell_value <= 80) or \
            (fire_type == "Low" and 1 <= cell_value <= 50):
        if water >= cell_value:
            water -= cell_value
            total_effort += 0.25 * cell_value
            put_out_cells.append(cell_value)

print(f"Cells:")
for cell in put_out_cells:
    print(f" - {cell}")
print(f"Effort: {total_effort:.2f}\nTotal Fire: {sum(put_out_cells)}")
