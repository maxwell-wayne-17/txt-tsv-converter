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
            while period_index != -1:
                # Cases where period may not be end of sentence
                sentence_length = len(sentence)

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

                # Separate words by tabs
                sub_sentence = sub_sentence.strip()
                sub_sentence = sub_sentence.replace(" ", "\t")
                sub_sentence += "\t" + "-1"
                # Add to list output
                converted_lines.append(sub_sentence)
                # Clear subsentence
                sub_sentence = ""

                #Reset sentence and period index
                sentence = sentence[period_index:len(sentence) - 1]
                #Remove period if there
                if (sentence[0] == "."):
                    sentence = sentence[1:len(sentence) - 1]
                #Get next period index
                period_index = sentence.find(".")

            if period_index == -1:
                sub_sentence = sentence.replace("\n", " ")

    return converted_lines

test_list = read_file("../data/test.txt")
correct_list = [
    "Here\tis\tthe\tfirst\tsentence\t-1",
    "Another\tsentence\tis\there\t-1",
    "This\tsentence\tis\ton\ta\tnew\tline\t-1",
    "Corner\tcase\tincludes\tthis,\tthat,\tother,\t(ect.)\t-1",
    "Here\tis\tanother\tcorner\tcase\twith\ta\tquote\t\"test\tquote.\"\t-1",
    "New\tsentence\tis\there\t-1"
]
# ** test_list is omitting "is" from sentence that spans new line **
print(test_list == correct_list)
print(test_list)






