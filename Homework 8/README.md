## Homework 8 - Linux Commands 2

<br />

1. Elevate your user access to root.  
    ```bash
    sudo su -
    sudo -i
    ```

2. Add a new user to your Linux OS and set a password for it.  
    ```bash
    useradd homework
    passwd homework
    ```

3. Test if you can log in using that user.  
    ```bash
    su homework
    # from a non elevated prompt
    ```

4. Using grep command check if the user is created.  
    ```bash
    grep "homework" /etc/passwd
    rg -w homework /etc/passwd
    ```

5. Grep the UI of each user.  
    ```bash
    grep -E 'dttw|homework' /etc/passwd | cut -d: -f3
    ```

6. Find out the GID of the created user.  
    ```bash
    grep 'homework' /etc/passwd | cut -d: -f4
    ```


7. Change the password of the user and force it to change the pass on his next login.  
    ```bash
    passwd -e homework
    # probably passwd homework will work?
    chage -l homework
    ```

8. Add a new user and set an expiration date for it, with a five-day warning period.  
    ```bash
    adduser tom
    chage -E yyyy-mm-dd tom
    chage -W 5 tom
    chage -l tom
    ```

9. Create a new group.  
    ```bash
    groupadd hmwrkgroup
    ```

10. Assign the two new users to that group.  
    ```bash
    usermod -a -G hmwrkgroup homework
    usermod -a -G hmwrkgroup tom
    ```

11. Lock one of the user accounts.  
    ```bash
    passwd -l homework
    ```

12. Change the shell of one user to tcsh.  
    ```bash
    usermod --shell /bin/tcsh homework
    ```

---
* as regular user:

13. Make sure your home dir has "execute" access enabled for group and other.
    ```bash
    chmod o+x,g+x
    chmod 755
    ```

14. Change to your home dir and create a dir called labs
15. Create an empty file in labs directory.
    ```bash
    mkdir labs && touch ~/labs/empty_file
    ```

16. Change permissions of file to rwx-rwx-rwx.  
17. List the file. What color is the file?
    ```bash
    chmod 777 empty_file
    ```

18. Change the permissions back to rx-rw-rw.
19. Check what owners does the file have.  
    ```bash
    chmod 566 empty_file
    ls -l empty_file
    ```

20. Change the user ownership of the file to another user  
    ```bash
    sudo chown tom empty_file
    ```

21. Create a group called group1 and assign two users to the group
    ```bash
    sudo groupadd group1
    sudo usermod -a -G group1 homework
    sudo usermod -a -G group1 tom
    ```

22. Create a file called group1.txt and redirect below input into the file:
"This is our group test file."  
    ```bash
    echo "This is our group test file." > group1.txt
    ```

23. Change the group of the file to the one of your users.
24. Give members of the group group1 read/write access to the file.
    ```bash
    sudo chgrp group group1.txt
    sudo chmod g+rw group1.txt
    ```