# from Learn.PYTHON.Check.uploaddata import SMC

# def xoa(SMC_data):
#     students = SMC_data.ds()
#     if not students:
#         print('Danh sach sinh vien trong.')
#         return
#     try:
#         student_id = int(input('Chon stt sinh vien: '))
#         if 1 <= student_id <= len(students):
#             delete_student=students.pop(student_id - 1)
#             print(f"Da xoa:{delete_student['name']}, Tuoi: {delete_student['age']}")
#             SMC_data.reload_file()
#     except ValueError:
#         print("Nhap sai")
            

# def hienthi(SMC_data):
#     students =SMC_data.ds()
#     if not students:
#         print('Danh sach sinh vien trong.')
#         return
#     print('Danh sach sinh vien: ')
#     for id, student in enumerate(students, start=1):
#         print(f"{id}. Ten:{student['name']}, Tuoi:{student['age']}")

# def themsinhvien(SMC_data):
#     name = input('Nhap ten: ')
#     age = input('Nhap tuoi: ')
#     SMC_data.themsinhvien(name,age)

# def main():
#     SMC_data = SMC()
#     SMC_data.data('data.csv')

#     while True:
#         print("Quan Ly Sinh Vien")
#         print("1. Hien thi danh sach sinh vien.")
#         print('2. Them sinh vien.')
#         print("3. Xoa.")
#         print("4. Thoat.")
#         choice = input ("Chon: ")
#         if choice == "1":
#             hienthi(SMC_data)
#         elif choice == "2":
#             themsinhvien(SMC_data)
#         elif choice =="3":
#             xoa(SMC_data)
#         elif choice == "4":
#             print("Thoat.")
#             break
#         else:
#             print("Lua chon sai.")
# if __name__ == '__main__':
#     main()
# print("anhhoandepzai")
# print("anhhoancungkhu")
# print("trantuanduong")