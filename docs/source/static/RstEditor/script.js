document.getElementById("editor").addEventListener("keydown", function(event) {
    if (event.key === "Tab") {
        event.preventDefault();
        const { selectionStart, selectionEnd, value } = this;
        const spaces = "    ";
        this.value = value.slice(0, selectionStart) + spaces + value.slice(selectionEnd);
        this.selectionStart = this.selectionEnd = selectionStart + spaces.length;
    }
});

async function loadPyodideAndDocutils() {
    window.pyodide = await loadPyodide();
    await pyodide.loadPackage("docutils");  // ✅ 只加载 docutils，不需要 micropip
    console.log("Pyodide 和 docutils 加载完成");
}
loadPyodideAndDocutils();

async function updatePreview() {
    if (!window.pyodide) {
        console.error("Pyodide 未加载，无法解析 RST");
        return;
    }

    const rstText = document.getElementById("editor").value;
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
    const rstText = document.getElementById("editor").value.trim();
    if (!rstText) return alert("文档为空，无法保存！");

    const firstLine = rstText.split(/\r?\n/).find(line => line.trim()) || "document";
    const fileName = firstLine.replace(/[^a-zA-Z0-9_\u4e00-\u9fa5-]/g, "_") + ".rst";

    const blob = new Blob([rstText], { type: "text/plain" });
    const a = Object.assign(document.createElement("a"), { href: URL.createObjectURL(blob), download: fileName });
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
}

function importFile() {
    const file = document.getElementById("fileInput").files[0];
    if (!file) return alert("请选择一个 RST 文件！");

    const reader = new FileReader();
    reader.onload = ({ target }) => {
        document.getElementById("editor").value = target.result;
        updatePreview();
    };
    reader.readAsText(file);
}

async function exportPDF() {
    const { jsPDF } = window.jspdf;
    const doc = new jsPDF();

    const fontUrl = "NotoSansSC-Regular.ttf";
    const fontData = await fetch(fontUrl).then(res => res.arrayBuffer());
    
    // **更优化的 Base64 处理**
    const byteArray = new Uint8Array(fontData);
    let binaryString = "";
    for (let i = 0; i < byteArray.length; i++) {
        binaryString += String.fromCharCode(byteArray[i]);
    }
    const base64Font = btoa(binaryString);

    // **注册并使用字体**
    doc.addFileToVFS("NotoSansSC-Regular.ttf", base64Font);
    doc.addFont("NotoSansSC-Regular.ttf", "NotoSansSC", "normal");
    doc.setFont("NotoSansSC");

    const previewText = document.getElementById("preview").textContent.trim();
    if (!previewText) {
        alert("预览区域为空，无法导出 PDF！");
        return;
    }

    doc.text(previewText, 10, 10, { maxWidth: 180 });
    doc.save("RST_Document.pdf");
}

function openHelp() {
    window.open("https://drestryrobot.readthedocs.io/产品展示/RstEditor.html", "_blank");
}
