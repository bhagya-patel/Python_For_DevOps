with open("demo.txt", "a+") as file:
    file.seek(0) 
    print(file.read())
    
    file.write("\nMy name is Bhagya Patel")


# | Mode   | Meaning                               |
# |--------|---------------------------------------|
# | "r"    | Read only                            |
# | "w"    | Write (overwrite existing file)      |
# | "a"    | Append (add at end)                  |
# | "r+"   | Read + Write (file must exist)       |
# | "a+"   | Read + Append (create if not exist)  |