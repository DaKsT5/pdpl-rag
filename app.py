import streamlit as st

from v1 import answer, ingest

MAX_QUESTIONS = 10
MAX_CHARS = 300
MAX_TOTAL = 500


@st.cache_resource
def total_counter():
    return {"count": 0}


@st.cache_resource
def prepare_database():
    return ingest()


st.set_page_config(page_title="PDPL RAG", page_icon="⚖️")

st.markdown(
    """
    <style>
    .stApp { direction: rtl; }
    .stTextArea textarea { direction: rtl; text-align: right; }
    [data-testid="stMarkdownContainer"] { text-align: right; }
    </style>
    """,
    unsafe_allow_html=True,
)

try:
    with st.spinner("جارٍ تجهيز قاعدة المواد (أول تشغيل فقط)..."):
        prepare_database()
except Exception:
    st.error("تعذّر تجهيز قاعدة المواد. حاول لاحقاً.")
    st.stop()

st.title("مساعد نظام حماية البيانات الشخصية")
st.caption("معلومات مستمدة من نص نظام حماية البيانات الشخصية السعودي (النسخة المعدّلة)، وليست استشارة قانونية.")
st.caption("الأجوبة مولّدة بالذكاء الاصطناعي من نص النظام، وقد تحتوي على أخطاء. راجع النص الرسمي للتأكد.")

if "asked" not in st.session_state:
    st.session_state.asked = 0

counter = total_counter()
question = st.text_area("اكتب سؤالك عن النظام", max_chars=MAX_CHARS, height=110)

if st.button("اسأل") and question.strip():
    if st.session_state.asked >= MAX_QUESTIONS:
        st.warning("انتهت أسئلة هذه الجلسة. شكراً لتجربتك.")
    elif counter["count"] >= MAX_TOTAL:
        st.warning("وصلت التجربة إلى الحد الأقصى من الأسئلة حالياً.")
    else:
        st.session_state.asked += 1
        counter["count"] += 1
        try:
            with st.spinner("جارٍ البحث في مواد النظام..."):
                result = answer(question.strip())

            if result["refused"]:
                st.error(result["answer"])
            else:
                st.success(result["answer"])
                with st.expander("المواد التي استرجعها النظام (أقرب 3 مواد للسؤال)"):
                    st.caption("الاستشهاد الدقيق (المادة والفقرة) موجود في نص الجواب أعلاه، وهذه المواد التي اطّلع عليها النموذج.")
                    for article_no in result["sources"]:
                        st.write(f"المادة رقم {article_no}")
        except Exception:
            st.warning("تعذّر الحصول على جواب حالياً. ربما انتهى رصيد التجربة، حاول لاحقاً.")

st.caption(f"الأسئلة المتبقية في هذه الجلسة: {MAX_QUESTIONS - st.session_state.asked}")