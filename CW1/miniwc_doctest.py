"""
>>> import subprocess
>>> subprocess.check_output('python3 minicw.py ./testinputs/testLong.txt', shell=True)
b'5 \\t 14 \\t 76 \\t ./testinputs/testLong.txt\\n'
>>> subprocess.check_output('python3 minicw.py ./testinputs/testShort.txt', shell=True)
b'1 \\t 2 \\t 17 \\t ./testinputs/testShort.txt\\n'
>>> subprocess.check_output('python3 minicw.py ./testinputs/testNull', shell=True)
b'0 \\t 0 \\t 0 \\t ./testinputs/testNull\\n'
>>> subprocess.check_output('python3 minicw.py ./testinputs/testerNotExist.txt', shell=True)
b'Error: ./testinputs/testerNotExist.txt : No such file or directory.\\n'
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()