import tkinter as tk
from tkinter import simpledialog
import winsound

class Alerter:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()

        self.message = simpledialog.askstring("Reminder", "Enter your reminder message:")
        while self.message and len(self.message) > 25:
            self.message = simpledialog.askstring("Reminder", "Message too long. Enter a message with 25 characters or less:", initialvalue=self.message)
        
        self.interval = simpledialog.askinteger("Interval", "Enter reminder interval (minutes):")
        self.beep = simpledialog.askstring("Beep", "To beep or not (y/n)")
        while self.beep and self.beep not in ['y', 'n']:
            self.beep = simpledialog.askstring("Beep", "Type (y for yes) or (n for no):")

        if not self.message or not self.interval:
            print("Invalid input. Exiting program.")
            self.root.destroy()
            return

        print(f"Reminder set! Message: {self.message}, Interval: {self.interval} seconds.")
        
        try:
            self.root.after(self.interval * 1000, self.show_alert)
            self.root.mainloop()
        except KeyboardInterrupt:
            print("Unalerted!")
            exit()

    def show_alert(self):
        alert = tk.Toplevel()
        alert.attributes('-fullscreen', True)
        alert.configure(bg='#1e1e2e', padx=20, pady=20)

        msg_label = tk.Label(alert, text=self.message, font=("Helvetica", 75, "bold"), fg="#cdd6f4", bg="#1e1e2e")
        msg_label.pack(expand=True)

        button_frame = tk.Frame(alert, bg='#1e1e2e')
        button_frame.pack(pady=100)

        dismiss_btn = tk.Button(button_frame, text="Dismiss", command=lambda: self.exit_program(alert), font=("Helvetica", 24), bg="#f38ba8", fg="#1e1e2e", relief="flat", padx=20, pady=10)
        dismiss_btn.pack(side=tk.LEFT, padx=20)

        snooze_btn = tk.Button(button_frame, text="Snooze", command=lambda: self.snooze_reminder(alert), font=("Helvetica", 24), bg="#fab387", fg="#1e1e2e", relief="flat", padx=20, pady=10)
        snooze_btn.pack(side=tk.LEFT, padx=20)

        alert.bind("<Escape>", lambda e: self.exit_program(alert))

        winsound.Beep(1000, 500) if self.beep == 'y' else None

    def exit_program(self, alert):
        if alert:
            alert.destroy()
        print("Reminded!")
        self.root.quit()
        exit()

    def snooze_reminder(self, alert):
        alert.destroy()
        snooze_time = simpledialog.askinteger("Snooze", "Enter snooze time (seconds):")
        if snooze_time:
            print(f"reminder snoozed for {snooze_time} seconds.")
            self.root.after(snooze_time * 1000, self.show_alert)
        else:
            print("invalid snooze time. returning to main reminder.")
            self.root.after(1000, self.show_alert)


if __name__ == "__main__":
    Alerter()
