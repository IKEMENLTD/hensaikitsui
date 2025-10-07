#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
HTMLファイル内のCSS/JS参照をMinifyバージョンに更新
"""

import os
import re
import glob

def update_html_file(file_path):
    """HTMLファイル内のCSS/JS参照を更新"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # CSS参照を更新
        content = re.sub(
            r'<link rel="stylesheet" href="css/style\.css">',
            '<link rel="stylesheet" href="css/style.min.css">',
            content
        )
        content = re.sub(
            r'<link rel="stylesheet" href="css/article\.css">',
            '<link rel="stylesheet" href="css/article.min.css">',
            content
        )
        content = re.sub(
            r'<link rel="stylesheet" href="css/animations\.css">',
            '<link rel="stylesheet" href="css/animations.min.css">',
            content
        )

        # JavaScript参照を更新
        content = re.sub(
            r'<script src="js/main\.js"></script>',
            '<script src="js/main.min.js"></script>',
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

    # HTMLファイルを検索（generated_articles内も含む）
    html_files = []
    html_files.extend(glob.glob(os.path.join(base_dir, '*.html')))
    html_files.extend(glob.glob(os.path.join(base_dir, 'generated_articles', '*.html')))

    print("=" * 60)
    print("HTMLファイル内のCSS/JS参照を更新")
    print("=" * 60)

    updated_count = 0
    skipped_count = 0
    error_count = 0

    for file_path in sorted(html_files):
        file_name = os.path.basename(file_path)
        result = update_html_file(file_path)

        if result is True:
            print(f"✓ {file_name}")
            updated_count += 1
        elif result is False:
            skipped_count += 1
        else:
            error_count += 1

    print("\n" + "=" * 60)
    print(f"完了: 更新 {updated_count}件 / スキップ {skipped_count}件 / エラー {error_count}件")
    print("=" * 60)

    if updated_count > 0:
        print("\n✓ すべてのHTMLファイルがMinifyバージョンを参照するよう更新されました")


if __name__ == '__main__':
    main()
