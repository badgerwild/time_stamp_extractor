###Python script that takes in a youtube video transcript and returns the time stamp in which it occurs

def stamp_extractor(file):
#funtion takes in a file and retuns an array of the file
    with open(file)as f:
        transcript = f.read().splitlines()
        return transcript


def word_finder()
if __name__ == "__main__":
    stamp_extractor("/home/jason/time_stamp_extractor/transcript.txt")
