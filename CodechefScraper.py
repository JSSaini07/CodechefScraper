import urllib
import re
import os


username=raw_input("Enter Username")
url="https://www.codechef.com/users/"+username
html=urllib.urlopen(url).read()
pattern="status/(.+?),"+username
regex=re.findall(pattern,html)
questions=regex

os.makedirs(username)
print("Created directory for user : "+username)

for q in range(0,len(questions)):
    print("Getting question:"+questions[q])
    url="https://www.codechef.com/status/"+questions[q]+","+username
    os.makedirs(username+"/"+questions[q])
    html=urllib.urlopen(url).read()
    html=html.split('<tr class="kol"')
    for i in range(1,len(html)):
        if("<img src='/misc/tick-icon.gif'>" in html[i]):
            pattern='[0-9]">(.+?)</td>'
            html[i]=re.findall(pattern,html[i])
            sub_id=html[i][0]
            sub_time=html[i][1]
            sub_time=html[i][4]
            sub_mem=html[i][5]
            sub_lang=html[i][6]
            file=open(username+"/"+questions[q]+"/"+sub_lang+"_"+sub_time+"_"+sub_mem+".txt", 'w')
            subhtml="https://www.codechef.com/viewplaintext/"+sub_id
            subhtml=urllib.urlopen(subhtml).read()
            subhtml=subhtml.split(">")[1]
            subhtml=subhtml.split("<")[0]
            subhtml=subhtml.replace('&gt;','>');
            subhtml=subhtml.replace('&lt;','<');
            subhtml=subhtml.replace('&quot;','""');
            file.write(subhtml)
