from string import *

# this is a code file that you can use as a template for submitting your
# solutions


# these are some example strings for use in testing your code

#  target strings

target1 = 'atgacatgcacaagtatgcat'
target2 = 'atgaatgcatggatgtaaatgcag'

# key strings

key10 = 'a'
key11 = 'atg'
key12 = 'atgc'
key13 = 'atgca'

targets = (target1, target2)
keys = (key10, key11, key12, key13)

def countSubStringMatch(target, key):
  instances = 0
  index = 0
  while find(target, key, index) != -1:
    index = find(target, key, index) + 1
    instances+=1
  return instances

def countSubStringMatchRecursive(target, key):
  if find(target, key) == -1: return 0
  else: return countSubStringMatchRecursive(target[find(target,key)+1:],key)+1

def subStringMatchExact(target, key):
  substrings = ()
  index = 0
  while find(target, key, index) != -1:
    index = find(target, key, index) + 1
    substrings += (index, )
  return substrings


### the following procedure you will use in Problem 3


def subStringMatchOneSub(key,target):
    """search for all locations of key in target, with one substitution"""
    allAnswers = ()
    for miss in range(0,len(key)):
        # miss picks location for missing element
        # key1 and key2 are substrings to match
        key1 = key[:miss]
        key2 = key[miss+1:]
        print 'breaking key',key,'into',key1,key2
        # match1 and match2 are tuples of locations of start of matches
        # for each substring in target
        match1 = subStringMatchExact(target,key1)
        match2 = subStringMatchExact(target,key2)
        # when we get here, we have two tuples of start points
        # need to filter pairs to decide which are correct
        filtered = constrainedMatchPair(match1,match2,len(key1))
        allAnswers = allAnswers + filtered
        print 'match1',match1
        print 'match2',match2
        print 'possible matches for',key1,key2,'start at',filtered
    return allAnswers
        

for t in range(0, len(targets)):
  for k in range(0, len(keys)):
    print "target", t+1, "key", k+1
    print countSubStringMatch(targets[t], keys[k]), ' ', \
        countSubStringMatchRecursive(targets[t], keys[k]), ' ', \
        subStringMatchExact(targets[t], keys[k])


