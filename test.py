# Open the input file in read mode and the output file in write mode
with open('AWS.txt', 'r') as input_file, open('result.txt', 'w') as output_file:
    # Iterate through each line in the input file
    for line in input_file:
        # Check if 'T605' is not in the current line
        if 'T6051' not in line:
            # Write the line to the output file
            output_file.write(line)