import urllib
import re
import os

''' at the end while writing the txt file format is encoded so here we create htmlCodes so as to decode it '''
htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;')
            )

username=raw_input("Enter Username")

url="https://www.codechef.com/users/"+username

flag=0     # flag maintained to check for internal server errors
while(flag==0):
    try:   # try until valid html is not recieved
        html=urllib.urlopen(url).read()
        if("Internal Server Error" not in html):
            flag=1
    except:
        pass

pattern='<a href="(.+?)>'    # pattern to find all questions
regex=re.findall(pattern,html)
questions=[]
x=[]
map={}                # question map to avoid duplicate question entry
for i in regex:
    if 'status' in i:
        i=i.split("/status/")
        i[1]=i[1].split('"')[0]
        try:
            map[i[1]]      # try to accept question in map if we get error question is to be included else pass
        except:
            map[i[1]]='1'
            questions.append(i)

totalquestions=len(questions)

''' questions is a 2-d string list with first string=contest name and second string=questionname'''


try:
    os.makedirs(username)
except:
    print("Could not make directory")
    exit()

print("Created directory for user : "+username)


for q in range(0,len(questions)):
    question_name=questions[q][1].split(","+username)[0]
    print("Getting question:"+question_name+" "+(q+1)+"/"+totalquestions)
    url="https://www.codechef.com/"+questions[q][0]+"/status/"+questions[q][1]
    os.makedirs(username+"/"+questions[q][0]+"_"+question_name)
    flag=0  # to avoid internal sever error
    while(flag==0):
        try:
            html=urllib.urlopen(url).read()
            if("Internal Server Error" not in html):
                flag=1
        except:
            pass
    html=html.split('<tr class="kol"') # all submission in table format
    for i in range(1,len(html)):
        html[i]=str(html[i])
        if("<img src='/misc/tick-icon.gif'>" in html[i]):  #if solution is accepted it contains tick-icon
            pattern='[0-9]">(.+?)</td>'   #get only necessary data
            html[i]=re.findall(pattern,html[i])
            sub_id=html[i][0]
            sub_time=html[i][1]
            sub_time=html[i][4]
            sub_mem=html[i][5]
            sub_lang=html[i][6]
            file=open(username+"/"+questions[q][0]+"_"+question_name+"/"+sub_lang+"_"+sub_time+"_"+sub_mem+".txt", 'w')
            suburl="https://www.codechef.com/viewplaintext/"+sub_id
            flag=0  #to avoid internal server error
            while(flag==0):
                try:
                    subhtml=urllib.urlopen(suburl).read()
                    if("Internal Server Error" not in subhtml):
                        flag=1
                except:
                    pass

            subhtml=subhtml.split(">")[1]
            subhtml=subhtml.split("<")[0]
            for code in htmlCodes:
                subhtml = subhtml.replace(code[1], code[0])
                file.write(subhtml)

print("All Done!")