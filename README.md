# Text Classification: Sentiment Analysis and Emotion Prediction Web Application

Welcome to the Text Classification: Sentiment Analysis and Emotion Prediction Web Application! This application is powered by Hugging Face's pre-trained text classification transformer models and seamlessly integrates natural language processing techniques to classify text as positive/negative sentiment and provide star-rated emotion predictions. The user-friendly interface is built using Streamlit, making it easy to interact with the models and gain insights into the sentiment and emotion behind text data.

## Video Demo

Check out the video demo of the application in action [here](https://github.com/ibadurrehman1/text_classification/assets/57496676/968916f8-7dfc-4401-ad9c-864421f9917b)

## Project URL

You can access the web application [here](https://textclassification-chatbot.streamlit.app/).

**Note:** This app is hosted on Streamlit's free platform, which means that after every query or interaction, you'll need to rerun the application using the "Rerun" button to refresh the session.

## Running the Application on Google Colab (Optional)

To run this application on Google Colab with GPU acceleration, follow these steps:

1. **Change Runtime to GPU T4:** In your Colab notebook, go to the "Runtime" menu, select "Change runtime type," and set the hardware accelerator to "GPU."

2. **Clone the Repository:** In the first cell of your Colab notebook, run the following command to clone the project repository:

    ```
    !git clone https://github.com/ibadurrehman1/text_classification.git
    ```

3. **Navigate to the Project Directory:** Move to the project directory:

    ```python
    %cd text_classification
    ```

4. **Install Dependencies:** Install the required dependencies using the `requirements.txt` file:

    ```python
    !pip install -r requirements.txt
    ```

5. **Install LocalTunnel:** Install LocalTunnel to expose the Streamlit app to the internet:

    ```python
    !npm install localtunnel
    ```

6. **Run the Application:** Start the Streamlit application in the background and save logs:

    ```python
    !streamlit run /content/text_classification/app.py &>/content/logs.txt &
    ```

7. **Retrieve Public IP Address:** Print the public IP address that you'll use in the next step:

    ```python
    print("Use this public IP inside the Tunnel website:")
    !curl ipv4.icanhazip.com
    ```

8. **Create a Tunnel:** Create a tunnel using LocalTunnel to access the app from your local browser:

    ```python
    !npx localtunnel --port 8501
    ```

After completing these steps, you'll have the application up and running in Google Colab with GPU acceleration. You can use the provided public IP address to access the app from your local browser. GPU acceleration can significantly speed up the prediction process and enhance the user experience.
