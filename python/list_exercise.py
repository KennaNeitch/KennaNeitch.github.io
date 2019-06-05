# create list
# conditional: stem search - if it has col*, make it color
#store the data
words = ["color", "colour", "target", "rainbow", "theatre", "theater"]
# for word in words:
#     if word == stem(col)
#         print(color)

#compare the words in some way - a la stemming

#create new empty list
new_list = []
#make a dictionary with {"standard_spelling": "variant"}
spellings = {"colour": "color", "theatre": "theater"}
#loop over the list
for word in words:
        #if a word is alternatively spelled
        # correct the spelling using the spellings dictionary
        # add that corrected words
    if word in spellings:
        corrected_word = spellings[word]
        new_list.append(corrected_word)
    else:
        # if a word if traditionally spelled, do something else
        new_list.append(word)
print(new_list)
