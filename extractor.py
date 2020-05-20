###Python script that takes in a youtube video transcript and returns the time stamp in which it occurs

def stamp_extractor(file):
    '''funtion takes in a file and retuns an array of the file'''
    with open(file)as f:
        transcript = f.read().splitlines()
        return transcript


def word_finder(array, words):
    """Function takes in an array, that contains interleved entries of time stamp
    and phrase at that time stap. will search for words and return the time stamp
    at which the occur"""
    time_stamp_list = []
    search_words = words
    for word in search_words:
        time_stamp_list.append(word)
        for index, temp in enumerate(array):
            if(word.lower() in temp.lower()):
                time_stamp_list.append(array[index-1])
    return time_stamp_list

if __name__ == "__main__":
    holder = stamp_extractor("/home/jason/time_stamp_extractor/transcript.txt")
    stop_condition = True
    search_term = []
    while(stop_condition):
        temp = input("Enter a search term, enter n to stop and perform the stop")
        if(temp == "n"):
            stop_condition = False
        else:
            search_term.append(temp)

    print(word_finder(holder, search_terms))
