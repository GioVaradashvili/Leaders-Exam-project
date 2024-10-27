# Your task is to sort a given string. Each word in the string will contain a single number. This number is the position the word should have in the result.

# NOTE: Numbers can be from 1 to 9. So 1 will be the first word (not 0).

# If the input string is empty, return an empty string. The words in the input String will only contain valid consecutive numbers.

# Examples:
# "is2 Thi1s T4est 3a"  -->  "Thi1s is2 3a T4est"
# "4 of Fo1r people g3ood th5e the2"  -->  "Fo1r the2 g3ood 4 of th5e people"
# ""  -->  ""


number = [1,2,3,4,5,6,7,8,9,10,]

def sort_by_number(s):
    words = s.split()
    index = len(words)
    oldest_number = []
    for word in words:
        for num in number:
            if str(num) in word:
                oldest_number.append(word)
                index -= 1
                break
            if num == number[-1]:
                oldest_number.append(word)
            if index == 0:
                return oldest_number

print(sort_by_number("is2 Thi1s T4est 3a"))