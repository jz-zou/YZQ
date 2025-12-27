import streamlit as st
import time
from datetime import datetime
import streamlit as st
import time
from datetime import datetime


import os
import streamlit as st
# 获取当前文件的绝对路径
current_dir = os.path.dirname(os.path.abspath(__file__))


st.set_page_config(
    page_title='To you',
    page_icon='🎶',
    layout="centered",
    initial_sidebar_state="collapsed"
)

songs_data = [
    {
        "id": 1,
        "name": "我成为我的同时",
        "artist": "十个勤天",
        "lyric":"“亲爱的你 别担心 世界先给你 一场雨 肯定是想送你 天晴”",
        "cover": os.path.join(current_dir, "assets/covers/song1.jpg"),  # 改为绝对路径
        "clip": os.path.join(current_dir, "assets/clips/song1_clip.mp3"),
        "full": os.path.join(current_dir, "assets/fulls/song1_full.mp3"),
        "description": "第一首神秘歌曲片段"
    },
    {
        "id": 2,
        "name": "DOU(live)",
        "artist": "黄子弘凡",
        "lyric":"“I promise I love U”",
        "cover": os.path.join(current_dir, "assets/covers/song2.jpg"),  # 改为绝对路径
        "clip": os.path.join(current_dir, "assets/clips/song2_clip.mp3"),
        "full": os.path.join(current_dir, "assets/fulls/song2_full.mp3"),
        "description": "第二首神秘歌曲片段"
    },
    {
        "id": 3,
        "name": "云裳羽衣曲",
        "artist": "周深",
        "lyric":"“故事鲜艳”",
        "cover": os.path.join(current_dir, "assets/covers/song3.jpg"),  # 改为绝对路径
        "clip": os.path.join(current_dir, "assets/clips/song3_clip.mp3"),
        "full": os.path.join(current_dir, "assets/fulls/song3_full.mp3"),
        "description": "第三首神秘歌曲片段"
    },
    {
        "id": 4,
        "name": "匿名的好友",
        "artist": "en",
        "lyric":"“也许我们当时年纪真的太小”",
        "cover": os.path.join(current_dir, "assets/covers/song4.jpg"),  # 改为绝对路径
        "clip": os.path.join(current_dir, "assets/clips/song4_clip.mp3"),
        "full": os.path.join(current_dir, "assets/fulls/song4_full.mp3"),
        "description": "第四首神秘歌曲片段"
    },
    {
        "id": 5,
        "name": "一定有人爱着你",
        "artist": "胡夏",
        "lyric":"“请记得一定有人爱着你”",
        "cover": os.path.join(current_dir, "assets/covers/song5.jpg"),  # 改为绝对路径
        "clip": os.path.join(current_dir, "assets/clips/song5_clip.mp3"),
        "full": os.path.join(current_dir, "assets/fulls/song5_full.mp3"),
        "description": "第五首神秘歌曲片段"
    },
    {
        "id": 6,
        "name": "去见你想见的人",
        "artist": "哈口HaKo",
        "lyric":"“去见你想见的人 过你想过的人生”",
        "cover": os.path.join(current_dir, "assets/covers/song6.jpg"),  # 改为绝对路径
        "clip": os.path.join(current_dir, "assets/clips/song6_clip.mp3"),
        "full": os.path.join(current_dir, "assets/fulls/song6_full.mp3"),
        "description": "第六首神秘歌曲片段"
    },
    {
        "id": 7,
        "name": "你是我的风景",
        "artist": "陈冰、赵磊",
        "lyric":"“让心自然的休息”",
        "cover": os.path.join(current_dir, "assets/covers/song7.jpg"),  # 改为绝对路径
        "clip": os.path.join(current_dir, "assets/clips/song7_clip.mp3"),
        "full": os.path.join(current_dir, "assets/fulls/song7_full.mp3"),
        "description": "第七首神秘歌曲片段"
    },
    {
        "id": 8,
        "name": "拉过钩的",
        "artist": "陆虎",
        "lyric":"“一些些散落的 曾经美好的画面”",
        "cover": os.path.join(current_dir, "assets/covers/song8.jpg"),  # 改为绝对路径
        "clip": os.path.join(current_dir, "assets/clips/song8_clip.mp3"),
        "full": os.path.join(current_dir, "assets/fulls/song8_full.mp3"),
        "description": "第八首神秘歌曲片段"
    },
    {
        "id": 9,
        "name": "同手同脚",
        "artist": "井迪、井胧",
        "lyric":"“依然清晰 回忆里那些曾经有笑有泪的光阴”",
        "cover": os.path.join(current_dir, "assets/covers/song9.jpg"),  # 改为绝对路径
        "clip": os.path.join(current_dir, "assets/clips/song9_clip.mp3"),
        "full": os.path.join(current_dir, "assets/fulls/song9_full.mp3"),
        "description": "第九首神秘歌曲片段"
    },
    {
        "id": 10,
        "name": "同手同脚",
        "artist": "🐟",
        "lyric":"“现在我唱的这首歌曲”",
        "cover": os.path.join(current_dir, "assets/covers/song10.jpg"),  # 改为绝对路径
        "clip": os.path.join(current_dir, "assets/clips/song10_clip.mp3"),
        #"full": os.path.join(current_dir, "assets/fulls/song10_full.mp3"),
        "description": "第十首神秘歌曲片段"
    }
]

# st.header("Ymal Zfaire Qdrame")
# st.header("😈🐟️の低语")
# 自定义CSS样式
st.markdown("""
<style>
    /* 登录页面样式 */
    .login-container {
        max-width: 400px;
        margin: 0 auto;
        padding: 40px 30px;
        border-radius: 15px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        background: white;
        margin-top: 30px;
        border: 2px solid #e0e0e0;
    }
    .platform-name {
        text-align: center;
        font-family: 'Arial', sans-serif;
        font-size: 32px;
        font-weight: 900;
        color: #1a1a2e;
        margin-bottom: 40px;
        letter-spacing: 3px;
        text-transform: uppercase;
    }
    .input-field {
        margin-bottom: 20px;
    }
    .input-field input {
        width: 100%;
        padding: 12px 15px;
        border: 1px solid #ddd;
        border-radius: 8px;
        font-size: 16px;
        transition: border-color 0.3s;
    }
    .input-field input:focus {
        outline: none;
        border-color: #667eea;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.1);
    }
    .login-btn {
        width: 100%;
        padding: 14px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 8px;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
        transition: transform 0.3s;
    }
    .login-btn:hover {
        transform: translateY(-2px);
        box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
    }
    .register-link {
        text-align: center;
        margin-top: 20px;
        font-size: 14px;
    }
    .register-link a {
        color: #667eea;
        text-decoration: none;
        font-weight: 500;
    }
    
    /* 注册页面样式 */
    .register-container {
        max-width: 400px;
        margin: 0 auto;
        padding: 30px;
        border-radius: 15px;
        background: white;
        box-shadow: 0 10px 30px rgba(0,0,0,0.1);
        margin-top: 30px;
        border: 2px solid #e0e0e0;
    }
    .verification-btn {
        background: linear-gradient(135deg, #4facfe 0%, #00f2fe 100%);
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 6px;
        cursor: pointer;
        font-size: 14px;
        transition: all 0.3s;
    }
    .verification-btn:hover {
        transform: scale(1.05);
    }
    .verification-btn:disabled {
        background: #cccccc;
        cursor: not-allowed;
    }
    
    /* 恶作剧页面样式 */
    .trick-container {
        text-align: center;
        padding: 50px 20px;
    }
    .trick-image {
        max-width: 300px;
        border-radius: 20px;
        margin: 30px auto;
        box-shadow: 0 10px 30px rgba(0,0,0,0.2);
        animation: float 3s ease-in-out infinite;
    }
    @keyframes float {
        0%, 100% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
    }
    .trick-text {
        font-size: 28px;
        font-weight: bold;
        margin: 30px 0;
        color: #ff6b6b;
    }
    .next-btn {
        padding: 15px 40px;
        background: linear-gradient(135deg, #43e97b 0%, #38f9d7 100%);
        color: white;
        border: none;
        border-radius: 50px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        margin: 20px auto;
        transition: all 0.3s;
    }
    .next-btn:hover {
        transform: scale(1.1);
        box-shadow: 0 10px 20px rgba(67, 233, 123, 0.3);
    }
    
    /* 隐藏Streamlit默认元素 */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .st-emotion-cache-1dp5vir {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# 初始化会话状态
if 'page' not in st.session_state:
    st.session_state.page = "login"  # login, register, trick1, trick2
    st.session_state.verification_count = 0
    st.session_state.countdown = 60

# 登录页面修正
def show_login_page():
    # ... [前面的代码保持不变] ...
    st.header("Ymal zfaireqdrame")
    st.markdown("### 🔐 登录到您的账户")
    
    # 登录表单
    with st.form("login_form", clear_on_submit=True):
        username = st.text_input("账号", 
                                placeholder="请输入您的账号", 
                                key="login_username")
        password = st.text_input("密码", 
                                type="password", 
                                placeholder="请输入您的密码", 
                                key="login_password")
        
        # === 必须使用 form_submit_button ===
        login_submitted = st.form_submit_button("登录", 
                                               use_container_width=True, 
                                               type="primary")
        
        if login_submitted:  # 注意：变量名已修改
            if username and password:
                st.error("❌ 账号或密码错误，请重试")
                st.info("提示：若未有账号，您可以点击下面的注册按钮")
            else:
                st.warning("⚠️ 请输入账号和密码")
    
    # ... [后面的代码保持不变] ...    
    # 注册链接
    st.markdown('<div class="register-link">', unsafe_allow_html=True)
    if st.button("📝 未有账号？立即注册", key="go_to_register"):
        st.session_state.page = "register"
        st.rerun()
    
    # 忘记密码链接
    st.markdown('<div style="text-align: center; margin-top: 15px;">', unsafe_allow_html=True)
    if st.button("🔓 忘记密码？", key="forgot_password"):
        st.info("请联系系统管理员重置密码")
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # 平台说明
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; font-size: 12px; margin-top: 40px;">
        <p>Ymal zfaire qdrame - 让数字生活更简单</p>
        <p>© 2025 YZQ Technologies. 保留所有权利。</p>
        <p style="font-size: 10px; margin-top: 10px;">版本号：v2.1.4 | 最后更新：2025-05-02</p>
    </div>
    """, unsafe_allow_html=True)

# 注册页面 - 完全修正版本
def show_register_page():
    st.header("Ymal zfaireqdrame")
    st.markdown("### 📱 创建新账户")
    st.markdown("请填写以下信息完成注册")
    
    # 显示点击次数（放在顶部）
    #if st.session_state.verification_count > 0:
        #st.caption(f"📱 已尝试获取验证码 {st.session_state.verification_count} 次")
    
    # === 1. 验证码部分：完全在表单外 ===
    col_ver1, col_ver2 = st.columns([2, 1])
    with col_ver1:
        verification_code = st.text_input("验证码", 
                                         placeholder="请输入6位验证码", 
                                         max_chars=6,
                                         key="verification_code_input")
    
    with col_ver2:
        st.markdown("<br>", unsafe_allow_html=True)
        # 独立的按钮，不在任何表单内
        if st.button("获取验证码", 
                    key="get_verification_code", 
                    type="secondary",
                    use_container_width=True):
            st.session_state.verification_count += 1
            
            if st.session_state.verification_count == 1:
                st.success("✅ 验证码已发送至您的手机，请注意查收")
                st.info("💡 提示：再点一次试试？")
                st.rerun()  # 立即刷新显示次数
            elif st.session_state.verification_count >= 2:
                st.session_state.page = "trick1"
                st.rerun()
    
    # === 2. 注册表单：只包含需要提交的字段 ===
    with st.form("register_form", clear_on_submit=True):
        username = st.text_input("用户名", 
                                placeholder="请输入您的用户名", 
                                help="建议使用字母和数字组合")
        
        phone = st.text_input("手机号码", 
                             placeholder="请输入11位手机号码", 
                             max_chars=11,
                             help="请输入有效的手机号码")
        
        password = st.text_input("密码", 
                                type="password", 
                                placeholder="请输入密码（6-20位）", 
                                help="建议使用字母、数字和特殊字符组合")
        
        confirm_password = st.text_input("确认密码", 
                                        type="password", 
                                        placeholder="请再次输入密码")
        
        agree = st.checkbox("我已阅读并同意《用户服务协议》和《隐私政策》")
        
        # === 必须在表单内使用 form_submit_button ===
        submitted = st.form_submit_button("立即注册", 
                                         type="primary", 
                                         use_container_width=True)
        
        if submitted:
            # 表单提交后的验证逻辑
            if not all([username, phone, password, confirm_password, verification_code]):
                st.warning("⚠️ 请填写所有必填信息")
            elif password != confirm_password:
                st.error("❌ 两次输入的密码不一致")
            elif not agree:
                st.warning("⚠️ 请阅读并同意用户协议")
            elif len(phone) != 11:
                st.error("❌ 请输入有效的11位手机号码")
            elif len(verification_code) != 6:
                st.error("❌ 请输入6位验证码")
            else:
                with st.spinner("正在注册中..."):
                    time.sleep(2)
                st.success("🎉 注册成功！")
                # 可以在这里添加跳转到登录页面的逻辑
                # time.sleep(2)
                # st.session_state.page = "login"
                # st.rerun()
    
    # === 3. 返回登录按钮（表单外） ===
    st.markdown("---")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("⬅️ 返回登录", 
                    key="back_to_login", 
                    use_container_width=True):
            st.session_state.page = "login"
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

# 恶作剧页面1
def show_trick_page1():
    st.markdown('<div class="trick-container">', unsafe_allow_html=True)
    
    st.markdown('<div class="trick-text">🎭 嘿嘿，骗你哒！</div>', unsafe_allow_html=True)
    
    # 恶作剧表情包图片
    st.markdown("""
    <div style="font-size: 100px; text-align: center; margin: 20px 0;">
        😜
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="font-size: 20px; color: #555; margin: 30px 0; padding: 20px; background: #fff9e6; border-radius: 15px; border-left: 5px solid #ffcc00;">
        <p><strong>解密时刻！🔍</strong></p>
        <p><strong>Ymal zfaire qdrame</strong> 其实是：</p>
        <p><span style="color: #ff6b6b; font-size: 24px;">Y</span>ZQ + <span style="color: #ff6b6b;">mal</span> + <span style="color: #ff6b6b;">faire</span> + <span style="color: #ff6b6b;">drame</span></p>
        <p>翻译过来就是：<strong>"YZQ的恶作剧"</strong>！</p>
        <p style="font-size: 16px; margin-top: 15px; color: #777;">🎯 <em>法语小课堂：mal = 恶，faire = 作，drame = 剧</em></p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: center; margin-top: 40px;">
        <p style="font-size: 18px; color: #333;">汝是否觉得疑惑？😄</p>
        <p style="font-size: 16px; color: #666;">莫疑惑，接下来正式开始！</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Next按钮
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎬 进入下一页", key="next_to_trick2", use_container_width=True):
            st.session_state.page = "trick2"
            st.rerun()

# 恶作剧页面2
def show_trick_page2():
    st.markdown('<div class="trick-container">', unsafe_allow_html=True)
    
    st.markdown('<div class="trick-text">🎉 惊喜正式开始！</div>', unsafe_allow_html=True)
    
    # 生日蛋糕图片
    st.markdown("""
    <div style="font-size: 100px; text-align: center; margin: 20px 0;">
        🎂
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="font-size: 22px; color: #333; margin: 30px 0; padding: 25px; background: linear-gradient(135deg, #fdfcfb 0%, #e2d1c3 100%); border-radius: 20px; border: 2px dashed #ff9a9e;">
        <p>Oh dear 佑：</p>
        <p style="margin: 15px 0;">刚才的恶作剧成功了吗？😏</p>
        <p>接下来，为你准备了一份特别的</p>
        <p style="color: #ff6b6b; font-size: 28px; font-weight: bold; margin: 10px 0;">🎁 礼物 🎁</p>
        <p>莫让小生逮到汝翻白眼了哟😈</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 倒计时效果
    with st.empty():
        for i in range(3, 0, -1):
            st.markdown(f"""
            <div style="text-align: center; font-size: 48px; color: #ff6b6b; margin: 20px 0;">
                {i}...
            </div>
            """, unsafe_allow_html=True)
            time.sleep(1)
    
    st.markdown("""
    <div style="text-align: center; margin-top: 40px;">
        <p style="font-size: 18px; color: #555;">准备好了吗？点击下面的按钮开始！</p>
    </div>
    """, unsafe_allow_html=True)
    
    # 开始按钮
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 我准备好啦！", key="start_main", use_container_width=True):
            st.success("✨ 即将进入主页面...")
            time.sleep(1)
            # 这里可以跳转到主页面
            st.session_state.page = "weather_question"
            st.rerun()
    
    st.markdown('</div>', unsafe_allow_html=True)

#第二部分
# ==================== 主页面问答部分 ====================

# 问答页面1：天气问题
def show_weather_question():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 40px;">
        <h1 style="color: #1a1a2e; font-size: 36px;">👿🐟の低语</h1>
        <div style="font-size: 24px; margin: 20px 0;">问题一</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #a8edea 0%, #fed6e3 100%); 
                padding: 40px; 
                border-radius: 20px; 
                margin: 20px 0;
                text-align: center;
                box-shadow: 0 10px 30px rgba(168, 237, 234, 0.3);">
        <h2 style="color: #2c3e50; font-size: 28px;">🌤️ 今天的天气怎么样？</h2>
        <p style="font-size: 18px; color: #34495e; margin-top: 15px;">
        请选择最符合的天气：
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 三个选项按钮
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("☀️ 晴空万里", key="sunny", use_container_width=True):
            st.session_state.weather_answer = "sunny"
            st.session_state.page = "weather_response_sunny"
            st.rerun()
    
    with col2:
        if st.button("☁️ 多云", key="cloudy", use_container_width=True):
            st.session_state.weather_answer = "cloudy"
            st.session_state.page = "weather_response_cloudy"
            st.rerun()
    
    with col3:
        if st.button("🌧️ 雨天", key="rainy", use_container_width=True):
            st.session_state.weather_answer = "rainy"
            st.session_state.page = "weather_response_rainy"
            st.rerun()

# 天气回答页面 - 晴空万里
def show_weather_response_sunny():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 40px;">
        <h1 style="color: #1a1a2e; font-size: 36px;">👿🐟の低语</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FFD700 0%, #FFA500 100%); 
                padding: 40px; 
                border-radius: 20px; 
                margin: 20px 0;
                text-align: center;
                animation: glow 2s infinite alternate;">
        <h2 style="color: #ffffff; font-size: 32px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
        ☀️ 像汝的笑容一样灿烂！</h2>
        <p style="font-size: 20px; color: #fff; margin-top: 20px; line-height: 1.6;">
        阳光正好，微风不燥<br>
        愿你的每一天都如晴空般明朗，心情永远阳光普照
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 继续按钮
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ 继续", key="continue_from_sunny", use_container_width=True):
            st.session_state.page = "memory_question"
            st.rerun()

# 天气回答页面 - 多云
def show_weather_response_cloudy():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 40px;">
        <h1 style="color: #1a1a2e; font-size: 36px;">👿🐟の低语</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #B0C4DE 0%, #DCDCDC 100%); 
                padding: 40px; 
                border-radius: 20px; 
                margin: 20px 0;
                text-align: center;">
        <h2 style="color: #2c3e50; font-size: 32px;">☁️ 像我们的关系一样柔软！</h2>
        <p style="font-size: 20px; color: #34495e; margin-top: 20px; line-height: 1.6;">
        云朵变幻，却始终温柔。<br>
        就像我们，时而靠近时而疏远，<br>
        但那份柔软与包容始终如一。
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 继续按钮
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ 继续", key="continue_from_cloudy", use_container_width=True):
            st.session_state.page = "memory_question"
            st.rerun()

# 天气回答页面 - 雨天
def show_weather_response_rainy():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 40px;">
        <h1 style="color: #1a1a2e; font-size: 36px;">👿🐟の低语</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4682B4 0%, #87CEEB 100%); 
                padding: 40px; 
                border-radius: 20px; 
                margin: 20px 0;
                text-align: center;">
        <h2 style="color: #ffffff; font-size: 32px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
        🌧️ 如小生的思念一般绵长！</h2>
        <p style="font-size: 20px; color: #fff; margin-top: 20px; line-height: 1.6;">
        雨丝如思念，连绵不绝，<br>
        每一滴雨都是想对你说的话，<br>
        汇聚成时光的长河，润物无声。
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 继续按钮
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("✨ 继续", key="continue_from_rainy", use_container_width=True):
            st.session_state.page = "memory_question"
            st.rerun()

# 问答页面2：记忆问题
def show_memory_question():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 40px;">
        <h1 style="color: #1a1a2e; font-size: 36px;">👿🐟の低语</h1>
        <div style="font-size: 24px; margin: 20px 0;">问题二</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #DDA0DD 0%, #EE82EE 100%); 
                padding: 40px; 
                border-radius: 20px; 
                margin: 20px 0;
                text-align: center;
                box-shadow: 0 10px 30px rgba(221, 160, 221, 0.3);">
        <h2 style="color: #4B0082; font-size: 28px;">💭 猜猜我记忆中关于我们快乐的美好时刻有多少？</h2>
        <p style="font-size: 18px; color: #8A2BE2; margin-top: 15px;">
        选择一个你认为最接近的数字：
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 三个选项按钮
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🤔 > 5", key="more_than_5", use_container_width=True):
            st.session_state.page = "memory_response"
            st.rerun()
    
    with col2:
        if st.button("🤯 > 10", key="more_than_10", use_container_width=True):
            st.session_state.page = "memory_response"
            st.rerun()
    
    with col3:
        if st.button("🤩 > 15", key="more_than_15", use_container_width=True):
            st.session_state.page = "memory_response"
            st.rerun()

# 修改记忆回答页面函数
def show_memory_response():
    html_content = """
    <div style="text-align: center; margin-bottom: 40px;">
        <h1 style="color: #1a1a2e; font-size: 36px;">👿🐟の低语</h1>
    </div>
    
    <div style="background: linear-gradient(135deg, #FFE4E1 0%, #FFF0F5 100%); 
                padding: 40px; 
                border-radius: 20px; 
                margin: 20px 0;
                text-align: center;
                border: 2px dashed #FF69B4;">
        <h2 style="color: #DB7093; font-size: 30px;">🤔 其实我也不知道...</h2>
        <p style="font-size: 20px; color: #C71585; margin-top: 20px; line-height: 1.6;">
        没坚持认真想完，但不少于15。<br>
        PS：最初打算让豆老师帮我重现的，<br>
        但豆老师着实勤奋又蠢笨，故而未能实现。
        </p>
        
    </div>
    
    <br><br>
    """
    
    st.markdown(html_content, unsafe_allow_html=True)
    
    # 按钮部分
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎭 继续", key="continue_to_rambling", use_container_width=True):
            st.session_state.page = "rambling_page"
            st.rerun()

# 修改胡言乱语页面函数
def show_rambling_page():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 40px;">
        <h1 style="color: #1a1a2e; font-size: 36px;">👿🐟の低语</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #4682B4 0%, #87CEEB 100%); 
                padding: 40px; 
                border-radius: 20px; 
                margin: 20px 0;
                text-align: center;">
        <h2 style="color: #ffffff; font-size: 32px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
        🗣️ 小生の胡言乱语</h2>
        <p style="font-size: 20px; color: #fff; margin-top: 20px; line-height: 1.6;">
        小生的设计逻辑太乱了，不管了硬接<br>
        汝听歌否？小生请汝听vip歌曲，<br>
        姑娘谨记，切不可外传，小生可是豁出去的
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    
    
    # 继续按钮
    st.markdown("<br><br>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎵 继续听歌", key="continue_to_song", use_container_width=True):
            st.session_state.page = "music_page"  # 后续可以接音乐页面
            st.rerun()

# 音乐页面（占位，后续可以添加音频播放）
def show_music_page():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 40px;">
        <h1 style="color: #1a1a2e; font-size: 36px;">👿🐟の低语</h1>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="background: linear-gradient(135deg, #8A2BE2 0%, #4B0082 100%); 
                padding: 40px; 
                border-radius: 20px; 
                margin: 20px 0;
                text-align: center;
                box-shadow: 0 10px 30px rgba(138, 43, 226, 0.3);">
        <h2 style="color: white; font-size: 32px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
        🎵 歌曲片段盲盒 🎵</h2>
        <p style="font-size: 20px; color: #E6E6FA; margin-top: 20px; line-height: 1.6;">
        此处有10个神秘的音乐片段盲盒<br>
        每个片段都是一首歌的精华部分<br>
        汝可能猜出为何首歌否？<br>
        ⚠️ ps：戴上耳机效果更佳<br>
           pps：若是蓝牙耳机需戴上两个效果更佳<br>
           ppps：汝也可外放，但不建议
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 创建10个音乐盲盒 - 第一行
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        if st.button("🎁 #1", key="song_box_1", use_container_width=True):
            st.session_state.current_song = 1
            st.session_state.page = "song_player"
            st.rerun()
    
    with col2:
        if st.button("🎁 #2", key="song_box_2", use_container_width=True):
            st.session_state.current_song = 2
            st.session_state.page = "song_player"
            st.rerun()
    
    with col3:
        if st.button("🎁 #3", key="song_box_3", use_container_width=True):
            st.session_state.current_song = 3
            st.session_state.page = "song_player"
            st.rerun()
    
    with col4:
        if st.button("🎁 #4", key="song_box_4", use_container_width=True):
            st.session_state.current_song = 4
            st.session_state.page = "song_player"
            st.rerun()
    
    with col5:
        if st.button("🎁 #5", key="song_box_5", use_container_width=True):
            st.session_state.current_song = 5
            st.session_state.page = "song_player"
            st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 第二行
    col6, col7, col8, col9, col10 = st.columns(5)
    
    with col6:
        if st.button("🎁 #6", key="song_box_6", use_container_width=True):
            st.session_state.current_song = 6
            st.session_state.page = "song_player"
            st.rerun()
    
    with col7:
        if st.button("🎁 #7", key="song_box_7", use_container_width=True):
            st.session_state.current_song = 7
            st.session_state.page = "song_player"
            st.rerun()
    
    with col8:
        if st.button("🎁 #8", key="song_box_8", use_container_width=True):
            st.session_state.current_song = 8
            st.session_state.page = "song_player"
            st.rerun()
    
    with col9:
        if st.button("🎁 #9", key="song_box_9", use_container_width=True):
            st.session_state.current_song = 9
            st.session_state.page = "song_player"
            st.rerun()
    
    with col10:
        if st.button("🎁 #10", key="song_box_10", use_container_width=True):
            st.session_state.current_song = 10
            st.session_state.page = "song_player"
            st.rerun()
    
    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # 返回按钮
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🔙 返回", key="back_from_music", use_container_width=True):
            st.session_state.page = "rambling_page"
            st.rerun()


def show_song_player():
    # 获取当前歌曲
    song_index = st.session_state.get('current_song', 1) - 1
    song = songs_data[song_index]
    
    # 初始化状态
    if 'song_revealed' not in st.session_state:
        st.session_state.song_revealed = False
    if 'full_played' not in st.session_state:
        st.session_state.full_played = False
    if 'cover_revealed' not in st.session_state:
        st.session_state.cover_revealed = False
    
    st.markdown("""
    <div style="text-align: center; margin-bottom: 40px;">
        <h1 style="color: #1a1a2e; font-size: 36px;">👿🐟の低语</h1>
    </div>
    """, unsafe_allow_html=True)
    
    # 盲盒提示
    st.markdown(f"""
    <div style="background: linear-gradient(135deg, #FF6B6B 0%, #FF8E53 100%); 
                padding: 30px; 
                border-radius: 20px; 
                margin: 20px 0;
                text-align: center;">
        <h2 style="color: white; font-size: 28px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
        🎵 盲盒 #{song_index + 1} - 歌曲片段</h2>
        <p style="font-size: 18px; color: #FFF5EE; margin-top: 15px;">
        ⬇️ 请仔细聆听这段神秘片段 ⬇️
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 播放歌曲片段
    st.markdown("""
    <div style="text-align: center; margin: 20px 0;">
        <h3 style="color: #2c3e50; font-size: 24px; margin-bottom: 15px;">
        🎧 神秘片段（仔细听哦~）
        </h3>
    </div>
    """, unsafe_allow_html=True)
    
    # 播放片段
    try:
        if 'clip' in song and song['clip']:
            audio_file = open(song['clip'], 'rb')
            audio_bytes = audio_file.read()
            
            # 使用Streamlit的音频播放器
            st.audio(audio_bytes, format='audio/mp3')
            
            # 片段提示
            st.info(f"💡 {song['description']}")
        else:
            st.warning("⚠️ 此歌曲片段暂不可用")
            
    except FileNotFoundError:
        st.error(f"❌ 片段文件未找到：{song.get('clip', '未指定')}")
        st.info("请确保音频文件已放置在正确路径")
    except Exception as e:
        st.error(f"❌ 播放错误：{str(e)}")
    
    st.markdown("---")
    
    # 猜歌区域
    if not st.session_state.song_revealed:
        # 猜歌按钮
        st.markdown("""
        <div style="text-align: center; margin: 30px 0;">
            <p style="font-size: 20px; color: #333; margin-bottom: 15px;">
            🎯 听出来是哪首歌了吗？
            </p>
            <p style="font-size: 16px; color: #666; margin-bottom: 25px;">
            猜对猜错都没关系，重要的是感受音乐~
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔍 揭秘歌曲名称", key="reveal_song", use_container_width=True):
                st.session_state.song_revealed = True
                st.rerun()
    else:
        # 显示歌曲信息
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                    padding: 30px; 
                    border-radius: 20px; 
                    margin: 20px 0;
                    text-align: center;
                    animation: fadeIn 1s;">
            <h2 style="color: white; font-size: 32px; margin-bottom: 10px;">🎉 歌曲揭秘！</h2>
            <p style="font-size: 28px; color: #FFD700; font-weight: bold; margin: 10px 0;">
            {song['name']}
            </p>
            <p style="font-size: 20px; color: #E6E6FA; margin-top: 10px;">
            演唱：{song['artist']}
            </p>
            <p style="font-size: 20px; color: #E6E6FA; margin-top: 10px;font-style: italic;font-weight: bold;font-family: 'Comic Sans MS', '楷体', cursive;">
            {song['lyric']}
            </p>
        </div>
        """, unsafe_allow_html=True)
        
        # 播放完整版按钮和查看封面按钮
        col1, col2, col3 = st.columns(3)
        
        with col1:
            if not st.session_state.full_played:
                if st.button("🎵 播放完整版", key="play_full", use_container_width=True):
                    st.session_state.full_played = True
                    st.rerun()
            else:
                # 播放完整版音乐
                st.markdown("""
                <div style="text-align: center; margin: 20px 0;">
                    <h4 style="color: #2c3e50; font-size: 20px; margin-bottom: 15px;">
                    🎶 完整版歌曲
                    </h4>
                </div>
                """, unsafe_allow_html=True)
                
                if st.session_state.current_song == 10:
                    
                    st.markdown("""
                    <div style="text-align: center; padding: 30px; 
                                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); 
                                border-radius: 20px; margin: 20px 0;">
                        <h3 style="color: white; font-size: 32px; text-shadow: 2px 2px 4px rgba(0,0,0,0.3);">
                        嘿嘿 还没有呢
                        </h3>
                        <p style="font-size: 18px; color: #E6E6FA; margin-top: 15px;">
                        但还有🐟︎的碎碎念
                        </p>
                    </div>
                    """, unsafe_allow_html=True)
                    st.markdown("<br>", unsafe_allow_html=True)
                    col1, col2, col3 = st.columns([1, 2, 1])
                    with col2:
                        if st.button("💌 看看小生的碎碎念", key="to_chatting", use_container_width=True):
                            st.session_state.page = "chatting_page"
                            st.rerun()
                    
                else:
                    try:
                        if 'full' in song and song['full']:
                            full_audio_file = open(song['full'], 'rb')
                            full_audio_bytes = full_audio_file.read()
                    
                            # 完整版播放器
                            st.audio(full_audio_bytes, format='audio/mp3')
                        else:
                            st.warning("⚠️ 完整版歌曲暂不可用")
                    except FileNotFoundError:
                        st.error(f"❌ 完整版文件找不到")
                    except Exception as e:
                        st.error(f"❌ 完整版播放错误：{str(e)}")
        
        with col2:
            if not st.session_state.cover_revealed:
                if st.button("🖼️ 查看封面", key="reveal_cover", use_container_width=True):
                    st.session_state.cover_revealed = True
                    st.rerun()
            else:
                # 显示封面
                st.markdown("""
                <div style="text-align: center;">
                    <h4 style="color: #2c3e50; font-size: 20px; margin-bottom: 15px;">
                    🎨 歌曲封面
                    </h4>
                </div>
                """, unsafe_allow_html=True)
                
                try:
                    if 'cover' in song and song['cover']:
                        st.image(song['cover'], 
                                caption=f"{song['name']} - {song['artist']}",
                                width=200,
                                use_container_width=False)
                    else:
                        st.warning("⚠️ 此歌曲暂无封面")
                except FileNotFoundError:
                    st.error(f"❌ 封面图片未找到")
                except Exception as e:
                    st.error(f"❌ 图片加载错误：{str(e)}")
        
        with col3:
            if st.button("🔄 重猜", key="re_guess", use_container_width=True):
                st.session_state.song_revealed = False
                st.session_state.full_played = False
                st.session_state.cover_revealed = False
                st.rerun()
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # 控制按钮区域
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        if st.button("⬅️ 上一首", key="prev_song", use_container_width=True):
            if st.session_state.current_song > 1:
                st.session_state.current_song -= 1
                st.session_state.song_revealed = False
                st.session_state.full_played = False
                st.session_state.cover_revealed = False
                st.rerun()
            else:
                st.warning("已经是第一首歌了")
    
    with col2:
        if st.button("🎵 重新盲选", key="back_to_boxes", use_container_width=True):
            st.session_state.page = "music_page"
            st.session_state.song_revealed = False
            st.session_state.full_played = False
            st.session_state.cover_revealed = False
            st.rerun()
    
    with col3:
        if st.button("🔁 重听片段", key="replay_clip", use_container_width=True):
            st.session_state.song_revealed = False
            st.session_state.full_played = False
            st.session_state.cover_revealed = False
            st.rerun()
    
    with col4:
        if st.button("➡️ 下一首", key="next_song", use_container_width=True):
            if st.session_state.current_song < len(songs_data):
                st.session_state.current_song += 1
                st.session_state.song_revealed = False
                st.session_state.full_played = False
                st.session_state.cover_revealed = False
                st.rerun()
            else:
                st.warning("已经是最后一首歌了")
    
    # 进度显示
    st.markdown(f"""
    <div style="text-align: center; margin-top: 30px; padding: 15px; background: #f0f2f6; border-radius: 10px;">
        <p style="color: #666; font-size: 16px;">
        📊 进度：第 <span style="color: #667eea; font-weight: bold;">{st.session_state.current_song}</span> / {len(songs_data)} 首
        </p>
    </div>
    """, unsafe_allow_html=True)

# 碎碎念页面
def show_chatting_page():
    st.markdown("""
    <div style="text-align: center; margin-bottom: 40px;">
        <h1 style="color: #1a1a2e; font-size: 36px;">🐟の低语</h1>
        <div style="font-size: 24px; margin: 20px 0; color: #667eea;">💭 小生的碎碎念</div>
    </div>
    """, unsafe_allow_html=True)
    
    # 标题区域
    st.markdown("""
    <div style="background: linear-gradient(135deg, #FFE4E1 0%, #FFF0F5 100%); 
                padding: 30px; 
                border-radius: 20px; 
                margin: 20px 0;
                text-align: center;
                border-left: 5px solid #FF69B4;">
        <h2 style="color: #DB7093; font-size: 28px;">Dear 佑，见字如面</h2>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div style="text-align: left; margin: 40px 0;">
        <p style="font-size: 20px; color: #333; margin-bottom: 20px;text-indent: 2em;">
        23岁3个月5天的佑，你好👋，这里是21岁10个月16天的🐟～一个来得很迟的生日快乐，我的表达能力特别差，但我觉得💰、自由和快乐是非常重要的东西，所以希望你未来能赚到很多很多的💰，拥有自由，每天都很快乐，不需要为任何事发愁——去岁千般皆如愿，今年万事定称心(虽然这句话用过了，但我觉得这个寓意真的特别特别好，就当是叠加祝福了😁)。
        </p>
        <p style="font-size: 20px; color: #333; margin-bottom: 20px;text-indent: 2em;">
        就像我前面说的，我的表达能力很差，也不知道说什么，就来解答一下部分或许是你对我的疑惑😶‍🌫️。其实我跟谁都没有很多话题，跟晟小🐶也一样，现在的我觉得很多事都没必要去说出来，哪怕是朋友或者同担，因为我一开始说就控制不住自己输出一堆，我想了想，如果是我朋友突然向我吐槽输出了一堆我不感兴趣或者不懂的，我会很忙乱不知道怎么说怎么回复才能帮到对方，有时候可能还会产生烦恼，就不如不去说(就是有点难控制住，近几个月就控制地应该还行了😌)这样就都好了，所以其实我对谁都一样，话题这个是不同的人有不同的话题，我觉得我跟你的话题会比跟晟小🐶多。
        </p>
        <p style="font-size: 20px; color: #333; margin-bottom: 20px;text-indent: 2em;">
        还有呢，其实我就是很叛逆又冷漠，共情能力差是这样的🥶，有时候越逼我做什么我就越不想做，比如某一天我心情还不错，我打算去洗个碗，如果这时候我妈或者我爸来对我说“去把碗洗了，一天都只知道玩手机”，彳亍。今天这个碗我绝对不碰了🥴。我就是酱紫的，还有呢我对朋友热情只是我装的，很累的，每次都得保持一些表情，感觉面无表情会很舒服，玩到后面她们可能以为我不开心不满意，其实是我没力气做表情了，也没有生气什么的(除非真的做了让我不满的事，但我会尽量继续装(简直是高耗电模式)，真问了我就会说没有我只是没电了)，内心很平静，相当于开了省电模式，我也发现了，我更适合一个人，我会更舒服。那天我在西湖走走停停就特别舒服，没有人认识我，没人会在意我，我只需要看自己想看的，去想去的地方，在绿树下，面朝湖海，晒着阳光就很舒服，so no worry me，我这样就很舒服😌。这种感觉真的很好，我觉得你也可以试试，在大树下晒着太阳，吹着风，会很让人放松😇。
        </p>
        <p style="font-size: 20px; color: #333; margin-bottom: 20px;text-indent: 2em;">
        我有时候也会和你一样会想起以前美好的时光，虽然我总说不喜欢回忆，回忆很难受，又回不去了，但还是控制不住自己在某节无聊的课堂上想起很多事。想起一起去吃岭头，三个人拿着10块一起去买想吃想玩的，一起到处逛；想起某次回程，汝之父开着摩托车搭着我们三个，晟小🐶坐前面我俩坐后面，三个人合唱着那首《有点甜》；想起汝之父带着我们仨和狗狗狩猎队们一起出门满山跑；想起父亲节一起上山摘红菌(题外话，红菌真的好好吃好香🤤)；想起在花生丰收的季节一起在田里摘花生，还比谁摘的多，时不时演起小剧场，还有三个小鬼守家收花生的日子，收花生有点累，但总是能带着点快乐的；再拉远一点会想起三个人半夜不睡觉一起玩某个三人小游戏时憋笑得不行的时刻；想起我们一起看电视剧时对某个角色的紫色唇妆的调侃和问某个角色“他是不是天不亮就要起来编头发”；想起一起去北海时，大人们还没吃完饭我们就着急地跑去沙滩，还有一起写选民证(虽然有点小累，但平静而美好)，还有某一天只有我们俩，汝提出要去寻汝之母，于是我俩就滑上滑板出发，中途似乎还碰到一辆以为是坏人的货车，一路走一路滑，虽然我只会坐在滑板上溜车，最后凭着汝的记忆，我们成功找到了汝之母，那时候肯定很有成就感，像一场通关的冒险(虽然两人最后好像被说了🤫)……在无聊课堂上的我的嘴角总会下意识被这些美好的回忆勾起，回过神来才会带着笑拿起笔假装认真听课了🤣，关于你说那些可能有点不美好的回忆，我记得的，只是并不会觉得谁不懂事或者不满，我的脑回路不是这样的，至于我的大脑是怎么标记这些事的那我就不能说了，我的大脑运行方式怎么能透露呢～😝
        </p>
        <p style="font-size: 20px; color: #333; margin-bottom: 20px;text-indent: 2em;">
        好了好了，多了多了，最后呢依旧是生日快乐，愿汝心想事成，万事如意，能赚到超级超级多的💰，每天都能奖励自己，拥有去想去的地方的自由和能力，天天开心！🥳
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("---")
    
    # 显示图片的按钮
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🎁 点击查看高清回忆", key="show_special_images", use_container_width=True):
            st.session_state.show_images = True
            st.rerun()
    
    # 显示图片的区域
    if st.session_state.get('show_images', False):
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # 第一张图片
        st.markdown("### 📸 双人版")
        try:
            # 修改这里的路径为你的第一张图片路径
            image1_path = os.path.join(current_dir, "assets/special/image1.jpg")
            st.image(image1_path, caption="双人版（即老师著作）", use_container_width=True)
        except FileNotFoundError:
            st.warning("第一张图片未找到，请确保图片已放在 assets/special/image1.jpg")
        
        st.markdown("<br><br>", unsafe_allow_html=True)
        
        # 第二张图片
        st.markdown("### 📸 三人版")
        try:
            # 修改这里的路径为你的第二张图片路径
            image2_path = os.path.join(current_dir, "assets/special/image2.jpg")
            st.image(image2_path, caption="三人版（即老师著作）", use_container_width=True)
        except FileNotFoundError:
            st.warning("第二张图片未找到，请确保图片已放在 assets/special/image2.jpg")
            
        # 第三张图片
        st.markdown("### 📸 原图")
        try:
            # 修改这里的路径为你的第三张图片路径
            image2_path = os.path.join(current_dir, "assets/special/image3.jpg")
            st.image(image2_path, caption="（似乎是某天从某处归来时跑上楼拍的）", use_container_width=True)
        except FileNotFoundError:
            st.warning("第三张图片未找到，请确保图片已放在 assets/special/image3.jpg")
        
        # 返回按钮
        st.markdown("<br><br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🔙 返回", key="back_from_chatting", use_container_width=True):
                st.session_state.show_images = False
                st.session_state.page = "song_player"
                st.rerun()
    
    # 返回音乐页面的按钮（如果没有点击显示图片）
    elif not st.session_state.get('show_images', False):
        st.markdown("<br><br>", unsafe_allow_html=True)
        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("🎵 返回听歌", key="back_to_songs", use_container_width=True):
                st.session_state.page = "song_player"
                st.rerun()


# 页面路由
if st.session_state.page == "main":
    st.session_state.page = "weather_question"

if st.session_state.page == "login":
    show_login_page()
elif st.session_state.page == "register":
    show_register_page()
elif st.session_state.page == "trick1":
    show_trick_page1()
elif st.session_state.page == "trick2":
    show_trick_page2()

# 在页面路由部分添加新的页面分支（找到原来的页面路由部分，在最后添加这些elif分支）：
# 查找原来的页面路由部分，然后在后面添加：
elif st.session_state.page == "weather_question":
    show_weather_question()
elif st.session_state.page == "weather_response_sunny":
    show_weather_response_sunny()
elif st.session_state.page == "weather_response_cloudy":
    show_weather_response_cloudy()
elif st.session_state.page == "weather_response_rainy":
    show_weather_response_rainy()
elif st.session_state.page == "memory_question":
    show_memory_question()
elif st.session_state.page == "memory_response":
    show_memory_response()
elif st.session_state.page == "rambling_page":
    show_rambling_page()
elif st.session_state.page == "music_page":
    show_music_page()
elif st.session_state.page == "song_player":
    show_song_player()
elif st.session_state.page == "chatting_page":
    show_chatting_page()