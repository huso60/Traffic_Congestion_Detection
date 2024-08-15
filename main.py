import cv2

cap=cv2.VideoCapture('cars.mp4')

model=cv2.CascadeClassifier('cars.xml')


while True:
    ret,frame=cap.read()
    if (type(frame)==type(None)):
        break
    gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    cars=model.detectMultiScale(gray,1.2,1)



    for (x1,y1,x2,y2) in cars:
        box=cv2.rectangle(frame,(x1,y1),(x1+x2,y1+y2),(255,0,255),2)
        img='img3.png'

        cv2.imwrite(img,box)

    cv2.imshow("video",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break




cv2.destroyAllWindows()





