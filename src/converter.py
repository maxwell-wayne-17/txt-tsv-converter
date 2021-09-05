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
        sub_sentence = " "
        period_index = 0
        spanned_lines = False

        #iterate through lines
        for line in f:

            if sub_sentence == " ":
                line_num += 1
            else:
                spanned_lines = True

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

                # Case where sentence spanned new line
                add_sentence = str(line_num ) + "\t" + sub_sentence + "\t" + "-1"
                # Add to list output
                converted_lines.append(add_sentence)
                # Clear subsentence
                sub_sentence = ""

                # Correct line number if previous sentence spanned a line
                if spanned_lines:
                    line_num += 1
                    spanned_lines = False

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

print(test_list == correct_list)
print(test_list)






