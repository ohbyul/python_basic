import pickle
# profile_file= open("profile.pickle" , 'wb')     # w 쓰기 b 바이너리
# profile = {"이름" : "박명수" , "나이" : 30 , "취미" : ["축구" , "배구"]}
# print(profile)
# pickle.dump(profile,profile_file)   # profile에 있는 정보를 file에 저장
# profile_file.close()

# profile_file= open("profile.pickle" , 'rb')
# profile = pickle.load(profile_file)
# print(profile)
# profile_file.close()

with open("profile.pickle" , 'rb') as profile_file:
    print(pickle.load(profile_file))