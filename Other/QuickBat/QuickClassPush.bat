cd ../../
git config --global user.name 'CY'
git config --global user.email '1871263099@qq.com'
git add .
set /p var=CommitMessage:
git commit -m %var%
@REM Gitee
git push
pause