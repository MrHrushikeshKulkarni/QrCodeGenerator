import qrcode
import image
qr = qrcode.QRCode(
    version = 15, # 15 means the version of the qr code high the number bigger the code image and complicated picture
    box_size = 10, #size of box where qr code will be displayed
    border = 5, #it is white part of image -- border in all 4 sides with white colour 
)

data = "https://www.linkedin.com/in/hrushikesh-kulkarni-a876a8256/"
# as i given the path of my linkdin profile 

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill="black", back_colour ="white")
img.save("test.png")