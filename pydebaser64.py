import platform
import sys
import os
import base64
import pyperclip

"""
def encode_file(file, file_out):
    message = ""
    with open(file, "rb") as f:
        data = f.read()
        message = base64.b64encode(data)

    with open(file_out, "wb") as f:
        f.write(message)
"""


def main():
    print("Debaser64 1.0 Python Edition\n")

    # check number or arguments
    if len(sys.argv) != 2:
        print("Usage: python.exe pydebaser64.py C:\\output_directory")
        sys.exit(1)

    # get data from clipboard
    data = pyperclip.paste()
    path = sys.argv[1]

    if data == "":
        print("Clipboard is empty")
        sys.exit(1)

    correct_format = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/="

    # check for correct format
    for a in range(len(data)):
        if data[a] not in correct_format:
            print("Incorrect symbol in base64 string")
            sys.exit(1)

    # check if directory is accessible
    if not os.access(path, os.W_OK):
        print(f"Directory {path} is not accessible")
        sys.exit(1)

    # file = os.path.join(path, "test.jpg")
    # file_out = os.path.join(path, "test_enc.txt")
    # encode_file(file, file_out)

    # data is base64 string
    data = data.encode("utf-8")
    decoded_data = base64.decodebytes(data)
    index = 0

    while True:
        full_path = os.path.join(path, "decoded-" + str(index) + ".txt")
        if os.path.isfile(full_path):
            index = index + 1
            continue
        else:
            try:
                with open(full_path, "wb") as file:
                    file.write(decoded_data)
                    break
            except IOError:
                print("Can't write to file, IOError")
                sys.exit(1)

    print("Decoded succesfully")


if __name__ == "__main__":
    system = platform.system()

    if system != "Windows":
        print("Sorry this script works only in Windows environment")
        sys.exit(1)
    else:
        main()
