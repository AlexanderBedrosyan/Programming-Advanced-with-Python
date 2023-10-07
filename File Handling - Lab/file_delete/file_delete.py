import os

try:
    os.remove('C:/Users/Alexander/PycharmProjects/file_handling_lab/file_writer/my_first_file.txt')

except FileNotFoundError:
    print('File already deleted!')
