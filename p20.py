mylist = [13,26,56,85,65,108,29]
result = list(filter(lambda x: (x % 13 == 0),mylist))
print("numbers divisible by 13 are ",result)