import sys
import json
import csv

cmdargs = len(sys.argv)

if cmdargs != 4:
    print ('Please enter JSON and CSV file names, and type of Data')
    exit()

jsonfile= sys.argv[1]
csvfile = sys.argv[2]
datatype= sys.argv[3]

#jsonfile = 'adapter.json'
#csvfile = 'adapter.csv'
#datatype = 'adapters'


print ('JSON File : ', jsonfile)
print ('CSV File : ', csvfile)
print ('Type of Data :', datatype)

# Opening JSON file and loading the data
# into the variable data


with open(jsonfile) as json_file:
    data = json.load(json_file)
    json_data = data[datatype]

  #  print(json_data)

    # now we will open a file for writing
    with open(csvfile,"w", newline='') as csv_file:

    # create the csv writer object
        csv_writer = csv.writer(csv_file)

      # Counter variable used for writing
      # headers to the CSV file
        count = 0
        for csvline in json_data:
            if count == 0:
            # Writing headers of CSV file
                header = csvline.keys()
                csv_writer.writerow(header)
                count += 1

            #Writing data of CSV file
            csv_writer.writerow(csvline.values())

        csv_file.close()

    json_file.close()

