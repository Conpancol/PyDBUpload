import csv


class CSVReader:
    def __init__(self):
        self.inputfile = ''

    def readFile(self, csvfile):
        try:

            csvfile_clean = self.fileFilter(csvfile)

        except Exception as exception:
            print(exception)

    def fileFilter(self, csvfile):
        try:
            with open(csvfile, 'r', encoding='utf-8') as f:
                reader = csv.reader(f, dialect="excel-tab")
                for row in reader:
                    print(row)

        except UnicodeDecodeError as exception:
            print(exception)
            input_file = open(csvfile, "rb")
            s = input_file.read()
            print(s)
            input_file.close()
            s = s.replace(b'\xb0', bytes(b'\xc2\xb0'))
            print(s)
            output_file = open(csvfile, "wb")
            output_file.write(s)
            output_file.close()

