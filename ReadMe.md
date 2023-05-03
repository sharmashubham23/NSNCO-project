
# NSNCO Backend Developer Internship Assignment 

I have implemented the given Assignment in django using django restframework.

Django project name: Assignment
App name: mainapp

It contains four tables or models:
1) CustomUser
2) Clienttable
3) workTable
4) artistTable

Given end points are working fine

http://127.0.0.1:8000/api/works
http://127.0.0.1:8000/api/works?artist=khan
http://127.0.0.1:8000/api/works?work_type=Youtube
http://127.0.0.1:8000/api/register
body {"username":"testuser2","password":"123123"}