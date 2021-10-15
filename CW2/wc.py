def countline(fileName):
    lineCounter = 0
    fileCounted = open(fileName, 'rb')
    fileContents = fileCounted.read()      
    lineCounter = fileContents.count('\n'.encode())
    fileCounted.close()
    return lineCounter 

def countword(fileName):
    wordCounter = 0
    with open(fileName, 'rb') as fileForLine:
        wordCounter += len(fileForLine.read().split())
    return wordCounter
    
def countbyte(fileName):
    byteCounter = 0
    with open(fileName, 'rb') as fileForLine:
        byteCounter = len(fileForLine.read())
    return byteCounter

def tryfile(fileName):
    global lineTab,wordTab,byteTab,triggerc,triggerl,triggerw,fileCounter
    try:
        testedFile = open(fileName, 'rb')
    except IsADirectoryError:
        print("wc:", fileName, ": Is a directory.")
        l = ''
        w = ''
        c = ''
        if triggerl: l=0
        if triggerw: w=0
        if triggerc: c=0
        print('%s%s%s%s%s%s%s%s' % (lineTab, str(l), wordTab, str(w), byteTab, str(c), '\t', fileName))
        fileCounter += 1
        return False
    except:
        print("wc:", fileName, ": No such file or directory.")
        return False
    else:
        testedFile.close()
        fileCounter += 1
        return True
    

if __name__ == "__main__":
    import sys
    
    lineCounter = ''
    wordCounter = ''
    byteCounter = ''
    lineTab = ''
    wordTab = ''
    byteTab = ''
    totalLine = ''
    totalWord = ''
    totalByte = ''
    triggerl = False
    triggerw = False
    triggerc = False
    fileCounter = 0
    flagCounter = 0
    
    if len(sys.argv)<=1:
        print("Error: We don't handle that situation yet!")
        exit(0)
        
    i = 1
    while len(sys.argv)>i:
        flag = sys.argv[i]
        flagList = ['l','w','c']
        flagInput = flag
        
        if flagInput[0] == '-' and len(flagInput)>1:
            trigger = True
            for flag in flagInput:
                if trigger:
                    trigger = False
                    continue
                if flag in flagList:
                    flagCounter += 1
                    if flag == 'l':
                        triggerl = True
                        totalLine = 0
                        lineTab = '\t'
                    elif flag == 'w':
                        triggerw = True
                        totalWord = 0
                        wordTab = '\t'
                    elif flag == 'c':
                        triggerc = True
                        totalByte = 0
                        byteTab = '\t'
                else:
                    print("wc: invalid option -- \'"+flag+"\'")
                    exit(0)
        i+=1
    
    if flagCounter == 0:
        triggerl = True
        triggerw = True
        triggerc = True
        totalLine = 0
        totalWord = 0
        totalByte = 0
        lineTab = '\t'
        wordTab = '\t'
        byteTab = '\t'        
        
    i = 1
    while len(sys.argv) > i:
        fileName = sys.argv[i]
        
        if fileName[0] == '-' and len(fileName)>1:
            i+=1
            continue
        elif len(fileName)<=1:
            tryfile(fileName)
            exit(0)
            
        if tryfile(fileName):
            if triggerl: 
                lineCounter = countline(fileName)
                totalLine += lineCounter
            if triggerw: 
                wordCounter = countword(fileName)
                totalWord += wordCounter
            if triggerc: 
                byteCounter = countbyte(fileName)
                totalByte += byteCounter
                
            print('%s%s%s%s%s%s%s%s' % (lineTab, str(lineCounter), wordTab, str(wordCounter), byteTab, str(byteCounter), '\t', fileName))  
            
        i=i+1
   
    if fileCounter>1:
        print('%s%s%s%s%s%s%s%s' % (lineTab, str(totalLine), wordTab, str(totalWord), byteTab, str(totalByte), '\t', 'total'))