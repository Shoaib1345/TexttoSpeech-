import tkinter as tk
from tkinter import ttk, messagebox
import pyttsx3


class TextToSpeechApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Text to Speech Converter")
        self.root.geometry("700x500")
        self.root.configure(bg="#f5f5f5")

        self.init_tts()
        self.create_widgets()

    def init_tts(self):
        self.engine = pyttsx3.init()
        self.voices = self.engine.getProperty("voices")
        self.current_text = ""
        self.is_speaking = False

    def create_widgets(self):
        # Title label
        title = tk.Label(
            self.root,
            text="Text to Speech Converter",
            font=("Arial", 18, "bold"),
            bg="#3f51b5",
            fg="white",
            pady=10
        )
        title.pack(fill="x")

        # Text input area
        self.text_input = tk.Text(self.root, wrap="word", font=("Arial", 12), height=10)
        self.text_input.pack(padx=20, pady=10, fill="both", expand=True)

        # Control buttons
        button_frame = tk.Frame(self.root, bg="#f5f5f5")
        button_frame.pack(pady=5)

        self.speak_btn = tk.Button(button_frame, text="Speak Text", command=self.speak_text,
                                   bg="#4CAF50", fg="white", font=("Arial", 10), width=12)
        self.speak_btn.grid(row=0, column=0, padx=5)

        self.pause_btn = tk.Button(button_frame, text="Pause", command=self.pause_speech,
                                   bg="#FF9800", fg="white", font=("Arial", 10), width=12)
        self.pause_btn.grid(row=0, column=1, padx=5)

        self.resume_btn = tk.Button(button_frame, text="Resume", command=self.resume_speech,
                                    bg="#2196F3", fg="white", font=("Arial", 10), width=12)
        self.resume_btn.grid(row=0, column=2, padx=5)

        self.stop_btn = tk.Button(button_frame, text="Stop", command=self.stop_speech,
                                  bg="#F44336", fg="white", font=("Arial", 10), width=12)
        self.stop_btn.grid(row=0, column=3, padx=5)

        # Voice, Rate, Volume controls
        settings_frame = tk.Frame(self.root, bg="#f5f5f5")
        settings_frame.pack(pady=10, fill="x", padx=20)

        tk.Label(settings_frame, text="Voice:", font=("Arial", 10), bg="#f5f5f5").grid(row=0, column=0, sticky="w")
        self.voice_combo = ttk.Combobox(settings_frame, font=("Arial", 10), width=30)
        self.voice_combo['values'] = [voice.name for voice in self.voices]
        self.voice_combo.current(0)
        self.voice_combo.grid(row=0, column=1, padx=10, pady=5)
        self.voice_combo.bind("<<ComboboxSelected>>", self.set_voice)

        tk.Label(settings_frame, text="Speed:", font=("Arial", 10), bg="#f5f5f5").grid(row=1, column=0, sticky="w")
        self.rate_slider = tk.Scale(settings_frame, from_=100, to=300, orient="horizontal",
                                    command=self.set_rate, bg="#f5f5f5")
        self.rate_slider.set(200)
        self.rate_slider.grid(row=1, column=1, padx=10, sticky="ew")

        tk.Label(settings_frame, text="Volume:", font=("Arial", 10), bg="#f5f5f5").grid(row=2, column=0, sticky="w")
        self.volume_slider = tk.Scale(settings_frame, from_=0, to=100, orient="horizontal",
                                      command=self.set_volume, bg="#f5f5f5")
        self.volume_slider.set(80)
        self.volume_slider.grid(row=2, column=1, padx=10, sticky="ew")

        # Status Label
        self.status_label = tk.Label(self.root, text="Ready", font=("Arial", 10), bg="#f5f5f5", fg="gray")
        self.status_label.pack(pady=5)

    def speak_text(self):
        self.stop_speech()
        text = self.text_input.get("1.0", "end").strip()
        if not text:
            messagebox.showwarning("Warning", "Please enter some text to speak.")
            return

        try:
            self.current_text = text
            self.engine.say(text)
            self.engine.runAndWait()
            self.status_label.config(text="Finished speaking")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred:\n{str(e)}")

    def pause_speech(self):
        # pyttsx3 does not support pause directly
        self.stop_speech()
        self.status_label.config(text="Speech paused (stopped internally)")

    def resume_speech(self):
        # pyttsx3 does not support resume, simulate by replaying
        if self.current_text:
            self.speak_text()
            self.status_label.config(text="Resuming speech...")

    def stop_speech(self):
        self.engine.stop()
        self.status_label.config(text="Speech stopped")

    def set_rate(self, val):
        self.engine.setProperty("rate", int(val))

    def set_volume(self, val):
        self.engine.setProperty("volume", int(val) / 100)

    def set_voice(self, event):
        index = self.voice_combo.current()
        self.engine.setProperty("voice", self.voices[index].id)


if __name__ == "__main__":
    root = tk.Tk()
    app = TextToSpeechApp(root)
    root.mainloop()