import re

str = """
<tr>
                                
                                <td>房地产经济</td>
                                <td>中级</td>
                                
                                <td>广东省人力资源和社会保障厅</td>
                                <td>2014-01-26</td>
                                <td></td>
                            </tr>
"""
str = re.sub('\s+', '', str).strip().replace("<tr>", "").replace("</tr>", "").replace("/", "").split("<td>")
certificate_name = str[1]
level = str[3]
licence_issuing = str[5]
date = str[7]
validity = str[9]
print(certificate_name)
print(level)
print(licence_issuing)
print(date)
print(validity)
