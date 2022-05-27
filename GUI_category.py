#GUI카테고리별로 들어갈 내용 분류 함수
def GUI_category():
    for i in range(len(category)):
        if(category[i]=="공지 사항"):
            Notice_cours.append(cours[i])
            Notice_title.append(title[i])
        elif(category[i]=="성적"):
            Score_cours.append(cours[i])
            Score_title.append(title[i])
        elif(category[i]=="과제"):
            #추가된 과제
            if(title[i][0]=="추"):
                Ass_cours.append(cours[i])
                Ass_title.append(title[i])
            #마감예정과제
            elif(title[i][0]=="마"):
                DeadlineAss_cours.append(cours[i])
                DeadlineAss_title.append(title[i])
        elif(category[i]=="프레젠테이션" or "텍스트 문서" or "pdf"):
            Document_cours.append(cours[i])
            Document_title.append(title[i])

##전체 코스이름&타이틀내용## - 제공예정/오늘/최근항목 나누지 않는 걸로 수정
cours=soup.select('.context.ellipsis>a')
title=soup.select('.js-title-link')

change_text(cours) 
change_text(title)

##GUI카테고리 리스트 구분##
GUI_category()
