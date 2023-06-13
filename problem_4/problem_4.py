max = 9009 # 91 * 99

for i in range(100,1000):
    for j in range(100,1000):
        sum = i * j
        # we can use 2 methods in python
        # 1. convert to string and check if it is palindrome
        # 2. use % and // to get the digits and check if it is palindrome
        # I will use the 2nd method because first one is too easy
        lst = [] # list to store the digits
        while sum > 0:
            lst.append(sum % 10)
            sum = sum // 10
        reverse_nth = -1 # to get the nth digit from the end
        n = 0 # to get the nth digit from the start
        is_palindrome = True # to check if it is palindrome
        while n < len(lst) // 2 : # because we only need to check half of the digits
            if lst[n] != lst[reverse_nth]:
                is_palindrome = False
                break
            n += 1
            reverse_nth -= 1
        if is_palindrome and max < i * j:
            max = i * j

print(max)

# answer: 906609
