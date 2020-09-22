import os

DATADIR = "C:\Temp\PythonSamples\data_wrangling\csv\\resources\\"
DATAFILE = "beatles-discography.csv"

'''
This function reads the input DATAFILE line by line, 
and for the first 10 lines (not including the header)

split each line on "," 
and then for each line, create a dictionary where the key is the header title of the field, 
and the value is the value of that field in the row.

The function parse_file returns a list of dictionaries,
each data line in the file being a single list entry.
'''
def parse_file(datafile):
    data = []
    with open(datafile, "r") as f:
        # The line below gives us a list of values that we can use as keys
        # for each one of the data items that we pull out of this file. 
        header = f.readline().split(",")
        counter = 0
        for line in f:
            if counter == 10:
                break

            # We split every line using the coma as a delimiter 
            fields = line.split(",")
            entry = {}
            
            # An enumerate gets an index value in addition to the value for each item in the fields list
            for i, value in enumerate(fields):
                # access the appropriate value in the header to use as a key for that particular field in our entry
                # string method strip() removes the extra whitespace
                entry[header[i].strip()] = value.strip()

            data.append(entry)
            counter += 1
    return data


def test():
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum', 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964', 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline
    print(d[0])
    
test()