# a simple File reader that will read an txt file
# and will format it to fit a typical html page
#files have to start with "!start"
#skelleton:
#!start
#title
#
#text
#text

error_message = "file formated wrong\n" \
                "file needs to start with:!start\n" \
                "ending program"

#loading config
config = open("blog_reader_config.txt","r")
write = config.readline()
write = write.removeprefix("write_output = ").removesuffix("\n")
print(write)

#get filepath
file_path = input("Drag and drop you file into the terminal\n")
file_path = file_path.removesuffix(" ") #is removed if terminal automatically adds a space
file = open(file_path,"r")

if not file.readline().startswith("!start"):
    print(error_message)
else:
    #Readline
    title = file.readline().removesuffix("\n")
    title = '<h2 class="mainblog-h2">'+title+"</h2>\n"
    file.readline()
    text = ""
    text += '\n<p class="mainblog-text">'

    for line in file:
        if line.startswith("\n"):
            line = line.replace("\n","<br><br>\n")
        text += line

    text+="\n</p>"

    if write=="no":
        print("###########################################\n")
        print(title)
        print(text)
        print("\n#####################end###################")
    elif write=="yes":
        print("###########################################\n")
        output_path = config.readline().removeprefix("output_path = ").removesuffix("\n")
        output_name = input("Please set a name for your outputfile\n")
        with open(output_path+"/"+output_name,"w") as output_file:
            output_file.write(title)
            output_file.write(text)
        print("done writing to file\n"
              "output file:"+output_path+"/"+output_name)
file.close()
config.close()
