from PIL import Image

def find_closest_palette_color(oldpixel):
    return (round(oldpixel[0]/255)*255,round(oldpixel[1]/255)*255,round(oldpixel[2]/255)*255)

def two_tuples_minus(t1,t2):
    return (t1[0]-t2[0],t1[1]-t2[1],t1[2]-t2[2])

def two_tuples_plus(t1,t2,const):
    return (int(t1[0]+t2[0]*const),int(t1[1]+t2[1]*const),int(t1[2]+t2[2]*const))

pic = Image.open('macka.png')
pixels = pic.load()

for y in range(pic.size[1]-1):
    for x in range(1,pic.size[0]-1):
        oldpixel = pixels[x,y] #tupla ?
        newpixel = find_closest_palette_color(oldpixel)
        pixels[x,y] = newpixel
        quant_error = two_tuples_minus(oldpixel,newpixel)
        pixels[x + 1,y] = two_tuples_plus(pixels[x + 1,y], quant_error, 7 / 16)
        pixels[x - 1,y + 1] = two_tuples_plus(pixels[x - 1,y + 1], quant_error * 3 / 16)
        pixels[x,y + 1] = two_tuples_plus(pixels[x,y + 1], quant_error * 5 / 16)
        pixels[x + 1,y + 1] = two_tuples_plus(pixels[x + 1,y + 1], quant_error * 1 / 16)
pic.save('macka1.png')