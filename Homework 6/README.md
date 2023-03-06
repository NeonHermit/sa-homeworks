## Homework 6 - Basic Linux Commands

<br/>

*Note:* I am adding the *.docx* file from the Homework that I originally have sent by email. Since this README.md contained the same screenshots, I am reformatting it to not duplicate things and improve the readabillity.

---

On Hyper-V/Oracle/VMware (whatever your preferred Linux workaround is currently) download Ubuntu image and install it as a virtual machine or WSL2. After this is done:  


1. Create a file friends.txt with a list of names of three of your friends on separate lines.
```bash
Option1: echo -e "Name1\nName2\nName3" > friends.txt
Option2: "vim or emacs friends.txt then type each name on new line and save"
```

2. Display the contents of friends.txt on the console.
```bash
cat friends.txt
```

3. Rename file friends.txt to bestfriends.txt
```bash
mv friends.txt bestfriends.txt
```

4. Make a copy of bestfriends.txt under the name sysadmins.txt
```bash
cp bestfriends.txt sysadmins.txt
```

5. List all files whose name begins with letter 'b' and ends with extension txt.
```bash
ls b*.txt
ls [bB]*.txt
```

6. Write a command that will tell you how many bytes are taken up by file sysadmins.txt
```bash
du -b sysadmins.txt
```

7. Create file cars.txt with a list of 5 brands of cars on separate lines.
```bash
Option1: echo -e "Car1\nCar2\nCar3\nCar4\nCar5" > cars.txt
Option2: "vim or emacs cars.txt then type each name on new line and save"
```

8. Check how many bytes are taken up by the file.
```bash
du -b cars.txt
```

9. Copy the file cars.txt into directory /tmp
```bash
cp cars.txt /tmp
```

10. List all files with extension *.txt in directory /tmp and verify that the file was copied properly.
```bash
ls /tmp/*.txt
```

11. Without leaving your home directory rename file cars.txt located in /tmp to vehicles.txt in /tmp
```bash
mv /tmp/cars.txt /tmp/vehicles.txt
```

12. Display the contents of /etc/passwd file on the screen interactively (so you can search, scroll up and down)
```bash
less /etc/passwd
```
