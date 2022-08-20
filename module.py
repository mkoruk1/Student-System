
import pandas as pd

class Student:
    
    global store_students
    store_students=[]
    
    def inputs(self):
        self.course_name=str(input("\nEnter course name:"))
        self.std_name=str(input("Enter your name:"))
        self.std_surname=str(input("Enter your surname:"))
        self.school_no=int(input("Enter your school number:"))
        self.grade=float(input("Enter your grade:"))
        if self.grade<49:
            self.status="FAILED"
        else:
            self.status="PASSED" 
              
    def grading_system(self):
        
        if self.grade<49 and self.grade>=0:
                print("Failed")           
        elif self.grade>49 and self.grade<=59:
                print("Passed with grade D")
        elif self.grade>59 and self.grade<=70:
                print("Passed with grade C")
        elif self.grade>70 and self.grade<=79:
                print("Passed with grade B")
        elif self.grade>79 and self.grade<=100:
            print("Passed with A")
        else: 
            print("Please enter a value between 0-100")

    def store_data(self):
        self.store_students=store_students.append((self.course_name,self.std_name,self.std_surname,self.school_no,self.grade,self.status))
    
    def load_file(self):
        self.file=pd.read_excel("Student System.xlsx")
        return self.file
    
    def convert_to_excel(self):
        self.dataframe=pd.DataFrame(store_students,columns=["Course Name","Name","Surname","No","Grade","Status"])
        copy=self.dataframe.copy()
        file_name="Student System.xlsx"
        try:
            self.load_file()
            finaldf = pd.concat([self.file,copy])
            finaldf.to_excel(file_name,sheet_name='Class',index=False)
        except FileNotFoundError:
            copy.to_excel(file_name,sheet_name='Class',index=False)

    def print_dataf(self):
        try:
            ex_file=self.load_file()
            print(ex_file)
        except FileNotFoundError:print("File is empty!")
       

        
