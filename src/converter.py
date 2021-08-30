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
            period_index = sentence.find(".")
            #if no period, go to next line and store current line in subsentence
            if period_index == -1:
                #replace newline with space
                sentence.replace("\n", " ")
                #store current line in sub_sentence
                sub_sentence += sentence
            else:
                #Cases where period may not be end of sentence
                if sentence[period_index + 1] == '\"' or sentence[period_index + 1] == ')':
                    sub_sentence += sentence.su






