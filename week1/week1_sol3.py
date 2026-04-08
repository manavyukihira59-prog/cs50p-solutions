img = input("File name: ").lower()
if "jpg" in img:
    print("image/jpg")
elif "jpeg" in img:
    print("image/jpeg")
elif "gif" in img:
    print("image/gif")   
elif "zip" in img:
    print("image/zip") 
elif "png" in img:
    print("image/png") 
elif "pdf" in img:
    print("image/pdf") 
elif "txt" in img:
    print("image/txt") 
else:                
     print("application/octet-stream")