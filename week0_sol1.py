def slow(text):
    text=text.replace(" ", "...")
    return text
    
u_input=input("Enter required string\n")
print(slow(u_input))