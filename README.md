

# 🕵️ Fake News Verifier

Ever found yourself scrolling through news and wondering, "Is this actually true?" You're not alone. In a world flooded with information, it's getting harder to separate fact from fiction. That's why I built **Fake News Verifier** - your friendly neighborhood fact-checking assistant!

## ✨ What It Does

Fake News Verifier is like having a truth-seeking detective in your pocket. It uses cutting-edge AI to analyze news claims and tell you whether they're likely real or fake. Here's what makes it special:

- 🎤 **Speak Your Mind**: Just click the microphone and speak the news you want to verify - no typing required!
- 🌐 **Multi-Language Support**: Works in English, Hindi, Telugu, and Tamil
- 🧠 **AI-Powered Analysis**: Uses advanced language models to cross-reference with reliable sources
- 📊 **Trust Scoring**: Get a percentage score showing how trustworthy each news item is
- 🌙 **Dark Mode**: Easy on the eyes, day or night
- 📱 **Mobile-Friendly**: Works beautifully on all your devices

## 🎯 See It in Action

Check out the live version: [https://fake-news-verifier-jswi.onrender.com/](https://fake-news-verifier-jswi.onrender.com/)

## 🛠️ The Tech Behind the Magic

I built this using some pretty cool tools:

- **Frontend**: HTML, CSS, and JavaScript with a modern glassmorphism design
- **Backend**: Flask (Python) for the server-side logic
- **AI Brain**: Groq's Llama 3.3 model for smart analysis
- **Source Verification**: Tavily API for finding reliable sources
- **Speech Recognition**: Web Speech API for voice input
- **Deployment**: Render for easy cloud hosting

## 🚀 Setting Up on Your Computer

Want to run it locally? It's easier than you might think! Here's how:

### Prerequisites

- Python 3.8 or higher
- A code editor (VSCode works great)

### Step-by-Step Setup

1. **Clone the Repository**
   ```bash
   git clone https://github.com/your-username/fake-news-verifier.git
   cd fake-news-verifier
   ```

2. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On Mac/Linux
   source venv/bin/activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Your API Keys**
   Create a file named `.env` in the project root and add:
   ```
   TAVILY_API_KEY=your_tavily_api_key_here
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```

6. **Open Your Browser**
   Navigate to `http://localhost:5000` and start fact-checking!

## 🌐 Deploying to the Cloud

I used Render to deploy this app, and it was surprisingly simple:

1. Push your code to GitHub
2. Create an account on [Render.com](https://render.com)
3. Connect your GitHub repository
4. Add your environment variables (API keys)
5. Deploy with one click!

That's it - your app is live for the world to see!

## 🎮 How to Use

Using Fake News Verifier is as easy as 1-2-3:

1. **Enter Your News**: Type or speak the news headline or article you want to check
2. **Choose Your Language**: Pick from English, Hindi, Telugu, or Tamil
3. **Click "Verify Claim"**: Sit back while the AI does its magic

In seconds, you'll get:
- A clear verdict: Real, Fake, or Unknown
- A trust score percentage
- An explanation of why the AI reached that conclusion
- Links to reliable sources that back up the analysis

## 🔑 About Those API Keys

To use this app, you'll need API keys from:

- **Tavily**: For finding reliable sources ([Get your key](https://tavily.com/))
- **Groq**: For the AI analysis ([Get your key](https://console.groq.com/))

The free tiers are generous enough for personal use, but if you're planning to share this widely, you might want to upgrade to paid plans.

## 🤝 Want to Contribute?

I'd love your help making this even better! Here are some ways you can contribute:

- **Report Bugs**: Found something that doesn't work? Let me know!
- **Suggest Features**: What would make this more useful for you?
- **Improve the Design**: Have an eye for design? I'd love your input!
- **Add Languages**: Help us support more languages

Just fork the repo, make your changes, and submit a pull request. Let's make the internet a little more truthful together!

## 📄 License

This project is licensed under the MIT License - feel free to use it however you'd like!

## 📧 Get in Touch

Have questions, suggestions, or just want to say hi? Reach out to me at [your.email@example.com](mailto:your.email@example.com). I'd love to hear from you!

---

Made with ❤️ by [Yaswanth](https://your-website.com)
