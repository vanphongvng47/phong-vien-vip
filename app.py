import streamlit as st
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Cấu hình trang
st.set_page_config(page_title="AI Phóng Viên Pro", layout="wide")

# Sidebar cấu hình
with st.sidebar:
    st.header("⚙️ Hệ thống")
    api_key = st.text_input("Nhập OpenAI API Key", type="password")
    model = st.selectbox("Chọn Model", ["gpt-4o", "gpt-3.5-turbo"])
    temp = st.slider("Độ sáng tạo", 0.0, 1.0, 0.7)

# Giao diện chính
st.title("✍️ AI Phóng Viên: Trợ Lý Tác Nghiệp")

col1, col2 = st.columns(2)

with col1:
    st.subheader("📥 Dữ liệu thô")
    data = st.text_area("Nhập nội dung/số liệu...", height=300)
    style = st.selectbox("Phong cách", ["Tin nhanh", "Phóng sự cảm xúc", "Xã luận"])
    run_btn = st.button("🚀 Chấp bút")

with col2:
    st.subheader("📰 Kết quả")
    if run_btn:
        if not api_key:
            st.error("Thiếu API Key!")
        elif not data:
            st.warning("Hãy nhập dữ liệu!")
        else:
            try:
                # Khởi tạo AI theo chuẩn mới nhất
                llm = ChatOpenAI(model=model, temperature=temp, api_key=api_key)
                prompt = ChatPromptTemplate.from_template("""
                Bạn là một phóng viên chuyên nghiệp viết về {style}.
                Dựa trên dữ liệu: {data}
                Hãy viết một bài báo có tiêu đề, sapo và nội dung hấp dẫn.
                """)
                
                # Chuỗi xử lý (Chain)
                chain = prompt | llm | StrOutputParser()
                
                result = chain.invoke({"style": style, "data": data})
                st.write(result)
                st.download_button("📥 Tải về", result, "bai_viet.txt")
            except Exception as e:
                st.error(f"Lỗi: {str(e)}")g tác và hoạt động đoàn thể.")