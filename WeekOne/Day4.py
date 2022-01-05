
def alphabet_position(text):
    
    # create a string of alphabets
    letters = "abcdefghijklmnopqrstuvwxyz"

    #change text to lower case
    text = text.lower()
    
    return " ".join([str(letters.find(i)+1) for i in text if i in letters])

text = "The narwhal bacons 10 at midnight."

print(alphabet_position(text))