import cv2

def checkclosestascii(pixelbrightness,asciicharacters):
    previousclosestcharacter = "?"
    for i in asciicharacters:
        if abs(pixelbrightness - i) < abs(pixelbrightness - (list(asciicharacters.keys())[list(asciicharacters.values()).index(previousclosestcharacter)])):
            previousclosestcharacter = asciicharacters[i]
    return previousclosestcharacter

def asciifyimage(img):
    asciicharacters = {255:".",207:",",184:":",161:";",138:"+",115:"*",92:"?",69:"%",46:"S",23:"#",0:"@"}



    asciiedpicture = ""

    for pixelline in range(resizedandgray.shape[0]):
        for pixel in range(resizedandgray.shape[1]):
            pixelbrightness = resizedandgray[pixelline][pixel]
            asciiedpicture += checkclosestascii(pixelbrightness,asciicharacters)
        asciiedpicture += "\n"

    return asciiedpicture


####################################
#ACTUAL CODE NOT FUNCTIONS##########
#FIXING IMAGE TO GRAYSCALE + SMALLER
####################################
img = cv2.imread("mitch.png")
#print(img.shape)
grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#print(grayscale.shape)

scale_percent = 20
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
    
resizedandgray = cv2.resize(grayscale, dim, interpolation = cv2.INTER_AREA)
#print(resizedandgray.shape)
cv2.imwrite("catimage.png",resizedandgray)


###############
#ASCIIFYING IMG
###############
string = asciifyimage(resizedandgray)
with open('asciiedimage.txt',"w") as file:
    for i in string.split("\n"):
        file.write(i)
        file.write("\n")