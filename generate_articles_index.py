#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
記事一覧用JSONファイルを生成するスクリプト
generated_articles/内の全記事を解析してメタデータを抽出
"""

import os
import json
import re
import glob
from datetime import datetime

def extract_metadata_from_html(html_path):
    """HTMLファイルからメタデータを抽出"""
    try:
        with open(html_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # タイトル抽出
        title_match = re.search(r'<meta property="og:title" content="([^"]+)">', content)
        title = title_match.group(1) if title_match else "無題"

        # 説明文抽出
        desc_match = re.search(r'<meta name="description" content="([^"]+)">', content)
        description = desc_match.group(1) if desc_match else ""

        # 画像URL抽出
        image_match = re.search(r'<meta property="og:image" content="([^"]+)">', content)
        image = image_match.group(1) if image_match else ""

        # カテゴリー抽出
        category_match = re.search(r'<span class="category">([^<]+)</span>', content)
        category = category_match.group(1) if category_match else "借金返済"

        # 日付抽出
        date_match = re.search(r'<time datetime="([^"]+)">', content)
        date = date_match.group(1) if date_match else "2025-10-06"

        # いいね数抽出
        likes_match = re.search(r'👁 (\d+) いいね', content)
        likes = int(likes_match.group(1)) if likes_match else 0

        # TikTok URL抽出
        tiktok_match = re.search(r'href="(https://www\.tiktok\.com/@hensaikitsui/video/[^"]+)"', content)
        tiktok_url = tiktok_match.group(1) if tiktok_match else ""

        # キーワード抽出
        keywords_match = re.search(r'<meta name="keywords" content="([^"]+)">', content)
        keywords = keywords_match.group(1).split(',') if keywords_match else []

        # ファイル名からIDを抽出
        filename = os.path.basename(html_path)
        article_id = filename.replace('.html', '')

        return {
            "id": article_id,
            "title": title.strip(),
            "description": description.strip(),
            "category": category.strip(),
            "date": date,
            "image": image,
            "likes": likes,
            "tiktok_url": tiktok_url,
            "keywords": [k.strip() for k in keywords],
            "url": f"generated_articles/{filename}"
        }

    except Exception as e:
        print(f"✗ エラー: {html_path} - {str(e)}")
        return None


def generate_articles_index():
    """記事一覧JSONを生成"""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    articles_dir = os.path.join(base_dir, 'generated_articles')

    if not os.path.exists(articles_dir):
        print(f"✗ エラー: {articles_dir} が見つかりません")
        return

    # 全HTMLファイルを取得
    html_files = glob.glob(os.path.join(articles_dir, 'article-*.html'))

    print("=" * 70)
    print("記事一覧JSON生成")
    print("=" * 70)
    print(f"\n対象ディレクトリ: {articles_dir}")
    print(f"記事ファイル数: {len(html_files)}件\n")

    articles = []
    success_count = 0
    error_count = 0

    for html_path in sorted(html_files):
        metadata = extract_metadata_from_html(html_path)

        if metadata:
            articles.append(metadata)
            success_count += 1
            if success_count % 20 == 0:
                print(f"処理中... {success_count}/{len(html_files)}")
        else:
            error_count += 1

    # いいね数でソート（降順）
    articles.sort(key=lambda x: x['likes'], reverse=True)

    # JSONファイルとして保存
    output_path = os.path.join(base_dir, 'articles-index.json')

    output_data = {
        "generated_at": datetime.now().isoformat(),
        "total_articles": len(articles),
        "articles": articles
    }

    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(output_data, f, ensure_ascii=False, indent=2)

    print(f"\n✓ 完了: {success_count}件の記事を処理")
    if error_count > 0:
        print(f"⚠ エラー: {error_count}件")

    print("\n" + "=" * 70)
    print(f"出力ファイル: {output_path}")
    print(f"合計記事数: {len(articles)}件")
    print("=" * 70)

    # カテゴリー別統計
    categories = {}
    for article in articles:
        cat = article['category']
        categories[cat] = categories.get(cat, 0) + 1

    print("\n【カテゴリー別記事数】")
    for cat, count in sorted(categories.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat}: {count}件")

    print("\n【人気記事TOP5】")
    for i, article in enumerate(articles[:5], 1):
        print(f"  {i}. {article['title'][:50]}... ({article['likes']}いいね)")


if __name__ == '__main__':
    generate_articles_index()
