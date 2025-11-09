from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import sys
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import threading

class YouTubeVideoExtractor:
    def __init__(self, root):
        self.root = root
        self.root.title("YouTube Channel Video URL Extractor")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        
        # Variables
        self.is_running = False
        self.driver = None
        
        # Setup UI
        self.setup_ui()
        
    def setup_ui(self):
        # Configure root grid
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))
        
        # Configure main_frame to center content
        main_frame.grid_columnconfigure(0, weight=1)
        
        # Title
        title_label = ttk.Label(main_frame, text="YouTube Channel Video URL Extractor", 
                                font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, pady=(0, 20))
        
        # URL Input
        ttk.Label(main_frame, text="YouTube Channel URL:", font=('Arial', 10)).grid(
            row=1, column=0, pady=(0, 5))
        
        self.url_entry = ttk.Entry(main_frame, width=60, font=('Arial', 10), justify='center')
        self.url_entry.grid(row=2, column=0, pady=(0, 20), ipady=5)
        self.url_entry.insert(0, "https://www.youtube.com/channel")
        
        # Buttons frame
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=3, column=0, pady=(0, 20))
        
        self.start_button = ttk.Button(button_frame, text="Start Extraction", 
                                       command=self.start_extraction, width=20)
        self.start_button.pack(side=tk.LEFT, padx=5)
        
        self.stop_button = ttk.Button(button_frame, text="Stop", 
                                      command=self.stop_extraction, width=20, state=tk.DISABLED)
        self.stop_button.pack(side=tk.LEFT, padx=5)
        
        # Progress bar
        self.progress = ttk.Progressbar(main_frame, mode='indeterminate', length=400)
        self.progress.grid(row=4, column=0, pady=(0, 10))
        
        # Status label
        self.status_label = ttk.Label(main_frame, text="Ready", font=('Arial', 10))
        self.status_label.grid(row=5, column=0, pady=(0, 10))
        
        # Log text area
        ttk.Label(main_frame, text="Log:", font=('Arial', 10, 'bold')).grid(
            row=6, column=0, pady=(0, 5))
        
        self.log_text = scrolledtext.ScrolledText(main_frame, width=65, height=15, 
                                                  font=('Consolas', 9), state=tk.DISABLED)
        self.log_text.grid(row=7, column=0, pady=(0, 10))
        
        # Footer
        footer = ttk.Label(main_frame, text="© 2025 - Extract all video URLs from any YouTube channel", 
                          font=('Arial', 8), foreground='gray')
        footer.grid(row=8, column=0, pady=(10, 0))
        
    def log(self, message):
        self.log_text.config(state=tk.NORMAL)
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)
        self.log_text.config(state=tk.DISABLED)
        self.root.update()
        
    def update_status(self, status):
        self.status_label.config(text=status)
        self.root.update()
        
    def start_extraction(self):
        channel_url = self.url_entry.get().strip()
        
        if not channel_url:
            messagebox.showerror("Error", "Please enter a YouTube channel URL!")
            return
        
        if not ('youtube.com' in channel_url or 'youtu.be' in channel_url):
            messagebox.showerror("Error", "Please enter a valid YouTube URL!")
            return
        
        self.is_running = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.progress.start()
        
        # Clear log
        self.log_text.config(state=tk.NORMAL)
        self.log_text.delete(1.0, tk.END)
        self.log_text.config(state=tk.DISABLED)
        
        # Start extraction in thread
        thread = threading.Thread(target=self.extract_videos, args=(channel_url,))
        thread.daemon = True
        thread.start()
        
    def stop_extraction(self):
        self.is_running = False
        self.update_status("Stopping...")
        self.log("⚠ Stop requested by user...")
        if self.driver:
            try:
                self.driver.quit()
            except:
                pass
        
    def extract_videos(self, channel_url):
        try:
            # Extract channel name BEFORE modifying URL
            channel_name = "channel"
            original_url = channel_url.rstrip('/')
            
            try:
                # Remove protocol and www
                url_part = original_url.replace('https://', '').replace('http://', '').replace('www.', '')
                url_part = url_part.replace('youtube.com/', '')
                
                # Get channel name from different URL formats
                if url_part.startswith('@'):
                    channel_name = url_part.split('@')[1].split('/')[0]
                elif url_part.startswith('c/'):
                    channel_name = url_part.split('c/')[1].split('/')[0]
                elif url_part.startswith('user/'):
                    channel_name = url_part.split('user/')[1].split('/')[0]
                elif url_part.startswith('channel/'):
                    channel_name = url_part.split('channel/')[1].split('/')[0]
                else:
                    # Direct channel name like youtube.com/oyunerbabi
                    channel_name = url_part.split('/')[0]
                
                # Remove invalid file name characters
                channel_name = re.sub(r'[<>:"/\\|?*]', '', channel_name)
                self.log(f"📝 Channel name extracted: {channel_name}")
            except Exception as e:
                self.log(f"⚠ Could not extract channel name: {e}")
            
            # Convert to videos page
            if not channel_url.endswith('/videos'):
                channel_url = channel_url.rstrip('/') + '/videos'
            
            self.log(f"🌐 Opening channel: {channel_url}")
            self.update_status("Setting up browser...")
            
            # Chrome options
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--no-sandbox')
            chrome_options.add_argument('--disable-dev-shm-usage')
            chrome_options.add_argument('--disable-gpu')
            chrome_options.add_argument('--window-size=1920,1080')
            chrome_options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36')
            chrome_options.add_argument('--log-level=3')
            
            # Start WebDriver
            self.log("🚀 Starting Chrome WebDriver...")
            self.driver = webdriver.Chrome(
                service=Service(ChromeDriverManager().install()), 
                options=chrome_options
            )
            
            self.driver.get(channel_url)
            self.update_status("Loading channel page...")
            time.sleep(3)
            
            # Close cookie popup if exists
            try:
                cookie_button = WebDriverWait(self.driver, 5).until(
                    EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Reject all' or contains(text(), 'Reject')]"))
                )
                cookie_button.click()
                self.log("✓ Cookie popup closed")
                time.sleep(1)
            except:
                pass
            
            self.log("📜 Scrolling to load all videos...")
            self.update_status("Loading all videos (this may take a while)...")
            
            # Scroll to bottom
            last_height = self.driver.execute_script("return document.documentElement.scrollHeight")
            video_count_prev = 0
            no_change_count = 0
            
            while self.is_running:
                # Scroll down
                self.driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
                time.sleep(2)
                
                # Check new height
                new_height = self.driver.execute_script("return document.documentElement.scrollHeight")
                
                # Count videos
                video_elements = self.driver.find_elements(By.XPATH, "//a[@id='video-title-link']")
                video_count = len(video_elements)
                
                if video_count > video_count_prev:
                    self.log(f"📹 Found {video_count} videos...")
                    self.update_status(f"Found {video_count} videos...")
                    video_count_prev = video_count
                    no_change_count = 0
                else:
                    no_change_count += 1
                
                # Check if reached bottom
                if new_height == last_height:
                    no_change_count += 1
                    if no_change_count >= 3:
                        self.log("✓ Reached end of page")
                        break
                else:
                    last_height = new_height
            
            if not self.is_running:
                self.log("⚠ Extraction stopped by user")
                self.finish_extraction(False)
                return
            
            # Collect all video URLs
            self.log("🔗 Extracting video URLs...")
            self.update_status("Extracting URLs...")
            
            video_elements = self.driver.find_elements(By.XPATH, "//a[@id='video-title-link']")
            
            video_urls = []
            for element in video_elements:
                href = element.get_attribute('href')
                if href and '/watch?v=' in href:
                    video_id = re.search(r'/watch\?v=([a-zA-Z0-9_-]{11})', href)
                    if video_id:
                        clean_url = f"https://www.youtube.com/watch?v={video_id.group(1)}"
                        if clean_url not in video_urls:
                            video_urls.append(clean_url)           
           
            
            # Save to file

            if(channel_name==""):
                channel_name="Extracted"
            filename = f"{channel_name}_Links.txt"
            with open(filename, 'w', encoding='utf-8') as f:
                for url in video_urls:
                    f.write(url + '\n')
            
            self.log(f"\n{'='*50}")
            self.log(f"✅ SUCCESS!")
            self.log(f"{'='*50}")
            self.log(f"📊 Total videos found: {len(video_urls)}")
            self.log(f"💾 Saved to: {filename}")
            self.log(f"{'='*50}\n")
            
            self.update_status(f"✅ Complete! {len(video_urls)} videos extracted")
            
            messagebox.showinfo("Success", 
                              f"Successfully extracted {len(video_urls)} videos!\n\nSaved to: {filename}")
            
            self.finish_extraction(True)
            
        except Exception as e:
            self.log(f"\n❌ ERROR: {str(e)}")
            self.update_status("❌ Error occurred")
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")
            self.finish_extraction(False)
        
    def finish_extraction(self, success):
        self.is_running = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.progress.stop()
        
        if self.driver:
            try:
                self.driver.quit()
            except:
                pass
            self.driver = None
        
        if not success:
            self.update_status("Ready")

def main():
    root = tk.Tk()
    app = YouTubeVideoExtractor(root)
    root.mainloop()

if __name__ == "__main__":
    main()