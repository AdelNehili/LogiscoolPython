if [ $1 == "git_init" ]; then
    echo "# LogiscoolPython" >> README.md
    git init
    git add README.md
    git commit -m "first commit"
    git branch -M main
    git remote add origin https://github.com/AdelNehili/LogiscoolPython.git
    git push -u origin main

elif [ $1 == "hello" ]; then
    echo "Hello"
else
    echo "Error, don't recognise this command:"
fi
