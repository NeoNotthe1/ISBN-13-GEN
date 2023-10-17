# ISBN 13th digit generator

# The last digit of an ISBN for a book is a check digit calculated using simple arithmetic.
# There are number of ways of calculating the check digit but one of the most frequently used methods is to
# use the first 12 digits in the ISBN, each individual digit in the string is multiplied by 1 if it is in an
# odd numbered position such as 1st, 3rd and so on,
# multiplied by 3 if it is an even numbered position such as 2nd, 4th and so on
# Then the resulting numbers are added together and divided by 10. If the remainder is 0 that becomes the check digit
# Otherwise the remainder is subtracted from 10 and that becomes the check digit. This is then added to the string,
# In this case as the 13th digit of the ISBN.

def chk_digit():
    twelve_num = input("Enter your 12 digit ISBN code -> ")
    if len(twelve_num) == 12:
        list_num = list(twelve_num)  # This creates alphanumeric list
        total_even_digit = 0  # global variable to calculate the total of even numbered position digits.
        total_odd_digit = 0  # same concept as the above comment.
        for i in range(len(list_num)):  # The var I is the index number to see whether it is an even positioned or odd.
            if i % 2 == 0:  # if it is 0 then it means the index 0 is considered to be 1 and that is an odd position.
                value_one = int(list_num[i])  # the list is string but the number must be calculated this converts it -
                # - into int
                odd_digit = value_one * 1  # This is the arithmetic part of the formula
                total_odd_digit += odd_digit  # This stores the total of even digits

            elif i % 2 != 0:
                value_two = int(list_num[i])  # This converts odd string number into odd integers
                even_digit = value_two * 3  # This is the arithmetic part of the formula
                total_even_digit += even_digit  # This stores the total of odd digits

        whole_digit = total_odd_digit + total_even_digit  # this is the final total of even and odd together
        if whole_digit % 10 == 0:  # If the remainder is zero that whole digit becomes the Check Digit
            new_string = str(whole_digit)  # This converts the whole digit back to string or an alphanumeric list
            list_num.append(new_string)  # after conversion the check digit is stored in the end
            delimiter_one = ""
            check_digit_isbn = delimiter_one.join(list_num)
            print("\n your 13TH number ISBN code is -> ", check_digit_isbn)  # The Final Showdown!!
        elif whole_digit % 10 != 0:
            remainder = whole_digit % 10
            ''' if the remainder is not zero according to the formula remainder must be subtracted from 10 '''
            new_digit = 10 - remainder
            new_string_two = str(new_digit)
            list_num.append(new_string_two)
            delimiter = ""
            check_digit_isbn_two = delimiter.join(list_num)
            print("\n your 13TH number ISBN code is -> ", check_digit_isbn_two)

    elif len(twelve_num) < 12:
        print("Feed me 12 Digits of code please...|-> ")
        x = input("Do you wish to try again? Y/N -> ")
        if x == "Y":
            chk_digit()
        else:
            print("Goodbye Friend")
            exit()


chk_digit()
