// 配置
const API_BASE = 'http://localhost:8000';
// 如果部署到 GitHub Pages，改为实际的后端地址
// const API_BASE = 'https://your-backend-url.com';

let allNews = [];
let currentCategory = 'all';

// 格式化时间
function formatTime(isoString) {
    if (!isoString) return '未知时间';
    
    const date = new Date(isoString);
    const now = new Date();
    const diff = now - date;
    
    // 分钟
    const minutes = Math.floor(diff / 60000);
    if (minutes < 60) return `${minutes}分钟前`;
    
    // 小时
    const hours = Math.floor(minutes / 60);
    if (hours < 24) return `${hours}小时前`;
    
    // 天
    const days = Math.floor(hours / 24);
    if (days < 3) return `${days}天前`;
    
    return date.toLocaleDateString('zh-CN');
}

// 格式化更新时间
function formatUpdateTime(isoString) {
    if (!isoString) return '--';
    const date = new Date(isoString);
    return date.toLocaleString('zh-CN');
}

// 获取新闻
async function fetchNews() {
    try {
        const response = await fetch(`${API_BASE}/api/news`);
        const data = await response.json();
        allNews = data.news || [];
        
        document.getElementById('last-update').textContent = 
            `最后更新：${formatUpdateTime(data.last_updated)}`;
        
        renderNews();
    } catch (error) {
        console.error('获取新闻失败:', error);
        document.getElementById('news-container').innerHTML = `
            <div class="loading">
                <p>⚠️ 无法连接到后端服务</p>
                <p style="font-size: 0.9rem; margin-top: 10px;">请确保后端服务正在运行</p>
            </div>
        `;
    }
}

// 渲染新闻
function renderNews() {
    const container = document.getElementById('news-container');
    
    if (allNews.length === 0) {
        container.innerHTML = '<div class="loading"><p>暂无新闻</p></div>';
        return;
    }
    
    const filteredNews = currentCategory === 'all' 
        ? allNews 
        : allNews.filter(n => n.category === currentCategory);
    
    if (filteredNews.length === 0) {
        container.innerHTML = '<div class="loading"><p>该分类下暂无新闻</p></div>';
        return;
    }
    
    container.innerHTML = filteredNews.map(news => `
        <article class="news-card">
            ${news.image ? `<img src="${news.image}" alt="${news.title}" class="news-image" onerror="this.style.display='none'">` : ''}
            <div class="news-content">
                <span class="news-source">${news.source || '未知来源'}</span>
                <h3 class="news-title">
                    <a href="${news.url}" target="_blank" rel="noopener">${news.title}</a>
                </h3>
                <p class="news-summary">${news.summary || ''}</p>
                <div class="news-meta">
                    <span class="news-time">🕐 ${formatTime(news.published)}</span>
                    <span>${news.category || 'AI'}</span>
                </div>
            </div>
        </article>
    `).join('');
}

// 分类切换
document.querySelectorAll('.category-btn').forEach(btn => {
    btn.addEventListener('click', () => {
        document.querySelectorAll('.category-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        currentCategory = btn.dataset.category;
        renderNews();
    });
});

// 倒计时
function startCountdown() {
    let seconds = 300; // 5 分钟
    
    setInterval(() => {
        seconds = seconds <= 0 ? 300 : seconds - 1;
        const minutes = Math.floor(seconds / 60);
        const secs = seconds % 60;
        document.getElementById('countdown').textContent = 
            `${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
        
        // 每 5 分钟刷新一次
        if (seconds === 0) {
            fetchNews();
        }
    }, 1000);
}

// 初始化
document.addEventListener('DOMContentLoaded', () => {
    fetchNews();
    startCountdown();
    
    // 每 5 分钟自动刷新
    setInterval(fetchNews, 300000);
});
