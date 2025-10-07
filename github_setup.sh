#!/bin/bash

echo "========================================="
echo "📦 GitHub リポジトリセットアップ"
echo "========================================="
echo ""
echo "GitHubユーザー: IKEMENLTD"
echo ""
echo "1. まず、GitHubで新しいリポジトリを作成してください："
echo "   https://github.com/new"
echo ""
echo "   リポジトリ名の推奨: hensaikitsui-media"
echo "   ※ README.mdの追加はチェックしないでください"
echo ""
echo "2. リポジトリ作成後、以下のコマンドを実行："
echo ""
echo "========================================="
echo ""

# リポジトリ名を入力
read -p "GitHubで作成したリポジトリ名を入力してください: " REPO_NAME

if [ -z "$REPO_NAME" ]; then
    REPO_NAME="hensaikitsui-media"
    echo "デフォルトのリポジトリ名を使用: $REPO_NAME"
fi

echo ""
echo "以下のコマンドを順番に実行してください："
echo ""
echo "# 1. リモートリポジトリを追加"
echo "git remote add origin https://github.com/IKEMENLTD/${REPO_NAME}.git"
echo ""
echo "# 2. ブランチ名をmainに変更"
echo "git branch -M main"
echo ""
echo "# 3. GitHubにプッシュ"
echo "git push -u origin main"
echo ""
echo "========================================="
echo ""
echo "もし認証を求められた場合："
echo "Username: IKEMENLTD"
echo "Password: GitHub個人アクセストークン（パスワードではない）"
echo ""
echo "トークンの作成方法："
echo "1. https://github.com/settings/tokens にアクセス"
echo "2. 'Generate new token (classic)' をクリック"
echo "3. 'repo' にチェックを入れて作成"
echo ""
echo "========================================="
echo ""
read -p "上記のコマンドを実行しますか？ (y/n): " CONFIRM

if [ "$CONFIRM" = "y" ] || [ "$CONFIRM" = "Y" ]; then
    echo ""
    echo "リモートリポジトリを追加中..."
    git remote add origin https://github.com/IKEMENLTD/${REPO_NAME}.git 2>/dev/null
    
    if [ $? -eq 0 ]; then
        echo "✅ リモートリポジトリを追加しました"
    else
        echo "⚠️  既にoriginが設定されている可能性があります"
        echo "現在の設定を確認中..."
        git remote -v
        echo ""
        read -p "originを上書きしますか？ (y/n): " OVERWRITE
        if [ "$OVERWRITE" = "y" ] || [ "$OVERWRITE" = "Y" ]; then
            git remote set-url origin https://github.com/IKEMENLTD/${REPO_NAME}.git
            echo "✅ リモートリポジトリのURLを更新しました"
        fi
    fi
    
    echo ""
    echo "ブランチ名をmainに変更中..."
    git branch -M main
    echo "✅ ブランチ名を変更しました"
    
    echo ""
    echo "========================================="
    echo "準備完了！"
    echo ""
    echo "次のコマンドでGitHubにプッシュしてください："
    echo ""
    echo "git push -u origin main"
    echo ""
    echo "========================================="
else
    echo "セットアップをキャンセルしました"
fi