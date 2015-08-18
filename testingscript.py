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

tempdict = katabank.getlookuptable('mykeyfile.txt')
tempdict[' _ |_  _|']=='5'

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
katabank.mychecksum(['6', '6', '4', '3', '7', '1', '4', '9', '5'])==False

katabank.offbyone(temp2,tempdict,'_| ')