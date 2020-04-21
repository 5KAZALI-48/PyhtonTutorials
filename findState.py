import re
s = "abc123AUG|AZ|UGAasdfg789"
pattern = "\|(.*?)\|"

substring = re.search(pattern, s).group(1)
print(substring)