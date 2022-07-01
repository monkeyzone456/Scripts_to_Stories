import os
import configparser

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    name = config['DEFAULT']['OUTPUT_NAME']
    if config['DEFAULT']['DWNLD_C'] == 'YES':
        out = 'C://Users/' + os.getlogin() + config['DEFAULT']['OUTPUT_DIR']
    else:
        out = 'D:/' + config['DEFAULT']['OUTPUT_DIR']
    files = os.listdir(os.getcwd())
    print(files)
    for f in files:
        if f.find('.txt') != -1 and f != name:
            file = f
            break
    convert(file,out,name)

def convert(input,out,name):
    script = open(input, "r")
    os.chdir(out)
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