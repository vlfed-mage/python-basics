weight = input('Weight: ')
unit = input('(L)bs of (K)g: ').lower()

converted_weight = float(weight) / 0.45 if unit == 'k' else float(weight) * 0.45
measuring_unit = 'pounds' if unit == 'k' else 'kilograms'

print(f'You are {converted_weight} {measuring_unit }')
