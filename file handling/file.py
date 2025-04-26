file = open("phone.txt","w")
phoneno = input('enter phone number')
file.writelines(phoneno)
file.close()
