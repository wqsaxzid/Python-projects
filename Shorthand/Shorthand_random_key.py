from steganocryptopy.steganography import Steganography

Steganography.generate_key("")
secret = Steganography.encrypt("key.key", "img/wolf.png", "Secret_message.txt")
secret.save("img/secret_wolf.png")

result = Steganography.decrypt("key.key", "img/secret_wolf.png")
print(result)