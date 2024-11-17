import customtkinter as ctk
from PIL import Image
from modules import textbox_manager


def style_buttons(button_frame, textbox):
    buttons = []

    # open file to get all styles
    with open("./data/styles.txt") as file:
        for line in file.readlines():

            # create button with custom text for each style
            button = ctk.CTkButton(
                button_frame,
                text=line.strip(),
                corner_radius=100,
                command=lambda line=line: (
                    textbox_manager.write_text(textbox, line.strip() + "\n\n"),
                    emotion_buttons(buttons, button_frame, textbox),
                ),
                compound="top",
                fg_color="transparent",
                hover_color="grey",
                text_color=(
                    "#F0F0F0" if ctk.get_appearance_mode() == "Dark" else "#2E2E2E"
                ),
                image=ctk.CTkImage(
                    Image.open(
                        f"./data/images/{line.strip().replace(" ", "_").lower()}.png"
                    ),
                    size=(200, 200),
                ),
            )
            buttons.append(button)

        for button in buttons:
            button.pack(side="left", padx=10, ipady=10)


def emotion_buttons(buttons, button_frame, textbox):
    # destroy all style buttons
    for button in buttons:
        button.destroy()

    # clear all buttons from list to add new
    buttons.clear()

    # open the file and add new buttons
    with open("./data/character/body/emotions.txt") as file:
        for line in file.readlines():
            button = ctk.CTkButton(
                button_frame,
                text=line.strip(),
                corner_radius=100,
                command=lambda line=line: (
                    textbox_manager.write_text(textbox, "A " + line.strip() + " "),
                    age_buttons(buttons, button_frame, textbox),
                ),
                compound="top",
                fg_color="transparent",
                hover_color="grey",
                text_color=(
                    "#F0F0F0" if ctk.get_appearance_mode() == "Dark" else "#2E2E2E"
                ),
            )

            buttons.append(button)

        for button in buttons:
            button.pack(side="left", padx=10, ipady=10)


def age_buttons(buttons, button_frame, textbox): ...
