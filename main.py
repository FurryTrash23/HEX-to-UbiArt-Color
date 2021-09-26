print('HEX to UAC (UbiArt color) convert\nby Worte\n')
hex = input('Enter hex: ').lstrip('#')
transparency = input('Enter transparency (0-100): ')
rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
output = []
output.append(round(float(transparency) / 100, 6))
output.append(round(rgb[0] / 255, 6))
output.append(round(rgb[0] / 255, 6))
output.append(round(rgb[0] / 255, 6))
uac = output
print(uac)
