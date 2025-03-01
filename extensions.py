filename = input("File name: ").strip().lower()


mime_types = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

for ext, mime in mime_types.items():
    if filename.endswith(ext):
        print(mime)
        break
else:
    print("application/octet-stream")  
