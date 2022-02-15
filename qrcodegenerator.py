import qrcode
import image
qr = qrcode.QRCode(
    version = 5 , #15 means the version of the qr code, high the number bigger the code image and complicated picture
    box_size = 10, #size of box where qr code will be diaplayed
    border = 5, #it is the white part of the image -- border in all 4 sides with white color

)
data = "https://github.com/saugat4315"

qr.add_data(data)
qr.make(fit = True)
img = qr.make_image(fill = "black", back_color = "white")
img.save("test.png")