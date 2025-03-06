# 🚀 DevX - Setup Guide (Windows)

Welcome to the **DevX** project! Follow the steps below to quickly set up the project on your Windows machine.

---

## Steps to Set Up

### 1. Clone the Repository
Start by cloning the **DevX** repository to your local machine:

```bash
git clone https://github.com/AnirbanNath-dev/DevX.git
```

### 2. Navigate to the Project Directory
Once cloned, move into the DevX directory:

```bash
cd DevX
```

### 3. Create a Python Virtual Environment
Create a virtual environment to isolate the project's dependencies:

```bash
python -m venv .venv
```

### 4. Activate the Virtual Environment
Activate the virtual environment you just created:

```bash
.\.venv\Scripts\activate
```

### 5. Install Required Dependencies
Now, install the necessary Python packages from the requirements.txt file:

```bash
pip install -r requirements.txt
```

### 6. Download Lavalink .JAR File
Download the latest Lavalink .jar file from [Lavalink GitHub](https://github.com/lavalink-devs/Lavalink)
 and place it inside the `lavalink` folder in your cloned repo.

### 7. Start Lavalink
Run Lavalink with the following command:

```bash
java -jar .\lavalink\Lavalink.jar
```

### 8. Run the Bot
Finally, start the bot with this command:

```bash
python -m bot.main
```


