import csv
#Hàm xuất data theo dạng tùy chỉnh
    #data_path: đường dẫn đền file text chứa dữ liệu số: mỗi số cách nhau bằng dấu phẩy, sau dấu phẩy là một khoảng trắng, không có xuống dòng
    #fm: dạng dữ liệu muốn xuất:
        # 'list': list
        # 'tuple': tuple
def exportData(data_path, fm = 'list'):
    #Bỏ dấu phẩy và khoảng trắng trong chuỗi
    content = open(data_path, 'r').readline().split(', ')
    if fm == 'tuple':
        return tuple(content)
    return content
#Hàm tính tổng n số nguyên đầu tiên
 #n: số lượng số nguyên đầu tiên, n là số tự nhiên
def sumFirstNPositiveInterger(n):
    sum = 0
    i = 1
    while i <= n:
        sum = sum + i 
        i = i + 1
    return sum
#Hàm tính tổng các phần từ là số trong list
    #lst: list chỉ chứa số và chuỗi
def sumNumber(lst):
    sum = 0
    for item in lst:
        try:
            num = float(item)
        except ValueError:
            continue
        sum += item
    return sum
#Hàm bỏ trùng lắp trong list
    #lst1: list chỉ chứa số hoặc chuỗi hoặc cả 2
def removeDuplicated(lst1):
    derived_set = set(lst1)
    return list(derived_set)
#Hàm dọc file csv và lưu giá trị vào list
    #csv_path: đường dẫn tới file csv
def readCsvToList(csv_path):
    csv_file = open('sample.csv', 'r')
    csv_content = csv.reader(csv_file)
    return list(csv_content)