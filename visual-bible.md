# Visual Bible 視覺一致性規範｜六年一班班親會

本規範為全套 14 頁簡報與響應式網站的硬性視覺基準，確保跨頁面風格統一、不漂移。

```yaml
canvas:
  ratio: "16:9"
  orientation: "landscape"
  resolution: "1920x1080 (Full HD / 投影友善)"

style:
  illustration: "溫暖柔和的手繪繪本風（Warm Picture-book Hand-drawn Style），帶有柔和水彩與粉彩筆觸"
  texture: "質樸紙質紋理，溫潤微暖，柔和無尖銳刺眼高光"
  lighting: "自然晨曦光、暖金黃色與柔和天藍色擴散光，營造安全、安心且朝氣蓬勃的氛圍"
  atmosphere: "包容、陪伴、成長、充滿希望與教育溫度"

color:
  primary: "#2C5E8A"       # 沉穩海軍藍 / 鹿陽藍（代表專業、信任與守護）
  secondary: "#E88D67"     # 暖暖活力橘 / 晨曦暖陽（代表熱情、童心與陪伴）
  accent: "#58A47E"        # 柔和森林綠 / 萌芽綠（代表成長、閱讀與健康）
  background: "#FDFBF7"    # 米白棉紙暖底色（投影不刺眼、閱讀舒適）
  card_bg: "rgba(255, 255, 255, 0.92)" # 內容卡片半透明白底
  text_dark: "#2D3748"     # 深炭灰文字（比純黑更溫柔耐看）
  text_muted: "#718096"    # 輔助說明文字灰

typography:
  font_family: "Microsoft JhengHei, 蘋方, 芫荽體, system-ui, sans-serif"
  title_zone: "左上或中央卡片，字級醒目，安全邊界大於 5%"
  body_zone: "搭配情境圖，文字不超過 30%，保留充足呼吸空間"

characters:
  teacher:
    role: "高志賢老師"
    appearance: "親切沉穩、戴眼鏡、面帶溫暖微笑、穿著整潔休閒襯衫或針織背心"
    vibe: "值得信任、善於傾聽與引導的良師益友"
  students:
    appearance: "六年級男女學生，身著整齊便服或活潑班服，身型修長自然，散發小六生微成熟的專注與純真氣質"
    diversity: "多元自然，著重互動神情，不刻意對應真實單一個別學生"

layout:
  safe_margin: "畫面四周至少保留 60px 安全留白（>5%）"
  composition: "70% 溫馨故事插畫情境 + 30% 精練繁體中文重點卡片"

negative_constraints:
  - "不要 AI 亂碼或殘缺文字"
  - "不要出現簡體字或非台灣用語"
  - "不要每頁突變畫風（如突然轉成 3D 渲染或冷冽科幻）"
  - "不要刺眼純黑底色或過度飽和螢光色"
  - "不要過多裝飾文字雜訊"
```

## 跨頁一致性自檢表
- [x] 全套 16:9 橫向畫幅
- [x] 高老師與學生角色形象氣質連貫
- [x] 溫和暖陽色調與棉紙紋理一致
- [x] 繁體中文全數正確、無錯字與亂碼
- [x] 簡報與網站視覺元素完全呼應
