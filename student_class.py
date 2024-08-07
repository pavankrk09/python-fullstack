class student:
     def __init__(self, firast_name, last_name, age, date_of_birth, gender):
        self.firast_name = firast_name
        self.last_name = last_name
        self.age = age
        self.date_of_birth = date_of_birth
        self.gender = gender

     def  get_full_name(self):
        full_name=self.firast_name+self.last_name
        if self.gender.lower() == "male":
          print(f"Hello Mr.{full_name}")
        elif self.gender.lower() == "female":
            print(f"HELLO Mis.{full_name}")
        else:
            print(f"Hello {full_name}")
        print(f"your  is {self.age} and your date of birth is {self.date_of_birth} ")
def main():  
 student_info=student("pavan","kumar","21","25-1-2003","male")
 student_info.get_full_nameet_full_name()


if __name__=="__main__":
 main()