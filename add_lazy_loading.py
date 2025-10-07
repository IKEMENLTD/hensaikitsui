#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
画像タグにloading="lazy"属性を追加するスクリプト
ネイティブのLazy Loading機能を活用
"""

import re
import os
import glob

def add_lazy_loading(html_content):
    """
    <img>タグにloading="lazy"属性を追加
    ただし、既にloading属性がある場合やファーストビュー画像は除外
    """

    # 既にloading属性がある画像はスキップ
    def replace_img(match):
        img_tag = match.group(0)

        # 既にloading属性がある場合はそのまま返す
        if 'loading=' in img_tag:
            return img_tag

        # article-hero内の画像（ファーストビュー）はeager
        if 'article-hero' in img_tag or 'hero' in img_tag.lower():
            # <img の直後に loading="eager" を挿入
            return img_tag.replace('<img ', '<img loading="eager" ')

        # その他の画像はlazy
        return img_tag.replace('<img ', '<img loading="lazy" ')

    # <img>タグを検索して置換
    html_content = re.sub(
        r'<img\s[^>]*>',
        replace_img,
        html_content,
        flags=re.IGNORECASE
    )

    return html_content


def process_html_file(file_path):
    """HTMLファイルを処理"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content
        updated_content = add_lazy_loading(content)

        # 変更があった場合のみ保存
        if updated_content != original_content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)

            # 追加した属性数をカウント
            lazy_count = updated_content.count('loading="lazy"') - original_content.count('loading="lazy"')
            eager_count = updated_content.count('loading="eager"') - original_content.count('loading="eager"')

            return (True, lazy_count, eager_count)

        return (False, 0, 0)

    except Exception as e:
        print(f"✗ エラー: {file_path} - {str(e)}")
        return (None, 0, 0)


def main():
    """メイン処理"""
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # HTMLファイルを取得
    html_files = []
    html_files.extend(glob.glob(os.path.join(base_dir, '*.html')))
    html_files.extend(glob.glob(os.path.join(base_dir, 'generated_articles', '*.html')))

    print("=" * 70)
    print("画像の遅延読み込み（Lazy Loading）実装")
    print("=" * 70)
    print("\nネイティブのloading属性を使用:")
    print("  • ファーストビュー画像: loading=\"eager\"")
    print("  • その他の画像: loading=\"lazy\"")
    print()

    updated_files = 0
    skipped_files = 0
    error_files = 0
    total_lazy = 0
    total_eager = 0

    for file_path in sorted(html_files):
        file_name = os.path.basename(file_path)
        result, lazy_count, eager_count = process_html_file(file_path)

        if result is True:
            if lazy_count > 0 or eager_count > 0:
                print(f"✓ {file_name} (lazy: {lazy_count}, eager: {eager_count})")
            updated_files += 1
            total_lazy += lazy_count
            total_eager += eager_count
        elif result is False:
            skipped_files += 1
        else:
            error_files += 1

    print("\n" + "=" * 70)
    print(f"完了: 更新 {updated_files}件 / スキップ {skipped_files}件 / エラー {error_files}件")
    print(f"追加した属性: loading=\"lazy\" × {total_lazy}個, loading=\"eager\" × {total_eager}個")
    print("=" * 70)

    if updated_files > 0:
        print("\n✓ すべての画像に遅延読み込み属性が追加されました")
        print("\n【効果】")
        print("  • 初期ページロード時間の短縮")
        print("  • データ使用量の削減")
        print("  • Lighthouseスコアの向上")


if __name__ == '__main__':
    main()
