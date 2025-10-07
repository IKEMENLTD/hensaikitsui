# Netlify CMS セットアップガイド

## 📋 概要

このサイトにはNetlify CMSが実装されており、ブラウザから記事やページの管理が可能です。

## 🚀 セットアップ手順

### 1. Netlifyにデプロイ

```bash
# Gitリポジトリを作成（まだの場合）
git init
git add .
git commit -m "Initial commit"

# GitHubにプッシュ
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git push -u origin main
```

Netlifyダッシュボードで：
1. 「New site from Git」をクリック
2. GitHubリポジトリを選択
3. デプロイ設定：
   - Build command: (空欄)
   - Publish directory: `.`

### 2. Netlify Identityを有効化

1. Netlifyダッシュボード → Site settings → Identity
2. 「Enable Identity」をクリック
3. Registration preferences → Invite only（推奨）
4. External providers → Google/GitHub等を有効化（任意）

### 3. Git Gatewayを有効化

1. Netlifyダッシュボード → Identity → Services
2. 「Enable Git Gateway」をクリック

### 4. 管理者ユーザーを招待

1. Netlifyダッシュボード → Identity → Invite users
2. 管理者のメールアドレスを入力
3. 受信したメールから登録を完了

### 5. CMSにアクセス

サイトURL + `/admin/` でCMSにアクセス

例: `https://your-site.netlify.app/admin/`

## 📝 使い方

### 記事を作成

1. `/admin/` にアクセス
2. 左メニューから「記事」を選択
3. 「New 記事」をクリック
4. 必要な項目を入力：
   - タイトル
   - スラッグ（URL用）
   - カテゴリー
   - 本文（Markdown）
   - アイキャッチ画像
   - TikTok URL（任意）
5. 「Publish」をクリック

### 記事を編集

1. 記事一覧から編集したい記事を選択
2. 内容を編集
3. 「Save」または「Publish」

### 画像をアップロード

1. 記事編集画面でアイキャッチ画像フィールドをクリック
2. 画像をアップロード
3. 自動的に`images/`フォルダに保存されます

## 🔧 カスタマイズ

### config.ymlの編集

`admin/config.yml`で以下が設定可能：

- コレクション（記事タイプ）の追加・削除
- フィールドの追加・削除・編集
- カテゴリーの選択肢
- メディアフォルダの変更

### ローカル開発

```bash
# Netlify CMSのローカルバックエンドを使用
npx netlify-cms-proxy-server
```

`admin/config.yml`の`local_backend`をtrueに設定

## 📂 ファイル構造

```
hensaikitsui-main/
├── admin/
│   ├── index.html        # CMS管理画面
│   └── config.yml        # CMS設定ファイル
├── content/
│   └── site-settings.json  # サイト設定
├── generated_articles/   # 記事ファイル（自動生成）
└── images/              # 画像フォルダ
```

## ⚠️ 注意事項

1. **Identity設定必須**: Netlify Identityが有効でないとCMSは動作しません
2. **招待制推奨**: セキュリティのため、Registration preferenceは「Invite only」に設定
3. **Git同期**: CMSで行った変更は自動的にGitリポジトリにコミットされます
4. **プレビュー**: 編集中の記事はプレビューボタンで確認できます

## 🔐 セキュリティ

- CMS管理画面は`/admin/`パスで保護されています
- アクセスにはNetlify Identity認証が必要
- 招待されたユーザーのみがログイン可能

## 📖 参考リンク

- [Netlify CMS Documentation](https://www.netlifycms.org/docs/)
- [Netlify Identity Documentation](https://docs.netlify.com/visitor-access/identity/)
- [Git Gateway Documentation](https://docs.netlify.com/visitor-access/git-gateway/)

## 🆘 トラブルシューティング

### CMSにログインできない
- Netlify Identityが有効か確認
- Git Gatewayが有効か確認
- 招待メールから登録を完了しているか確認

### 記事が公開されない
- 「Publish」ボタンを押したか確認
- Gitリポジトリにプッシュされているか確認

### 画像がアップロードできない
- ファイルサイズが大きすぎないか確認（推奨: 1MB以下）
- 画像形式が対応しているか確認（JPG, PNG, GIF, WebP）
