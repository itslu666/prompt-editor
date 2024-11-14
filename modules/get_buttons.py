import customtkinter as ctk
from PIL import Image


def show_buttons(button_frame):
    # open file to get all styles
    with open("./data/styles.txt") as file:
        for line in file.readlines():

            # create button with custom text for each style
            button = ctk.CTkButton(
                button_frame,
                text=line.strip(),
                image=ctk.CTkImage(
                    Image.open(
                        f"./data/images/{line.strip().replace(" ", "_").lower()}.png"
                    ),
                    size=(250, 250),
                ),
            )  # click event to show next buttons and write into textbox and hide all buttons // image of that style

            button.pack(side="left", padx=10)
