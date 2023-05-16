#creates a config for Blog_Reader.py
file = open("blog_reader_config.txt","w")

output_path = "/"
while True:
    write_output = input("Do you want to write to an output file\n"
                        "else Text will only be printed\n"
                        "yes/no\n")
    if(write_output=="yes" or write_output=="no"):
        break
    else:
        print("Wrong input please type yes or no")


if(write_output=="yes"):
    output_path = input("Please set an outputh path\n")

file.writelines("write_output = "+write_output+"\n")
file.writelines("output_path = "+output_path)