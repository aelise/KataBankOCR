import katabank

test=[' _     _  _     _  _  _  _  _ \n',
      '| |  | _| _||_||_ |_   ||_||_|\n',
      '|_|  ||_  _|  | _||_|  ||_| _|\n'] 

temp = katabank.rework3x3to1x9(test)
temp==[' _ | ||_|',
 '     |  |',
 ' _  _||_ ',
 ' _  _| _|',
 '   |_|  |',
 ' _ |_  _|',
 ' _ |_ |_|',
 ' _   |  |',
 ' _ |_||_|',
 ' _ |_| _|']

tempdict = katabank.fileparser('mykeyfile.txt','key',[])
temp==tempdict

katabank.charlookup(temp,tempdict)

temp2=[' _ | ||_|',
 '_    |  |',
 ' _  _||_ ',
 ' _  _| _|',
 '   |_|  |',
 ' _ |_  _|',
 ' _  _ |_|',
 ' _   |  |',
 ' _ |_||_|',
 ' _ |_| _|']

katabank.charlookup(temp2,tempdict)

wholetest = katabank.fileparser('testdata.txt','test',tempdict)

run katabank 'mykeyfile.txt' 'testdata.txt'

katabank.mychecksum('457508000')==True
katabank.mychecksum('664371495')==False