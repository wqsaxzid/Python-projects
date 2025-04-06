import pyAesCrypt  # library for encrypt
import os  # library for search
import sys


# file encryption function
def encryption(file, password):

    # setting the buffer size
    buffer_size = 512 * 1024

    # calling the encryption method
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )

    # to see the result, print the encrypted file
    print("[The file '"+ str(os.path.splitext(file)[0]) + "' is encrypted!]")

    # deleting the source file
    os.remove(file)


# directory scanning function
def walking_by_dirs(dir, password):

    # going through all the subdirectories in the specified directory
    for name in os.listdir(dir):
        path = os.path.join(dir, name)

        # if we find a file, we encrypt it
        if os.path.isfile(path):
            try:
                encryption(path, password)
            except Exception as ex:
                print(ex)
        # if we find the directory, we repeat the cycle in the search
        else:
            walking_by_dirs(path, password)

password = input("Enter the password for encryption: ")
walking_by_dirs("C:/Users/User/Python-projects/Encrypting files using python/secret_files", password)
# os.remove((str(sys.argv[0])))