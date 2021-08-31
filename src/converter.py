#function for reading information from the data file
#will output a list where an index is a tab separated sentence with a number at the end
def read_file(file_name):

    #list containing tab separated sentances with a number value at the end
    converted_lines = list()

    #open the file parameter
    with open(file_name, 'r') as f:

        #variables to temporarily hold sentences
        sentence = ""
        sub_sentence = ""
        period_index = 0

        #iterate through lines
        for line in f:

            sentence = line
            #Need to add while period_index != -1, change logic here
            period_index = sentence.find(".")
            #if no period, go to next line and store current line in subsentence
            if period_index == -1:
                #replace newline with space
                sentence.replace("\n", " ")
                #store current line in sub_sentence
                sub_sentence += sentence
            else:
                #Cases where period may not be end of sentence
                if len(sentence) < period_index and \
                        (sentence[period_index + 1] == '\"' or sentence[period_index + 1] == ')'):
                    sub_sentence += sentence[0:period_index + 2]
                #Case where period is end of sentence
                else:
                    sub_sentence += sentence[0:period_index + 1]

                #Separate words by tabs
                sub_sentence.replace(" ", "\t")
                sub_sentence += "\t-1"
                #Add to list output
                converted_lines.append(sub_sentence)
                #Clear subsentence
                sub_sentence = ""

    return converted_lines

test_list = read_file("../data/test.txt")
print(test_list)






