from random import choice

#open the file and assign its content to a variable
# var = raw_input("Tell me what you want to know about: ")

file = open ('conspiracies.txt', 'r')
text = file.read()
file.close()


#clear out all the equal signs from the headings
text=text.replace("=","")
#convert the text to a list of words that can be iterated over
words=text.split()


# list of keys that can be checked against the ditionary to decide when a sentence needs to end
end_sentence=[]
#create a dictionary to store pairs of adjacent words
transition_states= {}
#inital values for defining our dictionary keys
last1=''
last2=''


for word in words:
    if last1 !='' and last2 !='':
        #update the word_state to have the previous two words
        word_state=(last2,last1)

#if the current key sequence is already inside our dictionary add a new character to its list of potential values
        if word_state in transition_states:
            transition_states[word_state].append(word)
        else:
            #make a key-value pair out of the previous two words and the current one
            transition_states[word_state]=[word]

        # specify word sequences that end sentences and put them into a separate list to check from
        if (last1[-1:] == '.' or last1[-1] == '?' or last1[-1:] == '!'):
            end_sentence.append(word_state)

    # move on to the next words in the sequence
    last2=last1
    last1=word

#reset key
word_state=()
new_string=''
#select the number of words for generator, this will likely peak at around 60
for i in range(100):
    if word_state in transition_states:
        #find a random word from the given word_state's value list
        word=choice(transition_states[word_state])
        #add the new word to the output string
        new_string=new_string+' '+word
        #update the word_state to a key with the current word
        word_state=(word_state[1],word)
        #if current key has a value ending a sentence, pick another one that will lead to the end of a sentence
        if word_state in end_sentence:
            word_state=choice(end_sentence)
    #pick a word state that will be inside the the dictionary, and complete a phrase
    else:
        word_state = choice(end_sentence)
# print the output


for i in range(len(new_string)):
    if new_string[-1] != '.':
        new_string=new_string[:-1]
    else:
        break


print(new_string)
