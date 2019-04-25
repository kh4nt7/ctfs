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
