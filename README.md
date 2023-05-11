# SmartShell💊

SmartShell is used to help you easily write very complex shell commands within the shell, and requires support from OpenAI-ChatGPT.

develop with [@uni-zhuan](https://github.com/uni-zhuan)

1. set your environmental variable : OPENAI_API_KEY (export OPENAI_API_KEY=XXX)
2. git clone https://github.com/crazycth/smartShell.git
3. cd smartShell && bash install.sh (install with pip3)

```
(base) ➜ [/Users/richard] help 查找当前目录下所有以.py结尾的文件，提取到当前目录的上一层
find . -name '*.py' -exec mv {} .. \;
```

Note : The shell command has been pasted into the clipboard, just use command+v to paste it
