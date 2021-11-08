import xml.etree.ElementTree as eTree
import lxml.etree as ET
import xml.sax


class XML:
    fileName: str

    def __init__(self, fileName):
        self.fileName = fileName
        try:
            self.file = open(self.fileName, "r")
        except FileNotFoundError:
            print("File not found")


def search(fileName, ISearcher, filter):
    return (ISearcher.search(fileName, filter))


class ISearcher:
    def search(self, fileName, filter):
        pass


class SAX_Searcher(ISearcher):
    def search(self, fileName, filter):
        parser = xml.sax.make_parser()
        parser.setFeature(xml.sax.handler.feature_namespaces, 0)

        Handler = StudentsHandler(filter)
        parser.setContentHandler(Handler)
        parser.parse(fileName)
        return Handler.result


class DOM_Searcher(ISearcher):
    def search(self, fileName, filter):
        tree = eTree.parse(fileName)

        rootXML = tree.getroot()
        result = []
        for child in rootXML:
            student = Student()
            is_Valid = True
            for key, value in child.attrib.items():
                if (key == 'Name'):
                    if ('Name' not in filter or filter['Name'] == value):
                        student.Name_Surname = value
                    else:
                        is_Valid = False
                        break
                if (key == 'Faculty'):
                    if ('Faculty' not in filter or filter['Faculty'] == value):
                        student.Faculty = value
                    else:
                        is_Valid = False
                        break
                if (key == 'Department'):
                    if ('Department' not in filter or filter['Department'] == value):
                        student.Department = value
                    else:
                        is_Valid = False
                        break
                if (key == 'Course'):
                    if ('Course' not in filter or filter['Course'] == value):
                        student.Course = value
                    else:
                        is_Valid = False
                        break
                if (key == 'Mark'):
                    if ('Mark' not in filter or filter['Mark'] == value):
                        student.Mark = value
                    else:
                        is_Valid = False
                        break
            if (is_Valid):
                result.append(student)
        return result


class Student:
    Name_Surname: str
    Faculty: str
    Department: str
    Course: str
    Mark: str

    def __init__(self):
        self.Name_Surname = ''
        self.Faculty = ''
        self.Department = ''
        self.Course = ''
        self.Mark = ''


class StudentsHandler(xml.sax.ContentHandler):
    def __init__(self, filter):
        self.filter = filter
        self.result = []

    def startElement(self, tag, attributes):
        if tag == "student":
            student1 = Student()
            if 'Name' not in self.filter or self.filter['Name'] == attributes["Name"]:
                student1.Name_Surname = attributes["Name"]
            else:
                return
            if ('Faculty' not in self.filter or self.filter['Faculty'] == attributes["Faculty"]):
                student1.Faculty = attributes["Faculty"]
            else:
                return

            if ('Department' not in self.filter or self.filter['Department'] == attributes["Department"]):
                student1.Department = attributes["Department"]
            else:
                return

            if ('Course' not in self.filter or self.filter['Course'] == attributes["Course"]):
                student1.Course = attributes["Course"]
            else:
                return
            if ('Mark' not in self.filter or self.filter['Mark'] == attributes["Mark"]):
                student1.Mark= attributes["Mark"]
            else:
                return

            self.result.append(student1)



def transform():
    myfile = ET.parse('myfile.xml')
    students = ET.parse('students.xsl')
    transformation = ET.XSLT(students)
    newfile = transformation(myfile)
    newfile.write("output-toc.html", pretty_print=True)
