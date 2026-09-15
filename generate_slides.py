import os
from PIL import Image, ImageDraw, ImageFont

SLIDE_W = 1920
SLIDE_H = 1080
TOTAL_SLIDES = 24

OUT_DIR = r"C:\Antigravity\班親會\slides"
BRAIN_DIR = r"C:\Users\hp\.gemini\antigravity\brain\437cad19-ae1d-46bf-a0ef-ff951c2a0052"

os.makedirs(OUT_DIR, exist_ok=True)

FONT_BOLD = r"C:\Windows\Fonts\msjhbd.ttc"
FONT_REG = r"C:\Windows\Fonts\msjh.ttc"

def get_font(bold=False, size=32):
    path = FONT_BOLD if bold else FONT_REG
    try:
        return ImageFont.truetype(path, size)
    except:
        return ImageFont.load_default()

# Colors
NAVY = (44, 94, 138)
ORANGE = (232, 141, 103)
GREEN = (88, 164, 126)
BG_WARM = (253, 251, 247)
TEXT_DARK = (45, 55, 72)
TEXT_MUTED = (113, 128, 150)
WHITE = (255, 255, 255)
GOLD = (217, 142, 38)
RED_ACCENT = (214, 69, 41)

def create_base_canvas():
    img = Image.new("RGBA", (SLIDE_W, SLIDE_H), BG_WARM)
    draw = ImageDraw.Draw(img)
    for y in range(SLIDE_H):
        ratio = y / SLIDE_H
        r = int(253 - ratio * 8)
        g = int(251 - ratio * 12)
        b = int(247 - ratio * 16)
        draw.line([(0, y), (SLIDE_W, y)], fill=(r, g, b, 255))
    overlay = Image.new("RGBA", (SLIDE_W, SLIDE_H), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    ov_draw.ellipse([(-80, -80), (450, 450)], fill=(232, 141, 103, 30))
    ov_draw.ellipse([(SLIDE_W - 380, SLIDE_H - 380), (SLIDE_W + 150, SLIDE_H + 150)], fill=(44, 94, 138, 25))
    ov_draw.ellipse([(SLIDE_W - 280, -80), (SLIDE_W + 180, 380)], fill=(88, 164, 126, 25))
    return Image.alpha_composite(img, overlay)

def draw_badge(draw, text, x, y, bg_color=NAVY, text_color=WHITE, font_size=24, pad_x=24, pad_y=10):
    font = get_font(True, font_size)
    bbox = draw.textbbox((0, 0), text, font=font)
    w = bbox[2] - bbox[0] + pad_x * 2
    h = bbox[3] - bbox[1] + pad_y * 2
    draw.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=bg_color)
    draw.text((x + pad_x, y + pad_y), text, font=font, fill=text_color)
    return w, h

def draw_header_nav(draw, slide_num_str, title_str, subtitle_str=""):
    draw_badge(draw, "臺中市沙鹿區鹿陽國民小學 六年一班 班親會", 80, 45, bg_color=NAVY, text_color=WHITE, font_size=22)
    
    page_font = get_font(True, 26)
    page_text = f"PAGE {slide_num_str} / {TOTAL_SLIDES}"
    draw.text((SLIDE_W - 270, 52), page_text, font=page_font, fill=TEXT_MUTED)
    
    t_font = get_font(True, 52)
    draw.text((80, 115), title_str, font=t_font, fill=TEXT_DARK)
    
    if subtitle_str:
        s_font = get_font(False, 26)
        draw.text((80, 185), subtitle_str, font=s_font, fill=TEXT_MUTED)
        draw.rounded_rectangle([80, 226, 300, 232], radius=3, fill=ORANGE)
    else:
        draw.rounded_rectangle([80, 185, 300, 191], radius=3, fill=ORANGE)

def draw_card(img, bbox, bg_color=(255, 255, 255, 245), border_color=(226, 232, 240, 255), radius=20, border_width=2):
    overlay = Image.new("RGBA", (SLIDE_W, SLIDE_H), (0, 0, 0, 0))
    ov_draw = ImageDraw.Draw(overlay)
    ov_draw.rounded_rectangle(bbox, radius=radius, fill=bg_color, outline=border_color, width=border_width)
    return Image.alpha_composite(img, overlay)

def draw_dot(draw, x, y, color=NAVY, r=7):
    draw.ellipse([x - r, y - r, x + r, y + r], fill=color)

# ----------------- SLIDE 01: COVER -----------------
def gen_slide_01():
    cover_path = os.path.join(BRAIN_DIR, "slide_cover_1789343239327.jpg")
    base = Image.open(cover_path).convert("RGBA").resize((SLIDE_W, SLIDE_H), Image.Resampling.LANCZOS)
    
    card_w, card_h = 880, 720
    card_x, card_y = 90, 180
    
    card = Image.new("RGBA", (SLIDE_W, SLIDE_H), (0, 0, 0, 0))
    c_draw = ImageDraw.Draw(card)
    c_draw.rounded_rectangle([card_x, card_y, card_x + card_w, card_y + card_h], radius=24, fill=(255, 255, 255, 242), outline=(255, 255, 255, 255), width=3)
    
    out = Image.alpha_composite(base, card)
    draw = ImageDraw.Draw(out)
    
    draw_badge(draw, "115 學年度 第一學期 班親會", card_x + 50, card_y + 50, bg_color=ORANGE, font_size=26)
    draw.text((card_x + 50, card_y + 125), "航向未來的起點", font=get_font(True, 72), fill=NAVY)
    draw.text((card_x + 50, card_y + 225), "鹿陽國民小學 六年一班", font=get_font(True, 40), fill=TEXT_DARK)
    draw.line([(card_x + 50, card_y + 295), (card_x + card_w - 50, card_y + 295)], fill=(226, 232, 240, 255), width=3)
    
    quotes = [
        ("先相信孩子，再慢慢理解與引導", ORANGE),
        ("自主學習與愛閱家庭，深耕閱讀日常", GREEN),
        ("科技是翅膀而非猛獸，善用 3C 賦能成長", NAVY),
        ("攜手同行，做孩子最溫暖堅實的後盾", GOLD)
    ]
    qy = card_y + 330
    for text, dot_col in quotes:
        draw_dot(draw, card_x + 70, qy + 18, color=dot_col, r=8)
        draw.text((card_x + 95, qy), text, font=get_font(True, 30), fill=TEXT_DARK)
        qy += 66
        
    draw_badge(draw, "導師：高志賢 老師", card_x + 50, card_y + 600, bg_color=NAVY, font_size=32, pad_x=32, pad_y=14)
    out.convert("RGB").save(os.path.join(OUT_DIR, "01-cover.png"), quality=95)
    print("Slide 01 generated.")

# ----------------- SLIDE 02: WELCOME -----------------
def gen_slide_02():
    welcome_path = os.path.join(BRAIN_DIR, "slide_welcome_1789343255959.jpg")
    w_img = Image.open(welcome_path).convert("RGBA")
    
    base = create_base_canvas()
    illus_w = 880
    illus_h = int(illus_w * (1080 / 1920))
    w_img_resized = w_img.resize((illus_w, illus_h), Image.Resampling.LANCZOS)
    
    mask = Image.new("L", (illus_w, illus_h), 0)
    m_draw = ImageDraw.Draw(mask)
    m_draw.rounded_rectangle([0, 0, illus_w, illus_h], radius=20, fill=255)
    base.paste(w_img_resized, (960, 260), mask)
    
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "02", "走進青春期：孩子的拔節成長", "看見孩子升上小六的轉變・從依賴走向獨立的微妙時刻")
    
    cards = [
        ("班級步入常軌", [
            "開學至今，全班展現極佳的常規與凝聚力。",
            "學習態度認真專注，生活作息穩定踏實。"
        ]),
        ("自主意識萌芽", [
            "孩子開始有獨立主見，思考更加深入廣闊。",
            "渴望用自己的方式探索世界與解決問題。"
        ]),
        ("渴望被尊重與理解", [
            "這不是叛逆，而是孩子正在練習長大成熟。",
            "需要親師用溫暖包容、平等視角接納引導。"
        ])
    ]
    
    cy = 260
    for title, lines in cards:
        base = draw_card(base, [80, cy, 910, cy + 210], bg_color=(255, 255, 255, 248), border_color=(226, 232, 240, 255), radius=18)
        d = ImageDraw.Draw(base)
        draw_dot(d, 120, cy + 48, color=NAVY, r=9)
        d.text((145, cy + 26), title, font=get_font(True, 38), fill=NAVY)
        d.text((120, cy + 92), lines[0], font=get_font(False, 30), fill=TEXT_DARK)
        d.text((120, cy + 140), lines[1], font=get_font(False, 30), fill=TEXT_DARK)
        cy += 240
        
    base.convert("RGB").save(os.path.join(OUT_DIR, "02-welcome.png"), quality=95)
    print("Slide 02 generated.")

# ----------------- SLIDE 03: TEACHER PHILOSOPHY -----------------
def gen_slide_03():
    t_path = os.path.join(BRAIN_DIR, "slide_teacher_1789343271855.jpg")
    t_img = Image.open(t_path).convert("RGBA")
    
    base = create_base_canvas()
    illus_w = 880
    illus_h = int(illus_w * (1080 / 1920))
    t_img_resized = t_img.resize((illus_w, illus_h), Image.Resampling.LANCZOS)
    
    mask = Image.new("L", (illus_w, illus_h), 0)
    m_draw = ImageDraw.Draw(mask)
    m_draw.rounded_rectangle([0, 0, illus_w, illus_h], radius=20, fill=255)
    base.paste(t_img_resized, (960, 260), mask)
    
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "03", "高老師的陪伴哲學：先相信，再理解", "做孩子最堅實的後盾——絕不有罪推定・深究行為背後的心理密碼")
    
    cards = [
        ("信任第一，絕不有罪推定", [
            "在我的教室裡，衝突發生時絕不急於定罪。",
            "先接納孩子的情緒，給予全然的信任與安全感。"
        ]),
        ("穿透表象，探究心理原因", [
            "孩子的脫序行為往往只是情緒的冰山一角。",
            "深入探討背後的焦慮、挫折，以及心理需求。"
        ]),
        ("溫和堅定，陪伴負責修正", [
            "給孩子犯錯與調整的空間，營造反思氛圍。",
            "引導看見行為後果，陪伴孩子學會勇於負責。"
        ])
    ]
    
    cy = 260
    for title, lines in cards:
        base = draw_card(base, [80, cy, 910, cy + 210], bg_color=(255, 255, 255, 248), border_color=(232, 141, 103, 255), radius=18)
        d = ImageDraw.Draw(base)
        draw_dot(d, 120, cy + 48, color=ORANGE, r=9)
        d.text((145, cy + 26), title, font=get_font(True, 38), fill=ORANGE)
        d.text((120, cy + 92), lines[0], font=get_font(False, 30), fill=TEXT_DARK)
        d.text((120, cy + 140), lines[1], font=get_font(False, 30), fill=TEXT_DARK)
        cy += 240

    base.convert("RGB").save(os.path.join(OUT_DIR, "03-teacher.png"), quality=95)
    print("Slide 03 generated.")

# ----------------- SLIDE 04: SEL QUOTES (NEW SPLIT 1) -----------------
def gen_slide_04():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "04", "心靈的韌性：高年級 SEL 核心金句", "【輔導室推動】培養孩子在面對挫折與壓力時，依然能站起來的內在力量")
    
    # 2 Giant Golden Quote Cards
    # Quote 1
    base = draw_card(base, [120, 260, SLIDE_W - 120, 560], bg_color=(254, 243, 238, 255), border_color=(232, 141, 103, 255), radius=24)
    d = ImageDraw.Draw(base)
    draw_badge(d, "心靈成長金句 01", 170, 305, bg_color=ORANGE, font_size=26)
    d.text((170, 380), "「孩子需要的，不只是成功，", font=get_font(True, 44), fill=NAVY)
    d.text((170, 450), "   而是面對不成功的能力。」", font=get_font(True, 44), fill=ORANGE)
    
    # Quote 2
    base = draw_card(base, [120, 600, SLIDE_W - 120, 900], bg_color=(235, 244, 250, 255), border_color=(44, 94, 138, 255), radius=24)
    d = ImageDraw.Draw(base)
    draw_badge(d, "心靈成長金句 02", 170, 645, bg_color=NAVY, font_size=26)
    d.text((170, 720), "「求助不是我很弱，", font=get_font(True, 44), fill=ORANGE)
    d.text((170, 790), "   而是我知道什麼時候需要藉助別人的力量。」", font=get_font(True, 44), fill=NAVY)

    base.convert("RGB").save(os.path.join(OUT_DIR, "04-sel.png"), quality=95)
    print("Slide 04 generated.")

# ----------------- SLIDE 05: SEL ACTION (NEW SPLIT 2) -----------------
def gen_slide_05():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "05", "心靈的韌性：SEL 情緒調節與應對", "【輔導室推動】認識自己 → 管理情緒 → 理解他人 → 建立關係 → 做出負責任的選擇")
    
    # 3 Big Strategy Cards
    cards = [
        ("1. 看見與說出情緒", NAVY, [
            "覺察身體緊繃訊號，接納感受",
            "引導孩子把模糊的壓力說出來",
            "「能說出來，就是整理的開始」"
        ]),
        ("2. 暫停一下先穩住", ORANGE, [
            "情緒高漲時先深呼吸、喝杯溫水",
            "暫離現場，讓理智大腦重回冷靜",
            "落實「停一下、想一想、再決定」"
        ]),
        ("3. 拆解難題找支持", GREEN, [
            "把巨大的壓力拆解成下一小步",
            "不用一個人硬撐，主動尋求支持",
            "在陪伴中重新找回自信與安全感"
        ])
    ]
    
    cw = 540
    ch = 600
    cx_start = 80
    cy = 260
    for i, (title, color, bullets) in enumerate(cards):
        x = cx_start + i * (cw + 45)
        base = draw_card(base, [x, cy, x + cw, cy + ch], bg_color=(255, 255, 255, 248), border_color=color, radius=20)
        d = ImageDraw.Draw(base)
        draw_badge(d, f"步驟 0{i+1}", x + 40, cy + 38, bg_color=color, font_size=28)
        d.text((x + 40, cy + 115), title, font=get_font(True, 42), fill=color)
        d.line([(x + 40, cy + 185), (x + cw - 40, cy + 185)], fill=(226, 232, 240, 255), width=4)
        
        by = cy + 225
        for b in bullets:
            draw_dot(d, x + 38, by + 18, color=color, r=8)
            d.text((x + 60, by), b, font=get_font(False, 29), fill=TEXT_DARK)
            by += 105

    base.convert("RGB").save(os.path.join(OUT_DIR, "05-sel-action.png"), quality=95)
    print("Slide 05 generated.")

# ----------------- SLIDE 06: AUTONOMOUS LEARNING (NEW SPLIT) -----------------
def gen_slide_06():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "06", "從被動到自律：高年級自主學習關鍵", "高年級不再依賴大人盯梢・培養孩子終身受益的自律自學力")
    
    cards = [
        ("時間管理自主規劃", NAVY, "引導自主規劃每日課後作息與進度，建立守時自律好習慣。"),
        ("深耕自主閱讀習慣", GREEN, "由圖文書進階至長篇與思辨讀物，透過深度閱讀奠定思維力。"),
        ("勇於主動提問探究", ORANGE, "鼓勵多問「為什麼」，讓學習從被動應付轉為主動探索未知。"),
        ("建立自律與成就感", GOLD, "看見自己每天微小的進步與堅持，在克服挑戰中累積自信心。")
    ]
    
    cy = 260
    for title, color, desc in cards:
        base = draw_card(base, [100, cy, SLIDE_W - 100, cy + 140], bg_color=(255, 255, 255, 248), border_color=color, radius=18)
        d = ImageDraw.Draw(base)
        draw_badge(d, title, 140, cy + 36, bg_color=color, font_size=30, pad_x=26, pad_y=12)
        d.text((475, cy + 44), desc, font=get_font(False, 34), fill=TEXT_DARK)
        cy += 165

    base.convert("RGB").save(os.path.join(OUT_DIR, "06-learning.png"), quality=95)
    print("Slide 06 generated.")

# ----------------- SLIDE 07: LOVE READING POLICY (NEW SPLIT) -----------------
def gen_slide_07():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "07", "【教務處宣導】臺中市「愛閱家庭」實施計畫", "推動親子共讀・累積智慧存款・全面升級為雲端智慧存摺登錄")
    
    # 2 Big Cards
    # Left: 核心精神
    base = draw_card(base, [80, 260, 880, 880], bg_color=(240, 249, 244, 255), border_color=(88, 164, 126, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "計畫三大理念", 130, 305, bg_color=GREEN, font_size=28)
    d.text((130, 375), "「愛閱家庭」核心精神", font=get_font(True, 46), fill=GREEN)
    
    p1 = [
        ("i 閱（自我實踐）", "閱讀是自己的事，大人與孩子身體力行。"),
        ("愛閱（熱愛閱讀）", "把閱讀當成生活享受，而非沉重負擔。"),
        ("愛閱（家庭之愛）", "透過共讀增進情感，凝聚家庭溫暖時光。"),
        ("每日共讀 20 分鐘", "每天只要 20 分鐘，共創書香溫馨家庭。")
    ]
    py = 465
    for t, desc in p1:
        draw_dot(d, 145, py + 18, color=GREEN, r=8)
        d.text((168, py), f"{t}：", font=get_font(True, 34), fill=NAVY)
        d.text((168, py + 46), desc, font=get_font(False, 30), fill=TEXT_DARK)
        py += 102
        
    # Right: 雲端申請與登錄重要日程
    base = draw_card(base, [930, 260, SLIDE_W - 80, 880], bg_color=(255, 255, 255, 248), border_color=(44, 94, 138, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "重要行政日程", 980, 305, bg_color=NAVY, font_size=28)
    d.text((980, 375), "雲端登錄與集點流程", font=get_font(True, 46), fill=NAVY)
    
    p2 = [
        ("登錄網站平台", "臺中市愛閱家庭（雲端智慧存摺系統）"),
        ("家長線上申請期", "115.09.16 ～ 115.10.25（自行註冊）"),
        ("正式登錄起算日", "115.11.01 起，每月共讀滿 20 天即達標！"),
        ("閱讀達人榮譽獎", "連續達成任務，頒發教育局獎狀與證書！")
    ]
    py2 = 465
    for t, desc in p2:
        draw_dot(d, 995, py2 + 18, color=NAVY, r=8)
        d.text((1018, py2), f"{t}：", font=get_font(True, 34), fill=ORANGE)
        d.text((1018, py2 + 46), desc, font=get_font(False, 30), fill=TEXT_DARK)
        py2 += 102

    base.convert("RGB").save(os.path.join(OUT_DIR, "07-reading-policy.png"), quality=95)
    print("Slide 07 generated.")

# ----------------- SLIDE 08: AI READING (NEW) -----------------
def gen_slide_08():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "08", "【自主閱讀深耕】AI 雲端閱讀理解認證平台", "高老師運用 Google AI Studio 親自研發・以理解代替死記・啟發深層思考與表達")
    
    cards = [
        ("導師精選文本", ORANGE, "緊扣主題與時事", [
            "配合單元進度與生活時事",
            "涵蓋人文科普與情緒素養",
            "文章長度適中富思考深度",
            "扎根六年級跨領域自主力"
        ]),
        ("理解代替死記", NAVY, "用自己的話回答", [
            "告別選擇題與關鍵字抄寫",
            "針對核心主旨與推論做答",
            "鼓勵打字抒發個人真實想法",
            "鍛鍊文字組織與表達自信"
        ]),
        ("Google AI 賦能", GREEN, "智慧互動與回饋", [
            "AI 助教即時賞識肯定思考",
            "引導孩子發現盲點深入探究",
            "接納多元觀點，建立成就感",
            "解鎖閱讀認證，激發自律力"
        ])
    ]
    
    cw = 540
    ch = 580
    cx_start = 80
    cy = 260
    for i, (title, color, sub, bullets) in enumerate(cards):
        x = cx_start + i * (cw + 45)
        base = draw_card(base, [x, cy, x + cw, cy + ch], bg_color=(255, 255, 255, 248), border_color=color, radius=20)
        d = ImageDraw.Draw(base)
        draw_badge(d, sub, x + 35, cy + 32, bg_color=color, font_size=26)
        d.text((x + 35, cy + 102), title, font=get_font(True, 42), fill=color)
        d.line([(x + 35, cy + 172), (x + cw - 35, cy + 172)], fill=(226, 232, 240, 255), width=4)
        
        by = cy + 210
        for b in bullets:
            draw_dot(d, x + 45, by + 16, color=color, r=8)
            d.text((x + 70, by), b, font=get_font(False, 30), fill=TEXT_DARK)
            by += 88

    base = draw_card(base, [80, 865, SLIDE_W - 80, 965], bg_color=(235, 244, 250, 255), border_color=(44, 94, 138, 255), radius=16)
    d = ImageDraw.Draw(base)
    bw, bh = draw_badge(d, "高老師的初心", 120, 888, bg_color=NAVY, font_size=26)
    d.text((120 + bw + 30, 892), "把科技化為學習翅膀，讓孩子在對話中學會深度思考與理解！", font=get_font(True, 32), fill=NAVY)

    base.convert("RGB").save(os.path.join(OUT_DIR, "08-reading-ai.png"), quality=95)
    print("Slide 08 generated.")

# ----------------- SLIDE 09: GEAR NOVEL (NEW) -----------------
def gen_slide_09():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "09", "【長篇閱讀深耕】《冒險齒輪》少兒原創小說庫", "高老師親自開發・中英即時對照・語音朗讀・引導孩子靜心閱讀長篇小說")

    cards = [
        ("原創長篇小說", ORANGE, "克服長文閱讀恐懼", [
            "少兒專屬原創科幻解謎長篇",
            "告別只看漫畫與短影片習慣",
            "懸疑緊湊情節引領深度沉浸",
            "循序漸進培養長文專注耐性"
        ]),
        ("中英雙語對照", NAVY, "打破語言閱讀隔閡", [
            "中文與英文即時切換並列呈現",
            "照顧英語佳但中文吃力的孩子",
            "雙語沉浸對照，拓展雙語力",
            "無障礙共享閱讀冒險的樂趣"
        ]),
        ("智慧語音朗讀", GREEN, "多感官沉浸式體驗", [
            "內建語音朗讀有聲書隨點隨聽",
            "照顧不同學習特質與吸收風格",
            "解謎實驗室與專屬閱讀成就",
            "激發孩子主動追讀的內在動力"
        ])
    ]

    cw = 540
    ch = 580
    cx_start = 80
    cy = 260
    for i, (title, color, sub, bullets) in enumerate(cards):
        x = cx_start + i * (cw + 45)
        base = draw_card(base, [x, cy, x + cw, cy + ch], bg_color=(255, 255, 255, 248), border_color=color, radius=20)
        d = ImageDraw.Draw(base)
        draw_badge(d, sub, x + 35, cy + 32, bg_color=color, font_size=26)
        d.text((x + 35, cy + 102), title, font=get_font(True, 42), fill=color)
        d.line([(x + 35, cy + 172), (x + cw - 35, cy + 172)], fill=(226, 232, 240, 255), width=4)
        
        by = cy + 210
        for b in bullets:
            draw_dot(d, x + 45, by + 16, color=color, r=8)
            d.text((x + 70, by), b, font=get_font(False, 30), fill=TEXT_DARK)
            by += 88

    base = draw_card(base, [80, 865, SLIDE_W - 80, 965], bg_color=(235, 244, 250, 255), border_color=(44, 94, 138, 255), radius=16)
    d = ImageDraw.Draw(base)
    bw, bh = draw_badge(d, "教學轉變心法", 120, 888, bg_color=NAVY, font_size=26)
    d.text((120 + bw + 30, 892), "給孩子真正想看的故事，從被動催讀，變為主動廢寢忘食！", font=get_font(True, 32), fill=NAVY)

    base.convert("RGB").save(os.path.join(OUT_DIR, "09-gear-novel.png"), quality=95)
    print("Slide 09 generated.")

# ----------------- SLIDE 10: 3C PHILOSOPHY (NEW SPLIT) -----------------
def gen_slide_10():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "10", "科技是翅膀，不是猛獸：高老師的 3C 哲學", "不把 3C 當洪水猛獸・擁抱數位工具作為高年級自主學習的強大助力")
    
    # 2 Large Contrast Cards
    base = draw_card(base, [80, 260, 880, 880], bg_color=(254, 243, 238, 255), border_color=(232, 141, 103, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "傳統視角 vs. 高老師視角", 130, 305, bg_color=ORANGE, font_size=28)
    d.text((130, 375), "從全面防堵轉為正向賦能", font=get_font(True, 46), fill=ORANGE)
    
    p1 = [
        "3C 數位能力是未來的關鍵競爭力",
        "一味盲目禁止，只會讓孩子私下使用",
        "與其把科技當敵人，不如教孩子善用它",
        "引導孩子成為數位工具的聰明掌控者"
    ]
    py = 475
    for text in p1:
        draw_dot(d, 145, py + 18, color=ORANGE, r=9)
        d.text((172, py), text, font=get_font(True, 34), fill=TEXT_DARK)
        py += 98
        
    base = draw_card(base, [930, 260, SLIDE_W - 80, 880], bg_color=(235, 244, 250, 255), border_color=(44, 94, 138, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "學習上的強大助力", 980, 305, bg_color=NAVY, font_size=28)
    d.text((980, 375), "把 3C 用在對的地方！", font=get_font(True, 46), fill=NAVY)
    
    p2 = [
        "查閱科學百科、歷史文獻與最新知識",
        "課業難題主動搜尋、思辨與交叉驗證",
        "分組專案協作、簡報製作與資料統整",
        "化被動娛樂滑機，為主動數位探究解題"
    ]
    py2 = 475
    for text in p2:
        draw_dot(d, 995, py2 + 18, color=NAVY, r=9)
        d.text((1022, py2), text, font=get_font(True, 34), fill=TEXT_DARK)
        py2 += 98

    base.convert("RGB").save(os.path.join(OUT_DIR, "10-digital-wings.png"), quality=95)
    print("Slide 10 generated.")

# ----------------- SLIDE 11: 3C DISCIPLINE (NEW SPLIT) -----------------
def gen_slide_11():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "11", "親師步調一致：3C 數位健康與自律約定", "在家庭中建立健康的 3C 使用規範・陪伴孩子養成自我節制的好習慣")
    
    cards = [
        ("明確約定使用時限", NAVY, "每天約定固定使用時間，時間一到自覺休息護眼。"),
        ("公共空間公開使用", ORANGE, "在客廳等公共空間使用，睡前 1 小時手機不進臥室。"),
        ("用開放溝通代替沒收", GREEN, "多聊聊在網路上看見什麼，以傾聽討論代替高壓沒收。"),
        ("數位素養與自我負責", GOLD, "教導保護個人隱私、辨識網路假訊息，學會自我當責。")
    ]
    
    cy = 260
    for title, color, desc in cards:
        base = draw_card(base, [100, cy, SLIDE_W - 100, cy + 140], bg_color=(255, 255, 255, 248), border_color=color, radius=18)
        d = ImageDraw.Draw(base)
        draw_badge(d, title, 140, cy + 36, bg_color=color, font_size=30, pad_x=26, pad_y=12)
        d.text((475, cy + 44), desc, font=get_font(False, 34), fill=TEXT_DARK)
        cy += 165

    base.convert("RGB").save(os.path.join(OUT_DIR, "11-digital-discipline.png"), quality=95)
    print("Slide 11 generated.")

# ----------------- SLIDE 12: HEALTH 1 (NEW SPLIT) -----------------
def gen_slide_12():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "12", "【學務處衛教】校園健康：洗手與咳嗽禮節", "上呼吸道感染防護力從日常做起・少一點病毒傳播，多一點安心學習！")
    
    # 2 Giant Cards
    # Left: 洗手
    base = draw_card(base, [80, 260, 880, 880], bg_color=(235, 244, 250, 255), border_color=(44, 94, 138, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "守則 01", 130, 305, bg_color=NAVY, font_size=28)
    d.text((130, 375), "手部清潔做好做滿", font=get_font(True, 46), fill=NAVY)
    
    h1 = [
        "洗手七字訣：內・外・夾・弓・大・立・腕",
        "每次搓洗至少 40 秒，吃東西前務必洗手",
        "擤鼻涕、打噴嚏、如廁後徹底洗淨雙手",
        "以清水徹底沖淨肥皂泡沫，並務必擦乾！"
    ]
    hy1 = 475
    for text in h1:
        draw_dot(d, 145, hy1 + 18, color=NAVY, r=9)
        d.text((172, hy1), text, font=get_font(True, 34), fill=TEXT_DARK)
        hy1 += 98
        
    # Right: 咳嗽禮節
    base = draw_card(base, [930, 260, SLIDE_W - 80, 880], bg_color=(254, 243, 238, 255), border_color=(232, 141, 103, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "守則 02", 980, 305, bg_color=ORANGE, font_size=28)
    d.text((980, 375), "咳嗽禮節要做到", font=get_font(True, 46), fill=ORANGE)
    
    h2 = [
        "咳嗽或打噴嚏時，以手肘或面紙遮掩口鼻",
        "使用後的衛生紙面紙，立即妥善丟入垃圾桶",
        "有呼吸道症狀時全程戴口罩，保護彼此安全",
        "落實咳嗽禮節，是對同儕最溫暖貼心的尊重"
    ]
    hy2 = 475
    for text in h2:
        draw_dot(d, 995, hy2 + 18, color=ORANGE, r=9)
        d.text((1022, hy2), text, font=get_font(True, 34), fill=TEXT_DARK)
        hy2 += 98

    base.convert("RGB").save(os.path.join(OUT_DIR, "12-health-hygiene.png"), quality=95)
    print("Slide 12 generated.")

# ----------------- SLIDE 13: HEALTH 2 (NEW SPLIT) -----------------
def gen_slide_13():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "13", "【學務處衛教】通風換氣與生病不上課", "上呼吸道感染防護力從日常做起・不舒服別硬撐，落實健康自主管理")
    
    # 2 Giant Cards
    # Left: 通風
    base = draw_card(base, [80, 260, 880, 880], bg_color=(240, 249, 244, 255), border_color=(88, 164, 126, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "守則 03", 130, 305, bg_color=GREEN, font_size=28)
    d.text((130, 375), "教室保持通風良好", font=get_font(True, 46), fill=GREEN)
    
    h3 = [
        "適時開窗維持對流，確保空氣流通",
        "避免長時間處於通風不良密閉空間",
        "個人水壺、餐具專屬專用，絕不共用",
        "維持良好通風，大幅降低病毒傳播"
    ]
    hy3 = 475
    for text in h3:
        draw_dot(d, 145, hy3 + 18, color=GREEN, r=9)
        d.text((172, hy3), text, font=get_font(True, 34), fill=TEXT_DARK)
        hy3 += 98
        
    # Right: 生病不上課
    base = draw_card(base, [930, 260, SLIDE_W - 80, 880], bg_color=(254, 242, 242, 255), border_color=RED_ACCENT, radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "守則 04", 980, 305, bg_color=RED_ACCENT, font_size=28)
    d.text((980, 375), "不舒服就別硬撐！", font=get_font(True, 46), fill=RED_ACCENT)
    
    h4 = [
        "注意咳嗽、喉嚨痛、流鼻水、發燒等症狀",
        "充分休息補充水分，落實生病不上課",
        "發燒（耳溫≧38℃）請在家休養管理",
        "退燒滿 24 小時後再返校，守護同儕！"
    ]
    hy4 = 475
    for text in h4:
        draw_dot(d, 995, hy4 + 18, color=RED_ACCENT, r=9)
        d.text((1022, hy4), text, font=get_font(True, 34), fill=TEXT_DARK)
        hy4 += 98

    base.convert("RGB").save(os.path.join(OUT_DIR, "13-health-safety.png"), quality=95)
    print("Slide 13 generated.")

# ----------------- SLIDE 14: ATTENDANCE RULES (NEW SPLIT) -----------------
def gen_slide_14():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "14", "【學務處宣導】學生請假方式與通報管道", "明確掌握學生差勤行蹤・落實校園安全第一道防線")
    
    cards = [
        ("當日上午 8:30 前完成通報", NAVY, "孩子若因病或事故不克到校，請家長務必於當日 8:30 前告知。"),
        ("通報管道一：LINE 訊息", GREEN, "以 LINE 訊息告知高老師，方便導師第一時間掌握差勤與原因。"),
        ("通報管道二：學校總機專線", ORANGE, "撥打總機 04-26567968 轉分機 720 或 724 由生輔組代為登記。"),
        ("假單補辦手續規範", GOLD, "事假須事前填單提出；病喪假得於事後 3 日內補齊請假單手續。"),
        ("連續 3 日以上就醫證明", RED_ACCENT, "若病假連續滿 3 日（含）以上，返校時須附醫療院所之就醫證明。")
    ]
    
    cy = 260
    for title, color, desc in cards:
        base = draw_card(base, [100, cy, SLIDE_W - 100, cy + 120], bg_color=(255, 255, 255, 248), border_color=color, radius=18)
        d = ImageDraw.Draw(base)
        draw_badge(d, title, 135, cy + 26, bg_color=color, font_size=28, pad_x=24, pad_y=10)
        d.text((510, cy + 40), desc, font=get_font(False, 32), fill=TEXT_DARK)
        cy += 138

    base.convert("RGB").save(os.path.join(OUT_DIR, "14-attendance-rules.png"), quality=95)
    print("Slide 14 generated.")

# ----------------- SLIDE 15: ATTENDANCE SECURITY (NEW SPLIT) -----------------
def gen_slide_15():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "15", "【學務處宣導】審核層級與外出安全管制", "嚴謹校園安全管理制度・共同守護每位學童的平安")
    
    # 2 Big Cards
    # Left: 審核層級
    base = draw_card(base, [80, 260, 880, 880], bg_color=(255, 255, 255, 248), border_color=(44, 94, 138, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "行政審核規範", 130, 305, bg_color=NAVY, font_size=28)
    d.text((130, 375), "請假分級核准權責", font=get_font(True, 46), fill=NAVY)
    
    s1 = [
        ("請假 2 日以內", "由級任導師親自核准，落實差勤管理。"),
        ("請假 3 至未滿 5 日", "假單送生輔組，呈學務主任核定批准。"),
        ("請假 5 日以上", "假單送生輔組，呈報校長親自核定。"),
        ("義務教育常規", "國小屬義務教育階段，不得隨意休學。")
    ]
    sy1 = 465
    for t, desc in s1:
        draw_dot(d, 145, sy1 + 18, color=NAVY, r=8)
        d.text((168, sy1), f"{t}：", font=get_font(True, 34), fill=NAVY)
        d.text((168, sy1 + 46), desc, font=get_font(False, 30), fill=TEXT_DARK)
        sy1 += 102
        
    # Right: 臨時外出與中輟追蹤
    base = draw_card(base, [930, 260, SLIDE_W - 80, 880], bg_color=(254, 243, 238, 255), border_color=(232, 141, 103, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "校門管制規定", 980, 305, bg_color=ORANGE, font_size=28)
    d.text((980, 375), "臨時外出與差勤防護", font=get_font(True, 46), fill=ORANGE)
    
    s2 = [
        ("臨時外出通報", "家長須事先與導師電話聯繫確認事由。"),
        ("警衛室換證接回", "導師通知警衛室，核對身分無誤後接回。"),
        ("中輟追蹤機制", "無故曠課達 3 日者，依法通報教育局追蹤。"),
        ("校園安全至上", "精準掌握孩子行蹤，是親師最重大的責任！")
    ]
    sy2 = 465
    for t, desc in s2:
        draw_dot(d, 995, sy2 + 18, color=ORANGE, r=8)
        d.text((1018, sy2), f"{t}：", font=get_font(True, 34), fill=ORANGE)
        d.text((1018, sy2 + 46), desc, font=get_font(False, 30), fill=TEXT_DARK)
        sy2 += 102

    base.convert("RGB").save(os.path.join(OUT_DIR, "15-attendance-security.png"), quality=95)
    print("Slide 15 generated.")

# ----------------- SLIDE 16: GRADUATION -----------------
def gen_slide_16():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "16", "倒數計時的小學時光：六年級專屬盛事", "小學最後一年，攜手打造孩子一輩子珍藏的青春印記")
    
    # 2 Big Cards: 畢業旅行 & 畢業紀念冊
    # Left Card: 畢業旅行啟程
    base = draw_card(base, [80, 260, 920, 830], bg_color=(255, 255, 255, 248), border_color=(44, 94, 138, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "青春最璀璨的冒險", 130, 305, bg_color=NAVY, font_size=28)
    d.text((130, 375), "畢業旅行啟程", font=get_font(True, 46), fill=NAVY)
    d.line([(130, 440), (870, 440)], fill=(226, 232, 240, 255), width=3)
    
    b_trip = [
        "學習團體生活與自主獨立照顧能力",
        "走出教室實境體驗，拓展同窗眼界",
        "深化同學之間一生珍貴的夥伴情誼",
        "安全第一原則，細緻規劃每項參訪",
        "由學校學務處統籌，公開透明安心"
    ]
    by1 = 475
    for b in b_trip:
        draw_dot(d, 145, by1 + 16, color=NAVY, r=8)
        d.text((172, by1), b, font=get_font(True, 30), fill=TEXT_DARK)
        by1 += 68

    # Right Card: 畢業紀念冊編撰
    base = draw_card(base, [980, 260, 1820, 830], bg_color=(255, 255, 255, 248), border_color=(88, 164, 126, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "定格六年底蘊的美好", 1030, 305, bg_color=GREEN, font_size=28)
    d.text((1030, 375), "畢業紀念冊編撰", font=get_font(True, 46), fill=GREEN)
    d.line([(1030, 440), (1770, 440)], fill=(226, 232, 240, 255), width=3)
    
    b_album = [
        "記錄校園六年歡笑、汗水與成長",
        "每位孩子都有專屬篇幅燦爛笑顏",
        "親師生共同寫下真摯祝福與期許",
        "專業團隊細緻攝影，高品質美編",
        "長大後隨時翻閱的無價童年禮物"
    ]
    by2 = 475
    for b in b_album:
        draw_dot(d, 1045, by2 + 16, color=GREEN, r=8)
        d.text((1072, by2), b, font=get_font(True, 30), fill=TEXT_DARK)
        by2 += 68

    # Bottom Heartfelt Motto
    base = draw_card(base, [80, 860, SLIDE_W - 80, 960], bg_color=(235, 244, 250, 255), border_color=(44, 94, 138, 255), radius=16)
    d = ImageDraw.Draw(base)
    bw, bh = draw_badge(d, "高老師的心願", 120, 882, bg_color=NAVY, font_size=26)
    d.text((120 + bw + 30, 886), "讓每一位 601 的孩子，都能帶著被滿滿愛意包裹的溫暖記憶畢業！", font=get_font(True, 32), fill=NAVY)

    base.convert("RGB").save(os.path.join(OUT_DIR, "16-graduation.png"), quality=95)
    print("Slide 16 generated.")


# ----------------- SLIDE 17: ELECTION (NEW SPLIT) -----------------
def gen_slide_17():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "17", "班級自治：推選 601 班親會「會長」與「總務」", "正因有畢業旅行與畢業紀念冊等重大專案，更需要家長幹部共同把關！")
    
    # 2 Big Cards: 會長 & 總務
    # Left: 會長
    base = draw_card(base, [80, 260, 880, 880], bg_color=(255, 255, 255, 248), border_color=(44, 94, 138, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "幹部推選 01", 130, 305, bg_color=NAVY, font_size=28)
    d.text((130, 375), "班親會「會長」職責", font=get_font(True, 46), fill=NAVY)
    
    c1 = [
        "代表六年一班全體家長發聲與協調",
        "協助策劃支援班級重大活動（畢旅、專案）",
        "擔任家長與學校行政、導師間最佳橋樑",
        "凝聚全班家長向心力，營造溫暖親師社群",
        "歡迎熱心、富使命感的家長自薦或推薦！"
    ]
    cy1 = 475
    for c in c1:
        draw_dot(d, 145, cy1 + 18, color=NAVY, r=8)
        d.text((172, cy1), c, font=get_font(True, 32), fill=TEXT_DARK)
        cy1 += 78
        
    # Right: 總務
    base = draw_card(base, [930, 260, SLIDE_W - 80, 880], bg_color=(255, 255, 255, 248), border_color=(232, 141, 103, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "幹部推選 02", 980, 305, bg_color=ORANGE, font_size=28)
    d.text((980, 375), "班親會「總務」職責", font=get_font(True, 46), fill=ORANGE)
    
    c2 = [
        "管理班級專屬經費帳戶，專款專用",
        "負責畢業各項活動與專案款項之收取保管",
        "完整保留每一筆開銷單據與合法發票",
        "定期公開收支報表，財務透明全員安心",
        "歡迎細心、具財務經驗的家長熱情加入！"
    ]
    cy2 = 475
    for c in c2:
        draw_dot(d, 995, cy2 + 18, color=ORANGE, r=8)
        d.text((1022, cy2), c, font=get_font(True, 32), fill=TEXT_DARK)
        cy2 += 78

    base.convert("RGB").save(os.path.join(OUT_DIR, "17-election.png"), quality=95)
    print("Slide 17 generated.")

# ----------------- SLIDE 18: FINANCE TRANSPARENCY (NEW SPLIT) -----------------
def gen_slide_18():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "18", "財務公開透明：高老師與班親會的三大承諾", "讓每筆經費用在刀口・公開監督・老師專心教學、家長百分之百安心！")
    
    cards = [
        ("承諾一：專款專用", NAVY, "班級與畢業所有經費獨立建帳保管，絕不任意挪作他用。"),
        ("承諾二：帳目透明", GREEN, "所有單據與發票完整建檔留存，定期於群組公開清楚明細供檢視。"),
        ("承諾三：雙人覆核", ORANGE, "總務負責記帳、會長負責監督核銷，雙重把關確保每分錢清清楚楚。")
    ]
    
    cy = 275
    for title, color, desc in cards:
        base = draw_card(base, [100, cy, SLIDE_W - 100, cy + 185], bg_color=(255, 255, 255, 248), border_color=color, radius=20)
        d = ImageDraw.Draw(base)
        draw_badge(d, title, 140, cy + 32, bg_color=color, font_size=34, pad_x=28, pad_y=12)
        d.text((140, cy + 105), desc, font=get_font(False, 36), fill=TEXT_DARK)
        cy += 220

    base.convert("RGB").save(os.path.join(OUT_DIR, "18-finance-pledge.png"), quality=95)
    print("Slide 18 generated.")

# ----------------- SLIDE 19: COMMITTEE -----------------
def gen_slide_19():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "19", "誠摯致謝：家長委員會委員", "感謝家長委員熱心承擔重任・成為六年一班與全校孩子最堅實的溫暖後盾")
    
    base = draw_card(base, [120, 260, SLIDE_W - 120, 900], bg_color=(255, 255, 255, 252), border_color=GOLD, radius=24)
    d = ImageDraw.Draw(base)
    
    draw_badge(d, "衷心感謝・熱誠奉獻", 180, 305, bg_color=GOLD, font_size=30)
    d.text((180, 380), "恭喜並感謝本班家長委員會委員確認產生！", font=get_font(True, 48), fill=NAVY)
    d.text((180, 460), "經過前期的意願調查與推選，我們班已順利確定學校家長委員會委員名單。", font=get_font(False, 32), fill=TEXT_DARK)
    
    d.line([(180, 530), (SLIDE_W - 180, 530)], fill=(226, 232, 240, 255), width=3)
    
    items = [
        ("搭建親師橋樑", "代表班級參與學校校務會議，暢通班級與行政溝通管道。"),
        ("爭取豐沛資源", "為學童營造更優質學習環境，充實各項設備與活動基金。"),
        ("守護校園安全", "在各項校務決策中發揮家長專業，全面守護孩子身心安全。"),
        ("致上班級敬意", "高老師代表全班孩子與家長，致上最誠摯的感謝與熱烈掌聲！")
    ]
    iy = 565
    for t, desc in items:
        draw_badge(d, t, 180, iy - 6, bg_color=GOLD, font_size=26)
        d.text((400, iy), desc, font=get_font(False, 32), fill=TEXT_DARK)
        iy += 82
        
    base.convert("RGB").save(os.path.join(OUT_DIR, "19-committee.png"), quality=95)
    print("Slide 19 generated.")

# ----------------- SLIDE 20: VOLUNTEER RECRUITMENT -----------------
def gen_slide_20():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "20", "熱忱招募：115學年度愛心志工隊", "因為有您，孩子的安全更有保障；因為有您，孩子的笑容更加燦爛")
    
    # Left Card: 交通組 (Orange)
    base = draw_card(base, [80, 250, 930, 775], bg_color=(254, 243, 238, 255), border_color=(232, 141, 103, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "通學守護組", 130, 295, bg_color=ORANGE, font_size=26)
    d.text((130, 360), "交通組：學童安全維護", font=get_font(True, 40), fill=ORANGE)
    d.text((130, 420), "服務任務：上、下學時協助維護兒童交通安全", font=get_font(True, 26), fill=TEXT_DARK)
    
    draw_badge(d, "執勤時段（週一至週五・彈性單選）", 130, 470, bg_color=NAVY, font_size=22)
    
    slots = [
        ("早上時段", "07:10 - 07:50", "晨間通學巔峰路口導護與疏導"),
        ("中午時段", "12:45 - 13:10", "低年級或半天放學離校安全護送"),
        ("下午時段", "15:45 - 16:10", "全校放學重要路段守望與交管")
    ]
    sy = 530
    for name, time_str, note in slots:
        draw_badge(d, name, 130, sy, bg_color=ORANGE, font_size=22, pad_x=16, pad_y=6)
        d.text((260, sy + 2), time_str, font=get_font(True, 28), fill=NAVY)
        d.text((130, sy + 44), f"• {note}", font=get_font(False, 23), fill=TEXT_MUTED)
        sy += 75

    # Right Card: 圖書組 (Green)
    base = draw_card(base, [970, 250, SLIDE_W - 80, 775], bg_color=(240, 249, 244, 255), border_color=(88, 164, 126, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "校園悅讀組", 1020, 295, bg_color=GREEN, font_size=26)
    d.text((1020, 360), "圖書組：書籍整理與借還", font=get_font(True, 40), fill=GREEN)
    d.text((1020, 420), "服務任務：協助圖書室書籍整理、借閱歸還與推廣", font=get_font(True, 26), fill=TEXT_DARK)
    
    draw_badge(d, "執勤時段（週一至週五・上午半天）", 1020, 470, bg_color=NAVY, font_size=22)
    
    # Info boxes for Library
    draw_badge(d, "值勤時間", 1020, 530, bg_color=GREEN, font_size=22, pad_x=16, pad_y=6)
    d.text((1150, 532), "08:30 - 11:30", font=get_font(True, 28), fill=NAVY)
    d.text((1020, 574), "• 晨間半天服務，沉浸溫馨書香氣息", font=get_font(False, 23), fill=TEXT_MUTED)

    # Note about activity center
    base = draw_card(base, [1010, 625, SLIDE_W - 120, 735], bg_color=(255, 255, 255, 240), border_color=GREEN, radius=14)
    dd = ImageDraw.Draw(base)
    draw_badge(dd, "特別說明", 1030, 642, bg_color=GOLD, font_size=20, pad_x=12, pad_y=4)
    dd.text((1150, 644), "先登記意願，開館即排班", font=get_font(True, 24), fill=NAVY)
    dd.text((1030, 685), "※ 待學校活動中心整修驗收完畢後，即刻安排入館值勤！", font=get_font(False, 22), fill=TEXT_DARK)

    # Bottom Banner: 報名方式
    base = draw_card(base, [80, 805, SLIDE_W - 80, 955], bg_color=(235, 244, 250, 255), border_color=(44, 94, 138, 255), radius=18)
    d = ImageDraw.Draw(base)
    draw_badge(d, "志工報名方式", 120, 825, bg_color=NAVY, font_size=22)
    
    # 2 ways
    d.text((120, 880), "1. 紙本回條：填寫通知單回條並勾選組別與方便時段，交由孩子帶回學校。", font=get_font(True, 26), fill=TEXT_DARK)
    d.text((120, 915), "2. 導師登記：亦可直接向高志賢老師口頭登記，或於 LINE 班級官方訊息報名！", font=get_font(True, 26), fill=NAVY)
    
    base.convert("RGB").save(os.path.join(OUT_DIR, "20-volunteer.png"), quality=95)
    print("Slide 20 generated.")

# ----------------- SLIDE 21: COMMUNICATION -----------------
def gen_slide_21():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "21", "親師即時連線：攜手同行做孩子的橋樑", "孩子有任何狀況請第一時間與導師聯繫・親師互信合作比事後焦慮更有效")
    
    # Left Card: LINE
    base = draw_card(base, [80, 260, 880, 770], bg_color=(240, 249, 244, 255), border_color=(88, 164, 126, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "平時日常聯繫", 130, 310, bg_color=GREEN, font_size=26)
    d.text((130, 385), "LINE 官方訊息（推薦）", font=get_font(True, 42), fill=GREEN)
    
    l_info = [
        "適用孩子平日學習狀況與作業諮詢",
        "班級常規、作息或常態活動訊息交流",
        "上課期間老師全心在孩子身上",
        "老師會利用課間空檔或放學後詳細回覆",
        "歡迎隨時留言，不必擔心打擾！"
    ]
    ly = 465
    for l in l_info:
        draw_dot(d, 145, ly + 16, color=GREEN, r=7)
        d.text((170, ly), l, font=get_font(False, 28), fill=TEXT_DARK)
        ly += 56
        
    # Right Card: Phone
    base = draw_card(base, [930, 260, SLIDE_W - 80, 770], bg_color=(254, 243, 238, 255), border_color=(232, 141, 103, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "緊急突發狀況", 980, 310, bg_color=ORANGE, font_size=26)
    d.text((980, 385), "導師專線電話直撥", font=get_font(True, 42), fill=ORANGE)
    
    # Phone number highlight box (HUGE)
    base = draw_card(base, [980, 460, SLIDE_W - 130, 570], bg_color=(255, 255, 255, 255), border_color=ORANGE, radius=14, border_width=3)
    dd = ImageDraw.Draw(base)
    draw_badge(dd, "專線直撥", 1010, 485, bg_color=NAVY, font_size=24)
    dd.text((1160, 485), "0963-159-896", font=get_font(True, 42), fill=NAVY)
    
    p_info = [
        "孩子突發身體急症或意外受傷",
        "早晨臨時請假需即時口頭通報",
        "提醒：若遇忙線未接，老師一看到立刻回撥！"
    ]
    py = 600
    for p in p_info:
        draw_dot(dd, 995, py + 16, color=ORANGE, r=7)
        dd.text((1020, py), p, font=get_font(False, 28), fill=TEXT_DARK)
        py += 56

    # Bottom Motto
    base = draw_card(base, [80, 800, SLIDE_W - 80, 950], bg_color=(235, 244, 250, 255), border_color=(44, 94, 138, 255), radius=18)
    d = ImageDraw.Draw(base)
    draw_badge(d, "高老師的溝通原則", 120, 825, bg_color=NAVY, font_size=22)
    d.text((120, 880), "「孩子有任何狀況，請第一時間與我聯繫。我們坦誠對話、互相合作，讓小問題在第一時間得到最好照顧。」", font=get_font(True, 28), fill=TEXT_DARK)

    base.convert("RGB").save(os.path.join(OUT_DIR, "21-communication.png"), quality=95)
    print("Slide 21 generated.")

# ----------------- SLIDE 22: MESSAGE TO PARENTS -----------------
def gen_slide_22():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "22", "給家長的一封信：並肩走一段平穩堅定的路", "六年級是童年的尾聲，也是青春的序曲・讓我們給予孩子展翅飛翔的底氣")
    
    base = draw_card(base, [120, 260, SLIDE_W - 120, 920], bg_color=(255, 255, 255, 252), border_color=(232, 141, 103, 255), radius=24)
    d = ImageDraw.Draw(base)
    
    draw_badge(d, "導師的心裡話", 180, 310, bg_color=ORANGE, font_size=28)
    
    letter = [
        "親愛的家長：",
        "",
        "六年級，是小學階段最特別、也最關鍵的一年。",
        "孩子正在經歷從依賴走向獨立的拔節時刻，他們渴望證明自己，心底卻極度需要大人的支持。",
        "",
        "我們無法替孩子走完人生的每一步路，也無法替他經歷所有的考試與挫折；",
        "但我們可以在他跑累的時候遞上一杯溫水，",
        "在他跌倒時抱抱他，讓他明白——他隨時可以再勇敢站起來。",
        "",
        "感謝各位家長六年來的悉心灌溉。小學的最後一年，",
        "高老師會竭盡全力陪伴六年一班的每一個孩子，帶著豐盛的勇氣與愛，航向未來！"
    ]
    
    ly = 380
    for line in letter:
        if line == "":
            ly += 22
        elif line.startswith("親愛的家長") or line.startswith("感謝各位家長"):
            d.text((180, ly), line, font=get_font(True, 32), fill=NAVY)
            ly += 48
        elif "跌倒" in line or "無法替孩子" in line:
            d.text((180, ly), line, font=get_font(True, 30), fill=ORANGE)
            ly += 48
        else:
            d.text((180, ly), line, font=get_font(False, 29), fill=TEXT_DARK)
            ly += 48
            
    d.text((SLIDE_W - 620, 835), "六年一班導師 高志賢 敬上", font=get_font(True, 34), fill=NAVY)

    base.convert("RGB").save(os.path.join(OUT_DIR, "22-message.png"), quality=95)
    print("Slide 22 generated.")

# ----------------- SLIDE 23: QA & THANK YOU -----------------
def gen_slide_23():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "23", "感謝聆聽．交流時間（Q&A）", "臺中市沙鹿區鹿陽國民小學 六年一班・讓我們一起成為孩子最好的神隊友！")
    
    # Left Card
    base = draw_card(base, [80, 260, 920, 880], bg_color=(255, 255, 255, 248), border_color=(44, 94, 138, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "現場互動環節", 130, 305, bg_color=NAVY, font_size=28)
    d.text((130, 375), "自由提問與意見分享", font=get_font(True, 46), fill=NAVY)
    
    flow = [
        ("自由提問交流", "對孩子學習、作息與常規有任何想法均可提出。"),
        ("班親幹部推選", "現場推選班親會「會長」與「總務」，共同把關經費。"),
        ("畢業專案討論", "畢業旅行期望、活動規劃與紀念冊製作交流。"),
        ("填寫回饋表單", "歡迎家長掃描 QR Code 或填寫紙本，提供建言。")
    ]
    fy = 465
    for t, desc in flow:
        draw_dot(d, 145, fy + 18, color=ORANGE, r=8)
        d.text((170, fy), t, font=get_font(True, 34), fill=ORANGE)
        d.text((170, fy + 46), desc, font=get_font(False, 28), fill=TEXT_DARK)
        fy += 102
        
    # Right Card
    base = draw_card(base, [970, 260, SLIDE_W - 80, 880], bg_color=(240, 249, 244, 255), border_color=(88, 164, 126, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "親師聯繫總整理", 1020, 305, bg_color=GREEN, font_size=28)
    d.text((1020, 375), "陪伴孩子，隨時連線", font=get_font(True, 46), fill=GREEN)
    
    # Item 1: LINE
    draw_dot(d, 1035, 475 + 18, color=GREEN, r=9)
    d.text((1065, 475), "平常溝通：", font=get_font(True, 36), fill=NAVY)
    d.text((1065, 524), "LINE 官方班級社群 / 私訊留言", font=get_font(False, 32), fill=TEXT_DARK)
    
    # Item 2: Phone
    draw_dot(d, 1035, 605 + 18, color=GREEN, r=9)
    d.text((1065, 605), "導師專線手機（緊急直撥）：", font=get_font(True, 36), fill=NAVY)
    d.text((1065, 654), "0963-159-896", font=get_font(True, 44), fill=ORANGE)
    
    # Item 3: School
    draw_dot(d, 1035, 735 + 18, color=GREEN, r=9)
    d.text((1065, 735), "學校總機（差勤請假專線）：", font=get_font(True, 36), fill=NAVY)
    d.text((1065, 784), "04-26567968（分機 720 / 724）", font=get_font(False, 32), fill=TEXT_DARK)

    base.convert("RGB").save(os.path.join(OUT_DIR, "23-qa.png"), quality=95)
    print("Slide 23 generated.")

# ----------------- SLIDE 24: MEETING CHECKLIST / REMINDER -----------------
def gen_slide_24():
    base = create_base_canvas()
    draw = ImageDraw.Draw(base)
    draw_header_nav(draw, "24", "現場重要提醒：今日親師會三大必辦事項", "感謝各位家長熱情參與・離席前請協助確認完成以下三項核心要事")
    
    # Card 1: 1. 親師會家長簽到 (Navy Theme)
    base = draw_card(base, [70, 245, 630, 815], bg_color=(240, 246, 252, 255), border_color=(44, 94, 138, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "必辦要事 01", 110, 290, bg_color=NAVY, font_size=26)
    d.text((110, 360), "家長出席簽到", font=get_font(True, 38), fill=NAVY)
    draw_badge(d, "出席確認與資料領取", 110, 420, bg_color=(203, 222, 240), text_color=NAVY, font_size=20, pad_x=14, pad_y=4)
    
    c1_items = [
        "確認已於簽到表簽名",
        "掌握班級出席名冊",
        "領取各處室書面通知單",
        "確保親師通訊管道暢通"
    ]
    y = 485
    for item in c1_items:
        draw_dot(d, 120, y + 15, color=NAVY, r=7)
        d.text((145, y), item, font=get_font(True, 26), fill=TEXT_DARK)
        y += 70

    # Card 2: 2. 親師會會長及總務推選 (Orange Theme)
    base = draw_card(base, [680, 245, 1240, 815], bg_color=(254, 246, 240, 255), border_color=(232, 141, 103, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "必辦要事 02", 720, 290, bg_color=ORANGE, font_size=26)
    d.text((720, 360), "會長及總務推選", font=get_font(True, 38), fill=ORANGE)
    draw_badge(d, "班親自治核心團隊", 720, 420, bg_color=(254, 224, 210), text_color=ORANGE, font_size=20, pad_x=14, pad_y=4)
    
    c2_items = [
        "推選確認 601「班親會長」",
        "推選確認班級「總務幹部」",
        "共同把關畢業專案與各項經費",
        "親師攜手做孩子最強後援"
    ]
    y = 485
    for item in c2_items:
        draw_dot(d, 730, y + 15, color=ORANGE, r=7)
        d.text((755, y), item, font=get_font(True, 26), fill=TEXT_DARK)
        y += 70

    # Card 3: 3. 有意願當志工的家長 (Green Theme)
    base = draw_card(base, [1290, 245, 1850, 815], bg_color=(240, 249, 244, 255), border_color=(88, 164, 126, 255), radius=22)
    d = ImageDraw.Draw(base)
    draw_badge(d, "必辦要事 03", 1330, 290, bg_color=GREEN, font_size=26)
    d.text((1330, 360), "愛心志工意願登記", font=get_font(True, 38), fill=GREEN)
    draw_badge(d, "守護學童溫暖力量", 1330, 420, bg_color=(209, 237, 222), text_color=GREEN, font_size=20, pad_x=14, pad_y=4)
    
    c3_items = [
        "交通組：上放學路口導護",
        "圖書組：晨間書籍借還推廣",
        "現場向高老師登記報名",
        "或填妥紙本回條由孩子帶來"
    ]
    y = 485
    for item in c3_items:
        draw_dot(d, 1340, y + 15, color=GREEN, r=7)
        d.text((1365, y), item, font=get_font(True, 26), fill=TEXT_DARK)
        y += 70

    # Bottom Banner: 導師致謝與溫馨叮嚀
    base = draw_card(base, [70, 840, 1850, 960], bg_color=(255, 255, 255, 252), border_color=GOLD, radius=18)
    d = ImageDraw.Draw(base)
    draw_badge(d, "導師感謝與叮嚀", 110, 860, bg_color=GOLD, font_size=22)
    d.text((110, 908), "「再次誠摯感謝各位爸爸媽媽的蒞臨與支持！六年一班有您真好，夜深天涼，返家請注意安全！」", font=get_font(True, 28), fill=NAVY)

    base.convert("RGB").save(os.path.join(OUT_DIR, "24-reminder.png"), quality=95)
    print("Slide 24 generated.")

def main():
    print(f"Generating expanded {TOTAL_SLIDES} high-legibility slides (large font edition)...")
    for i in range(1, 25):
        globals()[f"gen_slide_{i:02d}"]()
    print("All 24 slides generated successfully.")
    
    # Auto-sync to website assets & root assets
    import shutil
    for target in [r"C:\Antigravity\班親會\assets\slides", r"C:\Antigravity\班親會\website\assets\slides"]:
        os.makedirs(target, exist_ok=True)
        for f in os.listdir(OUT_DIR):
            if f.endswith(".png"):
                shutil.copy2(os.path.join(OUT_DIR, f), os.path.join(target, f))
    print("All slides synced to web assets.")

if __name__ == "__main__":
    main()

