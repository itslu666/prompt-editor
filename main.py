import customtkinter as ctk
from modules import get_buttons


root = ctk.CTk()
root.geometry("900x600")

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
get_buttons.show_buttons(button_frame)

root.mainloop()
