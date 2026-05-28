
import streamlit as st
from datetime import datetime
import random
import json
import os

# ======================
# 保存ファイル
# ======================

SAVE_FILE = "mood_logs.json"

# ======================
# ページ設定
# ======================

st.set_page_config(
    page_title="こころ整理ノート",
    page_icon="🌸",
    layout="centered"
)

# ======================
# CSS
# ======================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(
        135deg,
        #ffe5ec 0%,
        #fff1f5 45%,
        #f8edff 100%
    );

    font-family:
    -apple-system,
    BlinkMacSystemFont,
    "Helvetica Neue",
    sans-serif;
}

/* メインカード */

.main-card {

    background:
    rgba(255,255,255,0.75);

    backdrop-filter: blur(14px);

    padding: 30px;

    border-radius: 32px;

    box-shadow:
    0 20px 60px rgba(255,182,193,0.18);

    margin-bottom: 24px;
}

/* ログカード */

.note-card {

    background:
    rgba(255,255,255,0.85);

    backdrop-filter: blur(12px);

    padding: 22px;

    border-radius: 28px;

    margin-bottom: 18px;

    box-shadow:
    0 10px 30px rgba(255,192,203,0.12);
}

/* ボタン */

.stButton button {

    background:
    linear-gradient(
        135deg,
        #ff8fab,
        #ffb3c6
    );

    color: white;

    border-radius: 999px;

    border: none;

    padding: 12px 24px;

    font-weight: 600;

    transition: 0.3s;
}

.stButton button:hover {

    transform: scale(1.03);

    background:
    linear-gradient(
        135deg,
        #fb6f92,
        #ff8fab
    );

    color: white;
}

/* 入力欄 */

.stTextArea textarea,
.stSelectbox div {

    border-radius: 18px !important;

    border:
    1px solid #ffd6e0 !important;

    background-color:
    rgba(255,255,255,0.8) !important;
}

/* 小文字 */

.small-text {

    color: #8f6f77;

    font-size: 14px;
}

/* タイトル */

h1, h2, h3 {

    color: #5c374c;
}

</style>
""", unsafe_allow_html=True)

# ======================
# ログ読み込み
# ======================

if "logs" not in st.session_state:

    if os.path.exists(SAVE_FILE):

        with open(
            SAVE_FILE,
            "r",
            encoding="utf-8"
        ) as f:

            st.session_state.logs = json.load(f)

    else:

        st.session_state.logs = []

# ======================
# タイトル
# ======================

st.markdown("""
<div class="main-card">

<h1>🌸 こころ整理ノート</h1>

<p>
AIなしで使える、
やさしい気分整理アプリ。
</p>

<p>
今の気分を書いて、
少しだけ心を軽くしよう。
</p>

</div>
""", unsafe_allow_html=True)

# ======================
# 日時
# ======================

today = datetime.today().strftime(
    "%Y-%m-%d %H:%M"
)

# ======================
# 気分選択
# ======================

mood = st.selectbox(
    "今の気分",
    [
        "🙂 普通",
        "😔 しんどい",
        "😵 パンク",
        "🥱 疲れた",
        "🔥 やる気ある",
        "🌙 眠い",
        "🥲 不安"
    ]
)

# ======================
# メモ入力
# ======================

note = st.text_area(
    "今の気持ちを書く",
    placeholder=
    "例：なんか疲れた。やること多いけど動けない。"
)

# ======================
# メッセージ
# ======================

messages = {

    "🙂 普通": [
        "普通の日もちゃんと進んでる。",
        "今日は無理に上げなくてOK。"
    ],

    "😔 しんどい": [
        "しんどい日は小さくしていい。",
        "今日は省エネでOK。"
    ],

    "😵 パンク": [
        "今は減らすのが先。",
        "全部やろうとしなくていい。"
    ],

    "🥱 疲れた": [
        "休むのもタスクです。",
        "今日は5分だけで合格。"
    ],

    "🔥 やる気ある": [
        "今の勢いを使って1個終わらせよう。",
        "小さい達成を作ろう。"
    ],

    "🌙 眠い": [
        "眠い日は判断を減らそう。",
        "まず休む準備をしよう。"
    ],

    "🥲 不安": [
        "不安を書けただけ前進。",
        "今できることだけ考えよう。"
    ]
}

# ======================
# 小さな行動
# ======================

small_actions = [

    "水を飲む",

    "深呼吸を3回する",

    "5分だけ休む",

    "机を1つだけ片付ける",

    "LINEを1件返す",

    "スマホを置いて目を閉じる",

    "洗濯機だけ回す",

    "やることを1個だけ書く"
]

# ======================
# 記録ボタン
# ======================

if st.button("気分を整理する"):

    if note.strip() == "":

        st.warning(
            "少しだけでも書いてみてね"
        )

    else:

        message = random.choice(
            messages[mood]
        )

        action = random.choice(
            small_actions
        )

        log = {

            "日時": today,

            "気分": mood,

            "メモ": note,

            "言葉": message,

            "小さな一歩": action
        }

        st.session_state.logs.append(log)

        # 保存
        with open(
            SAVE_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                st.session_state.logs,
                f,
                ensure_ascii=False,
                indent=2
            )

        st.success("記録したよ🌸")

        st.markdown(f"""
        <div class="note-card">

        <h3>{mood}</h3>

        <p>{message}</p>

        <p class="small-text">
        今できる小さな一歩：
        {action}
        </p>

        </div>
        """, unsafe_allow_html=True)

# ======================
# ログ表示
# ======================

st.divider()

st.subheader("📔 気分ログ")

if len(st.session_state.logs) == 0:

    st.info("まだ記録はありません")

else:

    for log in reversed(
        st.session_state.logs
    ):

        st.markdown(f"""
        <div class="note-card">

        <p class="small-text">
        {log['日時']}
        </p>

        <h3>{log['気分']}</h3>

        <p>{log['メモ']}</p>

        <p class="small-text">
        言葉：
        {log['言葉']}
        </p>

        <p class="small-text">
        小さな一歩：
        {log['小さな一歩']}
        </p>

        </div>
        """, unsafe_allow_html=True)

# ======================
# 全削除
# ======================

if st.button("ログを全部消す"):

    st.session_state.logs = []

    with open(
        SAVE_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump([], f)

    st.rerun()

