from pathlib import Path
from uuid import uuid4
import re

from flask import Flask, request

app = Flask(__name__)

# 文件保存在这个脚本旁边的 uploads 文件夹
UPLOAD_DIR = Path(__file__).resolve().parent / "uploads"
UPLOAD_DIR.mkdir(exist_ok=True)

# 每次上传请求最多 500 MB（包含表单数据）
app.config["MAX_CONTENT_LENGTH"] = 500 * 1024 * 1024

PAGE = """
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>文件上传</title>
</head>
<body>
    <h2>上传文件给我</h2>
    <p>支持多选，每次上传总大小请小于 500 MB。</p>
    <form method="post" enctype="multipart/form-data">
        <input type="file" name="files" multiple required>
        <button type="submit">上传</button>
    </form>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def upload():
    if request.method == "GET":
        return PAGE

    files = [
        f for f in request.files.getlist("files")
        if f.filename
    ]
    if not files:
        return "请先选择文件。", 400

    for file in files:
        # 去掉路径及 Windows 文件名中的非法字符，保留中文
        name = file.filename.replace("\\", "/").split("/")[-1]
        name = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", name)
        name = name.strip(" .")[:120] or "file"

        # 添加唯一编号，避免同名文件被覆盖
        target = UPLOAD_DIR / f"{uuid4().hex}_{name}"
        with target.open("xb") as output:
            file.save(output)

    return f"成功上传 {len(files)} 个文件！<br><a href='/'>继续上传</a>"


@app.errorhandler(413)
def too_large(error):
    return "上传总大小超过 500 MB，请分批上传。", 413


if __name__ == "__main__":
    print(f"文件保存位置：{UPLOAD_DIR}")
    app.run(host="0.0.0.0", port=8000, debug=False)