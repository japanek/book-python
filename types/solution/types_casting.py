meters = float(input('Distance [m]: '))

km = int(meters / 1000)
miles = float(meters / 1608)
nm = float(meters / 1852)

print(f'Meters: {meters}')
print(f'Kilometers: {km}')
print(f'Miles: {miles}')
print(f'Nautical Miles: {nm}')
print(f'All: {m}, {km}, {miles}, {nm}')
