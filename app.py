import streamlit as st
from pref_question import pref_location
from wiki import wiki

#ログイン情報
id_pwd = {'test': 'test'}

#ログインページ
def login():
    st.title('ログイン')
    user_id = st.text_input('ユーザーID')
    password = st.text_input('パスワード', type='password')
    if st.button('ログイン'):
        if user_id in id_pwd:
            if password == id_pwd[user_id]:
                st.success('ログインに成功しました')
                st.session_state.login = True  # ログイン状態をTrueに設定
                st.experimental_rerun()  # main()関数を再度実行
            else:
                st.error('パスワードが間違っています')
        else:
            st.error('ユーザーIDが間違っています')

#クイズページ
def pref_quiz():
    random_pref, city_name, pref_url = pref_location()
    st.session_state.prefecture = random_pref
    st.session_state.city = city_name
    st.session_state.url = pref_url
    st.title('都道府県クイズ')
    st.write(f'{random_pref}の県庁所在地はどこでしょう？')
    user_answer = st.text_input('回答')
    if st.button('回答する'):
        if user_answer == city_name:
            st.success('正解です！')
        else:
            st.error('不正解です！')
        st.write(f'正解は{city_name}です。')
        st.write(f'{random_pref}のWikipediaページはこちら：{pref_url}')

#Wikipedia検索ページ
def wikipedia():
    st.title('Wikipedia検索')
    word = st.text_input('検索ワード')
    if st.button('検索'):
        if word == '':
            st.warning('入力がないため、該当する結果がありませんでした')
        else:
            result = wiki(word)
            st.write(result)
            
#ログアウトページ
def logout():
    if st.confirm('ログアウトしてもよろしいですか？', show_cancel_button=False):
        st.session_state.login = False
        st.session_state.logout = True  # ログアウト状態をTrueに設定
        st.success('ログアウトしました')


#メインページ
def main():
    st.set_page_config(page_title='Webアプリ', page_icon=':memo:', layout='wide')
    st.title('Webアプリ')
    if 'login' not in st.session_state:
        st.session_state.login = False
    if not st.session_state.login:
        if login():
            st.session_state.login = True
    else:
        menu = ['ホーム', '都道府県クイズ', 'Wikipedia検索', 'ログアウト']
        choice = st.sidebar.selectbox('メニュー', menu)
        if choice == 'ホーム':
            st.write('ホームページです')
        elif choice == '都道府県クイズ':
            pref_quiz()
        elif choice == 'Wikipedia検索':
            wikipedia()
        elif choice == 'ログアウト':
            logout()

if __name__ == '__main__':
    main()
