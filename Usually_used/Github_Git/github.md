创建一个新的仓库：在GitHub上创建一个新的仓库，记下仓库的URL。

初始化本地仓库：在你的项目目录中打开命令行，然后输入以下命令来初始化一个新的Git仓库：

`git init`

改变分支

`git branch -m master main`

添加文件到仓库：使用以下命令将项目目录中的所有文件添加到仓库：

`git add .`

提交更改：使用以下命令来提交你的更改：

`git commit -m "Initial commit"`

添加远程仓库：使用以下命令将GitHub仓库添加为远程仓库：

`git remote add origin YOUR_REPOSITORY_URL`

将YOUR_REPOSITORY_URL替换为你在第一步中记下的URL。

推送更改到GitHub：使用以下命令将你的更改推送到GitHub仓库：

`git push -u origin main`
