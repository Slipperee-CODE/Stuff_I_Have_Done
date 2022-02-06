import enum
from transformers import pipeline
import cv2

generator = pipeline('text-generation',model='EleutherAI/gpt-neo-2.7B')

listofinspiration = []

prompt = "Happiness is"


for i in range(3):
    result = generator(prompt,max_length=15, do_sample = True, temperature = 0.9)

    print(result[0]['generated_text'])
    listofinspiration.append(result[0]['generated_text'])

print(listofinspiration)

for index,i in enumerate(listofinspiration):
    img = cv2.imread('inspire.jpg')
    dimensions = img.shape

    position = (0,dimensions[1]//3)


    img = cv2.putText(img,i[:len(prompt)],position,cv2.FONT_HERSHEY_TRIPLEX,1,(255,255,255),3)

    position = (0,dimensions[1]//2)
    img = cv2.putText(img,i[len(prompt):],position,cv2.FONT_HERSHEY_TRIPLEX,1,(255,255,255),3)

    cv2.imwrite(f"Quote {index}.jpg",img)
