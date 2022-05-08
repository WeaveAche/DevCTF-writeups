import requests
from bs4 import BeautifulSoup
from base64 import b64decode
import cv2
import pytesseract

r = requests.get("https://web.ctf.devclub.in/dev/4/")
soup = BeautifulSoup(r.text, "html.parser")

src = soup.find("img").attrs["src"].split(", ")[1]
img = b64decode(src)

with open("image.jpeg", "wb") as f:
    f.write(img)

img = cv2.imread("image.jpeg")
ans = pytesseract.image_to_string(img).strip()

cv2.imshow("title", img)
print(ans)

tt = soup.find(id="tt").attrs["value"]

r = requests.post("https://web.ctf.devclub.in/dev/4/", data = {"tt":tt, "captcha":ans})
print(r.text)

cv2.waitKey(0)
