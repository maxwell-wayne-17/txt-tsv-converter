#function for reading information from the data file
#will output a list where an index is a tab separated sentence with a number at the end
def read_file(file_name):

    #list containing tab separated sentances with a number value at the end
    converted_lines = list()
    #variable to track line number to merge relationship and line
    line_num = 0

    #open the file parameter
    with open(file_name, 'r') as f:

        #variables to temporarily hold sentences
        sentence = ""
        sub_sentence = "1\t"
        period_index = 0

        #iterate through lines
        for line in f:

            line_num += 1
            sentence = line

            period_index = sentence.find(".")
            #if no period, go to next line and store current line in subsentence
            while period_index != -1:

                # Case where period is end
                if period_index >= len(sentence) - 1:
                    sub_sentence += sentence[0:period_index]
                # Cases where period may not be end of sentence
                elif sentence[period_index + 1] == '\"' or sentence[period_index + 1] == ')':
                    #Include char and space after period
                    period_index += 2
                    sub_sentence += sentence[0:period_index]
                # Case where period is end of sentence
                else:
                    sub_sentence += sentence[0:period_index]

                # Separate **SENTENCE AND RELATIONSHIP** by tabs
                # (e.g, each index of list is line number \t sentence \t relationship)
                sub_sentence = sub_sentence.strip()
                #sub_sentence = sub_sentence.replace(" ", "\t")
                sub_sentence += "\t" + "-1"
                # Add to list output
                converted_lines.append(sub_sentence)
                # Clear subsentence ** NOT WORKING WITH SENTENCES THAT SPAN LINES **
                sub_sentence = str(line_num) + "\t"

                #Reset sentence and period index
                sentence = sentence[period_index:len(sentence)]
                #Remove period if there
                if (sentence[0] == "."):
                    sentence = sentence[1:len(sentence)]
                #Get next period index
                period_index = sentence.find(".")

            if period_index == -1:
                sub_sentence = sentence.replace("\n", " ")

    return converted_lines

test_list = read_file("../data/test.txt")
correct_list = [
    "1\tHere is the first sentence\t-1",
    "1\tAnother sentence is here\t-1",
    "2\tThis sentence is on a new line\t-1",
    "2\tCorner case includes this, that, other, (ect.)\t-1",
    "2\tHere is another corner case with a quote \"test quote.\"\t-1",
    "3\tNew sentence is here\t-1"
]
# ** test_list is omitting "is" from sentence that spans new line **
print(test_list == correct_list)
print(test_list)






