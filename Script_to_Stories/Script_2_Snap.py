import os
import configparser

def main():
    config = configparser.ConfigParser()
    config.read('config.ini')
    name = config['DEFAULT']['OUTPUT_NAME']
    counter = config['DEFAULT']['DAY_COUNTER']
    if config['DEFAULT']['DWNLD_C'] == 'Y':
        out = 'C://Users/' + os.getlogin() + config['DEFAULT']['OUTPUT_DIR']
    else:
        out = 'D:/' + config['DEFAULT']['OUTPUT_DIR']
    files = os.listdir(os.getcwd())
    print(files)
    for f in files:
        if f.find('.txt') != -1 and f != name:
            file = f
            break
    convert(file,out,name, counter)

def convert(input,out,name,counter):
    script = open(input, "r")
    os.chdir(out)
    output = open(name,"w")
    index = 0
    day = 1
    temp = ""
    for char in script.read():
        temp += char
        if index % 250 == 0:

            if counter == 'Y':
                output.write('\n\n======================================\nDay %d\n\n' % day)
            else:
               output.write('\n\n======================================\n\n')
            index = len(temp)
            day += 1
        if char == ' ':
            output.write(temp)
            temp = ""
        index = index + 1
    output.write(temp)

    script.close()
    output.close()
  
if __name__=="__main__":
    main()