set /p message="Enter your commit message: "
set /p branch="Enter your branch name: "

git add .
git commit -m "%message%"
git push -u origin %branch%

timeout /t 6 /nobreak
cls