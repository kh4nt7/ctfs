## Journey - 20 pts
___
### Description
Every journey starts on step one
```bash
nc p1.tjctf.org 8009
```

If we connect to the p1.tjctf.org at port 8009 we will receive something like this
```bash
root@pwnhub:~/ctfs/tjctf2019/journey# nc p1.tjctf.org 8009
Encountered 'one'
The first step: 
```

When we put one, we will receive another encounterd value to be able to step forward.
```bash
root@pwnhub:~/ctfs/tjctf2019/journey# nc p1.tjctf.org 8009
Encountered 'one'
The first step: one
Encountered 'infected'
The next step: 
```

This will ask you again and again. So, It will be so hard to be able to enter it manually.
So, I wrote a script. <br/>
Pseudo code is like this <br/>
1. Connect to the server
2. Receive first line which contains "Encountered 'one'"
3. Check if there were flag inside first line
4. Extract the encounter word
5. Receive second line until we could input
6. Send the word back
7. Loop from 2 to 6:D
<br/>

Here is my [code](https://github.com/kh4nt99/ctfs/blob/master/tjctf2019/journey/solution.py)
