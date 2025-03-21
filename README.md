# BeMuslim Counter 🕌

This is a simple tool to help count how many days each person sent an image in the BeMuslim WhatsApp group chat.

---

## 📥 How to Use

1. On your phone or laptop, go to the **BeMuslim chat**.
2. Tap **Export Chat** → choose **Without Media**.
3. Download the ZIP file and extract it.
4. Find the file called `_chat.txt`.
5. Upload it into the app.

---

## 🧪 Setup

### Step 1 – Clone the project

```bash
git clone https://github.com/Hteam121/bemuslim-counter.git
cd bemuslim-counter
```

### Step 2 – (Optional) Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3 – Install requirements

```bash
pip install -r requirements.txt
```

> If you're on macOS and get permission errors, try:

```bash
pip install --break-system-packages -r requirements.txt
```

---

## ▶️ Run the app

```bash
python app.py
```

Then open your browser and go to:  
[http://127.0.0.1:5000](http://127.0.0.1:5000)

---

That’s it! Let the counter do the work for you 🙌
