import re


DATA = {}
DATA["OSP"]={}

Tags = []

OSP = open("OSProjects/osp.md", "r")

CurrentName = ""
 
for line in OSP.readlines():
    if len(line.strip()):
	#print line.strip()
	if "##" in line:
		CurrentName = line[3:].strip()
		print CurrentName
		DATA["OSP"][CurrentName]={}
	if len(CurrentName):
		if line.startswith("*"):
			res = line.strip().split(":")
			if len(res) > 1:
				print "".join(res[1:])
				if "Tags" in res[0]:
    				    tmp = "".join(res[1:]).split(",")
				    tmp = [x for x in tmp if x]
				    if len(tmp):
					Tags = Tags + tmp
				elif  "Refs" in res[0]:		
					tmp = "".join(res[1:]).split(",")
					tmp = [x for x in tmp if x]
				else:
					tmp = "".join(res[1:])
				DATA["OSP"][CurrentName][res[0][2:]] = tmp

print DATA

ListProjects = ""
for project in DATA["OSP"].keys():
	Cles = DATA["OSP"][project].keys()
	if "Site" in Cles:
		ListProjects += "\n### ["+project+"]("+DATA["OSP"][project]["Site"]+")\n"
	else:
		ListProjects += "\n### "+project+"\n"

	if "Desc" in Cles:
	    if len(DATA["OSP"][project]["Desc"]):
		ListProjects += "#### Description\n"+DATA["OSP"][project]["Desc"]+"\n"

	if "Tags" in Cles:
	    if len(DATA["OSP"][project]["Tags"]):
		ListProjects += "* Some tags: "+", ".join(DATA["OSP"][project]["Tags"])+"\n"
	if "Refs" in Cles:
	    if len(DATA["OSP"][project]["Refs"]):
		ListProjects += "* Some references: "+", ".join(DATA["OSP"][project]["Refs"])+"\n"

OSP = open("intro.txt", "r")
intro = ""
for line in OSP.readlines():
    intro += line

intro = intro+"\n" + ListProjects


file = open("Readme.md","w") 
file.write(intro) 
file.close() 


