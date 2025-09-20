# 借金6億ニキ公式メディア

借金6億円から這い上がった男の実体験に基づくビジネス戦略とノウハウを発信する公式メディアサイト。

## 🌐 サイト概要

- **URL**: [デプロイ後のURL]
- **ターゲット**: 借金返済に悩む人、起業家、ビジネスを学びたい人
- **コンテンツ**: 実体験に基づく借金返済戦略、詐欺対策、ビジネス構築ノウハウ

## 🚀 主な機能

- 📝 実体験に基づく記事コンテンツ
- 🎯 カテゴリー別記事管理
- 📱 レスポンシブデザイン
- 💫 モダンなアニメーション効果
- 🔍 記事フィルタリング・ソート機能
- 📧 ニュースレター登録
- 💬 LINE連携

## 📁 ディレクトリ構造

```
hensaikitsui/
├── index.html              # トップページ
├── articles.html          # 記事一覧ページ
├── category.html          # カテゴリーページ
├── contact.html           # お問い合わせページ
├── 404.html              # 404エラーページ
├── article-*.html        # 個別記事ページ
├── css/
│   └── style.css         # メインスタイルシート
├── js/
│   └── main.js           # メインJavaScript
├── images/               # 画像ファイル
├── netlify.toml          # Netlifyデプロイ設定
└── README.md             # このファイル
```

## 🛠️ 技術スタック

- **フロントエンド**: HTML5, CSS3, JavaScript (Vanilla)
- **デザイン**: カスタムCSS、レスポンシブデザイン
- **ホスティング**: Netlify
- **バージョン管理**: Git/GitHub

## 🚀 デプロイ方法

### Netlifyでのデプロイ

1. GitHubリポジトリを作成
2. Netlifyアカウントにログイン
3. 「New site from Git」をクリック
4. GitHubリポジトリを選択
5. デプロイ設定は`netlify.toml`が自動で適用される
6. 「Deploy site」をクリック

### ローカル開発

```bash
# リポジトリのクローン
git clone [your-repo-url]
cd hensaikitsui

# ローカルサーバーの起動（VSCodeのLive Serverなど）
# またはPythonの簡易サーバー
python -m http.server 8000
```

## 📝 コンテンツ管理

### 新しい記事の追加

1. `article-template.html`を複製
2. ファイル名を変更（例: `article-new-topic.html`）
3. コンテンツを編集
4. `articles.html`に記事カードを追加
5. Git commitしてpush

### 画像の最適化

- 推奨サイズ: サムネイル 800x450px
- フォーマット: JPEG（写真）、PNG（図版）
- 圧縮: TinyPNGなどで最適化

## 🔧 カスタマイズ

### カラーテーマの変更

`css/style.css`の`:root`セクションで色を変更：

```css
:root {
    --primary-blue: #0066ff;
    --deep-blue: #003d99;
    /* 他のカラー変数 */
}
```

### フォントの変更

```css
--font-primary: 'Noto Sans JP', sans-serif;
--font-display: 'Orbitron', monospace;
```

## 📊 SEO対策

- 各ページにmetaタグ設定済み
- OGP対応
- 構造化データ（今後実装予定）
- サイトマップ（今後実装予定）

## 🔒 バックアップ

バックアップスクリプトが用意されています：

```bash
# 手動バックアップ
/mnt/c/Users/music005/Desktop/backup_script.sh "コメント"

# クイックバックアップ
/mnt/c/Users/music005/Desktop/quick_backup.sh
```

## 📞 サポート

- **公式LINE**: [リンク](https://s.lmes.jp/landing-qr/2004427078-bM8L3MM1?uLand=BqXkCI)
- **メール**: [後日設定]
- **Twitter**: [後日設定]

## 📜 ライセンス

© 2024 借金6億ニキ公式メディア. All rights reserved.

## 🙏 謝辞

このサイトを訪れてくださったすべての方々、そして借金返済の道を共に歩む仲間たちに感謝します。

---

**最終更新**: 2024年9月16日