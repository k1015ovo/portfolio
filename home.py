import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title='Cardiac disease', page_icon='❤')

# st.write("# 심장병 데이터 분석")

st.header("🔎 심장병 개요", divider='red')

df=pd.read_csv('he.csv')

st.subheader('심장병(Cardiac disease)이란?')
st.markdown('''
    심장병의 원인은 선천적인 원인과 후천적인 원인으로 나눌 수 있습니다. \n
    1. 선천성 심장 질환
        * 다운 증후군 같은 염색체 이상 (유전자 이상) \n
        * 풍진, 인플루엔지 당 바이러스 감염 \n
        * 항경련제, 항부정맥약, 정신과 약같은 약물 투여 등 \n
    2. 후천성 심장 질환
        * 음주 및 흡연 \n
        * 비만, 고혈압, 남성 호르몬 \n
        * 패스트푸드 및 인스턴트 등 가공식품 과다 섭취 \n
        * 각성제, 처방약 부작용 등 \n
''')

st.subheader('대표적인 심장 질환')
st.image('EKG-Cadi-dise.jpg')
st.markdown('''
    대표적인 심장 질환으로는 **심근경색**과 **협심증**입니다. \n

    1. 심근경색 \n
        심장 근육이 혈액 공급을 받지 못해 괴사하는 질환으로 심장 근육에 혈액을 공급하는 관상 동맥은 다른 혈관들에 비해 많은 혈액을 보내야 하므로 발생합니다. 
        특히 혈관벽에 콜레스테롤 등이 달라붙거나 하는 각종 이유로 혈관이 좁아져 :red[**이상운동이 발생**]하거나, 혈전으로 인해 :red[**혈관이 폐쇄**]되는 등 여러 원인들이 동시다발적으로 발생할 수 있습니다. 
        이러한 원인들로 인해 :red[**혈류 공급이 차단**]되면 심근이 제 기능을 하지 못하여 통증을 동반한 심장 마비가 오기도 한다. \n
        이 외에도 다른 위험인자가 존재합니다. \n
         * 고지혈증 : 전체 콜레스테롤 수치고 240mg/dL 이상일 경우 심근경색의 발병률이 증가합니다. 
         * 흡연 : 심혈관질병 외에도 뇌졸중, 말초동맥질환 등을 일으키는 원인으로 손꼽힙니다. 
         * 당뇨병 : 일반인에 비해 당뇨병환자는 발병률이 2~4배 더 높으며 특히 여성에게 치명적입니다. \n 
    2. 협심증 \n
        관상동맥이 막혀 :red[**조이듯이 통증**]이 온다. 기존 동맥경화증이 발졍해 좁아진 혈관에 혈전이 들어가 막혀버리거나, 동맥의 갑작스로운 수축, 혈관 내피가 벗겨지는 등이 대표적입니다. 
        사전 발견이 중요하나 흉통 자체의 원인은 야근, 과로, 스트레스, 운동 등으로도 충분히 느낄 수 있기 때문에 쉽게 발견되지는 않는다. 또한, 흉통 또는 심장 통증이 있어서:red[**심전도를 찍어도 결과가 정상인 사례**]도 흔하게 발견됩니다. 
''')