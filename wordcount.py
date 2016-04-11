# put your code here.
def counting_words(filename):
    """return number of word occurrences in the text file 
    """
    #open the file and create an empty dictionary
    text = open(filename)
    word_counts = {}
    #looping through each line and stripping the white space, splitting 
    #into single words
    for line in text:
        line.rstrip()
        words = line.split()
    #looping through the words in each list for single lines
        for word in words:
            # if the word exist as a key, return the value and add 1
            # if the word does not exist, create as a key and start count at 1
            # .get() will return default of 0 if word is not yet a key
            word_counts[word] = word_counts.get(word, 0) + 1

    print word_counts

#counting_words("test.txt")