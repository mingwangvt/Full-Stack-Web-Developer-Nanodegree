import urllib

def read_text():
    quotes = open("/Users/longxia/Desktop/nanodegree/programming fundamentals and web/6 check profanity/movie_quotes.txt")
        ##open is a build-in function in python standard library, because we do not need to import any library
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("profanity alert!!")
    elif "false" in output:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")
    
read_text()
