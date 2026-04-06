def convert(text):
    if ":)" in text:   
     return text.replace(":)","🙂")
    if ":(" in text:
     return text.replace(":(","🙁")
    



u_input=input("Enter a text\n")
print(convert(u_input))
