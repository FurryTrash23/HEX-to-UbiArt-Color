print('HEX to UAC (UbiArt color) convert\nby Worte\n')
hex = input('Enter hex: ').lstrip('#')
transparency = input('Enter transparency (0-100): ')
rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
output = []
output.append(rgb[0] / 255)
output.append(rgb[1] / 255)
output.append(rgb[2] / 255)
output.append(float(transparency) / 100)
print('If some of the values are something like "0.99999999999999999" you can round it if you want to.')
uac = output
print(uac)
