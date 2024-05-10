from setuptools import setup, find_packages

setup(
    name='tomltool',  # 模塊名稱
    version='1.0.0',  # 版本號
    author='saucejullyfish',  # 作者名稱
    author_email='saucejullyfish@gmail.com',  # 作者郵箱地址
    description='A TOML configuration file handler.',  # 模塊簡介
    # 長描述，通常是讀取README.md文件內容
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',  # README.md的文件類型
    url='https://github.com/Sauce-jullyfish/toml_tool',  # GitHub倉庫鏈接或相似鏈接
    packages=find_packages(),  # 自動找到項目中的所有包（packages和modules）
    install_requires=[
        'tomlkit',  # 這個模塊依賴 tomlkit，確保在setup.py中添加
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU GENERAL PUBLIC LICENSE',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.11',  # 指定支持的Python版本
)
