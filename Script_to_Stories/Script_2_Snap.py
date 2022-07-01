import os
import configparser

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    name = config['DEFAULT']['OUTPUT_NAME']
    out = config['DEFAULT']['OUTPUT_DIR']
    cwd = os.getcwd() 
    files = os.listdir(cwd)
    print(files)
    for f in files:
        if f.find('.txt') != -1 and f != 'README.txt' and f != name:
            file = f
            break

    convert(file,out,name)

def convert(input,out,name):
    script = open(input, "r")
    output = open(name,"w")
    index = 1
    temp = ""
    for char in script.read():
        temp += char
        if index == 250:
            output.write('\n\n======================================\n\n')
            index = len(temp)
        if char == ' ':
            output.write(temp)
            temp = ""
        index = index + 1
    output.write(temp)

    script.close()
    output.close()
  
if __name__=="__main__":
    main()