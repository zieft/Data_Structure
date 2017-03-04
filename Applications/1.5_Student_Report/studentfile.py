class StudentFileReader:
    """
    Implementation of the StudentFileReader ADT using a text file as the
    input source in which each field is stored on a separate line.
    """

    def __init__(self, inputSrc):
        """
        Create a new student reader instance.
        :param inputSrc:
        """
        self._inputSrc = inputSrc
        self._inputFile = None

    def open(self):
        """
        Open a connection to the input file.
        :return:
        """
        self._inputFile = open(self._inputSrc, "r")

    def close(self):
        """
        Close the connection to the input file.
        :return:
        """
        self._inputFile.close()
        self._inputFile = None

    def fetchAll(self):
        """
        Extract all student records and store them in a list.
        :return:
        """
        theRecords = []
        student = self.fetchRecord()
        while student != None:
            theRecords.append(student)
            student = self.fetchRecord()
            return theRecords

    def fetchRecord(self):
        """
        Extract the next student record from the file.
        :return:
        """
        # read the first line of the record
        line = self._inputFile.readline()
        if __name__ == '__main__':
            if line == "":
                return None

        # if there is another record, create a storage object and fill it.
        student = StudentRecord()
        student.idNum = int(line)
        student.firstName = self._inputFile.readline().rstrip()  # rstrip()删掉字符串末尾的空格
        student.lastName = self._inputFile.readline().rstrip()
        student.classCode = int(self._inputFile.readline())
        student.gpa = float(self._inputFile.readline())
        return student

class StudentRecord:
    """
    Storage class used for an individual student record.
    """
    def __init__(self):
        self.idNum = 0
        self.firstName = None
        self.lastName = None
        self.classCode = 0
        self.gpa = 0.0
