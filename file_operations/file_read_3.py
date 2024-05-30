with open("sample.txt") as file:  
    data = file.read() 
 
print(data)


#Note:
    #Here, with...open automatically closes the file, so we don't have to use the close() function.
    #Since we don't have to worry about closing the file, make a habit of using the with...open syntax
