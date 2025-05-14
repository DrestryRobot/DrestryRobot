const container = document.getElementById("gridContainer");
let currentCategory = "全部"; // 当前分类
let gridData = []; // 存储从 JSON 读取的数据

// 读取 JSON 数据
async function fetchData() {
  try {
    const response = await fetch("sites.json"); // 读取 sites.json
    gridData = await response.json();
    loadGrid(); // 加载数据
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
      gridItem.onclick = () => window.location.href = item.link;

      const icon = document.createElement("img");
      icon.src = item.image;
      icon.alt = item.name;

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
