# Problem : We have a string - A,B,D,E,E, F,G,H,IK,M, N, OO, PP, QQ, ZZ , X,Y,Z,9,4,3,1,5,6,7,8, 1.1.0.2

# Write logic to 
# 1. Sort in Ascending Order and Print
# 2. Sort in Descending Order and Print  
# 3. Extract Numbers only and Sort in Ascending Order and Print (Descending also)
# 4. Extract string only and Sort in Ascending Order and Print (Descending also)
# 5. Remove all duplicates and Sort ASC and Desc

class string_methods():
    def __init__(self):
        self.list=["A","B","D","E","E","F","G","H","IK","M", "N", "OO", "PP", "QQ", "ZZ" , "X","Y","Z","9","4","3","1","5","6","7","8", "1.1","0.2"]
        self.list.sort()
        print(f"\nSorted string in ascending order:\n\n{self.list}")

    def descending(self):
        self.list.sort(reverse=True)
        print(f"\nSorted string in descending order:\n \n{self.list}")

    def extract_numbers(self):
        self.numbers=[]
        for i in self.list:
            if self.is_number(i):
                self.numbers.append((i))
        return self.numbers
    
    def is_number(self,s):
        return s.replace('.','',1).isdigit()
    
    def sort_numbers(self):
        numbers = self.extract_numbers()
        numbers.sort()
        print(f"\nExtracted numbers from list and sorted in ascending order:\n\n{numbers}")
        numbers.sort(reverse=True)
        print(f"\nExtracted numbers from list and sorted in descending order:\n\n{numbers}")

    def extract_strings(self):
        self.strings = []
        for i in self.list:
            if not self.is_number(i):
                self.strings.append(i)
        return self.strings

    def sort_strings(self):
        strings = self.extract_strings()
        strings.sort()
        print(f"\nExtracted strings from list and sorted in ascending order:\n\n{strings}")
        strings.sort(reverse=True)
        print(f"\nExtracted strings from list and sorted in ascending order:\n\n{strings}")

    def remove_duplicates(self):
        self.originals = list(set(self.list))
        return self.originals

    def sorting(self):
        originals = self.remove_duplicates()
        originals.sort()
        print(f"\nRemoved duplicates from list and sorted in ascending order:\n\n{originals}")
        originals.sort(reverse=True)
        print(f"\nRemoved duplicates from list and sorted in descending order:\n\n{originals}")


def main():
    s=string_methods()
    s.descending()
    s.sort_numbers()
    s.sort_strings()
    s.sorting()


if __name__ == "__main__":
    main()
    
    