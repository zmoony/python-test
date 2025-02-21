# python-test
python 初期学习以及常用脚本

### 依赖工具
- setuptools
```pycon
python setup.py sdist bdist_wheel
```
- wheel
- twine
- sphinx (用于文档生成)
```pycon
sphinx-quickstart
```
- PyInstaller (双击运行，需要虚拟环境安装)
```pycon
pyinstaller --onefile --windowed doc_to_excel.py
pyinstaller --hidden-import=win32com --hidden-import=win32com.client doc_to_excel.py

```
- requirements.txt
```pycon
pip install -r requirements.txt
pip freeze > requirements.txt
```
- pipreqs
```pycon
pip install pipreqs
pipreqs .
```
- pip
```pycon
pip cache purge # 清除缓存
pip install --upgrade pip # 更新pip
pip install -r requirements.txt # 安装依赖
pip install -e . # 安装项目
pip uninstall -y package_name # 卸载包
pip install --no-cache-dir package_name # 忽略缓存
pip install sphinx -i https://mirrors.aliyun.com/pypi/simple/ # 安装指定源
pip check # 检查依赖
```
- pip-tools
```pycon
pip install pip-tools
```
 requirements.in -> requirements.txt
```text
   flask-appbuilder
   flask-babel
   alembic
   
```
```pycon
   pip-compile requirements.in
   pip-sync requirements.txt
```



### 设置镜像源
1. 查看镜像源
```pycon
pip config list
```
2. 设置镜像源
```pycon
pip config set global.index-url https://mirrors.aliyun.com/pypi/simple/
```
3. 删除镜像源
```pycon
pip config unset global.index-url # 删除全局镜像源
```
4. 配置多个镜像源
 %APPDATA%\pip\pip.ini
```ini
[global]
index-url = https://mirrors.aliyun.com/pypi/simple/

[install:aliyun]
index-url = https://mirrors.aliyun.com/pypi/simple/

[install:tsinghua]
index-url = https://pypi.tuna.tsinghua.edu.cn/simple/

[install:official]
index-url = https://pypi.org/simple/

```
```bash
pip install --config-file ~/.config/pip/pip.conf -c install:aliyun <package_name>
pip install --config-file ~/.config/pip/pip.conf -c install:tsinghua <package_name>
pip install --config-file ~/.config/pip/pip.conf -c install:official <package_name>

```
5. 脚本创建

linux 
~/.bashrc 或 ~/.zshrc 
```bash
alias pip_aliyun='PIP_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/ pip'
alias pip_tsinghua='PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple/ pip'
alias pip_official='PIP_INDEX_URL=https://pypi.org/simple/ pip'

```
 source ~/.bashrc 或 source ~/.zshrc
 ```bash
pip_aliyun install <package_name>
pip_tsinghua install <package_name>
pip_official install <package_name>

 ```

windows
pip_switch.bat
```bash
@echo off
if "%1" == "aliyun" (
    set PIP_INDEX_URL=https://mirrors.aliyun.com/pypi/simple/
) else if "%1" == "tsinghua" (
    set PIP_INDEX_URL=https://pypi.tuna.tsinghua.edu.cn/simple/
) else if "%1" == "official" (
    set PIP_INDEX_URL=https://pypi.org/simple/
) else (
    echo Invalid mirror source
    exit /b 1
)
shift
pip %*

```
```bash
pip_switch aliyun install <package_name>
pip_switch tsinghua install <package_name>
pip_switch official install <package_name>

```