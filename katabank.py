import sys


def rework(threelines):
  """ """
  #Takes an array of three lines, X characters and reworks to 
  #an array of X lines, 12 characters each
  #(each 12-char line in the output consists of 3 characters from 
  #each row, appended with those above/below them)
  #assumes each line ends with carriage return (\n)
  result = []
  temp = range(len(threelines[0])-2)
  for i,y in enumerate(temp[0::3]):
    result.append([])
    for x in range(3):
      result[i].extend(threelines[x][y:y+3])
  return [''.join(result[i]) for i,x in enumerate(result)]


def charlookup(codes,lookupdict):
  """ """
  finalseq = ''
  for x in codes:
    finalseq += lookupdict[x]
  return finalseq



def fileparser(filename,iskeyortest,lookupdict):
  """ Loops through files four lines at a time and
  takes appropriate action based on 'iskeyortest' param """
  #

  with open(filename) as myfile:
    threelines = []
    results = []
    for i,line in enumerate(myfile):
      if i % 4 == 3 and i>0:
        n = rework(threelines)
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


def main(keyfile, testfile):
  """ """

  #
  numlookupdict = fileparser(keyfile, 'key',[])
  
  #
  finalnums = fileparser(testfile, 'test', numlookupdict)

  print finalnums 


if __name__ == '__main__':
    main(sys.argv[1],sys.argv[2])
