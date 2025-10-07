#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSV記事化スクリプト - 借金6億ニキMEDIA
TikTok動画の文字起こしデータから記事HTMLを自動生成
"""

import csv
import os
import re
from datetime import datetime
from urllib.parse import urlparse

# カテゴリー分類のキーワードマッピング
CATEGORY_KEYWORDS = {
    '借金返済': ['借金', '返済', '債務整理', '自己破産', '多重債務', '滞納'],
    '詐欺対策': ['詐欺', '詐欺師', '投資詐欺', '共同経営'],
    '金融知識': ['ブラック', 'ブラックリスト', 'CIC', 'JICC', '信用情報', 'クレカ', 'デポジット'],
    'ビジネス': ['社長', '起業', 'ビジネス', '副業', '収入'],
    'マインドセット': ['メンタル', 'モチベーション', 'なぜなぜ'],
    'SNS戦略': ['TikTok', 'フォロワー', 'SNS']
}

def categorize_article(description, transcript):
    """説明文と文字起こしからカテゴリーを判定"""
    text = (description + ' ' + transcript).lower()

    # カテゴリーごとのマッチ数をカウント
    scores = {}
    for category, keywords in CATEGORY_KEYWORDS.items():
        score = sum(1 for keyword in keywords if keyword.lower() in text)
        scores[category] = score

    # 最もスコアが高いカテゴリーを返す
    if max(scores.values()) > 0:
        return max(scores, key=scores.get)
    return '借金返済'  # デフォルト

def extract_video_id(url):
    """TikTok URLから動画IDを抽出"""
    match = re.search(r'/video/(\d+)', url)
    return match.group(1) if match else None

def clean_text(text):
    """テキストをクリーニング（改行、空白の整理）"""
    if not text:
        return ""
    # 改行を段落に変換
    paragraphs = [p.strip() for p in text.split('\n') if p.strip()]
    return '\n\n'.join(paragraphs)

def generate_article_html(row, index):
    """CSV行から記事HTMLを生成"""
    video_url = row[0]
    thumbnail = row[1]
    likes = row[2]
    description = row[3]
    # 文字起こし修正(8列目)を優先、なければ文字起こし(7列目)を使用
    transcript_edited = row[7] if len(row) > 7 else ""
    transcript_original = row[6] if len(row) > 6 else ""
    transcript = transcript_edited.strip() if transcript_edited.strip() else transcript_original.strip()

    # 記事ID生成
    video_id = extract_video_id(video_url)
    article_id = f"article-{video_id}" if video_id else f"article-{index}"

    # カテゴリー判定
    category = categorize_article(description, transcript)

    # タイトル生成（説明文の最初の部分を使用）
    title = description.split('\n')[0].strip()
    if not title or title.startswith('#'):
        title = f"借金6億ニキの実体験 #{index}"

    # 説明文とハッシュタグを分離
    desc_parts = description.split('#')
    main_desc = desc_parts[0].strip()
    hashtags = ['#' + tag.strip() for tag in desc_parts[1:]] if len(desc_parts) > 1 else []

    # 文字起こしを段落に分割
    content_paragraphs = clean_text(transcript).split('\n\n')

    # 日付（現在日付を使用）
    date = datetime.now().strftime('%Y-%m-%d')
    date_jp = datetime.now().strftime('%Y年%m月%d日')

    # HTMLテンプレート
    html = f'''<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="{main_desc[:150]}">
    <meta name="keywords" content="借金6億ニキ,{category},{','.join(hashtags[:3])}">
    <meta property="og:title" content="{title}">
    <meta property="og:description" content="{main_desc[:150]}">
    <meta property="og:image" content="{thumbnail}">
    <meta property="og:type" content="article">
    <meta name="twitter:card" content="summary_large_image">
    <title>{title} | 借金6億ニキ公式メディア</title>
    <link rel="stylesheet" href="css/style.css">
    <link rel="stylesheet" href="css/animations.css">
    <link rel="stylesheet" href="css/article.css">
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700;900&family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
</head>
<body>
    <!-- ヘッダー -->
    <header class="main-header">
        <nav class="navbar">
            <div class="container">
                <div class="nav-wrapper">
                    <div class="logo">
                        <a href="index.html">
                            <span class="logo-text">借金<span class="highlight">6億</span>ニキ</span>
                            <span class="logo-subtitle">MEDIA</span>
                        </a>
                    </div>
                    <ul class="nav-menu">
                        <li><a href="index.html" class="nav-link">ホーム</a></li>
                        <li><a href="index.html#story" class="nav-link">ストーリー</a></li>
                        <li><a href="articles.html" class="nav-link">記事</a></li>
                        <li><a href="videos.html" class="nav-link">動画</a></li>
                        <li><a href="consulting.html" class="nav-link">コンサル</a></li>
                        <li><a href="contact.html" class="nav-link">お問い合わせ</a></li>
                    </ul>
                    <div class="hamburger">
                        <span></span>
                        <span></span>
                        <span></span>
                    </div>
                </div>
            </div>
        </nav>
    </header>

    <!-- 記事ヒーローセクション -->
    <section class="article-hero">
        <div class="article-hero-bg">
            <div class="gradient-overlay"></div>
            <img src="{thumbnail}" alt="{title}">
        </div>
        <div class="container">
            <div class="article-hero-content">
                <div class="breadcrumb">
                    <a href="index.html">ホーム</a>
                    <span>/</span>
                    <a href="articles.html">{category}</a>
                    <span>/</span>
                    <span>記事</span>
                </div>
                <h1 class="article-title">{title}</h1>
                <div class="article-meta-hero">
                    <div class="author">
                        <img src="images/author.jpg" alt="借金6億ニキ" class="author-avatar">
                        <div class="author-info">
                            <span class="author-name">借金6億ニキ</span>
                            <span class="publish-date">{date_jp}</span>
                        </div>
                    </div>
                    <div class="article-stats">
                        <span class="reading-time">⏱ 5分で読める</span>
                        <span class="views">👁 {likes} いいね</span>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <!-- 記事コンテンツ -->
    <article class="article-detail">
        <!-- 記事ヘッダー（要件に沿った構造） -->
        <header class="article-header">
            <div class="container">
                <img src="{thumbnail}" alt="{title}" class="article-image">
                <div class="article-meta">
                    <span class="category">{category}</span>
                    <time datetime="{date}">{date_jp}</time>
                </div>
                <h1 class="article-title">{title}</h1>
            </div>
        </header>

        <div class="container">
            <div class="content-wrapper">
                <!-- メインコンテンツ -->
                <div class="main-content">
                    <!-- イントロダクション -->
                    <section class="content-section">
                        <p class="lead-text">{main_desc}</p>
                    </section>

                    <!-- 本文 -->
                    <section class="content-section">
                        <h2>詳細内容</h2>
'''

    # 文字起こし内容を段落として追加
    for i, paragraph in enumerate(content_paragraphs):
        if paragraph:
            html += f'                        <p>{paragraph}</p>\n'

    # ハッシュタグがあれば追加
    if hashtags:
        html += f'''
                        <div class="tags">
                            {' '.join([f'<span class="tag">{tag}</span>' for tag in hashtags[:5]])}
                        </div>
'''

    # 動画リンク
    html += f'''
                        <div class="highlight-box">
                            <h3>📹 この内容はTikTok動画でも配信中</h3>
                            <a href="{video_url}" target="_blank" class="btn btn-primary">TikTokで見る</a>
                        </div>
                    </section>

                    <!-- シェアボタン -->
                    <div class="share-section">
                        <h3>この記事をシェア</h3>
                        <div class="share-buttons">
                            <button class="share-btn twitter">Twitter</button>
                            <button class="share-btn facebook">Facebook</button>
                            <button class="share-btn line">LINE</button>
                            <button class="share-btn copy">リンクをコピー</button>
                        </div>
                    </div>
                </div>

                <!-- 記事フッター（要件に沿った構造） -->
                <footer class="article-footer">
                    <a href="articles.html" class="read-more">他の記事を読む →</a>
                </footer>

                <!-- サイドバー -->
                <aside class="sidebar">
                    <!-- 著者プロフィール -->
                    <div class="widget author-widget">
                        <h3>著者プロフィール</h3>
                        <div class="author-card">
                            <img src="images/author-large.jpg" alt="借金6億ニキ">
                            <h4>借金6億ニキ</h4>
                            <p>最大6億円の借金を抱えながらも、独自の戦略で返済を続ける起業家。TikTokフォロワー6000人超。</p>
                            <div class="author-social">
                                <a href="#">TikTok</a>
                                <a href="#">YouTube</a>
                                <a href="#">Twitter</a>
                            </div>
                        </div>
                    </div>

                    <!-- カテゴリー -->
                    <div class="widget category-widget">
                        <h3>カテゴリー</h3>
                        <ul class="category-list">
                            <li><a href="#">借金返済 <span>(45)</span></a></li>
                            <li><a href="#">詐欺対策 <span>(38)</span></a></li>
                            <li><a href="#">金融知識 <span>(29)</span></a></li>
                            <li><a href="#">ビジネス <span>(52)</span></a></li>
                        </ul>
                    </div>

                    <!-- ニュースレター -->
                    <div class="widget newsletter-widget">
                        <h3>無料LINE登録</h3>
                        <p>週2回、限定コンテンツをお届け</p>
                        <a href="https://s.lmes.jp/landing-qr/2004427078-bM8L3MM1?uLand=BqXkCI" class="btn btn-primary" target="_blank">今すぐ登録</a>
                    </div>
                </aside>
            </div>
        </div>
    </article>

    <!-- フッター -->
    <footer class="main-footer">
        <div class="container">
            <div class="footer-content">
                <div class="footer-brand">
                    <div class="logo">
                        <span class="logo-text">借金<span class="highlight">6億</span>ニキ</span>
                    </div>
                    <p>どん底から這い上がった男が教える、人生逆転の方法論</p>
                </div>
                <div class="footer-links">
                    <div class="link-group">
                        <h4>コンテンツ</h4>
                        <ul>
                            <li><a href="articles.html">最新記事</a></li>
                            <li><a href="popular-articles.html">人気記事</a></li>
                            <li><a href="videos.html">動画コンテンツ</a></li>
                        </ul>
                    </div>
                    <div class="link-group">
                        <h4>サービス</h4>
                        <ul>
                            <li><a href="consulting.html">個別コンサル</a></li>
                        </ul>
                    </div>
                    <div class="link-group">
                        <h4>その他</h4>
                        <ul>
                            <li><a href="about.html">運営者情報</a></li>
                            <li><a href="privacy.html">プライバシーポリシー</a></li>
                            <li><a href="contact.html">お問い合わせ</a></li>
                        </ul>
                    </div>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2024 借金6億ニキ公式メディア. All rights reserved.</p>
            </div>
        </div>
    </footer>

    <script src="js/main.js"></script>
</body>
</html>
'''

    return article_id, html, category, likes, date

def main():
    csv_file = '6億ニキスクレイプ - スクレイプ.csv'
    output_dir = 'generated_articles'

    # 出力ディレクトリ作成
    os.makedirs(output_dir, exist_ok=True)

    # CSV読み込み
    articles = []
    with open(csv_file, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)  # ヘッダー行をスキップ

        for index, row in enumerate(reader, start=1):
            if len(row) < 3:  # 最低限のデータがない行はスキップ
                continue

            try:
                article_id, html, category, likes, date = generate_article_html(row, index)

                # HTMLファイル保存
                filename = f"{output_dir}/{article_id}.html"
                with open(filename, 'w', encoding='utf-8') as f:
                    f.write(html)

                # 記事情報を保存
                articles.append({
                    'id': article_id,
                    'filename': filename,
                    'category': category,
                    'likes': int(likes) if likes.isdigit() else 0,
                    'date': date
                })

                print(f"✓ 生成完了: {filename} (カテゴリ: {category})")

            except Exception as e:
                print(f"✗ エラー (行{index}): {e}")

    # カテゴリー別、いいね数順にソート
    articles.sort(key=lambda x: (-x['likes'], x['date']), reverse=False)

    # サマリー出力
    print(f"\n{'='*60}")
    print(f"記事生成完了！")
    print(f"{'='*60}")
    print(f"総記事数: {len(articles)}件")
    print(f"出力先: {output_dir}/")

    # カテゴリー別集計
    category_count = {}
    for article in articles:
        cat = article['category']
        category_count[cat] = category_count.get(cat, 0) + 1

    print(f"\nカテゴリー別記事数:")
    for cat, count in sorted(category_count.items(), key=lambda x: -x[1]):
        print(f"  - {cat}: {count}件")

    print(f"\nTOP 10 人気記事:")
    for i, article in enumerate(articles[:10], 1):
        print(f"  {i}. {article['filename']} ({article['likes']}いいね)")

if __name__ == "__main__":
    main()
