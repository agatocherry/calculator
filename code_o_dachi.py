#!/usr/bin/env python3
"""
Code-o-dachi: A Programming-Themed Tamagotchi
A virtual pet that loves coding, debugging, and learning new programming languages!
"""

import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
import time
import random
from datetime import datetime, timedelta


class CodeODachi:
    """Main class for the Code-o-dachi virtual pet"""
    
    def __init__(self):
        # Pet basic attributes
        self.name = "Code-o-dachi"
        self.level = 1
        self.experience = 0
        self.age_days = 0
        
        # Coding-themed stats (0-100)
        self.energy = 80
        self.knowledge = 50
        self.debugging_skill = 30
        self.creativity = 40
        self.coffee_level = 70
        self.happiness = 75
        
        # Programming languages known
        self.languages = ["Python"]
        self.current_project = None
        
        # Time tracking
        self.last_update = datetime.now()
        self.birth_time = datetime.now()
        
        # Pet state
        self.is_coding = False
        self.is_debugging = False
        self.is_learning = False
        
        # Available activities
        self.available_languages = [
            "JavaScript", "Java", "C++", "C#", "Go", "Rust", 
            "TypeScript", "Ruby", "PHP", "Swift", "Kotlin"
        ]
        
    def update_stats(self):
        """Update pet stats based on time passage"""
        now = datetime.now()
        time_diff = (now - self.last_update).total_seconds() / 60  # minutes
        
        if time_diff < 1:
            return
        
        # Gradual stat decay over time
        decay_rate = time_diff * 0.5
        self.energy = max(0, self.energy - decay_rate)
        self.coffee_level = max(0, self.coffee_level - decay_rate * 1.5)
        self.happiness = max(0, self.happiness - decay_rate * 0.3)
        
        # Age calculation
        self.age_days = (now - self.birth_time).days
        
        self.last_update = now
        
    def feed_coffee(self):
        """Give coffee to boost energy and coffee level"""
        self.coffee_level = min(100, self.coffee_level + 30)
        self.energy = min(100, self.energy + 20)
        self.happiness = min(100, self.happiness + 10)
        return "☕ *sip* Ahh, much better! Ready to code!"
        
    def start_coding_session(self):
        """Start a coding session"""
        if self.energy < 20:
            return "💤 Too tired to code! Need some rest or coffee first."
        
        if self.coffee_level < 10:
            return "☕ Need coffee to start coding!"
            
        self.is_coding = True
        self.energy -= 15
        self.coffee_level -= 10
        self.experience += random.randint(5, 15)
        self.knowledge = min(100, self.knowledge + random.randint(2, 8))
        self.happiness = min(100, self.happiness + 15)
        
        messages = [
            "💻 Starting a new coding session...",
            "🚀 Building something awesome!",
            "⌨️ Fingers flying across the keyboard!",
            "🎯 In the zone! Logic flows like poetry.",
            "🔥 Creating elegant solutions!"
        ]
        
        return random.choice(messages)
        
    def debug_code(self):
        """Debug existing code"""
        if self.energy < 25:
            return "🐛 Too tired to debug! Bugs are winning..."
            
        if not self.is_coding and self.experience < 10:
            return "🤔 Need some coding experience before debugging!"
            
        self.is_debugging = True
        self.energy -= 20
        self.debugging_skill = min(100, self.debugging_skill + random.randint(3, 10))
        self.experience += random.randint(3, 8)
        self.happiness = min(100, self.happiness + 20)
        
        debug_messages = [
            "🔍 Found the bug! It was hiding in plain sight.",
            "🐛➡️✨ Squashed another bug! Code is cleaner now.",
            "🕵️ Detective mode: ON. Logic errors, beware!",
            "🛠️ Refactoring for better maintainability...",
            "✅ All tests passing! Bug-free zone achieved!"
        ]
        
        return random.choice(debug_messages)
        
    def learn_language(self):
        """Learn a new programming language"""
        if self.energy < 30:
            return "📚 Too tired to learn! Brain needs rest."
            
        if self.knowledge < 40:
            return "🎓 Need more general knowledge before learning new languages!"
            
        available = [lang for lang in self.available_languages if lang not in self.languages]
        if not available:
            return "🎉 Wow! You know all the languages! True polyglot programmer!"
            
        new_language = random.choice(available)
        self.languages.append(new_language)
        self.is_learning = True
        self.energy -= 25
        self.knowledge = min(100, self.knowledge + random.randint(5, 15))
        self.experience += random.randint(10, 20)
        self.happiness = min(100, self.happiness + 25)
        
        return f"🌟 Learned {new_language}! Now knows: {', '.join(self.languages)}"
        
    def rest(self):
        """Let the pet rest to recover energy"""
        self.energy = min(100, self.energy + 40)
        self.happiness = min(100, self.happiness + 10)
        self.is_coding = False
        self.is_debugging = False
        self.is_learning = False
        
        rest_messages = [
            "😴 Taking a well-deserved break...",
            "🛌 Power nap complete! Ready for more coding!",
            "🧘 Meditation on clean code principles...",
            "🌱 Recharging creativity batteries...",
            "💤 Dreams of elegant algorithms..."
        ]
        
        return random.choice(rest_messages)
        
    def get_status(self):
        """Get current pet status"""
        status = "healthy"
        if self.energy < 20:
            status = "tired"
        elif self.coffee_level < 20:
            status = "needs coffee"
        elif self.happiness < 30:
            status = "stressed"
        elif self.is_coding:
            status = "coding"
        elif self.is_debugging:
            status = "debugging"
        elif self.is_learning:
            status = "learning"
            
        return status
        
    def get_pet_display(self):
        """Get ASCII art representation of the pet based on current state"""
        status = self.get_status()
        
        if status == "tired":
            return """
        ╭─────╮
        │ -.- │  💤
        │  ◡  │
        ╰─────╯
        """
        elif status == "needs coffee":
            return """
        ╭─────╮
        │ @.@ │  ☕?
        │  ◇  │
        ╰─────╯
        """
        elif status == "coding":
            return """
        ╭─────╮
        │ ^.^ │  💻
        │  ◡  │
        ╰─────╯
        """
        elif status == "debugging":
            return """
        ╭─────╮
        │ ಠ.ಠ │  🐛
        │  ◇  │
        ╰─────╯
        """
        elif status == "learning":
            return """
        ╭─────╮
        │ *.* │  📚
        │  ◡  │
        ╰─────╯
        """
        elif status == "stressed":
            return """
        ╭─────╮
        │ x.x │  😰
        │  ◇  │
        ╰─────╯
        """
        else:  # healthy/happy
            return """
        ╭─────╮
        │ ^.^ │  ✨
        │  ◡  │
        ╰─────╯
        """
        
    def save_to_file(self, filename="pet_data.json"):
        """Save pet data to file"""
        data = {
            "name": self.name,
            "level": self.level,
            "experience": self.experience,
            "age_days": self.age_days,
            "energy": self.energy,
            "knowledge": self.knowledge,
            "debugging_skill": self.debugging_skill,
            "creativity": self.creativity,
            "coffee_level": self.coffee_level,
            "happiness": self.happiness,
            "languages": self.languages,
            "current_project": self.current_project,
            "last_update": self.last_update.isoformat(),
            "birth_time": self.birth_time.isoformat(),
            "is_coding": self.is_coding,
            "is_debugging": self.is_debugging,
            "is_learning": self.is_learning
        }
        
        with open(filename, 'w') as f:
            json.dump(data, f, indent=2)
            
    def load_from_file(self, filename="pet_data.json"):
        """Load pet data from file"""
        if not os.path.exists(filename):
            return False
            
        try:
            with open(filename, 'r') as f:
                data = json.load(f)
                
            self.name = data.get("name", "Code-o-dachi")
            self.level = data.get("level", 1)
            self.experience = data.get("experience", 0)
            self.age_days = data.get("age_days", 0)
            self.energy = data.get("energy", 80)
            self.knowledge = data.get("knowledge", 50)
            self.debugging_skill = data.get("debugging_skill", 30)
            self.creativity = data.get("creativity", 40)
            self.coffee_level = data.get("coffee_level", 70)
            self.happiness = data.get("happiness", 75)
            self.languages = data.get("languages", ["Python"])
            self.current_project = data.get("current_project")
            self.last_update = datetime.fromisoformat(data.get("last_update", datetime.now().isoformat()))
            self.birth_time = datetime.fromisoformat(data.get("birth_time", datetime.now().isoformat()))
            self.is_coding = data.get("is_coding", False)
            self.is_debugging = data.get("is_debugging", False)
            self.is_learning = data.get("is_learning", False)
            
            return True
        except Exception as e:
            print(f"Error loading save file: {e}")
            return False


class CodeODachiGUI:
    """GUI interface for Code-o-dachi"""
    
    def __init__(self):
        self.pet = CodeODachi()
        self.pet.load_from_file()
        
        self.root = tk.Tk()
        self.root.title("Code-o-dachi 💻✨")
        self.root.geometry("600x700")
        self.root.resizable(False, False)
        
        # Configure style
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        self.setup_gui()
        self.update_display()
        
        # Auto-save and update every 30 seconds
        self.root.after(30000, self.auto_update)
        
    def setup_gui(self):
        """Setup the GUI layout"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Title
        title_label = ttk.Label(main_frame, text="Code-o-dachi 💻✨", 
                               font=("Arial", 18, "bold"))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # Pet display
        self.pet_display = tk.Text(main_frame, height=8, width=25, 
                                  font=("Courier", 12), justify="center",
                                  relief="solid", borderwidth=2)
        self.pet_display.grid(row=1, column=0, columnspan=2, pady=(0, 20))
        
        # Pet info
        info_frame = ttk.LabelFrame(main_frame, text="Pet Info", padding="10")
        info_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        self.name_label = ttk.Label(info_frame, text="", font=("Arial", 12, "bold"))
        self.name_label.grid(row=0, column=0, columnspan=2, pady=(0, 10))
        
        self.age_label = ttk.Label(info_frame, text="")
        self.age_label.grid(row=1, column=0, sticky=tk.W)
        
        self.languages_label = ttk.Label(info_frame, text="", wraplength=400)
        self.languages_label.grid(row=2, column=0, columnspan=2, sticky=tk.W)
        
        # Stats frame
        stats_frame = ttk.LabelFrame(main_frame, text="Stats", padding="10")
        stats_frame.grid(row=3, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # Progress bars for stats
        self.stats_bars = {}
        stats = [
            ("Energy", "energy"),
            ("Knowledge", "knowledge"),
            ("Debugging", "debugging_skill"),
            ("Creativity", "creativity"),
            ("Coffee", "coffee_level"),
            ("Happiness", "happiness")
        ]
        
        for i, (label, attr) in enumerate(stats):
            ttk.Label(stats_frame, text=f"{label}:").grid(row=i, column=0, sticky=tk.W, padx=(0, 10))
            progress = ttk.Progressbar(stats_frame, length=200, mode='determinate')
            progress.grid(row=i, column=1, sticky=(tk.W, tk.E), pady=2)
            self.stats_bars[attr] = progress
            
        # Actions frame
        actions_frame = ttk.LabelFrame(main_frame, text="Actions", padding="10")
        actions_frame.grid(row=4, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=(0, 20))
        
        # Action buttons
        buttons = [
            ("☕ Give Coffee", self.give_coffee),
            ("💻 Code Session", self.start_coding),
            ("🐛 Debug Code", self.debug_code),
            ("📚 Learn Language", self.learn_language),
            ("😴 Rest", self.rest),
            ("💾 Save", self.save_game)
        ]
        
        for i, (text, command) in enumerate(buttons):
            row = i // 2
            col = i % 2
            btn = ttk.Button(actions_frame, text=text, command=command, width=15)
            btn.grid(row=row, column=col, padx=5, pady=5)
            
        # Message area
        self.message_text = tk.Text(main_frame, height=6, width=70, wrap=tk.WORD,
                                   relief="solid", borderwidth=1)
        self.message_text.grid(row=5, column=0, columnspan=2, pady=(0, 10))
        
        # Configure grid weights
        main_frame.columnconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)
        
    def update_display(self):
        """Update all display elements"""
        self.pet.update_stats()
        
        # Update pet display
        self.pet_display.delete(1.0, tk.END)
        self.pet_display.insert(tk.END, self.pet.get_pet_display())
        self.pet_display.config(state=tk.DISABLED)
        
        # Update pet info
        self.name_label.config(text=f"{self.pet.name} (Level {self.pet.level})")
        self.age_label.config(text=f"Age: {self.pet.age_days} days | Status: {self.pet.get_status()}")
        self.languages_label.config(text=f"Languages: {', '.join(self.pet.languages)}")
        
        # Update stats bars
        for attr, bar in self.stats_bars.items():
            value = getattr(self.pet, attr)
            bar['value'] = value
            
            # Color coding for bars
            if value < 20:
                bar.config(style="red.Horizontal.TProgressbar")
            elif value < 50:
                bar.config(style="yellow.Horizontal.TProgressbar")
            else:
                bar.config(style="green.Horizontal.TProgressbar")
                
    def add_message(self, message):
        """Add a message to the message area"""
        timestamp = datetime.now().strftime("%H:%M:%S")
        self.message_text.insert(tk.END, f"[{timestamp}] {message}\n")
        self.message_text.see(tk.END)
        
    def give_coffee(self):
        """Give coffee to the pet"""
        message = self.pet.feed_coffee()
        self.add_message(message)
        self.update_display()
        
    def start_coding(self):
        """Start a coding session"""
        message = self.pet.start_coding_session()
        self.add_message(message)
        self.update_display()
        
    def debug_code(self):
        """Debug code"""
        message = self.pet.debug_code()
        self.add_message(message)
        self.update_display()
        
    def learn_language(self):
        """Learn a new language"""
        message = self.pet.learn_language()
        self.add_message(message)
        self.update_display()
        
    def rest(self):
        """Let pet rest"""
        message = self.pet.rest()
        self.add_message(message)
        self.update_display()
        
    def save_game(self):
        """Save the game"""
        self.pet.save_to_file()
        self.add_message("💾 Game saved successfully!")
        
    def auto_update(self):
        """Auto-update function called periodically"""
        self.update_display()
        self.pet.save_to_file()
        self.root.after(30000, self.auto_update)  # Schedule next update
        
    def run(self):
        """Start the GUI application"""
        self.add_message("🎉 Welcome to Code-o-dachi! Your coding companion is ready!")
        self.add_message("💡 Tip: Keep your pet happy by coding, debugging, and learning new languages!")
        
        # Handle window closing
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.root.mainloop()
        
    def on_closing(self):
        """Handle window closing"""
        self.pet.save_to_file()
        self.root.destroy()


def main():
    """Main function to run the application"""
    try:
        app = CodeODachiGUI()
        app.run()
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    main()