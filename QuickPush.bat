git add .
set /p var=CommitMessage:
git commit -m %var%
@REM Gitee
git push Gitee master
@REM Gihub
git push Github master
@REM GitCode
git push GitCode master

timeout /t 5 /nobreak >nul