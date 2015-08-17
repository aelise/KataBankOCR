"""
Coding Dojo Code Kata - KataBankoOCR
http://www.codingdojo.org/cgi-bin/index.pl?KataBankOCR

Written by Amber Willett: github.com/aelise
"""

import sys


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
      Assumes values are strings and returns one aggregated string. 
  """
  finalseq = ''
  for x in mykeys:
    try:
      finalseq += lookupdict[x]
    except Exception, e:
      finalseq += '?'
  return finalseq


def fileparser(filename,iskeyortest,lookupdict):
  """ Loops through files four lines at a time and
      takes appropriate action based on 'iskeyortest' param 
  """
  with open(filename) as myfile:
    threelines = []
    results = []
    for i,line in enumerate(myfile):
      if i % 4 == 3 and i>0:
        n = rework3x3to1x9(threelines)
        if iskeyortest == 'key':
          results = dict(zip(n,line))
        elif iskeyortest == 'test':
          results.append(charlookup(n,lookupdict))
          threelines = []
        else: 
          print 'Error:Instructions unclear'
      else:
          threelines.append(line)
  return results


def mychecksum(num):
  """ Compares a 9-digit number to the following checksum:
      checksum calculation:
      (d1+2*d2+3*d3 +..+9*d9) mod 11 = 0
      Returns boolean 
  """
  num = str(num)
  check = 0
  for i in range(9):
    check += (i+1)*int(num[8-i])

  if check%11==0:
    return True
  else:
    return False

def offbyone(codestr,acceptdict,offbywhat):
  """ Replaces one char in each code str with the offbywhat param 
  (one char at a time, each in turn) and compares to a checksum 
  function. Returns either a 9-digit str (if there is exactly one 
  off-by-one that passes checksum) or 'AMB' otherwise
  """
  possibles = []
  acceptdict = {v: k for k, v in acceptdict.items()}
  for digit in codestr:
    d = acceptdict(digit)
    for x in offbywhat:
      for y in d:
        d = d[:y] + x + d[y+1:]
        if mychecksum(x)==True:
          if possibles==[]:
            possibles = d
          else:
            return 'AMB'

  if possibles == []:
    return 'AMB'
  else:
    return possibles 




def main(keyfile, testfile):
  """ 
  """
  #Make lookup table for known characters
  numlookupdict = fileparser(keyfile, 'key',[])
  
  #Proceed with actual test data to be parsed
  nums = fileparser(testfile, 'test', numlookupdict)
  
  print 'Story 1:'
  print nums

  #Checksum each num in taggednums and record errors:
  # 'ERR' - failed checksum, 'ILL' - contains unknown char
  taggednums = nums
  for i,x in enumerate(taggednums):
    if x.find('?')==-1:
      if mychecksum(x)==False:
        taggednums[i] = x +' ERR'
    else:
      taggednums[i] = x +' ILL'

  print 'Story 2/3:'
  print taggednums

  #Check ERR/ILL values for missing _ or | which would make
  #valid checksum (label AMB if none are found or multiple 
  #possibilities are found)
  finalnums = taggednums
  for i,x in enumerate(finalnums):
    if x.find('ERR') or x.find('ILL'):
      temp = offbyone(x[:9],numlookupdict,'_| ')
      if temp == 'AMB':
        finalnums[i] = finalnums[i][:9] + ' AMB'
      else:
        finalnums[i] = temp

  print 'Story 4:'
  print finalnums



if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])
