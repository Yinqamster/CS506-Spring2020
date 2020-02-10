import csv
def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    """   
    data = []
    datafile = open(csv_file_path)
    csv_reader = csv.reader(datafile)
    for row in csv_reader:
            r = []
            for i in range(len(row)):
                    r.append(int(row[i]))
            data.append(r)
    """
    res = []
    with open(csv_file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
                res.append([eval(x) for x in line.split(",")])
    return res
    raise NotImplementedError()
