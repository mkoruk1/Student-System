
from project1module import *
import msvcrt as m
import time
import os

def menu():
    Students=Student()    
    while True:
        os.system('cls')
        print("\nSTUDENT SYSTEM\n-------------------------\nPress 1 to add student")
        print("\nPress 2 to print the list")
        print("\nPress 3 to exit")
        print("\n-------------------------")
        choice=int(input(":"))
        if choice==1:
            counter=0
            no=int(input("Enter number of students you want to add:"))
            os.system('cls')
            while counter<no:
                Students.inputs()
                Students.grading_system()
                Students.store_data()
                counter+=1
            Students.convert_to_excel()
                
        elif choice==2:
            os.system('cls')
            Students.print_dataf()
            print("\nPress any key to return to menu...")
            m.getch()
            
        elif choice==3:
            break

        else:
            print("Wrong value!")
            time.sleep(3)
            
                    
os.system('cls')
menu()
