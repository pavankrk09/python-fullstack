# Problem : We have a string - A,B,D,E,E, F,G,H,IK,M, N, OO, PP, QQ, ZZ , X,Y,Z,9,4,3,1,5,6,7,8, 1.1.0.2

# Write logic to 
# 1. Sort in Ascending Order and Print
# 2. Sort in Descending Order and Print  
# 3. Extract Numbers only and Sort in Ascending Order and Print (Descending also)
# 4. Extract string only and Sort in Ascending Order and Print (Descending also)
# 5. Remove all duplicates and Sort ASC and Desc
class list_operations:
    def __init__(self):
        print("1")
        self.list=["A","B","D","E","E","F","G","H","IK","M", "N", "OO", "PP", "QQ", "ZZ" , "X","Y","Z","9","4","3","1","5","6","7","8", "1.1","0.2"]
    def sorting_elements(self):
    #sorting the elements in the list in asending order
        def asending():
         print("2")
         self.list.sort()
        
    #sorting the elements in the list in descending order
        def descending(self):
          print("3")
          self.list.sort(reverse=True)
        return self.list,self.list.sort
    #find the numbers in the list and place it ina numbers list
    def find_numbers(self):
        print("4")
        self.numbers=[]
        for i in self.list:
            if self.is_number(i):
                self.numbers.append((i))
        return self.numbers
    
    def is_number(self,s):
        print("5")
        return s.replace('.','',1).isdigit()
    #finnd the strings in the list and place it in a strings list
    
    def find_strings(self):
        print("6")
        self.strings = []
        for i in self.list:
            if not self.is_number(i):
                self.strings.append(i)
        return self.strings
    def individual_sorting(self):
            print("7")
            def numbers_sorting(self):
                numbers = self.find_numbers()
                numbers.sort()
                print(f"\nRemoved numbers from list and sorted in ascending order:\n\n{numbers}")
                numbers.sort(reverse=True)
                print(f"\nRemoved numbers from list and sorted in descending order:\n\n{numbers}")
        
            def strings_sorting(self):
                 strings = self.find_strings()
                 strings.sort()
                 print(f"\nExtracted strings from list and sorted in ascending order:\n\n{strings}")
                 strings.sort(reverse=True)
                 print(f"\nExtracted strings from list and sorted in ascending order:\n\n{strings}")
    



    def remove_duplicates(self):
        self.originals = list(set(self.list))
        return self.originals

    def final_sorting(self):
        originals = self.remove_duplicates()
        originals.sort()
        print(f"\nRemoved duplicates from list and sorted in ascending order:\n\n{originals}")
        originals.sort(reverse=True)
        print(f"\nRemoved duplicates from list and sorted in descending order:\n\n{originals}")



   
def main():
    s=list_operations()
    s.sorting_elements()
   
    s.individual_sorting()
    s.final_sorting()
   


if __name__ == "__main__":
    main()
    
    

    
