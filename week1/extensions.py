def main():
    str_ext = input("File name: ").lower().strip()
    if str_ext.endswith(".gif"):
        print("image/gif")
    elif str_ext.endswith(".jpeg") or str_ext.endswith(".jpg"):
        print("image/jpeg")
    elif str_ext.endswith(".png"):
        print("image/png")
    elif str_ext.endswith(".pdf"):
        print("application/pdf")
    elif str_ext.endswith(".txt"):
        print("text/plain")
    elif str_ext.endswith(".zip"):
        print("application/zip")
    else:
        print("application/octet-stream")

main()

