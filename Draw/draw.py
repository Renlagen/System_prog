from PIL import Image, ImageDraw

# Пустой желтый фон.
im = Image.new('RGB', (900, 600), (0, 128, 0))
draw = ImageDraw.Draw(im)

draw.line(xy=((100, 150), (800, 150),), fill='black', width=30)

draw.line(xy=((100, 450), (800, 450),), fill='yellow', width=30)

draw.text((450, 100), 'CHECHNYA', fill='black', )

draw.rectangle((300, 300, 400, 200), fill='red', outline=(255, 255, 255))

im.save('draw.jpg', quality=95)
