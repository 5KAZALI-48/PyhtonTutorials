import re
string = "abc123AUG|AZ|UGAasdfg789"
state = "\|(.*?)\|"

substring = re.search(state, string).group(1)
print(substring)