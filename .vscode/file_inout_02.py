# with open("study.txt" , 'w', encoding="utf8") as study_file :
#     study_file.write('i study hard Python for me.')

# with open("study.txt" , 'r', encoding="utf8") as study_file :
#     print(study_file.read())

for week in range(1,51):
    filename = str(week)+"주차.txt"
    with open(filename , 'w', encoding="utf8") as work_file :
        work_file.write(' - {0} 주차 주간보고 -  \n부서 : 플랫폼개발팀 \n이름 : 오별 \n업무요약 : 집에 가고싶다.'.format(week))