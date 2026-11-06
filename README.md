# K-pop Fan Chant Guide

一個以繁體中文呈現的 K-pop 官方應援資料查找網站。使用者可依團體、專輯與歌曲瀏覽，搜尋歌曲並收藏常用歌曲。

## 本版本內容
- 網站首頁、團體頁、專輯頁、歌曲頁與收藏頁
- 搜尋、LocalStorage 收藏、首次使用提示
- 響應式版面
- &TEAM 精選 8 首歌曲：Mark on Me、Good Boy、Love Jang、We on Fire、Run Wild、Deer Hunter、Rush、Back to Life
- `AGENTS.md`：AI 後續新增資料與修改網站的開發規則

## 著作權與來源說明
本網站不轉載完整歌詞或大量應援文字。歌曲頁提供官方來源連結，完整內容與最新版本請以官方頁面為準。Good Boy 與 Love Jang 目前連結至 &TEAM 官方 Weverse media 集合頁，請在頁面搜尋歌曲名稱。

專輯封面與團體圖使用本專案自行製作的漸層佔位圖，不代表官方實際封面或官方宣傳照。若日後取得可合法使用的官方圖片，可替換 `assets/` 中對應 SVG，並保留相同檔案路徑。

## 本地預覽
因網站透過 `fetch()` 讀取 JSON，請使用本機靜態伺服器預覽，不建議直接以 `file://` 開啟。

例如在專案根目錄執行：
```bash
python3 -m http.server 8000
```
再開啟 `http://localhost:8000`。

## 部署至 GitHub Pages
1. 建立 GitHub repository。
2. 將 ZIP 解壓縮。
3. 將解壓縮後的**資料夾內所有檔案與資料夾**上傳至 repository 根目錄，保留 `css/`、`js/`、`data/`、`assets/` 結構。
4. 到 Settings → Pages，選擇 Deploy from a branch、`main`、`/(root)`。
5. 等待 Actions 部署完成後，使用 GitHub Pages 網址開啟。

## 專案規則
AI 接手專案時，請先閱讀 `AGENTS.md`，並遵循官方來源查證、資料格式、新增流程與完成檢查清單。
