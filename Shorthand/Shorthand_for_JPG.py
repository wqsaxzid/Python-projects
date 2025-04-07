from stegano import exifHeader

secret = exifHeader.hide("img/cat.jpg", "img/secret_cat.jpg", "I'm married!")

result = exifHeader.reveal("img/secret_cat.jpg")
result = result.decode()
print(result)
