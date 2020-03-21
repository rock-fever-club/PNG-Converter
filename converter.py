import sys
import os
import cv2
input = ""
path = ""

for i in range(1,len(sys.argv)):
    if i != 0:
        input = input + " " + sys.argv[i]
    else:
         input = sys.argv[i]
input = input.strip()
if len(input) == 0:
    print("usage: python script.py <path of file>")
else:
    img = cv2.imread(input,1)
    print(input)
    p = input.split("\\");
    for i in range(0, len(p) - 1):
        if i != 0:
            path = path + "\\" + p[i]
        else:
            path = p[i]
    print(os.path.join(path,"messi.png"))
    cv2.namedWindow('png image', cv2.WINDOW_NORMAL)
    cv2.imshow("png image", img, )
    cv2.waitKey(0) & 0xFF
    cv2.imwrite(os.path.join(path,"messi.png"),img)
