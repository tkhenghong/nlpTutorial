import re


def edit_distance(first, second):
    n = len(first)  # column
    m = len(second)  # row

    # Python list comprehension: https://www.w3schools.com/python/python_lists_comprehension.asp
    # Initialize Matrix in Python: https://www.geeksforgeeks.org/initialize-matrix-in-python/
    matrix = [[x + y for x in range(m + 1)] for y in range(n + 1)]
    print('matrix BEFORE: ', matrix)

    column_length = len(matrix)
    row_length = len(matrix[0])
    print('column_length: ', column_length)
    print('row_length: ', row_length)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # column i row j
            print('i: ', i)
            print('j: ', j)

            if first[i - 1] == second[j - 1]:  # Similar
                cost = 0
            else:
                cost = 1

            left_side = matrix[i - 1][j]
            bottom_side = matrix[i][j - 1]
            diagonal_side = matrix[i - 1][j - 1]

            matrix[i][j] = min(left_side + 1, bottom_side + 1, diagonal_side + cost)

    print('matrix AFTER: ', matrix)
    # for i in range(m):
    #     for j in range(n):
    #         # if i == 0:
    #         #     matrix[i][j] = j
    #         # elif j == 0:
    #         #     matrix[i][j] = i
    #         if target[i - 1] == source[j - 1]:  # Similar
    #             matrix[i][j] = matrix[i - 1][j - 1]
    #         else:
    #             cost = 0
    #             if target[i - 1] != source[j - 1]:  # Not similar
    #                 cost = 2
    #                 # move left + 1, move up + 1, diagonally + 2
    #             move_left = matrix[i][j - 1] + 1
    #             move_up = matrix[i - 1][j] + 1
    #             move_diagonally = matrix[i - 1][j - 1] + cost
    #             matrix[i][j] = min(move_left, move_up, move_diagonally)

    response = matrix[n - 1][m - 1]

    return response

def backtrace():
    return



# NLP Homework
# Regex

# https://colab.research.google.com/drive/1Pf1n48GvvQ-DA9hiBCxL9Q-UFp3NR55E#scrollTo=XGnRKzIfs2du

# In the W3C Date Time Format, dates are represented like this: 2009-12-31. Replace the ? in the following Python code with a regular expression, in order to convert the string '2009-12-31' to a list of integers [2009, 12, 31]: [int(n) for n in re.findall(?, '2009-12-31')]
def regexQuestionOne(dateString):
    # Reference: https://stackoverflow.com/a/2841557
    # \d is a digit
    # + means one or more times
    # d+ means 1 or more digits
    return [int(n) for n in re.findall('\d+', dateString)]


# Are you able to write a regular expression to tokenize text in such a way that the word don't is tokenized into do and n't? Explain why this regular expression won't work: «n't|\w+».
def regexQuestionTwo():
    # reads in a text
    # f = open('corpus.txt')
    # raw = f.read()
    matches = re.findall(r'\b(do)(n\'t)', 'don\'t')

    # The correct regular expression: \b(do)(n\'t)
    # Expected output: ['do', 'n't']

    # \w is any word character
    # + means one or more times
    # \w+ means 1 or more word characters

    # Question: Why n't|\w+ is not working?
    # Answer: Because single quote is not escaped, we need to escape n\'t|\w+.

    return matches


# Try to write code to convert text into hAck3r, using regular expressions and substitution,
# where e → 3, i → 1, o → 0, l → |, s → 5, . → 5w33t!, ate → 8.
# Normalize the text to lowercase before converting it. Add more substitutions of your own.
# Now try to map s to two different values: $ for word-initial s, and 5 for word-internal s.
def regexQuestionThird(text):
    """converts a text to hacker"""
    new_text = []

    # initial pass substitutes 8 for ate.
    pattern = re.compile(r'ate')
    text = pattern.sub('8', text)

    # regex that searches through the text to find instances of the letters to be converted.
    pattern = re.compile(r'[eiols]|\.')

    # converts all the letters
    for w in text:
        if re.search(pattern, w):
            if w == 'e':
                w = '3'
            elif w == 'i':
                w = '1'
            elif w == 'o':
                w = '0'
            elif w == 's':
                w = '5'
            elif w == 'l':
                w = '|'
            elif w == '.':
                w = '5w33t!'
        new_text.extend(w)
    new_text = ''.join(new_text)

    # regex searching for word initial s.
    pattern = re.compile(r'\b5')
    new_text = pattern.sub('$', new_text)

    return new_text


# Backtrack
# https://docs.google.com/document/d/1GbR6HftTPwJ5YhdjCkQWWjyvpq6cCoz7wf0f7dTsP30/edit


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # array = regexQuestionOne('2009-12-31') # --> ['2009', '12', '31'] -> [2009, 12, 31]
    # print(array)

    matches = regexQuestionTwo()
    print(matches)

    text = regexQuestionThird('hacker')
    print(text)
    text2 = regexQuestionThird('hate')
    print(text2)
    text3 = regexQuestionThird('sweet')
    print(text3)
    text4 = regexQuestionThird('...')
    print(text4)

    answer = edit_distance("execution", "intention")
    print(answer)

