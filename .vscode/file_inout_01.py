# score_file = open("score.txt","w" ,encoding="utf8")     # W 는 덮어씀
# print("수학  : 0" , file=score_file)
# print("영어  : 100" , file=score_file)
# score_file.close()


# score_file = open("score.txt","a" ,encoding="utf8")
# score_file.write('과학 : 80')
# score_file.write('\n코딩 : 100')
# score_file.close()



score_file = open("score.txt","r" ,encoding="utf8")
print(score_file.read())
score_file.close()