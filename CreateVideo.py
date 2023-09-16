import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        images.append(file_name)
        
# print(len(images))
count = len(images)
frame = cv2.imread(images[0])
# cv2.imshow(images[0])
height, width, channel = frame.shape
size = (height, width) 
# print(size)

#sunset
# sunset = cv2.VideoWriter("Sunset.avi", cv2.VideoWriter_fourcc(*'XVID'), 5, size)

# for i in range(0,count-1 ):
#     frame = cv2.imread(images[i])
#     sunset.write(frame)
# sunset.release()

#SUNRISE
sunrise = cv2.VideoWriter("Sunrise.avi", cv2.VideoWriter_fourcc(*'DIVX'), 5, size)

for i in range(count, 0, -1 ):
    frame = cv2.imread(images[i])
    sunrise.write(frame)
sunrise.release()
