file = input("File name: ")
file = file.lower().strip()
file_split = file.split(".")

img_extensions = ["gif", "jpg", "jpeg", "png"]
app_extensions = ["pdf", "txt", "zip"]

if len(file_split) != 1:
    extension = file_split[-1]
    if extension in img_extensions:
        if extension == "jpg":
            extension = "jpeg"
        print(f"image/{extension}")
    elif extension in app_extensions:
        if extension == "txt":
            print(f"text/{file_split[0]}")
        else:
            print(f"application/{extension}")
    else:
        print("application/octet-stream")
else:
    print("application/octet-stream")
