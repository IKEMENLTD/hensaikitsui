# Lighthouse最適化チェックリスト

## ✅ 実装済み最適化

### Performance（パフォーマンス）
- ✅ CSS/JavaScriptのMinify化
  - `style.css` → `style.min.css` (27.9%削減)
  - `article.css` → `article.min.css` (33.9%削減)
  - `animations.css` → `animations.min.css` (39.5%削減)
  - `main.js` → `main.min.js` (40.6%削減)

- ✅ 画像の遅延読み込み（Lazy Loading）
  - 全画像に`loading="lazy"`属性を追加（603個）
  - ファーストビュー画像は`loading="eager"`で最適化

- ✅ HTTPヘッダー最適化（netlify.toml）
  - キャッシュ制御設定
  - 圧縮（Gzip/Brotli）自動適用
  - セキュリティヘッダー

### SEO
- ✅ メタタグ最適化
  - OGPタグ完備
  - Twitter Card対応
  - 適切なtitle/description

- ✅ セマンティックHTML
  - `<article>`, `<header>`, `<footer>`等の適切な使用
  - 見出しタグの階層構造

### Accessibility（アクセシビリティ）
- ✅ 画像のalt属性設定
- ✅ 適切なコントラスト比
- ✅ レスポンシブデザイン

### Best Practices
- ✅ HTTPS対応（Netlify自動）
- ✅ 適切なファイル構造
- ✅ エラーハンドリング

## 🔧 追加推奨最適化

### Performance向上施策

#### 1. フォント最適化
```html
<!-- Google Fontsの最適化 -->
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700;900&display=swap" rel="stylesheet">
```

**推奨**:
- `&display=swap`を追加（✅実装済み）
- 使用していないウェイトを削除
- サブセット化を検討（日本語フォント）

#### 2. 画像最適化
```bash
# WebPへの変換（手動実行が必要）
# 例: ImageMagickを使用
convert images/article-blacklist-thumb.jpg -quality 80 images/article-blacklist-thumb.webp

# 複数画像を一括変換
for img in images/*.jpg; do
    convert "$img" -quality 80 "${img%.jpg}.webp"
done
```

**現在の画像サイズ**:
- `article-blacklist-thumb.jpg`: 119KB
- `article-repayment-thumb.jpg`: 238KB
- `article-scam-thumb.jpg`: 205KB

**推奨サイズ**: 各50KB以下（WebP変換で実現可能）

#### 3. Critical CSS
ファーストビュー用のCSSをインライン化：

```html
<head>
    <style>
        /* Critical CSS - ファーストビューの必須スタイル */
        :root{--midnight-blue:#0a1628;--dark-blue:#0f2744}
        body{margin:0;font-family:'Noto Sans JP',sans-serif}
        .main-header{position:fixed;top:0;width:100%;z-index:1000}
        /* ... */
    </style>
    <link rel="preload" href="css/style.min.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
</head>
```

#### 4. JavaScriptの非同期読み込み
```html
<script src="js/main.min.js" defer></script>
<script src="js/animations.js" defer></script>
```

### 実装方法

#### A. netlify.tomlに追加設定
```toml
# 追加のパフォーマンスヘッダー
[[headers]]
  for = "/*.js"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]
  for = "/*.css"
  [headers.values]
    Cache-Control = "public, max-age=31536000, immutable"

[[headers]]
  for = "/images/*"
  [headers.values]
    Cache-Control = "public, max-age=604800"
```

#### B. 使用していないCSS削除
```bash
# PurgeCSSを使用（オプション）
npm install -g purgecss
purgecss --css css/style.min.css --content "*.html" --output css/
```

## 📊 Lighthouseスコア目標

### 現在の状態（推定）
- **Performance**: 70-80点（Minify化・Lazy Loading実装済み）
- **Accessibility**: 85-95点（alt属性・セマンティックHTML対応済み）
- **Best Practices**: 85-95点（適切な構造・セキュリティ）
- **SEO**: 90-100点（メタタグ完備）

### 目標スコア
全カテゴリで **80点以上**

### スコア確認方法

1. **Chrome DevTools**
```
1. Chromeでサイトを開く
2. F12でDevToolsを開く
3. Lighthouseタブを選択
4. "Generate report"をクリック
```

2. **PageSpeed Insights**
https://pagespeed.web.dev/
- URLを入力してテスト
- モバイル・デスクトップ両方を確認

3. **Netlifyデプロイ後**
本番環境でのスコアが正確
- ローカルとスコアが異なる場合あり

## 🎯 優先度別実施推奨

### 高優先度（即実施推奨）
1. ✅ CSS/JSのMinify化（完了）
2. ✅ Lazy Loading実装（完了）
3. ⏳ 画像のWebP変換（ツール環境依存のためスキップ可）
4. ⏳ `<script>`タグに`defer`属性追加

### 中優先度（デプロイ後に確認）
1. ⏳ Critical CSS実装
2. ⏳ 使用していないCSSの削除
3. ⏳ フォントのサブセット化

### 低優先度（必要に応じて）
1. Service Worker実装（PWA化）
2. HTTP/2 Server Push
3. Resource Hints最適化

## 📝 メモ

- 現在実装済みの最適化で、多くの場合80点以上は達成可能
- 画像WebP変換は手動実行が必要（ツールがWSL環境に未インストールのため）
- netlify.tomlの設定により、Netlifyデプロイ時に自動的に多くの最適化が適用される
- 最終的なスコアは本番環境（Netlify）で測定すること

## 🚀 次のステップ

1. Netlifyにデプロイ
2. PageSpeed Insightsでスコア測定
3. 80点未満の項目を特定
4. 該当する最適化を追加実施
