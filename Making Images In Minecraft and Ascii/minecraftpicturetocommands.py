import cv2

def checkclosestblock(pixelbrightness,blocks):
    previousclosestcharacter = list(blocks.values())[0]
    for i in blocks:
        if abs(pixelbrightness - i) < abs(pixelbrightness - (list(blocks.keys())[list(blocks.values()).index(previousclosestcharacter)])):
            previousclosestcharacter = blocks[i]
    return previousclosestcharacter

def blockifyimage(img):
    blocks = {255:"minecraft:quartz_block 0",207:"minecraft:iron_block",184:"minecraft:wool 0",161:"minecraft:wool 8",138:"minecraft:stonebrick 0",115:"minecraft:stone 0",92:"minecraft:stone_slab 0",69:"minecraft:wool 15",46:"minecraft:coal_block",23:"minecraft:obsidian",0:"minecraft:stained_hardened_clay 15"}



    blockedpicture = []

    for pixelline in range(img.shape[0]):
        for pixel in range(img.shape[1]):
            pixelbrightness = img[pixelline][pixel]
            blockedpicture += [checkclosestblock(pixelbrightness,blocks),]
        blockedpicture += ["newline",]

    return blockedpicture

img = cv2.imread('rick.jpg')
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

scale_percent = 10
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
    
resizedandgray = cv2.resize(grayscale, dim, interpolation = cv2.INTER_AREA)

listofblocks = blockifyimage(resizedandgray)
#print(listofblocks)
'''
with open('commands.txt',"w") as file:
    x,y,z = 0,100,0
    for i in listofblocks:
        if i == "newline":
            z -= 1
            x = 0
        else:
            file.write(f'/setblock {x} {y} {z} {i}')
            x += 1
        
        file.write('\n')
'''

'''
with open('othercommands.txt',"w") as file:
    x,y,z = 0,100,0
    previousblock = 'nothing :('
    for i in listofblocks:
        if i == "newline":
            z -= 1
            x = 0
        else:
            if i == previousblock:
                x += 1
                print("same block as last so skipping")
            else:
                try:
                    print(oldx)
                    print(x)
                    file.write(f'/fill {oldx} {y} {z} {x} {y} {z} {i}')
                    file.write('\n')
                    print(f"Wasnt Same and Also Not First : {previousblock} was last block and current block {i}")
                except Exception:
                    print("First Block :D")
                    oldx = x
                    file.write(f'/fill {oldx} {y} {z} {x} {y} {z} {i}')
                    file.write('\n')
                x += 1
                oldx = "".join([i for i in str(x)])
                
        
        previousblock = "".join(list(i))
'''
#if block same block increase x
#if block newline do all up till now
#if block new do all up until now
#print(listofblocks)
#DONT TOUCH
with open('othercommands.txt',"w") as file:
    x,y,z = 0,100,0
    previousblock = 'nothing :('
    oldx = 0

    for i in listofblocks:
        if i == "newline":
            file.write(f'/fill {oldx} {y} {z} {x} {y} {z} {previousblock}')
            file.write("\n")
            x = 0
            oldx = 0
            z -= 1
        else:
            if i == previousblock:
                x += 1
            else:
                if previousblock == "newline":
                    file.write(f'/fill {oldx} {y} {z} {x} {y} {z} {i}')
                    file.write("\n")
                else:
                    file.write(f'/fill {oldx} {y} {z} {x} {y} {z} {previousblock}')
                    file.write("\n")
                    oldx = x + 1
                    x += 1
        #print(i)
        previousblock = i
