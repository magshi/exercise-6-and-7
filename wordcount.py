# read every line, split by space
# uses the get function to see if the key already exists
# if the key exists, up the counter by one
# if the key doesn't yet exist, create it and increment by one
# for each key, print its value i.e. for key, value in dictionary_name,
# print key, value

def main():
    text = open("twain.txt")
    word_list = []
    count_list = []
    word_dict = {}
    wordcount_dict = {}

    for line in text:
        line = line.rstrip()
        line = line.lower()
        cleaned_line = ""
        for char in line:
            if ord(str(char)) >= 97 and ord(str(char)) <= 122:
                pass
            else:
                char = " "
            cleaned_line += char
        word_list += cleaned_line.split(" ")

    for word in word_list:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1 

    for key, value in word_dict.iteritems():
#        print key, value
        if value in wordcount_dict.keys():
            wordcount_dict[value].append(key)
        else:
            wordcount_dict[value] = [key]

    for key, value in wordcount_dict.iteritems():
        value.sort()
        count_list.append(key)

    count_list.sort()
    count_list.reverse()

    for count in count_list:
        for word in wordcount_dict[count]:
            print count, word
        # print wordcount_dict[count], count

if __name__ == "__main__":
    main()