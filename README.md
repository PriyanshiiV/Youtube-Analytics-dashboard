 📊 YouTube Multi-Channel Analytics Dashboard

This project is a comprehensive solution for analyzing and visualizing data from multiple YouTube channels. Using **Python** and the **YouTube Data API**, we extract real-time statistics from selected channels and visualize the insights through an interactive **Power BI** dashboard.

Whether you're a content creator, digital marketer, or data analyst, understanding how different YouTube channels perform is crucial. This project allows you to:
* Fetch live subscriber, view, and video counts from multiple channels
* Store data for future analysis
* Create a professional dashboard to compare metrics across channels

 🚀 Features

✅ Fetch data from the **YouTube Data API v3**
✅ Analyze multiple channels in one go
✅ Save the data into a structured CSV file
✅ Build interactive **Power BI** visuals for insights
✅ Compare channels side-by-side on key performance metrics

 🔧 Tech Stack

| Tool             | Purpose                              |
| ---------------- | ------------------------------------ |
| Python           | Scripting and data extraction        |
| Pandas           | Data manipulation and CSV export     |
| YouTube Data API | Channel data retrieval               |
| Power BI         | Dashboard creation and visualization |

 📂 Project Structure

```
📁 YouTube-Dashboard/
│
├── yt_data_python.py               # Python script to fetch channel stats
├── multi_channel_stats.csv         # Exported dataset from API
└── Youtube multi-channel dashboard.pbix  # Power BI dashboard file
```

---

 📌 Channels Used

The current setup analyzes the following channels:

* [Google Developers](https://www.youtube.com/@GoogleDevelopers)
* [TEDx Talks](https://www.youtube.com/@TEDxTalks)
* [Netflix](https://www.youtube.com/@Netflix)
* [5-Minute Crafts](https://www.youtube.com/@5MinuteCrafts)
* [BB Ki Vines](https://www.youtube.com/@BBKiVines)

> You can customize and add more channels using their Channel IDs in the script.

---

🛠️ How to Use

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/YouTube-Dashboard.git
cd YouTube-Dashboard
'
 2. Install Requirements


pip install google-api-python-client pandas
```

### 3. Get Your YouTube API Key

* Visit [Google Developers Console](https://console.developers.google.com/)
* Enable YouTube Data API v3
* Generate an API Key and paste it in `yt_data_python.py`

### 4. Run the Script

```bash
python yt_data_python.py
```

This will generate `multi_channel_stats.csv` containing the statistics of each channel.

### 5. Open the Power BI Dashboard

* Open `Youtube multi-channel dashboard.pbix` in Power BI Desktop.
* Refresh the dataset to visualize the latest data.

💡 Future Enhancements

* Add sentiment analysis of video comments
* Track channel growth over time
* Automate daily/weekly data updates
* Deploy a web-based version of the dashboard

🙌 Acknowledgements

* [YouTube Data API](https://developers.google.com/youtube/v3)
* [Google API Client for Python](https://github.com/googleapis/google-api-python-client)
* [Microsoft Power BI](https://powerbi.microsoft.com/)

---

📬 Contact

**Priyanshi Vishwakarma**
📧 Email: *\[pvkdkv@gmail.com]*



