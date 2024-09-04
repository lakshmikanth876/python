#removing the punctuations from the sentence
punct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
str =  my_str = "Hello!!!, he said ---and went."
nopunct = ""
for char in str:
    if char not in punct:
        nopunct = nopunct + char
print(nopunct)