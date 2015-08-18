"""
Coding Dojo Code Kata - KataBankoOCR
http://www.codingdojo.org/cgi-bin/index.pl?KataBankOCR

Written by Amber Willett: github.com/aelise
"""

import sys

class AccountNumber():

  def __init__(self, underscoresandpipes, lookupdict):
    self.codes = rework3x3to1x9(underscoresandpipes)
    self.num = charlookup(self.codes, lookupdict)


def rework3x3to1x9(threelines):
  """ Takes an array of three lines, X*3 characters each and reworks  
      to an array of X lines, 9 characters each
  """
  #(each 9-char line in the output consists of 3 characters from 
  #each row, appended with those above/below them)
  #assumes each line ends with carriage return (\n)
  result = []
  temp = range(len(threelines[0])-2)
  for i,y in enumerate(temp[0::3]):
    result.append([])
    for x in range(3):
      result[i].extend(threelines[x][y:y+3])
  return [''.join(result[i]) for i,x in enumerate(result)]


def charlookup(mykeys,lookupdict):
  """ Simple dict lookup for a list of keys
      Assumes values are strings and returns a list of characters. 
  """
  finalseq = []
  for x in mykeys:
    try:
      finalseq.append(lookupdict[x])
    except Exception, e:
      finalseq += '?'
  return finalseq


def getlookuptable(filename):
  """ Makes lookup table for mapping characters to their 3x3 
      representation. 
  """
  with open(filename) as myfile:
    threelines = []
    for i,line in enumerate(myfile):
      if i == 3:
        n = rework3x3to1x9(threelines)
        results = dict(zip(n,line))
      else:
        threelines.append(line)
  return results


def fileparser(filename,lookupdict):
  """ Loops through file four lines at a time and returns a
      list of account number objects (having translated the numbers)
  """
  results = []
  threelines = []
  with open(filename) as myfile:
    for i,line in enumerate(myfile):
      if i % 4 == 3 and i>0:
        results.append(AccountNumber(threelines, lookupdict))
        threelines = []
      else:
        threelines.append(line)
  return results


def mychecksum(num):
  """ Compares a 9-digit number to the following checksum:
      (d1+2*d2+3*d3 +..+9*d9) mod 11 = 0
      Returns boolean 
      Assumes arg is a list of either ints or strings 
      (or a single string)
  """
  if '?' in num:
    return False

  check = 0
  for i in range(9):
    check += (i+1) * int(num[8-i])

  if check % 11 == 0:
    return True
  else:
    return False


def offbyone(codelist,acceptdict,offbywhat):
  """ Replaces one char in each code str with the offbywhat param 
      (one char at a time, each in turn) and compares to a checksum 
      function. Returns either a list of 9 digits (if there is exactly one 
      off-by-one that passes checksum) or 'AMB' otherwise
  """
  possibles = []
  for i,code in enumerate(codelist):
    for x in offbywhat:
      for j,y in enumerate(code):
        newcode = code[:j] + x + code[j+1:]
        codelist[i] = newcode
        newnum = charlookup(codelist, acceptdict)
        if (newcode in acceptdict) and (mychecksum(newnum) == True):
          if possibles == []:
            possibles = newnum
          else:
            return ' AMB'

  if possibles == []:
    return ' AMB'
  else:
    return possibles 


def main(keyfile, testfile):
  """ 
  """
  #Make lookup table for known characters
  numlookupdict = getlookuptable(keyfile)
  
  #Proceed with actual test data to be parsed
  nums = fileparser(testfile, numlookupdict)
  
  print 'Story 1:'
  print [''.join(x.num) for x in nums]

  #Checksum each num in taggednums and record errors:
  # 'ERR' - failed checksum, 'ILL' - contains unknown char
  taggednums = nums
  for x in taggednums:
    if '?' in x.num:
      x.num.append(' ILL')
    else:
      if mychecksum(x.num) == False:
        x.num.append(' ERR')
      

  print 'Story 2/3:'
  print [''.join(x.num) for x in taggednums]

  #Check ERR/ILL values for missing _ or | which would make
  #valid checksum (label AMB if none are found or multiple 
  #possibilities are found)
  finalnums = taggednums
  for y in finalnums:
    if ' ERR' in y.num or ' ILL' in y.num:
      temp = offbyone(y.codes, numlookupdict, '_| ')
      if temp == ' AMB':
        y.num.append(' AMB')
      else:
        y.num = temp

  print 'Story 4:'
  print [''.join(x.num) for x in finalnums]


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
