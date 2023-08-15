import streamlit as st
import pandas as pd
import plotly.express as px
from transformers import pipeline
from streamlit_star_rating import st_star_rating
import plotly.express as px
import pandas as pd

global star_key
star_key=0

st.title("TEXT CLASSIFICATION")
st.cache_resource()
def positive_negative():
  p_n_review = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")
  return p_n_review
st.cache_resource()
def star_review():
  star = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")
  return star
st.cache_resource()
def emotion_detection():
  emotion=pipeline("text-classification", model="j-hartmann/emotion-english-distilroberta-base", top_k=5)
  return emotion

def figure(emotion):
    emotions_dict = emotion[0]
    emotion_labels = [item['label'] for item in emotions_dict]
    emotion_scores = [item['score'] for item in emotions_dict]
    other_emotion_score = sum(score for score in emotion_scores if score < 0.1)
    emotion_labels = [label if score >= 0.1 else 'Other' for label, score in zip(emotion_labels, emotion_scores)]
    emotion_scores = [score if score >= 0.1 else other_emotion_score for score in emotion_scores]
    df = pd.DataFrame({'emotion': emotion_labels, 'score': emotion_scores})
    df=df.drop_duplicates()
    return df

def assistant_template(star_value,positive,negative,df):
    global star_key
    try:
        st_star_rating(label = "Review Sentiment Analysis: Star Rating", maxValue = 5, defaultValue = star_value, key = star_key, read_only = True )
    except:
        
        star_key+=1
        st_star_rating(label = "Review Sentiment Analysis: Star Rating", maxValue = 5, defaultValue = star_value, key = star_key, read_only = True )
    
    num_unique_labels = df['emotion'].nunique()

# Get the Plotly colors based on the number of unique labels
    colors = px.colors.qualitative.Plotly[:num_unique_labels]
    fig = px.pie(df, values='score', names='emotion', color_discrete_sequence=colors)
    st.divider()
    st.subheader("Review Sentiment Analysis: Positivity and Negativity Percentages")
    col1,col2=st.columns(2)
    
    with col1:
        st.metric("f", positive, "Postive",label_visibility='hidden')
        
        
    with col2:
        st.metric("ga", negative, "-Negative",label_visibility='hidden')
        
    st.divider()
    st.subheader("Emotion Analysis: Detected Emotion")
    st.plotly_chart(fig, use_container_width=True)


if "messages" not in st.session_state:
    st.session_state.messages = []
    
for message in st.session_state.messages:

    star_key+=1
    if message["role"] == "user":
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
            
    elif message["role"] == "assistant":
        with st.chat_message(message["role"]):
            print(message)
            star_value=message['star']
            df=message['chart_data']
            negative=message['negative']
            positive=message['positive']
            assistant_template(star_value,positive,negative,df)

        star_key+=1
        
    

                
if prompt := st.chat_input("Write a Sentence"):
    # Display user message in chat message container
    st.chat_message("user").markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

    
    star = star_review()

    star_data=star(prompt)
    
    # Extract the label (star rating) with the highest score
    star_value = int(star_data[0]['label'][0])

    
   
    p_n_review = positive_negative()
    p_n_classify=p_n_review(prompt) 

    if p_n_classify[0]['label'] == 'NEGATIVE':
        negative = "{:.2f}%".format(p_n_classify[0]['score'] * 100)
        positive = "{:.2f}%".format((1 - p_n_classify[0]['score']) * 100)
    elif p_n_classify[0]['label'] == 'POSITIVE':
        positive = "{:.2f}%".format(p_n_classify[0]['score'] * 100)
        negative = "{:.2f}%".format((1 - p_n_classify[0]['score']) * 100)
        
    emotion_detect=emotion_detection()
    emotion=emotion_detect(prompt)
    

  
    # Generate a random chart data (you can replace this with your own chart creation code)
    df = figure(emotion)
    

    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        assistant_template(star_value,positive,negative,df)
  
    star_key+=1
    # Add assistant response and chart data to chat history
    st.session_state.messages.append({"role": "assistant", "star": star_value, "chart_data": df,"negative":negative,"positive":positive})

    

