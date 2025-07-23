#!/usr/bin/env python3
"""
极简版MCP工具制作模板
最简单的MCP工具开发模板，只需替换示例函数即可

使用步骤：
1. 修改工具名称
2. 替换 my_tool 函数为你的功能
3. 运行测试
"""

import json
import logging
from datetime import datetime
from mcp.server.fastmcp import FastMCP

# ================================
# 1. 配置你的工具
# ================================
TOOL_NAME = "我的MCP工具"  # 修改为你的工具名

# 设置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(TOOL_NAME)

# 创建MCP服务器
mcp = FastMCP(TOOL_NAME)

# ================================
# 2. 工具函数（替换这里的内容）
# ================================

@mcp.tool()
def my_tool(text: str) -> str:
    """
    我的工具函数 - 替换为你需要的功能
    
    这是一个文本分析示例，你可以替换为任何功能：
    - 文件操作
    - API调用  
    - 数据处理
    - 系统命令
    - 等等...
    
    Args:
        text (str): 输入的文本
        
    Returns:
        str: 处理结果
    """
    try:
        # 参数检查
        if not text or not text.strip():
            return "❌ 错误：文本不能为空"
        
        # 你的核心逻辑 - 替换下面的代码
        # ================================
        result = {
            "输入文本": text,
            "字符数": len(text),
            "单词数": len(text.split()),
            "处理时间": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        }
        # ================================
        
        # 返回格式化结果
        return f"✅ 处理完成\n\n{json.dumps(result, indent=2, ensure_ascii=False)}"
        
    except Exception as e:
        logger.error(f"工具执行错误: {e}")
        return f"❌ 执行失败: {str(e)}"

# ================================
# 3. 启动服务器
# ================================
if __name__ == "__main__":
    logger.info(f"启动 {TOOL_NAME}")
    try:
        mcp.run()
    except KeyboardInterrupt:
        logger.info("正在关闭...")
    finally:
        logger.info("服务器已关闭")

# ================================
# 4. 使用说明
# ================================
"""
🚀 三步创建你的MCP工具：

1️⃣ 修改工具名：
   TOOL_NAME = "你的工具名"

2️⃣ 替换工具函数：
   把 my_tool 函数里的逻辑替换为你需要的功能

3️⃣ 运行测试：
   python your_tool.py

💡 常见工具类型：
   - 文件工具：读写文件、压缩解压
   - 网络工具：发送请求、下载文件  
   - 数据工具：Excel处理、JSON转换
   - 系统工具：执行命令、获取信息
   - AI工具：调用API、文本处理

🔧 函数模板：
   @mcp.tool()
   def 函数名(参数: 类型) -> str:
       try:
           # 你的逻辑
           return "✅ 成功结果"
       except Exception as e:
           return f"❌ 错误: {e}"
"""