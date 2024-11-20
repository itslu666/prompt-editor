import customtkinter as ctk
from modules import show_buttons
import test


root = ctk.CTk()
root.geometry("900x600")
ctk.set_appearance_mode("system")

# make frames
# make a horizontal scrollable frame
button_frame = ctk.CTkScrollableFrame(root, orientation="horizontal")
prompt_frame = ctk.CTkFrame(root)

# make prompt tb
prompt_tb = ctk.CTkTextbox(prompt_frame)

# place frames + textbox
button_frame.pack(expand=True, fill="both", pady=(10, 0), padx=10)
prompt_frame.pack(expand=True, fill="both", pady=10, padx=10)
prompt_tb.pack(expand=True, fill="both", padx=10, pady=10)

# show all buttons / start the process
# show_buttons.style_buttons(button_frame, prompt_tb)
show_buttons.style_buttons(button_frame, prompt_tb)

root.mainloop()
