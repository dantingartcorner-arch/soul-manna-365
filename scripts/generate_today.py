import json
from datetime import datetime, timezone, timedelta

tz = timezone(timedelta(hours=8))
now = datetime.now(tz)
day_of_year = now.timetuple().tm_yday

with open("data/verses_365.json", "r", encoding="utf-8") as f:
    verses = json.load(f)

index = (day_of_year - 1) % len(verses)
today = verses[index].copy()
today["date"] = now.strftime("%Y-%m-%d")
today["day_of_year"] = day_of_year

with open("docs/today.json", "w", encoding="utf-8") as f:
    json.dump(today, f, ensure_ascii=False, indent=2)

print(f"今天是第 {day_of_year} 天，使用第 {today['index']} 筆：{today['reference']}")
