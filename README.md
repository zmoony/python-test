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

### 离线开发运行

1. 本地在线下载
```pycon
# 在线时运行
pip download -r requirements.txt -d ./offline_packages
```
或者创建 wheel 文件（.whl），然后在离线环境中安装这些文件。
```pycon
# 在线时运行
pip wheel --wheel-dir=./offline_packages -r requirements.txt
```
2. 离线运行
```pycon
pip install --no-index --find-links=./offline_packages -r requirements.txt
pip install --no-index --find-links=./offline_packages package_name
```
3. 使用虚拟环境
创建一个虚拟环境并在其中安装所有依赖项，这样可以确保你的开发环境是独立且一致的。
```pycon
# 在线时运行
python -m venv myenv
source myenv/bin/activate  # Linux/MacOS
myenv\Scripts\activate     # Windows

pip install -r requirements.txt
# 离线使用
pip3 install --no-index --find-links=/home/user/packages requests
python3 file_operations.py

```
然后将整个虚拟环境复制到离线机器上。

4. 使用docker
使用 Docker 容器来创建一个包含所有依赖项的开发环境。你可以在线时构建 Docker 镜像，然后将其导出并导入到离线环境中。
```bash
# 构建镜像
docker build -t my-python-env .

# 导出镜像
docker save -o my-python-env.tar my-python-env

# 在离线环境中导入镜像
docker load -i my-python-env.tar

```
5. 示例
5.1. 在线把包下载到一个离线的文件夹中
5.2. 文件在拷贝到宿主机
5.3. 离线安装依赖包
5.4  运行py文件
```bash
# 下载依赖
 pip download -r requirements.txt -d ./offline_packages
# 创建虚拟环境，并安装依赖
 python -m venv myenv
 source myenv/bin/activate  # Linux/MacOS
 myenv\Scripts\activate     # Windows
 pip install -r requirements.txt
 # 创建一个目录来存放离线包
mkdir offline_packages
# 下载所有依赖包及其依赖项到 offline_packages 目录
pip download -r requirements.txt -d ./offline_packages

 
 
# 离线使用
# 将 myenv 目录和 offline_packages 目录复制到离线机器。
# 激活虚拟环境并安装依赖
 python -m venv myenv
 source myenv/bin/activate  # Linux/MacOS
 myenv\Scripts\activate     # Windows
 pip install --no-index --find-links=./offline_packages -r requirements.txt
 # 复制虚拟环境和依赖包
 # 从有网络的环境复制到宿主机
scp -r myenv user@host:/home/user/my_project
scp -r offline_packages user@host:/home/user/my_project
# 激活虚拟环境
source /home/user/my_project/myenv/bin/activate  # Linux/MacOS
/home/user/my_project/myenv/Scripts/activate     # Windows

# 安装离线依赖包
pip install --no-index --find-links=/home/user/my_project/offline_packages -r /home/user/my_project/requirements.txt


```

