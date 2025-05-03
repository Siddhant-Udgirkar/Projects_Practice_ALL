"""
If Vowel Print 0,
Else Consonant 1
"""

user_input= input("Enter a letter: ").lower()
vowels= ["a", "e", "i", "o" ,"u" ]


if user_input in vowels:
    print(0)
else:
    print(1)

