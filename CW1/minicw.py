if __name__ == "__main__":
    import sys
    
    try:
        fileName = sys.argv[1]
        fileCounted = open(fileName, 'r')
        fileContents = fileCounted.read()
    except:
        print("Error:", fileName, ": No such file or directory.")
    else:
        fileCounted.close()
        
        try:
            wordCounter = len(fileContents.split())
            lineCounter = 0
            byteCounter = 0
            
            with open(fileName, 'r') as fileForLine:
                for line in fileForLine:
                    lineCounter += 1
                    byteCounter += len(line.strip())    #count the number of character in each line.
            byteCounter += lineCounter                  #count the line breaker in.
        except:
            print("Error: We don't handle that situation yet!")
        else:
            print(lineCounter, '\t', wordCounter, '\t', byteCounter, '\t', fileName)
    
    