import katabank

test=[' _     _  _     _  _  _  _  _ \n',
      '| |  | _| _||_||_ |_   ||_||_|\n',
      '|_|  ||_  _|  | _||_|  ||_| _|\n'] 

temp = katabank.rework(test)
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

temp2 = katabank.fileparser('mykeyfile.txt','key',[])

temp==temp2

katabank.charlookup(' _ | ||_|',temp2)
