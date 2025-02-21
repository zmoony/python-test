from setuptools import setup, find_packages

setup(
    name='python_test01',  # 项目名称
    version='0.1.0',    # 版本号
    description='just begin test python3.',  # 简短描述
    long_description=open('README.md').read(),  # 详细描述，通常从 README 文件读取
    long_description_content_type='text/markdown',  # 描述内容类型
    author='aurora',  # 作者名
    author_email='zy789789zg@163.com',  # 作者邮箱
    url='https://github.com/yourusername/my_project',  # 项目主页
    packages=find_packages(exclude=['tests']),  # 自动查找并包含所有包
    include_package_data=True,  # 包含非Python文件（如配置文件）
    install_requires=[
        'requests>=2.25.1',  # 项目依赖的第三方库
        'numpy>=1.19.5',
        # 添加更多依赖项
    ],
    python_requires='>=3.6',  # 指定支持的 Python 版本
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    entry_points={
        'console_scripts': [
            'doc_to_excel=python_test01.scripts.doc_to_excel:main',  # 定义命令行工具
        ],
    },
)
