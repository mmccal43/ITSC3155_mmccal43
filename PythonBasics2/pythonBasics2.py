# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  # YOUR CODE HERE
  threes = (int)(n/3)
  return threes


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  # YOUR CODE HERE
  character = ''
  count = 0
  mostChar = ''
  highCount = 0
  for i in s:
      if i == character:
          count += 1
          if count > highCount:
              mostChar = character
              highCount = count
      else:
          if count > highCount:
              mostChar = character
              highCount = count
          character = i
          count = 1
  return mostChar


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  # YOUR CODE HERE
  sc = s.lower()
  sc = sc.replace(' ', '')
  rs = sc [::-1]
  if(sc == rs):
      return True
  else:
      return False
  #listWord = []
  #revList = []
  #ls = s.lower()
  #for i in range(len(ls)):
  #    if s[i] != ' ':
  #        listWord.append(ls[i])
  #revList = listWord
  #revList = revList.reverse()
  #print(listWord)
  #print(revList)
  #if listWord == listWord.reverse():
  #    return True
  #else:
   #   return False