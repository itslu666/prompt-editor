import customtkinter as ctk


def show_buttons(button_frame):
    # open file to get all styles
    with open("./data/styles.txt") as file:
        for line in file.readlines():

            # create button with custom text for each style
            button = ctk.CTkButton(
                button_frame, text=line.strip()
            )  # click event to show next buttons and write into textbox and hide all buttons // image of that style

            button.pack(side="left", padx=10)
