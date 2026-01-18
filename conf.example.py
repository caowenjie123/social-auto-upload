from pathlib import Path

BASE_DIR = Path(__file__).parent.resolve()
XHS_SERVER = "http://127.0.0.1:11901"
LOCAL_CHROME_PATH = ""   # change me necessary！ for example C:/Program Files/Google/Chrome/Application/chrome.exe
LOCAL_CHROME_HEADLESS = False

# 输入延迟时间（秒），控制填写内容的速度，建议 1-2 秒
TYPING_DELAY = 1.5

# 是否手动确认发布，设置为 True 时，程序会在发布前等待用户在终端按回车确认
MANUAL_PUBLISH = True

# 是否保持浏览器打开，设置为 True 时，上传完成后浏览器不会自动关闭，需要用户手动关闭
KEEP_BROWSER_OPEN = True
