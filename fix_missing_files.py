#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
存在しないファイル参照を修正するスクリプト
"""

import os
import re
import glob

def remove_footer_css(html_content):
    """footer.cssへの参照を削除"""
    return re.sub(
        r'<link rel="stylesheet" href="css/footer\.css">\s*\n',
        '',
        html_content
    )

def remove_animations_js(html_content):
    """animations.jsへの参照を削除"""
    return re.sub(
        r'<script src="js/animations\.js"></script>\s*\n',
        '',
        html_content
    )

def process_html_file(file_path):
    """HTMLファイルを処理"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_content = content

        # 存在しないファイル参照を削除
        content = remove_footer_css(content)
        content = remove_animations_js(content)

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

    # HTMLファイルを取得
    html_files = glob.glob(os.path.join(base_dir, '*.html'))

    print("=" * 60)
    print("存在しないファイル参照を修正")
    print("=" * 60)
    print("\n対象:")
    print("  • footer.css への参照削除")
    print("  • animations.js への参照削除")
    print()

    updated_files = 0
    skipped_files = 0
    error_files = 0

    for file_path in sorted(html_files):
        file_name = os.path.basename(file_path)
        result = process_html_file(file_path)

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
        print("\n✓ 存在しないファイルへの参照を削除しました")


if __name__ == '__main__':
    main()
