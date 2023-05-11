import os,sys,requests,json,pyperclip

def unescape_string(s):
    return s.encode('utf-8').decode('unicode_escape')

def build_prompt(message):
    prompt = f'''
        请帮我根据输入的要求,输出可执行的shell语句
        输入message: "输出hello"
        输出: "echo hello"
        输入message: "列出当前目录下所有文件"
        输出: "ls"
        输入message: "删除文件test.txt"
        输出: "rm test.txt"
        输入message: "打开文件test.txt"
        输出: "open test.txt"
        输入message: "创建一个名为test的空文件夹"
        输出: "mkdir test"
        输入message: "无法实现"
        输出: "抱歉，我无法理解您的要求。"
        输入message:"{message}"
        输出:'''
    return prompt

def main():
    API_KEY = os.environ.get("OPENAI_API_KEY")
    if len(API_KEY)==0:
        print("openai api key empty! please check your OPENAI_API_KEY")
        return
    elif len(sys.argv)<=1:
        print("no prompt input!")
        return
    msg = sys.argv[1]
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}"
    }   
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {"role": "user", "content": build_prompt(msg)}
            ],
        "temperature": 0.1,
    }
    # Send the request
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, data=json.dumps(payload))
    result = response.json()["choices"][0]["message"]["content"].strip('"')
    pyperclip.copy(result)
    print(result)

if __name__ == "__main__":
    main()