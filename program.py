#Hàm xuất data theo dạng tùy chỉnh
    #data_path: đường dẫn đền file text chứa dữ liệu số: mỗi số cách nhau bằng dấu phẩy, sau dấu phẩy là một khoảng trắng, không có xuống dòng
    #fm: dạng dữ liệu muốn xuất:
        # 'list': list
        # 'tuple': tuple
import re


def exportData(data_path, fm = 'list'):
    #Bỏ dấu phẩy và khoảng trắng trong chuỗi
    content = open('sampleData.txt', 'r').readline().split(', ')
    if fm == 'tuple':
        return tuple(content)
    return content
#test
def test():
    return 2

