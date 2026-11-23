class Solution(object):

  def plusOne(self, digits):
    number = int("".join(map(str, digits)))
    number += 1

    inc = []
    while number > 0:
      inc.append(number % 10)
      number //= 10  

    inc.reverse()
    return inc