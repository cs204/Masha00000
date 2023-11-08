def main():
    file_name = input("File name: ")

    if file_name.lower().endswith((".gif", ".jpg", ".jpeg", ".png", ".pdf", ".txt", ".zip")):
        print(determine_media_type(file_name))
    else:
        print("Media type: application/octet-stream")

def determine_media_type(file_name):
    file_extension = file_name.lower().split(".")[-1]

    if file_extension == "gif":
        return "image/gif"
    elif file_extension in ("jpg", "jpeg"):
        return "image/jpeg"
    elif file_extension == "png":
        return "image/png"
    elif file_extension == "pdf":
        return "application/pdf"
    elif file_extension == "txt":
        return "text/plain"
    elif file_extension == "zip":
        return "application/zip"
    else:
        return "unknown"
main()