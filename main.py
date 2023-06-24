import qrcode

#to change dimensions of QR code
features = qrcode.QRCode(version=1, box_size=30, border=4)

#to add data
features.add_data("https://www.linkedin.com/in/rishika-sarkar-40855722b/?lipi=urn%3Ali%3Apage%3Ad_flagship3_feed%3Bon2DYEKATeySjV4icm%2FeRA%3D%3D")
#generate_image = qrcode.make("HEY")
features.make(fit=True)
generate_image = features.make_image(fill_colour="black", back_colour="white")
generate_image.save('QR code.png')
