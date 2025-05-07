// // 缓存图标，避免重复请求
// const iconCache = JSON.parse(localStorage.getItem("iconCache")) || {};

// // 检测图片能否加载成功
// async function checkImage(url) {
//     return new Promise((resolve) => {
//         const img = new Image();
//         img.onload = () => resolve(url);
//         img.onerror = () => resolve(null);
//         img.src = url;
//     });
// }

// // 尝试获取最佳图标：先查 manifest，再尝试 apple-touch-icon、favicon，最后降级到 Google S2 API
// async function getBestIcon(domain) {
//     if (iconCache[domain]) { 
//         return iconCache[domain];
//     }

//     const manifestUrl = `https://${domain}/manifest.json`;
//     try {
//         const response = await fetch(manifestUrl);
//         if (response.ok) {
//             const data = await response.json();
//             if (data.icons && data.icons.length) {
//                 let largestIcon = data.icons[data.icons.length - 1].src;
//                 let iconUrl = new URL(largestIcon, manifestUrl).href;
//                 if (await checkImage(iconUrl)) {
//                     iconCache[domain] = iconUrl;
//                     localStorage.setItem("iconCache", JSON.stringify(iconCache));
//                     return iconUrl;
//                 }
//             }
//         }
//     } catch (e) {}

//     const appleIcon = `https://${domain}/apple-touch-icon.png`;
//     const favicon = `https://${domain}/favicon.ico`;
//     const googleIcon = `https://www.google.com/s2/favicons?domain=${domain}&sz=64`;

//     const result = await Promise.race([
//         checkImage(appleIcon),
//         checkImage(favicon),
//         Promise.resolve(googleIcon)
//     ]);
//     iconCache[domain] = result || googleIcon;
//     localStorage.setItem("iconCache", JSON.stringify(iconCache));
//     return iconCache[domain];
// }

// // 获取网站数据
// async function fetchSiteData() {
//     const response = await fetch("https://drestryrobot.readthedocs.io/zh-cn/latest/_static/SiteSearch/sites.json");
//     return response.json();
// }

// const container = document.getElementById("gridContainer");
// let currentCategory = "全部"; // 当前分类

// // 加载网格项，支持分类与搜索（同时过滤）
// async function loadGrid(category = "全部", searchQuery = "") {
//     container.innerHTML = "";
    
//     const gridData = await fetchSiteData();
//     const iconPromises = gridData.map(item => getBestIcon(item.domain));
//     const icons = await Promise.all(iconPromises);

//     gridData.forEach((item, index) => {
//         // 先按分类过滤，再按搜索文字过滤（忽略大小写）
//         if ((category === "全部" || item.category === category) &&
//             (searchQuery === "" || item.name.toLowerCase().includes(searchQuery.toLowerCase()))) {
//             const wrapper = document.createElement("div");
//             wrapper.className = "grid-item-wrapper";

//             const gridItem = document.createElement("div");
//             gridItem.className = "grid-item";
//             gridItem.onclick = () => window.location.href = item.link;

//             const icon = document.createElement("img");
//             icon.src = icons[index];
//             icon.alt = item.name;

//             const title = document.createElement("div");
//             title.className = "grid-name";
//             title.innerText = item.name;

//             gridItem.appendChild(icon);
//             wrapper.appendChild(gridItem);
//             wrapper.appendChild(title);
//             container.appendChild(wrapper);
//         }
//     });
// }

// // 分类按钮点击时调用此函数
// function filterGrid(category) {
//     currentCategory = category;
//     const searchText = document.getElementById("searchBox").value.trim();
//     loadGrid(currentCategory, searchText);
// }

// // 在搜索框内输入时实时过滤
// document.getElementById("searchBox").addEventListener("input", function() {
//     loadGrid(currentCategory, this.value.trim());
// });

// // 在用户按下回车后自动清空搜索框
// document.getElementById("searchBox").addEventListener("keydown", function(event) {
//     if (event.key === "Enter") {
//         this.value = ""; // 清空输入框
//     }
// });


// // 初始加载全部项
// loadGrid();



// 缓存图标，避免重复请求
const iconCache = JSON.parse(localStorage.getItem("iconCache")) || {};

// GitHub 图标存储路径
const getGitHubIconUrl = (domain) => `https://drestryrobot.github.io/icon-storage/icons/${domain}.png`;

// 检测图片能否加载成功
async function checkImage(url) {
    return new Promise((resolve) => {
        const img = new Image();
        img.onload = () => resolve(url);
        img.onerror = () => resolve(null);
        img.src = url;
    });
}

// 只从 GitHub 获取图标
async function getBestIcon(domain) {
    if (iconCache[domain]) { 
        return iconCache[domain];
    }

    const githubIcon = getGitHubIconUrl(domain);
    const validIcon = await checkImage(githubIcon);

    iconCache[domain] = validIcon || githubIcon; // 如果 GitHub 图标不存在，仍然返回默认路径
    localStorage.setItem("iconCache", JSON.stringify(iconCache));
    return iconCache[domain];
}

// 获取网站数据
async function fetchSiteData() {
    const response = await fetch("https://drestryrobot.readthedocs.io/zh-cn/latest/_static/SiteSearch/sites.json");
    return response.json();
}

const container = document.getElementById("gridContainer");
let currentCategory = "全部"; // 当前分类

// 加载网格项，支持分类与搜索（同时过滤）
async function loadGrid(category = "全部", searchQuery = "") {
    container.innerHTML = "";
    
    const gridData = await fetchSiteData();
    const iconPromises = gridData.map(item => getBestIcon(item.domain));
    const icons = await Promise.all(iconPromises);

    gridData.forEach((item, index) => {
        // 先按分类过滤，再按搜索文字过滤（忽略大小写）
        if ((category === "全部" || item.category === category) &&
            (searchQuery === "" || item.name.toLowerCase().includes(searchQuery.toLowerCase()))) {
            const wrapper = document.createElement("div");
            wrapper.className = "grid-item-wrapper";

            const gridItem = document.createElement("div");
            gridItem.className = "grid-item";
            gridItem.onclick = () => window.location.href = item.link;

            const icon = document.createElement("img");
            icon.src = icons[index];
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

// 在用户按下回车后自动清空搜索框
document.getElementById("searchBox").addEventListener("keydown", function(event) {
    if (event.key === "Enter") {
        this.value = ""; // 清空输入框
    }
});

// 初始加载全部项
loadGrid();

