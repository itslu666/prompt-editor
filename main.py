import customtkinter as ctk

root = ctk.CTk()
root.geometry("900x600")

# make frames
button_frame = ctk.CTkScrollableFrame(root, border_width=2, orientation="horizontal")
prompt_frame = ctk.CTkFrame(root, border_width=2)
bottom_frame = ctk.CTkFrame(root, border_width=2)

# make prompt tb
prompt_tb = ctk.CTkTextbox(prompt_frame)

# place frames
button_frame.place(relx=0, rely=0, relwidth=1, relheight=0.5)
prompt_frame.place(relx=0, rely=0.5, relwidth=1, relheight=0.4)
bottom_frame.place(relx=0, rely=0.9, relwidth=1, relheight=0.1) 

root.mainloop()
