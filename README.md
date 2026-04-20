# Daily Verse 每日靈修系統

## 架構
GitHub Actions (每天台灣時間 07:55)
  → 讀取 data/verses_365.json
  → 輸出 docs/today.json
  → iPhone 捷徑 / LINE / IG / 網站 讀取

## today.json 格式
{
  "date": "2026-04-20",
  "day_of_year": 110,
  "index": 110,
  "verse": "在至高之處榮耀歸與神",
  "reference": "路加福音 2:14",
  "prayer": "主啊，讓榮耀歸祢，讓平安在我心裡。"
}

## GitHub raw URL（上傳後替換帳號與 repo 名稱）
https://raw.githubusercontent.com/[帳號]/[repo]/main/docs/today.json

## iPhone 捷徑
1. 取得 URL 內容 → 填入上方 URL
2. 取得字典值 → Key: verse / prayer / reference
3. 顯示通知 或 傳送訊息
