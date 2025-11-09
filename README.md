# 🎥 YouTube Channel Video URL Extractor

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Platform](https://img.shields.io/badge/Platform-Windows-lightgrey.svg)

Extract **ALL** video URLs from any YouTube channel with a single click! No API key required. Works with channels of any size.

## ✨ Features

- ✅ **Extract ALL videos** from any YouTube channel
- ✅ **No API key required** - uses web scraping
- ✅ **User-friendly GUI** - simple and intuitive interface
- ✅ **Real-time progress** monitoring
- ✅ **Automatic setup** - one-click installation
- ✅ **Stop/Resume** capability
- ✅ **Clean output** format (one URL per line)
- ✅ **Works with any channel size** - from small to millions of videos

## 🚀 Quick Start

### Prerequisites

1. **Install Python** (one-time setup)
   - Download from: [python.org/downloads](https://www.python.org/downloads/)
   - ⚠️ **IMPORTANT**: Check "Add Python to PATH" during installation
   - Click "Install Now"

2. **Install Chrome Browser** (if not already installed)

### Installation & Usage

1. **Clone or download this repository**
   ```bash
   git clone https://github.com/yourusername/youtube-video-extractor.git
   cd youtube-video-extractor
   ```

2. **Run the program**
   - **Windows**: Double-click `INSTALL_AND_RUN.bat`
   - **Manual**: Run `python extractor.py`

3. **Extract videos**
   - Enter YouTube channel URL
   - Click "Start Extraction"
   - Wait for completion
   - Find your file: `<ChannelName>Links.txt`

## 📖 Usage Guide

### Supported URL Formats

The tool accepts any of these YouTube channel URL formats:

```
https://www.youtube.com/channelname
https://www.youtube.com/c/channelname
https://www.youtube.com/channel/CHANNEL_ID
https://www.youtube.com/user/username
```

### Example

**Input:**
```
https://www.youtube.com/oyunerbabi
```

**Output:**
```
oyunerbabiLinks.txt
```

**File Contents:**
```
https://www.youtube.com/watch?v=VIDEO_ID_1
https://www.youtube.com/watch?v=VIDEO_ID_2
https://www.youtube.com/watch?v=VIDEO_ID_3
...
```

## 📁 Project Structure

```
youtube-video-extractor/
├── extractor.py              # Main program file
├── INSTALL_AND_RUN.bat       # One-click installer & launcher (Windows)
├── requirements.txt          # Python dependencies
└── README.md                 # This file
```

## 🔧 Manual Installation

If you prefer to install dependencies manually:

```bash
pip install selenium webdriver-manager
python extractor.py
```

## 💡 How It Works

1. **Opens the channel** using Selenium WebDriver
2. **Scrolls automatically** to load all videos
3. **Extracts video URLs** from the page
4. **Saves to file** with channel name

## ⚙️ Technical Details

- **Language**: Python 3.7+
- **GUI Framework**: Tkinter
- **Web Automation**: Selenium + Chrome WebDriver
- **Driver Management**: webdriver-manager (auto-updates)

## ⚡ Performance

| Channel Size | Estimated Time |
|--------------|----------------|
| < 100 videos | 1-2 minutes    |
| 100-500 videos | 3-5 minutes  |
| 500-1000 videos | 5-10 minutes |
| 1000+ videos | 10-15 minutes  |

*Note: Time varies based on internet speed and system performance*

## 🐛 Troubleshooting

### "Python is not installed" error
- Install Python from [python.org](https://www.python.org/downloads/)
- Ensure "Add Python to PATH" is checked during installation

### "extractor.py not found" error
- Make sure all files are in the same directory
- Don't rename `extractor.py`

### Program doesn't start
- Right-click `INSTALL_AND_RUN.bat`
- Select "Run as administrator"

### Chrome version error
- Update your Chrome browser to the latest version
- Restart the program (WebDriver auto-updates)

### Slow extraction
- This is normal for large channels
- Progress is shown in real-time
- You can stop and save partial results anytime

### "Channel not found" error
- Verify the URL is correct
- Ensure the channel is public
- Try using a different URL format

## 🎯 Use Cases

- 📊 **Backup** channel video lists
- 🔍 **Research** and analysis
- 📝 **Create playlists** from channel content
- 💾 **Archive** purposes
- 📈 **Content management**
- 🎓 **Educational** data collection

## ⚠️ Important Notes

- Requires active **internet connection**
- Works with **public channels only**
- Does **not** require YouTube login
- Does **not** download videos (only URLs)
- Respects YouTube's structure
- **Completely free** to use

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Selenium WebDriver for browser automation
- webdriver-manager for easy driver management
- Python Tkinter for the GUI

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Troubleshooting](#-troubleshooting) section
2. Open an [Issue](https://github.com/yourusername/youtube-video-extractor/issues)
3. Make sure Python and Chrome are up to date

## 🔄 Updates

To update to the latest version:

```bash
git pull origin main
```

No reinstallation needed - just replace the files.

---

<div align="center">

**Made with ❤️ for easy video list extraction**

⭐ Star this repo if you find it useful!

</div>