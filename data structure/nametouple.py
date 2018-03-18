from collections import namedtuple

student = namedtuple('student',['name','age','sex','email']) 

s = student('Jim','16','male','lee@leeid.me')

print(s.name)