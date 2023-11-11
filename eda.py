import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from PIL import Image

st.set_page_config (
    page_title= 'Obesity Prediction - EDA',
    layout = 'wide',
    initial_sidebar_state='expanded'
    )

def run():
        #membuat title
        st.title('Obesity Prediction')
        st.write('Project Created by Samuel chriss (SBY-001)')

        #membuat sub_header
        st.subheader('What About You?')

        #menambahkan gambar
        st.image('foto.jpg')

        # Menambahkan deskripsi
        st.write('Obesity is a condition where body weight exceeds normal limits due to the accumulation of excess fat in the body. Obesity occurs because calorie intake is more than the number of calories burned, so the body stores unused calories in the form of fat.')
        st.write("")
        st.write("BMI adalah indikator pengukuran yang digunakan untuk menentukan kategori berat badan ideal atau tidak. BMI dikembangkan oleh Adolphe Quetelet selama abad ke-19. Melalui hasil perhitungan BMI, Anda akan mengetahui kategori berat badan, yaitu kurus, ideal, berlebihan, atau bahkan obesitas.")
        st.write("Metode perhitungan ini juga bisa menjadi alat skrining untuk melihat risiko kesehatan tertentu. Menurut WHO, hasil BMI yang tidak normal/ideal akan meningkatkan risiko terkena beberapa penyakit. Maka dari itu, sekiranya Anda perlu memahami bagaimana cara menghitung BMI secara tepat untuk meminimalisir kenaikan atau penurunan berat badan secara berlebihan.")
        st.write("Adapun beberapa masalah kesehatan yang salah satu faktor risikonya adalah obesitas, di antaranya penyakit kardiovaskular, kematian dini, hipertensi, dan diabetes.")
        st.write("")
        st.write("Rumus BMI metrik adalah perhitungan yang paling sering digunakan di Indonesia, di mana satuannya adalah kilogram (berat badan) dan meter (tinggi badan).")
        st.write("")
        st.write("Sehingga rumusnya adalah:")
        st.write("- [berat badan (kg) : (tinggi badan (m) x tinggi badan (m))]")
        st.write("Contohnya, Anda memiliki berat badan 60 kg dengan tinggi badan 150 cm (1,5 m), maka cara menghitung BMI adalah sebagai berikut:")
        st.write("BMI = 60 : (1,5 x 1,5) = 60 : 2,25 = 26,6")
        st.write("Jadi, hasil perhitungan BMI dari seseorang dengan berat badan 60 kg dan tinggi badan 150 cm adalah 26,6.")
        st.write("")
        st.write("Setelah Mengetahui Massa index Tubuh, jangan ragu untuk mencoba prediksi terhadap tubuh Anda menggunakan model ini pada halaman Predict Your Body.")
        
        #membuat garis lurus
        st.markdown('---')

        #show dataframe
        st.title('Dataset')
        df = pd.read_csv('Obesity_Classification.csv')
        st.dataframe(df)
        st.write("Data set ini adalah sebuah tabel yang berisi informasi mengenai beberapa individu. Berikut adalah penjelasan singkat mengenai setiap kolom data:")
        st.write("1. **ID**: Kolom ini berisi identifikasi unik untuk setiap individu dalam data set.")
        st.write("2. **Age**: Menunjukkan usia individu dalam tahun.")
        st.write("3. **Gender**: Menunjukkan jenis kelamin individu (Male untuk pria, Female untuk wanita).")
        st.write("4. **Height**: Merupakan tinggi badan individu dalam sentimeter.")
        st.write("5. **Weight**: Merupakan berat badan individu dalam kilogram.")
        st.write("6. **BMI**: Ini adalah indeks massa tubuh (Body Mass Index) yang dihitung berdasarkan berat badan dan tinggi badan individu. Ini adalah angka yang menggambarkan apakah seseorang berada dalam kategori berat badan yang sehat.")
        st.write("7. **Label**: Merupakan kategori berat badan individu berdasarkan nilai BMI. Misalnya, 'Normal Weight' untuk berat badan normal, 'Overweight' untuk berat badan berlebih, 'Underweight' untuk berat badan kurang, dan 'Obese' untuk obesitas.")
        st.write("Data ini dapat digunakan untuk analisis berat badan, tinggi badan, usia, jenis kelamin, dan status berat badan individu.")

        #membuat garis lurus
        st.markdown('---')

        #membuat barplot 
        st.write('### Plot Label')
        fig = plt.figure(figsize=(10,8),dpi=50)
        sns.countplot(data=df,x='Label',palette='deep')
        plt.title('Labels and their total count')
        st.pyplot(fig)
        st.write('Dari data di atas diketahui Terdapat 47 individu yang termasuk dalam kelompok underweight. Ini menunjukkan bahwa sebagian besar orang dalam sampel memiliki berat badan di bawah batas berat badan yang sehat. Sebanyak 29 orang masuk ke dalam Berat Badan Normal ini. Ini berarti bahwa sejumlah kecil orang dalam sampel memiliki berat badan yang sesuai dengan tinggi badan mereka, atau berada dalam kisaran berat badan yang sehat. selain itu Terdapat 20 individu yang termasuk Overweight. Ini menunjukkan bahwa sejumlah orang dalam sampel memiliki berat badan lebih dari yang seharusnya, tetapi belum mencapai tingkat obesitas. dan yang terakhir  Ada 12 orang Obesitas. Ini mengindikasikan bahwa sejumlah kecil orang dalam sampel memiliki berat badan yang jauh melebihi batas berat badan yang sehat, dan mereka termasuk dalam kategori obesitas')
        st.markdown('---')

        #membuat barplot
        st.write('### Plot BMI')
        image = Image.open("output.png")
        st.image(image, caption='BMI Statistics by Body Label', use_column_width=True)
        bmi_stats = df.set_index("Label")
        bmi_stats.plot(kind="bar", figsize=(10, 6))
        plt.xlabel("Label")
        plt.ylabel("BMI Value")
        plt.title("BMI Statistics by Body Label")
        plt.xticks(rotation=45)
        plt.legend(["Min BMI", "Max BMI", "Mean BMI"])
        plt.savefig("bmi_statistics.jpg")
        st.write("Normal Weight:")
        st.write("1. Nilai minimum BMI adalah 21.2.")
        st.write("2. Nilai maksimum BMI adalah 25.3.")
        st.write("3. Rata-rata BMI untuk kategori ini adalah sekitar 22.83.")
        st.write("Obese:")
        st.write("1. Nilai minimum BMI adalah 28.9.")
        st.write("2. Nilai maksimum BMI adalah 37.2.")
        st.write("3. Rata-rata BMI untuk kategori ini adalah sekitar 32.34.")
        st.write("Overweight:")
        st.write("1. Nilai minimum BMI adalah 25.0.")
        st.write("2. Nilai maksimum BMI adalah 29.1.")
        st.write("3. Rata-rata BMI untuk kategori ini adalah sekitar 26.60.")
        st.write("Underweight:")
        st.write("1. Nilai minimum BMI sangat rendah, yaitu 3.9.")
        st.write("2. Nilai maksimum BMI adalah 20.0.")
        st.write("3. Rata-rata BMI untuk kategori ini adalah sekitar 13.55.")
        
        #membuat barplot 
        st.write('### Plot BMI')
        fig = plt.figure(figsize = (15, 10))
        sns.countplot(data = df, x = 'BMI', hue = 'Label')
        plt.title('BMI VS Label')
        st.pyplot(fig)
        st.write('Data ini memberikan informasi tentang BMI (Body Mass Index) dan jumlah individu dalam masing-masing kategori berdasarkan nilai BMI dan label yang diberikan')
        st.write("Dari grafik di atas dapat disimpulkan data sebagai berikut:")
        st.write("1. Kurang dari 20,00 berarti berat badan kurang (underweight).")
        st.write("2. Antara 21,00 - 25,00 berarti berat badan normal.")
        st.write("3. Antara 25-29,1 berarti berat badan berlebih (overweight).")
        st.write("4. Di atas 30 berarti obesitas.")
        st.markdown('---')

        #membuat barplot 
        st.write('### Plot BMI & Weight')
        fig, ax = plt.subplots()  # Membuat objek Figure dan Axes
        ax.scatter(df['BMI'], df['Weight'])
        ax.set_xlabel('BMI')
        ax.set_ylabel('Weight')
        ax.set_title('Scatter Plot: BMI vs. Weight')
        ax.grid(True)
        st.pyplot(fig)  # Menampilkan plot menggunakan Streamlit
        st.write('Data ini Ini menunjukkan bahwa ada hubungan positif yang sangat kuat antara BMI dan berat badan. Dalam konteks ini, semakin tinggi nilai BMI seseorang, semakin tinggi pula berat badan mereka. Sebaliknya, semakin rendah nilai BMI, semakin rendah pula berat badan. Dengan kata lain, data menunjukkan bahwa individu dengan nilai BMI yang tinggi cenderung memiliki berat badan yang tinggi, sementara individu dengan nilai BMI yang rendah cenderung memiliki berat badan yang rendah. Hubungan positif yang kuat ini menunjukkan bahwa BMI dan berat badan cenderung bergerak seiring satu sama lain, dan perubahan dalam satu variabel akan mengakibatkan perubahan yang sejalan dalam variabel lainnya.')
        st.markdown('---')

        #membuat barplot 
        st.write('### Plot Height')
        fig = plt.figure(figsize=(15,5))
        sns.histplot(df['Height'], bins=20, kde=True).set(title='Height')
        plt.title('Height')
        st.pyplot(fig)
        st.write('Dari data di atas dapat diketahui bahwa tinggi maksimal dari data ini adalah 210 cm dan yang paling pendek atau rendah adalah 120 cm')
        st.markdown('---')

        #membuat barplot 
        st.write('### Plot Weight')
        fig = plt.figure(figsize=(15,5))
        sns.histplot(df['Weight'], bins=20, kde=True).set(title='Weight')
        st.pyplot(fig)
        st.write('dari data di atas dapat dilihat rata2 berat dari total 108 orang adalah 58 kg dan untuk orang yang paling berat ada pada 120 kg dan yang apling ringan ada pada 10 kg.')
        st.markdown('---')

        #membuat barplot 
        st.write('### Plot Height & Weight')
        fig, ax = plt.subplots()  # Membuat objek Figure dan Axes
        ax.scatter(df['Height'], df['Weight'])
        ax.set_xlabel('Height')
        ax.set_ylabel('Weight')
        ax.set_title('Scatter Plot: Height vs. Weight')
        ax.grid(True)
        st.pyplot(fig)  # Menampilkan plot menggunakan Streamlit
        st.write('Data ini menunjukkan bahwa ada variasi dalam data yang tidak dapat dijelaskan oleh hubungan antara tinggi badan dan berat badan. Dengan kata lain, masih banyak faktor lain yang dapat memengaruhi berat badan selain tinggi badan.')
        st.markdown('---')

        # Membuat histogram plot untuk Age
        st.write('## Plot Age')
        fig = plt.figure(figsize=(10, 6), dpi=80)
        sns.histplot(data=df, x='Age', kde=True, hue='Label', multiple='stack', palette='deep')
        plt.title('Distribution of Age with weight labels')
        st.pyplot(fig)
        st.write('dari data disini terlihat bahwa usia paling muda adalah 10 tahun dan yang paling tua adalah 112 tahun. Selain itu, dari grafik di atas terlihat bahwa semua penderita obesitas berusia 40 tahun ke atas.')
        st.markdown('---')

        # Membuat scatter plot untuk Age dan BMI
        st.write('## Plot Age vs BMI')
        fig, ax = plt.subplots()
        ax.scatter(df['Age'], df['BMI'])
        ax.set_xlabel('Age')
        ax.set_ylabel('BMI')
        ax.set_title('Scatter Plot: Age vs. BMI')
        ax.grid(True)
        st.pyplot(fig)
        st.write('Dari grafik di atas, terlihat bahwa ada variasi dalam data yang tidak dapat dijelaskan oleh hubungan antara usia dan BMI. Artinya, masih ada faktor-faktor lain yang memengaruhi nilai BMI selain usia. Oleh karena itu, korelasi ini menunjukkan bahwa terdapat sejenis hubungan positif antara usia dan BMI dalam data ini, tetapi tidak cukup kuat untuk mengatakan bahwa usia adalah faktor penentu utama BMI, dan masih ada banyak faktor lain yang perlu dipertimbangkan.')
        st.markdown('---')

        # Membuat pie chart untuk Gender
        st.write('### Plot Gender')
        fig, ax1 = plt.subplots(figsize=(8, 8))
        df['Gender'].value_counts().plot(kind='pie', autopct='%.2f%%', ax=ax1)
        st.pyplot(fig)
        st.write('Dari total 108 data di atas, didominasi oleh laki-laki dengan 51.82% atau 56 orang pria dan 48.15% atau 52 orang perempuan.')
        st.markdown('---')

        # Membuat countplot untuk Gender & Label
        st.write('### Plot Gender & Label')
        fig = plt.figure(figsize=(10, 6), dpi=80)
        ax = sns.countplot(data=df, x="Gender", hue='Label')
        st.pyplot(fig)
        st.write('Dari grafik di atas dapat dilihat bahwa laki-laki dalam kumpulan data di atas terdistribusi secara normal di semua kategori, tetapi untuk perempuan, kategori terbesar adalah berat badan kurang, dan dapat dilihat bahwa tidak ada bagian yang mengalami obesitas.')
        st.markdown('---')


if __name__ == '__main___':
    run()