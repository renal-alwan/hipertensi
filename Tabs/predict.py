import streamlit as st

from web_functions import predict

def app(df, x, y):

    st.title("Halaman Prediksi")

    col1, col2= st.columns(2)

    with col1:
        cp = st.text_input ('input nilai Jenis nyeri dada (0;typical angina, 1;atypical angina, 2;non-anginal, 3;Asimtomatik)')
    with col1:
        trestbps = st.text_input ('input nilai Tekanan darah sistolik saat istirahat dalam (mmHg)')
    with col1:
        chol = st.text_input ('input nilai Kadar kolesterol dalam (mg/dL)')
    with col1:
        fbs = st.text_input ('input nilai Kadar gula darah puasa (1: Gula darah puasa > 120 mg/dL, 0: Gula darah puasa ≤ 120 mg/dL)')
    with col1:
        restecg = st.text_input ('input nilai Hasil elektrokardiogram (EKG) saat istirahat')
    with col2:
        thalach = st.text_input ('input nilai Denyut jantung maksimum yang dicapai selama tes atau observasi')
    with col2:
        exang = st.text_input ('input nilai Angina yang dipicu oleh olahraga (1: Ya, 0: Tidak)')
    with col2:
        oldpeak = st.text_input ('input nilai Depresi ST yang diinduksi oleh olahraga relatif terhadap istirahat')
    with col2:
        slope = st.text_input ('input nilai Kemiringan segmen ST pada EKG')
    with col2:
        ca = st.text_input ('input nilai jumlah pembuluh utama yang diwarnai dengan fluoroskopi.')
    with col2:
        thal = st.text_input ('input nilai Jenis thalassemia')

    features = [cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal,]

    #tombol
    if st.button("prediksi"):
        prediction, score =  predict(x,y,features)
        score = score
        st.info("prediksi sukses")

        if (prediction [0]== 0):
            st.warning("pasien tidak terkena hipertensi")
        else:
            st.success("pasien terkena hiperetensi")
        
        st.write("model akurasi", (score*100), "%")