Описание команд при создании локального репозитария и отправке на Githab
Макс@LAPTOP-TEB88LOV MINGW64 /d/МОИ ДОКУМЕНТЫ/РАБОТА 2025/ОБУЧЕНИЕ АВТОТЕСТ/autotests-ui
$ git status
fatal: not a git repository (or any of the parent directories): .git

Макс@LAPTOP-TEB88LOV MINGW64 /d/МОИ ДОКУМЕНТЫ/РАБОТА 2025/ОБУЧЕНИЕ АВТОТЕСТ/autotests-ui
$ git init
Initialized empty Git repository in D:/МОИ ДОКУМЕНТЫ/РАБОТА 2025/ОБУЧЕНИЕ АВТОТЕ
СТ/autotests-ui/.git/

Макс@LAPTOP-TEB88LOV MINGW64 /d/МОИ ДОКУМЕНТЫ/РАБОТА 2025/ОБУЧЕНИЕ АВТОТЕСТ/autotests-ui (master)
$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        .idea/
        main.py

nothing added to commit but untracked files present (use "git add" to track)

Макс@LAPTOP-TEB88LOV MINGW64 /d/МОИ ДОКУМЕНТЫ/РАБОТА 2025/ОБУЧЕНИЕ АВТОТЕСТ/autotests-ui (master)
$ git add .
warning: in the working copy of '.idea/inspectionProfiles/profiles_settings.xml'
, LF will be replaced by CRLF the next time Git touches it

Макс@LAPTOP-TEB88LOV MINGW64 /d/МОИ ДОКУМЕНТЫ/РАБОТА 2025/ОБУЧЕНИЕ АВТОТЕСТ/autotests-ui (master)
$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .idea/.gitignore
        new file:   .idea/autotests-ui.iml
        new file:   .idea/inspectionProfiles/profiles_settings.xml
        new file:   .idea/misc.xml
        new file:   .idea/modules.xml
        new file:   main.py


Макс@LAPTOP-TEB88LOV MINGW64 /d/МОИ ДОКУМЕНТЫ/РАБОТА 2025/ОБУЧЕНИЕ АВТОТЕСТ/autotests-ui (master)
$ git checkout -b main
Switched to a new branch 'main'

Макс@LAPTOP-TEB88LOV MINGW64 /d/МОИ ДОКУМЕНТЫ/РАБОТА 2025/ОБУЧЕНИЕ АВТОТЕСТ/autotests-ui (main)
$ git add .

Макс@LAPTOP-TEB88LOV MINGW64 /d/МОИ ДОКУМЕНТЫ/РАБОТА 2025/ОБУЧЕНИЕ АВТОТЕСТ/autotests-ui (main)
$ git status
On branch main

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)
        new file:   .idea/.gitignore
        new file:   .idea/autotests-ui.iml
        new file:   .idea/inspectionProfiles/profiles_settings.xml
        new file:   .idea/misc.xml
        new file:   .idea/modules.xml
        new file:   main.py


Макс@LAPTOP-TEB88LOV MINGW64 /d/МОИ ДОКУМЕНТЫ/РАБОТА 2025/ОБУЧЕНИЕ АВТОТЕСТ/autotests-ui (main)
$ git remote add origin https://github.com/MaxS70/autotests-ui.git

Макс@LAPTOP-TEB88LOV MINGW64 /d/МОИ ДОКУМЕНТЫ/РАБОТА 2025/ОБУЧЕНИЕ АВТОТЕСТ/autotests-ui (main)
$ git remote -v
origin  https://github.com/MaxS70/autotests-ui.git (fetch)
origin  https://github.com/MaxS70/autotests-ui.git (push)

Макс@LAPTOP-TEB88LOV MINGW64 /d/МОИ ДОКУМЕНТЫ/РАБОТА 2025/ОБУЧЕНИЕ АВТОТЕСТ/autotests-ui (main)
$ git commit -m "Initial commit"
[main (root-commit) 7725e81] Initial commit
 6 files changed, 40 insertions(+)
 create mode 100644 .idea/.gitignore
 create mode 100644 .idea/autotests-ui.iml
 create mode 100644 .idea/inspectionProfiles/profiles_settings.xml
 create mode 100644 .idea/misc.xml
 create mode 100644 .idea/modules.xml
 create mode 100644 main.py

Макс@LAPTOP-TEB88LOV MINGW64 /d/МОИ ДОКУМЕНТЫ/РАБОТА 2025/ОБУЧЕНИЕ АВТОТЕСТ/autotests-ui (main)
$ git log
commit 7725e81fa2fe7616a10d17f479a552cab48a8d7d (HEAD -> main)
Author: MaxS70 <Kobra_70@mail.ru>
Date:   Tue Sep 23 23:28:54 2025 +0300

    Initial commit

Макс@LAPTOP-TEB88LOV MINGW64 /d/МОИ ДОКУМЕНТЫ/РАБОТА 2025/ОБУЧЕНИЕ АВТОТЕСТ/autotests-ui (main)
$ git push -u origin main
Enumerating objects: 10, done.
Counting objects: 100% (10/10), done.
Delta compression using up to 8 threads
Compressing objects: 100% (8/8), done.
Writing objects: 100% (10/10), 1.36 KiB | 462.00 KiB/s, done.
Total 10 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
To https://github.com/MaxS70/autotests-ui.git
 * [new branch]      main -> main
branch 'main' set up to track 'origin/main'.

Макс@LAPTOP-TEB88LOV MINGW64 /d/МОИ ДОКУМЕНТЫ/РАБОТА 2025/ОБУЧЕНИЕ АВТОТЕСТ/autotests-ui (main)
