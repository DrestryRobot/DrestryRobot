document.getElementById("editor").addEventListener("keydown", function(event) {
    if (event.key === "Tab") {
        event.preventDefault();
        const start = this.selectionStart;
        const end = this.selectionEnd;
        const spaces = "    ";
        this.value = this.value.substring(0, start) + spaces + this.value.substring(end);
        this.selectionStart = this.selectionEnd = start + spaces.length;
    }
});

function updatePreview() {
    const rstText = document.getElementById("editor").value;
    fetch("/preview", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ text: rstText })
    })
    .then(response => response.text())
    .then(data => document.getElementById("preview").innerHTML = data);
}

function saveFile() {
    const editor = document.getElementById("editor");
    const rstText = editor.value.trim(); // 去除前后空格

    if (!rstText) {
        alert("文档为空，无法保存！");
        return;
    }

    // **确保获取真正的首行，而不是 `=`**
    const lines = rstText.split(/\r?\n/).filter(line => line.trim() !== "" && !/^=+$/.test(line));
    let firstLine = lines.length > 0 ? lines[0].trim() : "document"; // 确保首行有效

    // **防止只匹配字母和数字，保证中文字符正确保存**
    if (!firstLine.match(/[\w\u4e00-\u9fa5]/)) {
        firstLine = "document";
    }

    // **优化文件名处理**
    const fileName = firstLine.replace(/[^a-zA-Z0-9_\u4e00-\u9fa5-]/g, "_") + ".rst";

    console.log("最终文件名:", fileName); // **调试：检查最终文件名**

    // **创建 Blob 下载**
    const blob = new Blob([rstText], { type: "text/plain" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = fileName;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}
