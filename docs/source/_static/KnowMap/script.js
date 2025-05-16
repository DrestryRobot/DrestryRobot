const container = document.getElementById("gridContainer");
let currentCategory = "全部"; // 当前分类
let gridData = []; // 存储从 JSON 读取的数据

const BASE_URL = "https://drestryrobot.readthedocs.io/技术总结/"; // 知识点基础路径
const IMAGE_BASE_URL = "https://drestryrobot.readthedocs.io/_static/KnowMap/images/"; // 图片基础路径

// 读取 JSON 数据
async function fetchData() {
  try {
    const response = await fetch("sites.json");
    if (!response.ok) {
      throw new Error(`HTTP 错误！状态码: ${response.status}`);
    }
    gridData = await response.json();
    loadGrid();
  } catch (error) {
    console.error("数据加载失败:", error);
  }
}

// 加载网格项，支持分类与搜索
function loadGrid(category = "全部", searchQuery = "") {
  container.innerHTML = "";

  gridData.forEach(item => {
    if ((category === "全部" || item.category === category) &&
        (searchQuery === "" || item.name.toLowerCase().includes(searchQuery.toLowerCase()))) {
      const wrapper = document.createElement("div");
      wrapper.className = "grid-item-wrapper";

      const gridItem = document.createElement("div");
      gridItem.className = "grid-item";
      gridItem.onclick = () => window.location.href = BASE_URL + item.name + ".html"; // ✅ 自动拼接完整知识点链接

      const icon = document.createElement("img");
      icon.src = IMAGE_BASE_URL + item.name + ".png"; // 尝试使用自定义图片
      icon.alt = item.name;

      // 如果图片加载失败，则使用默认图片
      icon.onerror = () => {
        icon.src = IMAGE_BASE_URL + "默认图标.png";
      };

      const title = document.createElement("div");
      title.className = "grid-name";
      title.innerText = item.name;

      gridItem.appendChild(icon);
      wrapper.appendChild(gridItem);
      wrapper.appendChild(title);
      container.appendChild(wrapper);
    }
  });
}

// 分类按钮点击时调用此函数
function filterGrid(category) {
  currentCategory = category;
  const searchText = document.getElementById("searchBox").value.trim();
  loadGrid(currentCategory, searchText);
}

// 在搜索框内输入时实时过滤
document.getElementById("searchBox").addEventListener("input", function() {
  loadGrid(currentCategory, this.value.trim());
});

// 读取 JSON 数据并加载页面
fetchData();
