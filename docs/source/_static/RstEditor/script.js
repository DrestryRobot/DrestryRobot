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

async function preloadPyodide() {
    window.pyodide = await loadPyodide();
    await pyodide.loadPackage(["micropip"]);
    await pyodide.runPythonAsync("import micropip; micropip.install('docutils')");
    console.log("Pyodide 和 docutils 加载完成");
}
preloadPyodide(); // **提前加载**


async function loadPyodideAndDocutils() {
    window.pyodide = await loadPyodide();
    await pyodide.loadPackage(["micropip"]);
    await pyodide.runPythonAsync("import micropip; micropip.install('docutils')");
    console.log("Pyodide 和 docutils 加载完成");
}
loadPyodideAndDocutils();


async function updatePreview() {
    if (!window.pyodide) {
        console.error("Pyodide 未加载，无法解析 RST");
        return;
    }

    // **正确处理换行符**
    const rstText = document.getElementById("editor").value.replace(/\r?\n/g, "\\n");

    let pyCode = `
from docutils.core import publish_parts
rst_text = """${rstText}"""
html_output = publish_parts(rst_text, writer_name="html")["html_body"]
html_output
    `;

    try {
        let result = await pyodide.runPythonAsync(pyCode);
        document.getElementById("preview").innerHTML = result;
    } catch (error) {
        console.error("RST 解析失败:", error);
        document.getElementById("preview").innerHTML = "<p style='color:red;'>无法解析 RST 格式</p>";
    }
}



function saveFile() {
    const editor = document.getElementById("editor");
    const rstText = editor.value.trim(); 

    if (!rstText) {
        alert("文档为空，无法保存！");
        return;
    }

    // 获取首行并确保有效内容
    const lines = rstText.split(/\r?\n/).filter(line => line.trim() !== "" && !/^=+$/.test(line));
    let firstLine = lines.length > 0 ? lines[0].trim() : "document";

    if (!firstLine.match(/[\w\u4e00-\u9fa5]/)) {
        firstLine = "document";
    }

    const fileName = firstLine.replace(/[^a-zA-Z0-9_\u4e00-\u9fa5-]/g, "_") + ".rst";

    console.log("文件名:", fileName);

    const blob = new Blob([rstText], { type: "text/plain" });
    const a = document.createElement("a");
    a.href = URL.createObjectURL(blob);
    a.download = fileName;
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}
