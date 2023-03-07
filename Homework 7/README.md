## Homework 7 - Shell scripts

<br/>

1. Write a shell script to get the current date, time, username and current working directory.  
    ```bash
        #!/bin/bash

        echo "Date: `date`"

        echo "Username: `whoami`"

        echo "Current Working Directory: `pwd`"
    ```

2. Write a shell script that prints “I love learning about DevOps” on the screen.  
Message should be a variable.  
    ```bash
        #!/bin/bash

        msg="I love learning about DevOps"
        echo $msg
    ```

3. Write a shell script that displays “plan code build test release deploy” on the screen with each appearing on a separate line.  
    ```bash
        #!/bin/bash

        echo -e "plan\ncode\nbuild\ntest\nrelease\ndeploy"
    ```

4. Write a shell script that prompts the user for a name of a file or directory and reports if it is a regular file, a directory, or another type of file. Also perform a ls command against the file or directory with the long listing option.  
    ```bash
        #!/bin/bash

        read -p "Enter a file or dir pathname: " name

        if [ -f "$name" ]
        then
            echo "$name is a file."
            ls -l "$name"
        elif [ -d "$name" ]
        then
            echo "$name is a directory."
            ls -l "$name"
        else
            echo "$name is another type of file."
        fi
    ```

5. Use arguments in a script. Total number of arguments should be three.  
    ```bash
        #!/bin/bash

        echo "Name: $1"
        echo "Lastname: $2"
        echo "City: $3"
    ```

    Execute:
    ```shell
        ./scriptname.sh "Name" "Lastname" "City"
    ```

6. Write a script that will output your name out of a variable and will display the server uptime. 
    ```bash
        #!/bin/bash

        read -p "Enter your name: " name

        echo "Hello $name."
        echo "The uptime is: `uptime`"
    ```