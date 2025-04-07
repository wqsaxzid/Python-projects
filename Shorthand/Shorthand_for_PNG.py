from stegano import lsb

secret = lsb.hide("img/mountain.png", "Your password: qwerty")
secret.save("img/secret_mountain.png")

result = lsb.reveal("img/secret_mountain.png")
print(result)
