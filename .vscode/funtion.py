# glob : 경로 내의 폴더 / 파일 목록 조회 (윈도우 dir)
import glob
# print(glob.glob("*.py"))

# os : 운영체제에서 제공하는 기본 기능
import os
# test = os.getcwd()      # 현재 디렉토리
# print(test)

# folder = "sample_dir"

# if os.path.exists(folder):
#     print("이미 존재하는 폴더입니다.")
#     os.rmdir(folder)
#     print(folder,"폴더를 삭제하였습니다.")
# else:
#     os.makedirs(folder)
#     print(folder,"폴더를 생성하였습니다.")

print(os.listdir())\

import time
print(time.localtime())
print(time.strftime("%Y-%m-%d "))

import byme
byme.bymePackage()