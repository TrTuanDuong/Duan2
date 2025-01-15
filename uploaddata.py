import csv

class SMC:
    def __init__(self):
        self.students=[]

    def data(self, data):
        try:
            with open(data,mode='r',encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    self.students.append({
                        'name':row['name'],
                        'age': int(row['age'])
                        })
            print("Compelete!")
        except FileNotFoundError:
            print(f"File{data} rong")
        except Exception as e:
            print(f"Error: {e}")

    def ds(self):
        return self.students
    
    def reload_file(self):
        try:
            with open('data.csv',mode='w', encoding='utf-8', newline='') as file:
                fieldnames=['name','age']
                write = csv.DictWriter(file, fieldnames=fieldnames)
                write.writeheader()
                for student in self.students:
                    write.writerow(student)
            print('Compelete!')
        except Exception as e:
            print(f"ERROR:{e}")
    def themsinhvien(self,name,age):
        hsm={'name':name,'age':int(age)}
        self.students.append(hsm)
        self.reload_file()
        print(f"Compelete:Ten {name}, Tuoi{age}")