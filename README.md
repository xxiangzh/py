# py

# 下载包
下载安装包命令
pip install package-name

移除软件包命令
pip uninstall package-name

查看已经安装的软件包命令
pip list

导出当前环境的配置到当前目录下命令
pip freeze > requirements.txt

重新创建相同的环境命令
pip install -r requirements.txt

# 打包exe
下载pyinstaller包
pip install pywin32
pip install pyinstaller
打包
cd <demo.py所在目录>
pyinstaller -F demo.py -w

解决编译后exe文件太大问题，使用Python虚拟环境（virtualenv）
