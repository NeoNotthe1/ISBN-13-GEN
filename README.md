# ISBN-13 Code Generator
 The last digit of an ISBN for a book is a check digit calculated using simple arithmetic.
 There are number of ways of calculating the check digit but one of the most frequently used methods is to
 use the first 12 digits in the ISBN, each individual digit in the string is multiplied by 1 if it is in an
 odd numbered position such as 1st, 3rd and so on,
 multiplied by 3 if it is an even numbered position such as 2nd, 4th and so on
 Then the resulting numbers are added together and divided by 10. If the remainder is 0 that becomes the check digit
 Otherwise the remainder is subtracted from 10 and that becomes the check digit. This is then added to the string,
 In this case as the 13th digit of the ISBN.
