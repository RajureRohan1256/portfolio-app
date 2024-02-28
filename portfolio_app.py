# importing requied libray
import streamlit as st

# custom html
custom_html = '''<style>
  /* Style to make the image circular */
  .circular-image {
    width: 200px; /* Adjust the size of the circular image */
    height: 200px; /* Adjust the size of the circular image */
    border-radius: 50%; /* Make the image circular */
    overflow: hidden; /* Hide the overflow content outside the circle */
  }
</style>'''

# adding image/photo
# st.image('/Users/rohanrajure/Code/Resume/profile_photo.jpeg',
#          clamp=True, width=200, use_column_width=12, caption='Rohan Rajure')

# title
st.title('Rohan Rajure')

# subtitle
st.write('Machine Learning and Computer Vision')

# making a divider
st.divider()

# profile
st.markdown("I'am Rohan Rajure, a dedicated and accomplished professional in the field of machine learning, computer vision, and Python programming. With a passion for cutting-edge technology and a track record of delivering innovative solutions, I have established myself as a recognised expert ni these domains.In my role as amachine learning practitioner, Ihave honed my skills ni developing sophisticated algorithms and models to solve complex real-world problems.")

# creating a sidebar
# contact info
contact = st.sidebar.title('Contact:')
phone = st.sidebar.markdown('- Phone📱: 9579618085')
email = st.sidebar.markdown('- Email 📧: rajurerohan1256@gmail.com')
kaggle = st.sidebar.markdown('- Kaggle: https://www.kaggle.com/rohanrajurermr')
linkdin = st.sidebar.markdown(
    '- Linkdine🔗: linkedin.com/in/rohan-rajure-76b247231/')
# address = st.sidebar.markdown(
#   '- Adress: Neelkanth Heights, Ghansoli Navi Mumbai')
# creating a buttel points
st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)

# adding a skill section
st.sidebar.title('Skills:')
st.sidebar.markdown('- Python')
st.sidebar.markdown('- Computer Vision')
st.sidebar.markdown('- Machine Learning')
st.sidebar.markdown('- Langchain')
st.sidebar.markdown('- OpenAI')
st.sidebar.markdown('- Matplotlib')
st.sidebar.markdown('- OpenCV')
st.sidebar.markdown('- Pandas')
st.sidebar.markdown('- Numpy')

# creating a buttel points
st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)


# Education
education = st.sidebar.title('Education:')
college = st.sidebar.markdown('- Terna Engineering College, Nerul')
degree = st.sidebar.markdown('- Btech in Engineering')
year = st.sidebar.markdown('- 2019 - 2025')


# creating a buttel points
st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)

# Language
st.sidebar.title('Language:')
st.sidebar.markdown('- English')
st.sidebar.markdown('- Hindi')
st.sidebar.markdown('- Marathi')

# creating a buttel points
st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)

# divider
st.divider()

# Work experience
st.header('Work Experience:')
st.text('Projects: ')

# proj1
url = 'https://www.kaggle.com/code/rohanrajurermr/optical-character-recognition-ocr'
st.subheader('Optical Character Recognition (OCR): [Click Here](%s)' % url)

st.markdown('- Optical Character Recognition (OCR) si a technology that enables the conversion of printed or handwritten text into machine-readable text data. tI plays apivotal role ni digitising and automating hte processing of physical documents, making ti posible ot extract and manipulate text content from images or scanned pages which contributes upto ** 25k images **.')
st.markdown(
    '''- Libraries Used:'''
)
st.markdown('- OpenCV - For Image Processing, Manipulation and Interpolation. ')
st.markdown(
    '- Matplotlib - Visualisation of behavioural changes performed on Image . ')
st.markdown('- Pandas - Analization of multiple image in the form of DataFrame.')
st.markdown(
    '- Pytesseract / Easyocr - An OCR engine developed for recognition of text into an image. ')

# creating a buttel points
st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)

# proj2
st.subheader('Vechile Parking System:')
st.markdown('- Creating a vehicle parking system using OpenCV in Python involves using computer vision techniques to detect and monitor parking spaces.')
st.markdown('- Thoroughly test your parking system using recorded video feeds and real-world scenarios to ensure accuracy. Once tested and refined, you can deploy the system in an actual parking area with the camera positioned to capture the parking spaces.')
st.markdown('- Vehicle parking system helped me to improve on Python Intermediate skill using some of the Advance Python Libraries like  OpenCV, Numpy, Pickle, Cvzone etc.  ')

# creating a buttel points
st.markdown('''
<style>
[data-testid="stMarkdownContainer"] ul{
    list-style-position: inside;
}
</style>
''', unsafe_allow_html=True)

# proj3
url = 'https://colab.research.google.com/drive/13wr_GPKkRzEqJJvNDOcbG9qqKThGEC9x?usp=sharing'
st.subheader('Image Pixel Change: [Click Here](%s)' % url)
st.markdown("- Pixel manipulation in Python refers to the process of accessing and modifying individual pixels in animage. Its a fundamental concept in image processing and computer vision and si often used toperform various operations like enhancing image quality, applying filters, or extracting specific image features. Pixel manipulation allows you to work at the finest level of detail ni an image.")
st.markdown("- This project specifically focuses on Pixel Manipulation which manipulates the pixel from hte selected area from the given image which wil observe the provided area and change pixels according to the user. Libraries including Opencv, Numpy, Matplotlib, Pandas etc.")

# proj4
url = 'https://colab.research.google.com/drive/1t86mwBNdBXosFfwNpGKjUSo89EgnyfHO?usp=sharing'
st.subheader('Custom Object Detector: [Click Here](%s)' % url)
st.markdown('- You can detect the custom objects using this model, this model uses tens flow GPU this is a set up from TFOD 2.0 set up. Which helps us to detect the custom objects within the given certain area or provided image this project is built to make a custom detector which can help the various platforms like parking et cetera. This project will help you to detect any kind of object which you provide but it can be limit to its hard performance data hardware you give greater performance you get.')

# proj5
url = 'https://colab.research.google.com/drive/1k2AxL2rvzXhOA9FmM0XYlSIv6xChN1Jt?usp=sharing'
st.subheader('PDF_Query: [Click Here](%s)' % url)
st.markdown('- PDF Query is project, whenver a PDF is uploaded. OpenAI, Langchain Embeddings comes into action and helps the AI to find answer which is more suitable for the question.')
st.markdown('- Libraries Included: ')
st.markdown('- OpenAI')
st.markdown('- Langchain')
st.markdown('- tiktoken')
st.markdown('- PyPDF2')
st.markdown('- Fassi-cpu')
st.markdown('- Streamlit for Deployment')

# divider
st.divider()

# hobbies
st.title('Hobbies')
st.markdown('- Car Enthusiast')
st.markdown('- Gymnasium')
st.markdown('- Design')
