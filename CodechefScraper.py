import urllib
import re
import os

htmlCodes = (
            ("'", '&#39;'),
            ('"', '&quot;'),
            ('>', '&gt;'),
            ('<', '&lt;'),
            ('&', '&amp;')
            )

username=raw_input("Enter Username")
url="https://www.codechef.com/users/"+username
flag=0
while(flag==0):
    try:
        html=urllib.urlopen(url).read()
        if("Internal Server Error" not in html):
            flag=1
    except:
        pass

pattern='<a href="(.+?)>'
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

try:
    os.makedirs(username)
except:
    print("Could not make directory")
    exit()

print("Created directory for user : "+username)
for q in range(0,len(questions)):
    question_name=questions[q][1].split(","+username)[0]
    print("Getting question:"+question_name)
    url="https://www.codechef.com/"+questions[q][0]+"/status/"+questions[q][1]
    os.makedirs(username+"/"+questions[q][0]+"_"+question_name)
    flag=0
    while(flag==0):
        try:
            html=urllib.urlopen(url).read()
            if("Internal Server Error" not in html):
                flag=1
        except:
            pass
    html=html.split('<tr class="kol"')
    for i in range(1,len(html)):
        html[i]=str(html[i])
        if("<img src='/misc/tick-icon.gif'>" in html[i]):
            pattern='[0-9]">(.+?)</td>'
            html[i]=re.findall(pattern,html[i])
            sub_id=html[i][0]
            sub_time=html[i][1]
            sub_time=html[i][4]
            sub_mem=html[i][5]
            sub_lang=html[i][6]
            file=open(username+"/"+questions[q][0]+"_"+question_name+"/"+sub_lang+"_"+sub_time+"_"+sub_mem+".txt", 'w')
            suburl="https://www.codechef.com/viewplaintext/"+sub_id
            flag=0
            while(flag==0):
                try:
                    subhtml=urllib.urlopen(suburl).read()
                    flag=1
                except:
                    pass

            subhtml=subhtml.split(">")[1]
            subhtml=subhtml.split("<")[0]
            for code in htmlCodes:
                subhtml = subhtml.replace(code[1], code[0])
            file.write(subhtml)
    if(os.listdir(username+"/"+questions[q][0]+"_"+question_name)==[]):
        print(html)
        exit()

'''
x=['<!DOCTYPE html>\n<html lang="en" >\n<head>\n<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n    <script type="text/javascript">var _sf_startpt = (new Date()).getTime()</script>\n    <title>Internal Server Error | CodeChef</title>\n    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />\n<meta name="keywords" content="programming, language, algorithm, contest, contester, Java, C#, Pascal, C, C++, python, ruby, caml, ocaml, perl, haskell, lisp, prolog, fortran, assembler, asembler, functional, online, judge, problem, problemset, ACM" />\n<link rel="shortcut icon" href="/misc/favicon.ico" type="image/x-icon" />\n    <link type="text/css" rel="stylesheet" media="all" href="/sites/all/themes/abessive/style.css" />\n    <link type="text/css" rel="stylesheet" media="all" href="/sites/all/themes/abessive/new-style.css" />\n    <style type="text/css">\n        .ns-content {\n            padding-top: 40px;\n            text-align: center;\n        }\n        .ns-content .err-big-label {\n            font-size: 7em;\n        }\n        .ns-content .err-message {\n            font-size: 2em;\n        }\n\n        .err-back-link {\n            visibility: hidden;\n        }\n    </style>\n    <script type="text/javascript">\n        $(document).ready(function() {\n            if(window.history) {\n                if (document.referrer != \'\' && window.history.length > 1)  {\n                    $(\'.err-back-link\').css(\'display\',\'block\');\n                }\n            }\n        });\n    </script>\n</head>\n<body>\n<center>\n    <div id="header" class="wrapper">\n        <div class="inner-wrapper">\n            <!-- Header -->\n            <div id="logo-floater" class="cols-2">\n                <a href="/" title=""><img src="/sites/all/themes/abessive/logo.png" alt="CodeChef is a non-commercial competitive programming community" id="logo" /><span></span></a>            </div>\n            <div class="cols-2">\n            </div>\n        </div>\n    </div>\n    <!-- /HEADER -->\n    <center>\n        <table cellspacing="0" cellpadding="10" id="maintable" class="maintable">\n            <tr>\n                <td class="content" width="99%">\n                    <div class="c4s_wrapper-in-new">\n                        <div class="c4s_content">\n                            <div class="c4s_content-in-new">\n                                <div class="ns-content">\n                                    <p class="err-big-label">503</p>\n\t\t\t\t\t\t\t\t\t<p class="err-message">Server cannot process your request. Please try again. </p>\n\t\t\t\t\t\t\t\t\t<p class="err-message">You may be exceeding the number of request\'s limit or our server is too busy.</p>\n\t\t\t\t\t\t\t\t\t<a href="javascript:window.history.back();" class="err-back-link">< Go Back</a>\n                                </div>\n                            </div>\n                        </div>\n                    </div>\n                </td>\n            </tr>\n        </table>\n\n                <div id="footer" class="wrapper">\n            <!--<div class="r1 t"></div><div class="r2"></div><div class="r3"></div><div class="r4"></div><div class="r5"></div>-->\n            <div class="content clear-block">\n                <!-- Footer Contents -->\n                <div id="block-block-13" class="block block-block block-header">\n  <div class="content">\n        <script language="javascript" type="text/javascript">\nfunction formatTime(ts) {\n  now = new Date(ts);\n \n  localtime = new Date();\n  hour = now.getHours();\n  min = now.getMinutes();\n  sec = now.getSeconds();\n  \n  if (min <= 9) {\n\t min = "0" + min;\n  }\n  if (sec <= 9) {\n\t sec = "0" + sec;\n  }\n  if (hour > 12) {\n\t hour = hour - 12;\n\t add = " PM";\n  } else {\n\t hour = hour;\n\t add = " AM";\n  }\n  if (hour == 12) {\n\t add = " PM";\n  }\n  if (hour == 00) {\n\t hour = "12";\n  }\n\t\n  $(\'#server-time\').html(((hour<=9) ? "0" + hour : hour) + ":" + min + ":" + sec + add);\n  \n  nextSec = (now.getTime() + 1000);\n  \n  setTimeout("formatTime("+nextSec+")", 1000);\n}\nfunction getDtTimeZone() \n{\nvar rightNow = new Date();\nvar toDay = new Date(rightNow.getFullYear(), 0, 1, 0, 0, 0, 0);\nvar temp = toDay.toGMTString();\nvar date2 = new Date(temp.substring(0, temp.lastIndexOf(" ") -1));\nvar stdTime = (toDay - date2) / (1000 * 60 * 60);\nreturn stdTime;\n}\n/*var d=new Date();\n$.ajax({\nurl: \'/umtza\',\ntype:\'POST\',\ndata: \'umtza=\'+d.toString(),\n});\n*/\n</script>\n<div id="disclaimer">CodeChef is a non-commercial competitive programming community</div>\n<div class="inner-wrapper">\n<div class="cols-2">\n<div id="secondary-nav">\n<ul>\n    <li><a href="http://www.codechef.com/aboutus/">About CodeChef</a></li>\n    <li><a target="_blank" href="http://www.directi.com/">About Directi</a></li>\n    <li><a href="http://www.codechef.com/ceoscorner/">CEO\'s Corner</a></li>\n    <li><a href="http://www.codechef.com/c-programming">C-Programming</a></li>\n    <li><a href="http://www.codechef.com/Programming-Languages">Programming Languages</a></li>\n    <li><a href="http://www.codechef.com/contactus">Contact Us</a></li>\n</ul>\n</div>\n<div id="copyright" class="cols-2">&copy; 2009 <a style="color: rgb(0, 0, 0);" href="http://www.directi.com">Directi Group</a>.  All Rights Reserved.  CodeChef uses SPOJ &copy; by <a style="color: rgb(0, 0, 0);" href="http://www.sphere-research.com">Sphere Research Labs</a></div>\n<div id="copyright-msg">In order to report copyright violations of any kind, send in an email to <a href="mailto:copyright@codechef.com">copyright@codechef.com</a></div>\n</div>\n<div align="right" class="cols-2-right" style="float:right;">\n<div id="sponsor-strip"><a target="_blank" href="http://www.directi.com"><img alt="CodeChef a product of Directi" src="/sites/all/themes/abessive/images/footer-sponsor-strip.gif" /></a><br />\n<span>The time now is: <span id="server-time"></span></span>\n\t\t\t\t<script language=\'javascript\'>\n\t\t\t\t\t\tformatTime(\'September 01, 2014 16:46:08\');\n\t\t\t\t\t</script></div>\n</div>\n</div>\n<script type="text/javascript">\n\n  var _gaq = _gaq || [];\n  _gaq.push([\'_setAccount\', \'UA-53602-42\']);\n  _gaq.push([\'_trackPageview\']);\n\n  (function() {\n    var ga = document.createElement(\'script\'); ga.type = \'text/javascript\'; ga.async = true;\n    ga.src = (\'https:\' == document.location.protocol ? \'https://ssl\' : \'http://www\') + \'.google-analytics.com/ga.js\';\n    var s = document.getElementsByTagName(\'script\')[0]; s.parentNode.insertBefore(ga, s);\n  })();\n\n</script>\n\n\n<!-- Google Code for Visitors that do not sign-up Remarketing List -->\n<script type="text/javascript">\n/* <![CDATA[ */\nvar google_conversion_id = 1066618556;\nvar google_conversion_language = "en";\nvar google_conversion_format = "3";\nvar google_conversion_color = "666666";\nvar google_conversion_label = "gbUUCPTlhAIQvJ3N_AM";\nvar google_conversion_value = 0;\n/* ]]> */\n</script>\n<script type="text/javascript" src="//www.googleadservices.com/pagead/conversion.js">\n</script>\n<noscript>\n<div style="display:inline;">\n<img height="1" width="1" style="border-style:none;" alt="" src="//www.googleadservices.com/pagead/conversion/1066618556/?label=gbUUCPTlhAIQvJ3N_AM&amp;guid=ON&amp;script=0"/>\n</div>\n</noscript>\n\n<!-- Google Code for RM codechef Remarketing List -->\n<script type="text/javascript">\n/* <![CDATA[ */\nvar google_conversion_id = 968176136;\nvar google_conversion_language = "en";\nvar google_conversion_format = "3";\nvar google_conversion_color = "ffffff";\nvar google_conversion_label = "iDk7CPDZ7wMQiOTUzQM";\nvar google_conversion_value = 0;\n/* ]]> */\n</script>\n<script type="text/javascript" src="//www.googleadservices.com/pagead/conversion.js">\n</script>\n<noscript>\n<div style="display:inline;">\n<img height="1" width="1" style="border-style:none;" alt="" src="//www.googleadservices.com/pagead/conversion/968176136/?label=iDk7CPDZ7wMQiOTUzQM&amp;guid=ON&amp;script=0"/>\n</div>\n</noscript>\n\n<div class=\'cc-footer-seo\'>\n<span><a href=\'/\'>CodeChef</a> - A Platform for Aspiring Programmers</span>\n<p>CodeChef was created as a platform to help programmers make it big in the world of algorithms, <strong>computer programming</strong> and <strong>programming contests</strong>. At CodeChef we work hard to revive the geek in you by hosting a <strong>programming contest</strong> at the start of the month and another smaller programming challenge in the middle of the month. We also aim to have training sessions and discussions related to <strong>algorithms, binary search</strong>, technicalities like <strong>array size</strong> and the likes. Apart from providing a platform for <strong>programming competitions</strong>, CodeChef also has various algorithm tutorials and forum discussions to help those who are new to the world of <strong>computer programming</strong>.</p>\n<p></p>\n<span><a href=\'/problems/easy\'>Practice Section</a> - A Place to hone your \'Computer Programming Skills\'</span>\n<p>Try your hand at one of our many practice problems and submit your solution in a language of your choice. Our <strong>programming contest</strong> judge accepts solutions in over 35+ programming languages. Preparing for coding contests were never this much fun! Receive points, and move up through the CodeChef ranks. Use our practice section to better prepare yourself for the multiple <strong>programming challenges</strong> that take place through-out the month on CodeChef. </p>\n<p></p>\n<span><a href=\'/contests/\'>Compete</a> - Monthly Programming Contests and Cook-offs</span>\n<p>Here is where you can show off your <strong>computer programming</strong> skills. Take part in our 10 day long monthly <strong>coding contest</strong> and the shorter format Cook-off <strong>coding contest</strong>. Put yourself up for recognition and win great prizes. Our <strong>programming contests</strong> have prizes worth up to Rs.20,000 and $700lots more CodeChef goodies up for grabs. </p>\n<p></p>\n<span><a href=\'http://discuss.codechef.com/\'>Discuss</a></span>\n<p>Are you new to <strong>computer programming</strong>? Do you need help with algorithms? Then be a part of CodeChef\'s Forums and interact with all our programmers - they love helping out other programmers and sharing their ideas. Have discussions around <strong>binary search, array size, branch-and-bound, Dijkstra\'s algorithm, Encryption algorithm</strong> and more by visiting the CodeChef Forums and Wiki section.</p>\n<p></p>\n<span><a href=\'/community\'>CodeChef Community</a></span>\n<p>As part of our Educational initiative, we give institutes the opportunity to associate with CodeChef in the form of Campus Chapters. Hosting <strong>online programming competitions</strong> is not the only feature on CodeChef. You can also host a <strong>coding contest</strong> for your institute on CodeChef, organize an <strong>algorithm</strong> event and be a guest author on our blog. </p>\n<p></p>\n<span><a href=\'/goforgold\'>Go For Gold</a></span>\n<p>The Go for Gold Initiative was launched about a year after CodeChef was incepted, to help prepare Indian students for the <strong>ACM ICPC</strong> World Finals competition. In the run up to the <strong>ACM ICPC</strong> competition, the Go for Gold initiative uses CodeChef as a platform to train students for the <strong>ACM ICPC</strong> competition via multiple warm up contests. As an added incentive the Go for Gold initiative is also offering over Rs.8 lacs to the Indian team that beats the 29th position at the <strong>ACM ICPC</strong> world finals. Find out more about the Go for Gold and the <strong>ACM ICPC</strong> competition <a href="/goforgold">here</a>.</p>\n</div>  </div>\n</div>\n<div id="block-block-48" class="block block-block block-header">\n  <div class="content">\n        <script type =\'text/javascript\' src =\'/misc/jquery.cookie.js\'>  </script><script type =\'text/javascript\' src =\'/misc/contest-notification.js\'>  </script>  </div>\n</div>\n            </div>\n        </div>\n                    </center>\n</center>\n</body>\n</html>\n\n']
for i in x:
    print("Internal Server Error" in i)
    print(x)
'''