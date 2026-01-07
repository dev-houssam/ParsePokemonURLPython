# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility
import json
import re

regex = r"(https)://([w]{3})\.([0-9a-zA-Z]+)\.([0-9a-zA-Z]{1,3})/([a-z]+)/([a-z]+)/([a-z]+)/([a-z]+)/([a-z]+)/([0-9]+)"

test_str = ("https://www.google.com/list/pokemon/categorie/feux/id/253\n"
	"https://www.google.com/list/pokemon/categorie/feux/id/255\n"
	"https://www.google.com/list/pokemon/categorie/feux/id/100\n"
	"https://www.google.com/list/pokemon/categorie/feux/id/2954\n")

subst = "{\\n\\tprotocole:\"\\g<1>\", \\n\\tsous_domaine:\"\\g<2>\", \\n\\tdomaine:\"\\g<3>.\\g<4>\", \\n\\ttype:\"\\g<5>\", \\n\\tlist: [{animal:\"\\g<6>\", \\n\\tgroupe:\"\\g<7>\", \\n\\ttype_pokemon:\"\\g<8>\", \\n\\tcritere:\"\\g<9>\", \\n\\tid:\"\\g<10>\"},]\\n},"

# You can manually specify the number of replacements by changing the 4th argument
result = re.sub(regex, subst, test_str, 0, re.MULTILINE)

if result:
    #print (result)
    new_data = json.loads("["+result+"]")
    print(new_data)

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.
