// 記事動的表示スクリプト
(function() {
    'use strict';

    let allArticles = [];
    let filteredArticles = [];
    let currentPage = 1;
    const articlesPerPage = 12;
    let currentCategory = 'all';
    let searchQuery = '';

    // 初期化
    async function init() {
        try {
            const response = await fetch('articles-index.json');
            const data = await response.json();
            allArticles = data.articles;
            filteredArticles = allArticles;

            renderArticles();
            setupEventListeners();
            updateStats();
        } catch (error) {
            console.error('記事データの読み込みに失敗:', error);
            document.getElementById('articlesGrid').innerHTML =
                '<div class="no-results">記事データの読み込みに失敗しました。</div>';
        }
    }

    // イベントリスナー設定
    function setupEventListeners() {
        // カテゴリーフィルター
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.addEventListener('click', function() {
                document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
                this.classList.add('active');
                currentCategory = this.dataset.category;
                currentPage = 1;
                filterArticles();
            });
        });

        // 検索
        const searchInput = document.getElementById('searchInput');
        searchInput.addEventListener('input', function() {
            searchQuery = this.value.toLowerCase();
            currentPage = 1;
            filterArticles();
        });
    }

    // 記事フィルタリング
    function filterArticles() {
        filteredArticles = allArticles.filter(article => {
            // カテゴリーフィルター
            const categoryMatch = currentCategory === 'all' || article.category === currentCategory;

            // 検索フィルター
            const searchMatch = !searchQuery ||
                article.title.toLowerCase().includes(searchQuery) ||
                article.description.toLowerCase().includes(searchQuery) ||
                article.keywords.some(k => k.toLowerCase().includes(searchQuery));

            return categoryMatch && searchMatch;
        });

        renderArticles();
        updateStats();
    }

    // 記事レンダリング
    function renderArticles() {
        const grid = document.getElementById('articlesGrid');
        const pagination = document.getElementById('pagination');

        // ページ範囲計算
        const start = (currentPage - 1) * articlesPerPage;
        const end = start + articlesPerPage;
        const pageArticles = filteredArticles.slice(start, end);

        if (pageArticles.length === 0) {
            grid.innerHTML = '<div class="no-results">該当する記事が見つかりませんでした。</div>';
            pagination.style.display = 'none';
            return;
        }

        // 記事カード生成
        grid.innerHTML = pageArticles.map(article => `
            <div class="article-card" onclick="location.href='${article.url}'">
                <img loading="lazy" src="${article.image}" alt="${escapeHtml(article.title)}" class="article-thumbnail" onerror="this.src='images/article-placeholder.jpg'">
                <div class="article-info">
                    <span class="article-category">${escapeHtml(article.category)}</span>
                    <h3 class="article-title">${escapeHtml(article.title)}</h3>
                    <p class="article-description">${escapeHtml(article.description)}</p>
                    <div class="article-meta">
                        <span>${article.date}</span>
                        <span class="article-likes">👁 ${article.likes.toLocaleString()} いいね</span>
                    </div>
                </div>
            </div>
        `).join('');

        // ページネーション生成
        renderPagination();
    }

    // ページネーション生成
    function renderPagination() {
        const pagination = document.getElementById('pagination');
        const totalPages = Math.ceil(filteredArticles.length / articlesPerPage);

        if (totalPages <= 1) {
            pagination.style.display = 'none';
            return;
        }

        pagination.style.display = 'flex';

        let html = '';

        // 前へボタン
        html += `<button class="pagination-btn" ${currentPage === 1 ? 'disabled' : ''} onclick="changePage(${currentPage - 1})">« 前へ</button>`;

        // ページ番号
        const maxButtons = 5;
        let startPage = Math.max(1, currentPage - Math.floor(maxButtons / 2));
        let endPage = Math.min(totalPages, startPage + maxButtons - 1);

        if (endPage - startPage < maxButtons - 1) {
            startPage = Math.max(1, endPage - maxButtons + 1);
        }

        if (startPage > 1) {
            html += `<button class="pagination-btn" onclick="changePage(1)">1</button>`;
            if (startPage > 2) html += '<span style="padding: 0 0.5rem; color: rgba(255,255,255,0.5);">...</span>';
        }

        for (let i = startPage; i <= endPage; i++) {
            html += `<button class="pagination-btn ${i === currentPage ? 'active' : ''}" onclick="changePage(${i})">${i}</button>`;
        }

        if (endPage < totalPages) {
            if (endPage < totalPages - 1) html += '<span style="padding: 0 0.5rem; color: rgba(255,255,255,0.5);">...</span>';
            html += `<button class="pagination-btn" onclick="changePage(${totalPages})">${totalPages}</button>`;
        }

        // 次へボタン
        html += `<button class="pagination-btn" ${currentPage === totalPages ? 'disabled' : ''} onclick="changePage(${currentPage + 1})">次へ »</button>`;

        pagination.innerHTML = html;
    }

    // ページ変更
    window.changePage = function(page) {
        currentPage = page;
        renderArticles();
        window.scrollTo({ top: 0, behavior: 'smooth' });
    };

    // 統計更新
    function updateStats() {
        const statsText = document.getElementById('statsText');
        const showing = Math.min(currentPage * articlesPerPage, filteredArticles.length);
        const start = filteredArticles.length > 0 ? (currentPage - 1) * articlesPerPage + 1 : 0;

        let text = `全${allArticles.length}件中 ${filteredArticles.length}件`;
        if (filteredArticles.length > articlesPerPage) {
            text += ` （${start}〜${showing}件を表示）`;
        }

        statsText.textContent = text;
    }

    // HTMLエスケープ
    function escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }

    // ページ読み込み時に実行
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', init);
    } else {
        init();
    }
})();
