// 臺中市沙鹿區鹿陽國小 六年一班 班親會網站互動邏輯
document.addEventListener("DOMContentLoaded", () => {
  // Slide Data
    const slides = [
    {
      file: "assets/slides/01-cover.png",
      title: "Page 01｜航向未來的起點（開場封面）",
      note: "導師開場歡迎：小學六年的最後一哩路，歡迎各位家長走進六年一班，一同陪伴孩子展開新旅程。"
    },
    {
      file: "assets/slides/02-welcome.png",
      title: "Page 02｜走進青春期：孩子的拔節成長",
      note: "班級現況觀察：全班生活常規已上軌道，自主意識萌芽，我們用包容與尊重接納孩子練習長大的模樣。"
    },
    {
      file: "assets/slides/03-teacher.png",
      title: "Page 03｜高老師的陪伴哲學：先相信，再理解",
      note: "教育核心信念：在我的教室永遠沒有有罪推定。先接住情緒，再深究行為背後的心理需求。"
    },
    {
      file: "assets/slides/04-sel.png",
      title: "Page 04｜SEL 心靈金句：培養挫折復原力",
      note: "「孩子需要的，不只是成功，而是面對不成功的能力。」「求助不是我很弱，而是懂得適時借力。」"
    },
    {
      file: "assets/slides/05-sel-action.png",
      title: "Page 05｜SEL 行動引導：情緒調節三步驟",
      note: "親師共育指引：① 看見與說出情緒、② 暫停一下深呼吸、③ 拆解困難找資源，陪伴孩子建立情商防護罩。"
    },
    {
      file: "assets/slides/06-learning.png",
      title: "Page 06｜自主學習力：從被動監督到自主規劃",
      note: "自主學習核心：自主訂定進度、建立檢核反思、學會時間分配，引導孩子從被催促轉化為自我當責。"
    },
    {
      file: "assets/slides/07-reading-policy.png",
      title: "Page 07｜愛閱家庭推動：臺中市雲端智慧存摺",
      note: "臺中市「愛閱家庭」雲端智慧存摺：115.09.16~10.25 線上申請，每週共讀 3 次、每次 20 分鐘，共創書香家庭。"
    },
    {
      file: "assets/slides/08-taichung-digital-reading.png",
      title: "Page 08｜市府數位閱讀寶庫：國語日報 ＆ Hami 書城",
      note: "臺中市政府全額授權閱讀福利：① 國語日報數位 (https://mdnereading.mdnkids.com/)；② Hami 書城 (https://www.hamibook.com.tw/Homes/book)。萬人同時在線免排隊零等待！"
    },
    {
      file: "assets/slides/09-reading-plan.png",
      title: "Page 09｜親子共訂閱讀計畫：探討專屬書單與學期目標",
      note: "親師生共讀共融：邀請家長與孩子共同探討專屬書單，訂定每日 20 分鐘共讀節奏，透過高層次提問分享，讓閱讀被看見、被肯定。"
    },
    {
      file: "assets/slides/10-reading-ai.png",
      title: "Page 10｜【自主閱讀深耕】AI 雲端閱讀理解認證平台",
      note: "高老師研發創新：運用 Google AI Studio 開發之專屬閱讀認證系統，引導孩子以理解代替死記，用自己的話思考表達。"
    },
    {
      file: "assets/slides/11-gear-novel.png",
      title: "Page 11｜【長篇閱讀深耕】《冒險齒輪》少兒原創小說庫",
      note: "高老師原創開發：專為少兒打造的長篇解謎科幻小說，支援中英即時切換與語音朗讀，引導孩子靜心閱讀長篇文章。"
    },
    {
      file: "assets/slides/12-assessment.png",
      title: "Page 12｜學業成就與多元發展：115 學年度第一學期成績評量辦法",
      note: "601 成績評量重點：兩次定期考日程（期中11/5-6、期末1/12-13）；定期考 50% ＋ 平時 50% 破除一試定江山；英語重視聽力口說、藝能彈性適性多元評量。"
    },
    {
      file: "assets/slides/13-practical-assessment.png",
      title: "Page 13｜跳脫死背，學以致用：六年級跨領域實作評量",
      note: "實作評量核心：培育動手實踐、主動解題、思辨查核能力。全班本年度進行一次實作評量，含 AI 解題、冰棒棍桁架橋、名畫社會顯影三大跨域任務與三軌評量機制。"
    },
    {
      file: "assets/slides/14-digital-wings.png",
      title: "Page 14｜3C 學習哲學：科技是翅膀而非猛獸",
      note: "高老師理念：3C 是數位時代的關鍵翅膀！引導孩子善用科技於查證百科、解題輔助與生活探索，正向賦能。"
    },
    {
      file: "assets/slides/15-digital-discipline.png",
      title: "Page 15｜數位自律公約：親師一致的健康使用準則",
      note: "親師一致約定：屏幕使用每日時限約定、睡前 1 小時手機不進臥室、專注學習時不切換娛樂視窗，建立健康數位習慣。"
    },
    {
      file: "assets/slides/16-health-hygiene.png",
      title: "Page 16｜校園衛教守則：正確洗手與呼吸道禮節",
      note: "校園衛生防護：洗手七字訣（內外夾弓大立腕）搓洗 40 秒、咳嗽噴嚏手肘遮口鼻，共同守護校園衛生。"
    },
    {
      file: "assets/slides/17-health-safety.png",
      title: "Page 17｜校園健康守護：環境通風與發燒休養",
      note: "健康中心叮嚀：對角開窗維持通風；發燒（≥37.5℃）請假在家休養，退燒滿 24 小時再返校，不舒服別硬撐。"
    },
    {
      file: "assets/slides/18-attendance-rules.png",
      title: "Page 18｜請假規範指南：8:30 前通報管道與流程",
      note: "差勤通報準則：每日 8:30 前完成請假通報（LINE 或學校總機 04-26567968 轉 720/724），2日內導師核准。"
    },
    {
      file: "assets/slides/19-attendance-security.png",
      title: "Page 19｜校園安全管理：外出嚴格審核與中輟通報",
      note: "安全出入把關：臨時外出需由家長至警衛室換證接回；未請假達 3 日依法通報中輟，親師聯手守護平安。"
    },
    {
      file: "assets/slides/20-graduation.png",
      title: "Page 20｜六年級專屬盛事：畢旅與畢業紀念冊",
      note: "小學里程碑盛事：兩天一夜畢業旅行鍛鍊獨立自主、畢業紀念冊典藏童年最美笑顏。"
    },
    {
      file: "assets/slides/21-album-quotation.png",
      title: "Page 21｜【畢業專案費用公開】畢業紀念冊規格、攝影與費用預估",
      note: "天藝數位影像報價公開：整本購買每本 870 元（28位專屬頁＋蝴蝶裝完全攤平＋2吋證件照8張與修片QR檔）；僅拍照不購冊每人 250 元工本費。費用透明、滿意再付款。"
    },
    {
      file: "assets/slides/22-election.png",
      title: "Page 22｜班級自治與推選：班親會長與總務幹部",
      note: "推選班親會長（親師溝通代表）與總務幹部（專案經費保管與記帳），熱情邀請熱心家長一同為班級服務！"
    },
    {
      file: "assets/slides/23-finance-pledge.png",
      title: "Page 23｜班級財務透明：高老師的三大透明承諾",
      note: "高老師承諾三大保證：① 專款專用、② 帳目公開透明、③ 總務與導師/會長雙人覆核，每一筆花費清清楚楚。"
    },
    {
      file: "assets/slides/24-committee.png",
      title: "Page 24｜誠摯致謝：114學年度本班家長委員會委員",
      note: "公開感謝本班家長委員無私承擔重任，搭建班級與學校的堅實橋樑，為六年一班孩子爭取最優質資源。"
    },
    {
      file: "assets/slides/25-volunteer.png",
      title: "Page 25｜熱忱招募：115學年度愛心志工隊（交通組／圖書組）",
      note: "學校志工隊招募：「因為有您，孩子的安全更有保障；因為有您，孩子的笑容更加燦爛。」包含交通安全維護與圖書室推廣，歡迎家長填寫回條或向導師報名！"
    },
    {
      file: "assets/slides/26-communication.png",
      title: "Page 26｜親師即時連線：LINE 常態溝通與緊急專線",
      note: "平時日常聯繫請多利用 LINE 留言；遇突發急症或緊急事故，請直接撥打導師專線：0963-159-896。"
    },
    {
      file: "assets/slides/27-message.png",
      title: "Page 27｜給家長的一封信：並肩走一段平穩堅定的路",
      note: "「我們不替孩子走完人生的路，但在他跌倒時，陪伴他勇敢站起來。」感謝家長六年來的悉心灌溉，未來一年親師繼續並肩做神隊友，給孩子展翅的底氣。"
    },
    {
      file: "assets/slides/28-qa.png",
      title: "Page 28｜感謝聆聽與交流時間（Q&A）",
      note: "現場自由提問、班親幹部推選與意見交流。祝各位闔家平安，感謝各位家長對六年一班的溫暖支持！"
    },
    {
      file: "assets/slides/29-reminder.png",
      title: "Page 29｜現場重要提醒：今日親師會三大必辦事項",
      note: "離席前三大叮嚀：① 完成出席簽到表簽名、② 推選確認 601 班親會長與總務幹部、③ 有意願擔任愛心志工的家長登記回條。感謝家長！"
    }
  ];

  let currentIdx = 0;
  const slideImg = document.getElementById("slide-viewer-img");
  const slideTitle = document.getElementById("slide-viewer-title");
  const slideNote = document.getElementById("slide-viewer-note");
  const slideCounter = document.getElementById("slide-counter");
  const prevBtn = document.getElementById("slide-prev");
  const nextBtn = document.getElementById("slide-next");

  function updateSlide(idx) {
    if (idx < 0) idx = 0;
    if (idx >= slides.length) idx = slides.length - 1;
    currentIdx = idx;

    slideImg.src = slides[currentIdx].file;
    slideTitle.textContent = slides[currentIdx].title;
    slideNote.textContent = slides[currentIdx].note;
    slideCounter.textContent = `${currentIdx + 1} / ${slides.length}`;

    prevBtn.disabled = currentIdx === 0;
    nextBtn.disabled = currentIdx === slides.length - 1;
    prevBtn.style.opacity = currentIdx === 0 ? "0.4" : "1";
    nextBtn.style.opacity = currentIdx === slides.length - 1 ? "0.4" : "1";
  }

  if (prevBtn && nextBtn) {
    prevBtn.addEventListener("click", () => updateSlide(currentIdx - 1));
    nextBtn.addEventListener("click", () => updateSlide(currentIdx + 1));

    // Keyboard navigation
    document.addEventListener("keydown", (e) => {
      if (e.key === "ArrowLeft") updateSlide(currentIdx - 1);
      if (e.key === "ArrowRight") updateSlide(currentIdx + 1);
    });

    updateSlide(0);
  }

  // Accordion Logic
  const accordions = document.querySelectorAll(".accordion");
  accordions.forEach((acc) => {
    const header = acc.querySelector(".accordion-header");
    header.addEventListener("click", () => {
      const isActive = acc.classList.contains("active");
      // Close other accordions
      accordions.forEach((other) => other.classList.remove("active"));
      if (!isActive) {
        acc.classList.add("active");
      }
    });
  });
});
