#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
articles.html へのリンクを articles-dynamic.html に更新
"""

import os
import re
import glob

def update_articles_links(file_path):
    """HTMLファイル内のarticles.htmlリンクを更新"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # articles.html → articles-dynamic.html
        content = re.sub(
            r'href="articles\.html"',
            'href="articles-dynamic.html"',
            content
        )

        # 変更があった場合のみ保存
        if content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True

        return False

    except Exception as e:
        print(f"✗ エラー: {file_path} - {str(e)}")
        return None


def main():
    """メイン処理"""
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # 対象HTMLファイル
    html_files = glob.glob(os.path.join(base_dir, '*.html'))

    print("=" * 60)
    print("記事リンクを動的ページに更新")
    print("=" * 60)
    print("\narticles.html → articles-dynamic.html\n")

    updated_files = 0
    skipped_files = 0
    error_files = 0

    for file_path in sorted(html_files):
        file_name = os.path.basename(file_path)

        # articles.html 自体はスキップ
        if file_name == 'articles.html':
            continue

        result = update_articles_links(file_path)

        if result is True:
            print(f"✓ {file_name}")
            updated_files += 1
        elif result is False:
            skipped_files += 1
        else:
            error_files += 1

    print("\n" + "=" * 60)
    print(f"完了: 更新 {updated_files}件 / スキップ {skipped_files}件 / エラー {error_files}件")
    print("=" * 60)

    if updated_files > 0:
        print("\n✓ 記事リンクを動的ページに更新しました")


if __name__ == '__main__':
    main()
