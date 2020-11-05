import 	cv2
path=input("Enter The PATH of the Video File : ")
#cap=cv2.VideoCapture("models/image_examples/walking.avi")
cap=cv2.VideoCapture(path)
font=cv2.FONT_HERSHEY_PLAIN
xml=input("Enter The PATH of the xml File : ")

#hercascade=cv2.CascadeClassifier("models/Haarcascades/haarcascade_fullbody.xml")
hercascade=cv2.CascadeClassifier(xml)
while True:
	ret,frames=cap.read()
	gray=cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)
	full_body=hercascade.detectMultiScale(gray,1.3,2)
	for(x,y,w,h) in full_body:
		cv2.rectangle(frames,(x,y),(x+w,y+h),(0,255,255),2)
		cv2.putText(frames,str("HUMAN"),(x,y+h),font,1,255)
	cv2.imshow("FRAME",frames)
	if cv2.waitKey(33) == ord('q'):
		break
cv2.destroyAllWindows()