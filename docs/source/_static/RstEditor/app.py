import os
import docutils.core
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__)

# 创建 rst_files 目录（用于存储 RST 文档）
rst_dir = os.path.join(os.path.dirname(__file__), "rst_files")
os.makedirs(rst_dir, exist_ok=True)

@app.route("/")
def index():
    """ 加载 RST 编辑器网页 """
    base_dir = os.path.dirname(os.path.abspath(__file__))
    html_path = os.path.join(base_dir, "index.html")

    if not os.path.exists(html_path):
        return "Error: index.html 文件不存在", 500

    with open(html_path, "r", encoding="utf-8") as f:
        return f.read()

# 提供静态文件（CSS 和 JS）
@app.route("/styles.css")
def styles():
    return send_from_directory(".", "styles.css")

@app.route("/script.js")
def script():
    return send_from_directory(".", "script.js")

@app.route("/preview", methods=["POST"])
def preview():
    """ 解析 RST 文档并返回 HTML """
    data = request.json
    rst_text = data.get("text", "").strip()

    if not rst_text:
        return jsonify({"error": "预览失败：文档内容为空"}), 400

    html = docutils.core.publish_parts(source=rst_text, writer_name="html")["html_body"]
    return html

@app.route("/save", methods=["POST"])
def save():
    """ 服务器保存 RST 文档，文件名自动取第一行 """
    data = request.json
    rst_text = data.get("text", "").strip()

    if not rst_text:
        return jsonify({"error": "保存失败：文档内容为空"}), 400

    first_line = rst_text.split("\n", 1)[0].strip()
    filename = f"{first_line or 'untitled'}.rst".replace(" ", "_")
    file_path = os.path.join(rst_dir, filename)

    try:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(rst_text)
        return jsonify({"message": "文件已保存", "filename": filename})
    except Exception as e:
        return jsonify({"error": f"文件保存失败：{str(e)}"}), 500

if __name__ == "__main__":
    print("RST 编辑器 API 启动成功！")
    app.run(debug=True)
