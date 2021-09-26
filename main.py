print('HEX to UAC (UbiArt color) convert\nby Worte\n')
hex = input('Enter hex: ').lstrip('#')
transparency = input('Enter transparency (0-100): ')
rgb = tuple(int(hex[i:i+2], 16) for i in (0, 2, 4))
output = []
output.append(str(float(transparency) / 100)[:8])
output.append(str(rgb[0] / 255)[:8])
output.append(str(rgb[1] / 255)[:8])
output.append(str(rgb[2] / 255)[:8])
uac = output
print(uac)
