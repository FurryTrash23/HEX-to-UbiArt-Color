print('HEX to UAC (UbiArt color) convert\nby Worte\n')
rgb = tuple(int(input('Enter hex: ').lstrip('#')[i:i+2], 16) for i in (0, 2, 4))
print([].append(rgb[0] / 255).append(rgb[1] / 255).append(rgb[2] / 255).append(input('Enter transparency (0-100): ') * 2.55 / 255))
