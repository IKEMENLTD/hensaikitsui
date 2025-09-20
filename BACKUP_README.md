# バックアップシステム

このプロジェクトには自動バックアップシステムが設定されています。

## バックアップの場所

```
/mnt/c/Users/music005/Desktop/hensaikitsui_backups/
```

## バックアップ方法

### 1. 手動バックアップ

```bash
# 基本的なバックアップ
/mnt/c/Users/music005/Desktop/backup_script.sh

# コメント付きバックアップ
/mnt/c/Users/music005/Desktop/backup_script.sh "article_updates"
/mnt/c/Users/music005/Desktop/backup_script.sh "css_improvements"
/mnt/c/Users/music005/Desktop/backup_script.sh "before_major_changes"
```

### 2. 重要な更新前のバックアップ

以下のような変更を行う前には必ずバックアップを作成してください：

- 新しい記事の追加
- CSSの大幅な変更
- HTMLページの新規作成
- JavaScript機能の追加
- 画像の追加/変更

## バックアップの命名規則

```
backup_YYYYMMDD_HHMMSS_[コメント]
```

例：
- `backup_20240916_143022_manual_backup`
- `backup_20240916_145530_article_updates`
- `backup_20240916_151245_css_improvements`

## 自動管理機能

- **自動削除**: 30個を超えるバックアップは自動的に古いものから削除
- **ログ記録**: 全てのバックアップ操作は `backup_log.txt` に記録
- **サイズ表示**: バックアップサイズとファイル数を表示

## バックアップログの確認

```bash
cat /mnt/c/Users/music005/Desktop/hensaikitsui_backups/backup_log.txt
```

## 復元方法

1. バックアップディレクトリから適切なバックアップを選択
2. 現在のプロジェクトディレクトリをリネーム（安全のため）
3. バックアップをコピーして復元

```bash
# 現在のプロジェクトをリネーム
mv /mnt/c/Users/music005/Desktop/hensaikitsui /mnt/c/Users/music005/Desktop/hensaikitsui_current

# バックアップから復元（例：2024年9月16日14:30のバックアップ）
cp -r /mnt/c/Users/music005/Desktop/hensaikitsui_backups/backup_20240916_143022_manual_backup /mnt/c/Users/music005/Desktop/hensaikitsui
```

## 推奨バックアップタイミング

1. **作業開始前** - 新しい作業を始める前
2. **重要な変更後** - 大きな機能追加や修正後
3. **作業終了時** - 1日の作業を終える時
4. **デプロイ前** - 本番環境に反映する前

## 注意事項

- バックアップは自動的に古いものから削除されるため、重要なバックアップは別途保存してください
- 大きなファイルや機密情報を含む場合は、バックアップの保存場所に注意してください
- バックアップスクリプトは定期的に動作確認を行ってください