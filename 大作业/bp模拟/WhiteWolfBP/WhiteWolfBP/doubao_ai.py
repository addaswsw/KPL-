# 文件名: doubao_ai.py
import os
from volcenginesdkarkruntime import Ark

# 【最终修正】使用你提供的方舟大模型专用API Key
client = Ark(
    api_key="50fcde62-d03f-4bdb-9d02-91481829504c",
    timeout=60, # 设置60秒超时
)

def get_ai_commentary(prompt_text):
    """
    接收一个提示，返回豆包AI的回答
    """
    try:
        print("正在向豆包方舟API发送请求...")
        
        # 使用 client.chat.completions.create 方法
        response = client.chat.completions.create(
            # 使用你指定的模型ID
            model="doubao-seed-1.6-250615",
            messages=[
                {
                    "role": "system",
                    "content": "你是一位专业的KPL王者荣耀赛事解说。你的任务是根据当前的BP情况，用简洁、专业的语言进行分析和评论。不要说“你好”等多余的话，直接开始解说。"
                },
                {
                    "role": "user", 
                    "content": prompt_text
                }
            ],
        )
        
        print("成功收到AI回复。")
        # 返回AI生成的文本内容
        return response.choices[0].message.content
        
    except Exception as e:
        print(f"调用豆包API时出错: {e}")
        # 返回更详细的错误信息，方便调试
        return f"AI解说出现错误: {e}"