#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CSS/JavaScript Minifier
軽量なMinify処理を行うスクリプト
"""

import re
import os

def minify_css(css_content):
    """CSSをMinify化する"""
    # コメントを削除
    css_content = re.sub(r'/\*[\s\S]*?\*/', '', css_content)

    # 改行とタブを削除
    css_content = re.sub(r'\n', '', css_content)
    css_content = re.sub(r'\t', '', css_content)

    # 複数のスペースを1つに
    css_content = re.sub(r'\s+', ' ', css_content)

    # ブロック前後の不要なスペースを削除
    css_content = re.sub(r'\s*{\s*', '{', css_content)
    css_content = re.sub(r'\s*}\s*', '}', css_content)
    css_content = re.sub(r'\s*:\s*', ':', css_content)
    css_content = re.sub(r'\s*;\s*', ';', css_content)
    css_content = re.sub(r'\s*,\s*', ',', css_content)

    # セミコロン直前のスペース削除
    css_content = re.sub(r';\s*}', '}', css_content)

    return css_content.strip()


def minify_js(js_content):
    """JavaScriptをMinify化する（基本的な処理のみ）"""
    # 単行コメントを削除（ただし、URLの//は保持）
    js_content = re.sub(r'(?<!:)//.*$', '', js_content, flags=re.MULTILINE)

    # 複数行コメントを削除
    js_content = re.sub(r'/\*[\s\S]*?\*/', '', js_content)

    # 複数の空行を1つに
    js_content = re.sub(r'\n\s*\n', '\n', js_content)

    # 行末のスペース削除
    js_content = re.sub(r'\s+$', '', js_content, flags=re.MULTILINE)

    # 行頭のスペース削除（インデント削除）
    js_content = re.sub(r'^\s+', '', js_content, flags=re.MULTILINE)

    return js_content.strip()


def process_file(input_path, output_path, file_type):
    """ファイルを読み込んでMinify処理し、保存する"""
    try:
        with open(input_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original_size = len(content)

        if file_type == 'css':
            minified = minify_css(content)
        elif file_type == 'js':
            minified = minify_js(content)
        else:
            raise ValueError(f"Unsupported file type: {file_type}")

        minified_size = len(minified)
        reduction = ((original_size - minified_size) / original_size) * 100

        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(minified)

        print(f"✓ {os.path.basename(input_path)}")
        print(f"  {original_size:,} bytes → {minified_size:,} bytes ({reduction:.1f}% 削減)")

        return True

    except Exception as e:
        print(f"✗ エラー: {input_path}")
        print(f"  {str(e)}")
        return False


def main():
    """メイン処理"""
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # Minify対象ファイル
    css_files = [
        ('css/style.css', 'css/style.min.css'),
        ('css/article.css', 'css/article.min.css'),
        ('css/animations.css', 'css/animations.min.css'),
    ]

    js_files = [
        ('js/main.js', 'js/main.min.js'),
    ]

    print("=" * 50)
    print("CSS/JavaScript Minify処理開始")
    print("=" * 50)

    # CSS処理
    print("\n【CSS Minify】")
    css_success = 0
    for input_file, output_file in css_files:
        input_path = os.path.join(base_dir, input_file)
        output_path = os.path.join(base_dir, output_file)

        if os.path.exists(input_path):
            if process_file(input_path, output_path, 'css'):
                css_success += 1
        else:
            print(f"⚠ ファイルが見つかりません: {input_file}")

    # JavaScript処理
    print("\n【JavaScript Minify】")
    js_success = 0
    for input_file, output_file in js_files:
        input_path = os.path.join(base_dir, input_file)
        output_path = os.path.join(base_dir, output_file)

        if os.path.exists(input_path):
            if process_file(input_path, output_path, 'js'):
                js_success += 1
        else:
            print(f"⚠ ファイルが見つかりません: {input_file}")

    # サマリー
    print("\n" + "=" * 50)
    print(f"完了: CSS {css_success}/{len(css_files)}件, JS {js_success}/{len(js_files)}件")
    print("=" * 50)

    print("\n【次のステップ】")
    print("HTMLファイル内のCSS/JS参照を .min.css / .min.js に変更してください")
    print("例: <link rel=\"stylesheet\" href=\"css/style.min.css\">")


if __name__ == '__main__':
    main()
