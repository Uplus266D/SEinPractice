"""
>>> import subprocess
>>> subprocess.check_output('python3 wc.py ./testinputs/testLong.txt', shell=True)
b'\\t5\\t14\\t76\\t./testinputs/testLong.txt\\n'
>>> subprocess.check_output('python3 wc.py -c ./testinputs/testShort.txt', shell=True)
b'\\t6\\t./testinputs/testShort.txt\\n'
>>> subprocess.check_output('python3 wc.py -llllllccgccwwa ./testinputs/testNull', shell=True)
b"wc: invalid option -- 'g'\\n"
>>> subprocess.check_output('python3 wc.py -llcl ./testinputs/Test.pdf', shell=True)
b'\\t218\\t46341\\t./testinputs/Test.pdf\\n'
>>> subprocess.check_output('python3 wc.py ./testinputs/testLong.txt ./testinputs/testerNotExist.txt ./testinputs/testLong.txt', shell=True)
b'\\t5\\t14\\t76\\t./testinputs/testLong.txt\\nwc: ./testinputs/testerNotExist.txt : No such file or directory.\\n\\t5\\t14\\t76\\t./testinputs/testLong.txt\\n\\t10\\t28\\t152\\ttotal\\n'
>>> subprocess.check_output('python3 wc.py -', shell=True)
b'wc: - : No such file or directory.\\n'
>>> subprocess.check_output('python3 wc.py ./testinputs/testNumber.txt -wl ./testinputs/testUnicode.txt', shell=True)
b'\\t3\\t3\\t./testinputs/testNumber.txt\\n\\t4\\t4\\t./testinputs/testUnicode.txt\\n\\t7\\t7\\ttotal\\n'
>>> subprocess.check_output('python3 wc.py -test.txt', shell=True)
b"wc: invalid option -- 't'\\n"
>>> subprocess.check_output('python3 wc.py -lwc -', shell=True)
b'wc: - : No such file or directory.\\n'
>>> subprocess.check_output('python3 wc.py l w c', shell=True)
b'wc: l : No such file or directory.\\n'
>>> subprocess.check_output('python3 wc.py -lwc ./testinputs ./testinputs/testUnicode.txt', shell=True)
b'wc: ./testinputs : Is a directory.\\n\\t0\\t0\\t0\\t./testinputs\\n\\t4\\t4\\t13\\t./testinputs/testUnicode.txt\\n\\t4\\t4\\t13\\ttotal\\n'
>>> subprocess.check_output('python3 wc.py ./testinputs/ -wl', shell=True)
b'wc: ./testinputs/ : Is a directory.\\n\\t0\\t0\\t./testinputs/\\n'
>>> subprocess.check_output('python3 wc.py ./testinputs/binarytest.jpg', shell=True)
b'\\t105\\t605\\t50476\\t./testinputs/binarytest.jpg\\n'
>>> subprocess.check_output('python3 wc.py ./testinputs/Test.pdf', shell=True)
b'\\t218\\t1091\\t46341\\t./testinputs/Test.pdf\\n'
>>> subprocess.check_output('python3 wc.py ./testinputs/testUnicode.txt', shell=True)
b'\\t4\\t4\\t13\\t./testinputs/testUnicode.txt\\n'
"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()