#python / OOP question! Should I have defined this within my class, or outside of it in another class/outside of the class
#declaration? Does this matter much?
def gen_keywords(fileToOpen):
    with open(fileToOpen, 'r') as keywordsFile:
        wordArray = []
        for line in keywordsFile.readlines():
            line = line.strip()
            wordArray.append(line)
            
        return wordArray