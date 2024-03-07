import os
import sys
import random

seed_value = random.randint(0, 1000000)
def generate_codes():
    random.seed(seed_value)
    code1 = str(random.randrange(0, 10))
    code2 = str(random.randrange(0, 10))
    code3 = str(random.randrange(0, 10))
    code4 = str(random.randrange(0, 10))
    code5 = str(random.randrange(0, 10))
    code6 = str(random.randrange(0, 10))

    return code1, code2, code3, code4, code5, code6
if __name__ == "__main__":
    code1, code2, code3, code4, code5, code6 = generate_codes()
code1, code2, code3, code4, code5, code6 = generate_codes()
code1_str = eval("code1")
code2_str = eval("code2")
code3_str = eval("code3")
code4_str = eval("code4")
code5_str = eval("code5")
code6_str = eval("code6")

coder = "{},{},{},{},{},{}".format(code1_str, code2_str, code3_str, code4_str, code5_str, code6_str)
coderr = coder.replace(" ", "")
coderrr = coderr.replace(",", "")
code = coderrr.replace("'", "")

if sys.platform == 'win32':
    encoding = 'cp949'  # Windows의 경우

# 홈 디렉토리 가져오기
home_directory = os.path.expanduser('~')

# 문서 폴더 경로 생성
documents_folder = os.path.join(home_directory, 'Documents')

#  문서 폴더가 없는 경우 생성(설마...)
if not os.path.exists(documents_folder):
    os.makedirs(documents_folder)

# 텍스트 파일 경로 생성
file_path = os.path.join(documents_folder, 'example.game.txt')

# 텍스트 파일 생성
def make():
    with open(file_path, 'w', encoding=encoding) as file:
        file.write("코드: ")
        file.write(repr(code))

print(f"텍스트 파일이 {file_path}에 생성되었음")
print("랜덤 시드 값:", seed_value ,"임")
print("코드:",code)
print("코드 string:",code1_str, code2_str, code3_str, code4_str, code5_str, code6_str)
print("코드 string:",code1, code2, code3, code4, code5, code6)
print("?")