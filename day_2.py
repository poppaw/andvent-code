def import_spreadsheet():
    '''convert all raws from file to one list'''
    listed_raws = []
    with open("input2.txt") as f:
        for line in f:
            for raw in line.rstrip().split("\t"):
                listed_raws.append(raw)
    #print (listed_raws)
    return listed_raws


def count_checksum0(listed_raws):
    checksum = 0
    for element in listed_raws:
        difference = int(max(element)) - int(min(element))
        checksum += difference
    print (checksum)
    return checksum

        
#listed_raws = import_spreadsheet()
#count_checksum0(listed_raws)

# Task 1
def spreadsheet_input():
    '''Return raws from input files
    as a list of listed raws for each line'''
    listed_lines = []
    with open("input2.txt", "r") as f:
        for line in f:
            listed_lines.append([int(raw) for raw in line.split("\t")])
    print (listed_lines)
    return listed_lines


def count_checksum(listed_lines):
    checksum = 0
    for row in listed_lines:
        diff = max(row) - min(row)
        checksum += diff
    print (checksum)
    return checksum

# Task 2
def sum_natural_divisions_results(listed_lines):
    sum_of_divisions = 0
    for line in listed_lines:
        for el in line:
            for i in range(len(line)):
                if el != line[i] and el % line[i] == 0:
                    sum_of_divisions += el / line[i]
    print (sum_of_divisions)
    return sum_of_divisions






listed_lines = spreadsheet_input()
count_checksum(listed_lines)
sum_natural_divisions_results(listed_lines)


