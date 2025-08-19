Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
>>> this_list = ["panda", "lion", "giraffe", "tiger", "elephant", "monkey", "fish", "snake", "bearded dragon", "koala"]
... 
... def feeding(this_list):
...     if len(this_list) == 1:
...         print("The " + this_list[0] + " has been fed")
...     else:
...         MidOfList = len(this_list) // 2
...         first_half = this_list[:MidOfList]
...         second_half = this_list[MidOfList:]
...         feeding(first_half)
...         feeding(second_half)
... 
