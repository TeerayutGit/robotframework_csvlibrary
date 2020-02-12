import csv

class csvlibrary(object):
    """ Reads a given CSV file and returns it as a dictionary. """
    def read_csv_as_dictionary_by_column_value(self, filename, key_column, value_columns):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            output = {}
            for row in reader:
                if type(value_columns) == str:
                    output[row[key_column]] = row[value_columns]
                elif type(value_columns) == list:
                    valueList = []
                    for value in value_columns:
                        valueList.append(row[value])
                    output[row[key_column]] = valueList

        csvfile.close()
        return output

    def read_csv_as_dictionary_by_column(self, filename, key_column):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            output = {}
            for row in reader:
                output[row[key_column]] = row

        csvfile.close()
        return output

    """ Reads a given CSV file and returns it as a list containing all rows as list. """

    def read_csv_as_list(self, filename, delimiter='\n'):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            output = []
            for row in csvfile:
                output.append(row)
        csvfile.close()
        return output

    """ Reads a given CSV file and returns it as a single list containing all values. """

    def read_csv_as_single_list(self, filename, delimiter='\n'):
        with open(filename, newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            output = []
            for row in reader:
                output.append(row)
        csvfile.close()
        return output
