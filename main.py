print('HEX to UAC (UbiArt color) convert\nby Worte\n')

# Taking input for HEX and transparency
hex_value = input('Enter hex: ').lstrip('#')
transparency = input('Enter transparency (0-100): ')

# Converting HEX to RGB
rgb = tuple(int(hex_value[i:i+2], 16) for i in (0, 2, 4))

# Calculating UAC values
uac_transparency = str(float(transparency) / 100)[:8]
uac_red = str(rgb[0] / 255)[:8]
uac_green = str(rgb[1] / 255)[:8]
uac_blue = str(rgb[2] / 255)[:8]

# Forming the UAC string
uac = f'{uac_transparency},{uac_red},{uac_green},{uac_blue}'

# Printing UAC
print(uac)

# Writing UAC to a text file
with open('ubiartcolor.txt', 'w') as file:
    file.write(uac)
