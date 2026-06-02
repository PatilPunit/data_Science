import re

text="""
1. My name is Jarad and my email is jarad123@gmail.com.Jaraddddd

2. Contact me at +91-9876543210 or 8765432109.

3. The meeting is scheduled on 15/06/2026 at 09:30 AM.

4. Visit our website: https://www.datascienceworld.com

5. Alternate email: support_team@company.co.in

6. Student ID: STU202600145

7. Total project budget is ₹45,000.

8. Server IP Address: 192.168.1.101

9. Error Code: ERR-404-NOTFOUND

10. Follow us on Instagram @datascience_hub

11. Product Code: PRD-A7X9-2025 """

#search
search = re.search(r'\d',text,flags=re.M)
print(search)
sq=re.search(r'jarad',text,flags=re.I)
print(sq)

#findall
fq=re.findall(pattern=r'\d',string=text)
print(fq)

fw=re.findall(pattern=r'\d+/\d+/\d+',string=text)
print(fw)

fe=re.findall(pattern=r'[Jarad]',string=text)
print(fe)