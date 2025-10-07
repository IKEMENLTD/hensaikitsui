# 📚 デプロイガイド - Git & Netlify

## 🚀 GitHubへのプッシュとNetlifyデプロイ

### 1️⃣ GitHubリポジトリの作成

1. [GitHub](https://github.com)にログイン
2. 右上の「+」→「New repository」をクリック
3. リポジトリ情報を入力：
   - Repository name: `hensaikitsui-media`
   - Description: 借金6億ニキ公式メディアサイト
   - Public/Private: お好みで選択
   - **重要**: 「Add a README file」のチェックは外す
4. 「Create repository」をクリック

### 2️⃣ ローカルリポジトリをGitHubに接続

GitHubでリポジトリ作成後に表示されるコマンドをコピーして実行：

```bash
cd /mnt/c/Users/music005/Desktop/hensaikitsui

# リモートリポジトリを追加
git remote add origin https://github.com/[あなたのユーザー名]/hensaikitsui-media.git

# ブランチ名をmainに変更（推奨）
git branch -M main

# GitHubにプッシュ
git push -u origin main
```

もしユーザー名とパスワードを求められた場合：
- Username: GitHubのユーザー名
- Password: GitHubの個人アクセストークン（パスワードではない）

### 3️⃣ GitHub個人アクセストークンの作成（必要な場合）

1. GitHub → Settings → Developer settings → Personal access tokens → Tokens (classic)
2. 「Generate new token」→「Generate new token (classic)」
3. 設定：
   - Note: `hensaikitsui-deploy`
   - Expiration: 90 days（お好みで）
   - Select scopes: `repo`にチェック
4. 「Generate token」をクリック
5. **トークンをコピー**（一度しか表示されません）

### 4️⃣ Netlifyでのデプロイ

1. [Netlify](https://netlify.com)にログイン（GitHubアカウントでログイン推奨）

2. 「Sites」→「Add new site」→「Import an existing project」

3. 「Connect to Git provider」でGitHubを選択

4. リポジトリを選択：`hensaikitsui-media`

5. デプロイ設定（自動で設定される）：
   - Build command: （空欄）
   - Publish directory: `.`
   - これらは`netlify.toml`から自動読み込み

6. 「Deploy site」をクリック

### 5️⃣ カスタムドメインの設定（オプション）

1. Netlifyダッシュボード → Domain settings
2. 「Add custom domain」
3. ドメインを入力（例：`hensaikitsui.com`）
4. DNSレコードを設定

### 6️⃣ 自動デプロイの確認

GitHubにプッシュすると自動でNetlifyがデプロイします：

```bash
# 変更をコミット
git add .
git commit -m "サイト更新：新しい記事を追加"

# GitHubにプッシュ（自動デプロイが始まる）
git push
```

## 📝 日常的な更新フロー

### 記事を追加する場合

```bash
# 1. バックアップを作成
/mnt/c/Users/music005/Desktop/backup_script.sh "before_article_add"

# 2. 記事を作成・編集
# （HTMLファイルを編集）

# 3. 変更をコミット
git add .
git commit -m "記事追加：[記事タイトル]"

# 4. GitHubにプッシュ（自動デプロイ）
git push

# 5. 更新後のバックアップ
/mnt/c/Users/music005/Desktop/backup_script.sh "after_article_add"
```

### デザイン変更の場合

```bash
# 1. 変更前バックアップ
/mnt/c/Users/music005/Desktop/backup_script.sh "before_design_change"

# 2. CSSを編集

# 3. ローカルで確認

# 4. コミット＆プッシュ
git add css/
git commit -m "デザイン更新：[変更内容]"
git push

# 5. 変更後バックアップ
/mnt/c/Users/music005/Desktop/backup_script.sh "after_design_change"
```

## 🔍 デプロイ状態の確認

### Netlifyダッシュボード

1. [Netlify](https://app.netlify.com)にログイン
2. サイトを選択
3. デプロイ状態を確認：
   - 🟢 Published: デプロイ成功
   - 🟡 Building: デプロイ中
   - 🔴 Failed: デプロイ失敗

### デプロイログの確認

1. Netlifyダッシュボード → Deploys
2. 該当のデプロイをクリック
3. ログを確認

## 🚨 トラブルシューティング

### プッシュできない場合

```bash
# リモートの最新を取得
git pull origin main

# コンフリクトがある場合は解決して
git add .
git commit -m "コンフリクト解決"
git push
```

### Netlifyデプロイが失敗する場合

1. `netlify.toml`の設定を確認
2. ファイルパスの大文字小文字を確認
3. 画像ファイルのサイズを確認（10MB以下推奨）

### サイトが表示されない場合

1. `index.html`がルートディレクトリにあることを確認
2. Netlifyのデプロイログを確認
3. ブラウザのキャッシュをクリア

## 📊 パフォーマンス最適化

### 画像の最適化

```bash
# 画像を圧縮してからコミット
# オンラインツール：https://tinypng.com/
```

### Netlify設定の最適化

`netlify.toml`で以下を設定済み：
- キャッシュヘッダー
- セキュリティヘッダー
- 圧縮設定

## 🔗 便利なリンク

- [Netlifyステータス](https://www.netlifystatus.com/)
- [Netlifyドキュメント](https://docs.netlify.com/)
- [GitHub Docs](https://docs.github.com/)

## 📧 サポート

問題が発生した場合：
1. Netlifyのサポートフォーラムをチェック
2. GitHubのIssuesで質問
3. 公式LINEで相談

---

最終更新：2024年9月16日