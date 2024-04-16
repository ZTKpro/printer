import os
import win32print

folder_path = os.getcwd()
file_counter = 0

for filename in os.listdir(folder_path):
    if filename.endswith('.docx'):
        file_path = os.path.join(folder_path, filename)
        file_counter += 1
        print(f"Plik {filename} został wysłany do drukarki.")
print(f"Łącznie wysłano {file_counter} plików do drukarki.")
