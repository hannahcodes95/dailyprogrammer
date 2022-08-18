# For the purpose of today's challenge, a Roman numeral is a non-empty string of the characters M, D, C, L, X, V, and I,
# each of which has the value 1000, 500, 100, 50, 10, 5, and 1. The characters are arranged in descending order, and the
# total value of the numeral is the sum of the values of its characters. For example, the numeral MDCCXXVIIII has the
# value 1000 + 500 + 2x100 + 2x10 + 5 + 4x1 = 1729. This challenge uses only additive notation for roman numerals.
# There's also subtractive notation, where 9 would be written as IX. You don't need to handle subtractive notation
# (but you can if you want to, as an optional bonus).
# Given two Roman numerals, return whether the first one is less than the second one:


# numcompare("I", "I") => false
# numcompare("I", "II") => true
# numcompare("II", "I") => false
# numcompare("V", "IIII") => false
# numcompare("MDCLXV", "MDCLXVI") => true
# numcompare("MM", "MDCCCCLXXXXVIIII") => false
# You only need to correctly handle the case where there are at most 1 each of D, L, and V, and at most 4 each of C, X,
# and I. You don't need to validate the input, but you can if you want. Any behavior for invalid inputs like numcompare
# ("V", "IIIIIIIIII") is fine - true, false, or error.

numeral_dict = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}


def additive_roman_numeral(*args):

   number = 0
   numeral_input = input("Enter a Roman numeral: ").split()
   for value in numeral_input:
      number += numeral_dict.get(value)

   print(number)

# additive_roman_numeral()


def subtractive_roman_numeral(input):

   number = 0
   numeral_input = list(input.replace(" ", ""))
   # numeral_input = input("Enter a Roman numeral: ").split()
   for i, value in enumerate(numeral_input):
      if i < (len(numeral_input) -1) and numeral_dict.get(numeral_input[i+1]) > numeral_dict.get(value):
         number -= numeral_dict.get(value)
      else:
         number += numeral_dict.get(value)

   return number

# subtractive_roman_numeral('X L')


def compare_numeral_values(numeral1, numeral2):
   return subtractive_roman_numeral(numeral1) < subtractive_roman_numeral(numeral2)

print(compare_numeral_values('X  L', 'X X'))


