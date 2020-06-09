import argparse
import re
import os
import copy
import string
import sys



def extValue(cont, fr, to):
    #print(cont)
    #if cont.find(fr)==-1:
    #    return
        #raise ValueError("Can't not find:\t" + fr)
    return cont.split(fr)[-1].split(to)[0] 





html_table_body = ""






all_cont =  sys.stdin.read()


for block in all_cont.split("------------------------------------------------------------------------"):

    if block.find("year:") == -1:
        continue
    year = extValue(block, "year: ", "\n")
    conf = extValue(block, "conf: ", "\n")
    title = extValue(block, "title: ", "\n")
    author = extValue(block, "author: ", "\n")
    url = extValue(block, "url: ", "\n")
    citation = extValue(block, "citation: ", "\n")
    tag = extValue(block, "tag: ", "\n")




    html_row = "<tr>"
    html_row += "<td>" + str(year) + "</td>" + "\n"
    html_row += "<td>" + str(conf) + "</td>" + "\n"
    html_row += "<td>" + tag + "</td>" + "\n"
    html_row += "<td>" + str(citation) + "</td>"    + "\n"
    html_row += "<td>" + title + "</td>" + "\n"
    html_row += "<td>" + author + "</td>" + "\n"    
    html_row += "<td>" + url + "</td>" + "\n"
    html_row += "</tr>" 

    
    html_table_body += html_row + "\n"



path_template_html = "template_summ.html"

fin = open(path_template_html,"r")
all_cont = fin.read()
all_cont = all_cont.replace("__placeholder_table_content__", html_table_body)
print(all_cont)

