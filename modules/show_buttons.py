import customtkinter as ctk
from modules import textbox_manager
from PIL import Image


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
                    textbox_manager.write_text(textbox, line.strip()),
                    generate_buttons(
                        buttons,
                        button_frame,
                        textbox,
                        line.strip().replace(" ", "_").lower(),
                        None,
                    ),
                ),
                compound="top",
                fg_color="transparent",
                hover_color="grey",
                text_color=(
                    "#F0F0F0" if ctk.get_appearance_mode() == "Dark" else "#2E2E2E"
                ),
                image=ctk.CTkImage(
                    Image.open(
                        f"./data/images/styles/{line.strip().replace(" ", "_").lower()}.png"
                    ),
                    size=(200, 200),
                ),
            )
            buttons.append(button)

        for button in buttons:
            button.pack(side="left", padx=10, ipady=10)


def generate_buttons(buttons, button_frame, textbox, style, txt_file):
    for button in buttons:
        button.destroy()

    buttons.clear()

    # my definition of state machine xD
    if not txt_file:
        txt_file = "./data/character/body/emotions.txt"
        base_img_file = f"./data/images/{style}/emotions/"
        textbox_input = "\n\nA "

    elif txt_file == "./data/character/body/emotions.txt":
        txt_file = "./data/character/body/age.txt"
        base_img_file = f"./data/images/{style}/age/"
        textbox_input = ", "

    elif txt_file == "./data/character/body/age.txt":
        txt_file = "./data/character/body/ethnicity.txt"
        base_img_file = f"./data/images/{style}/ethnicity/"
        textbox_input = ", "

    elif txt_file == "./data/character/body/ethnicity.txt":
        txt_file = "./data/character/body/gender.txt"
        base_img_file = f"./data/images/{style}/gender/"
        textbox_input = " "

    elif txt_file == "./data/character/body/gender.txt":
        txt_file = "./data/character/body/hair/hair_length.txt"
        base_img_file = f"./data/images/{style}/hair/length/"
        textbox_input = " with "

    elif txt_file == "./data/character/body/hair/hair_length.txt":
        txt_file = "./data/character/body/hair/hair_style.txt"
        base_img_file = f"./data/images/{style}/hair/style/"
        textbox_input = ", "

    elif txt_file == "./data/character/body/hair/hair_style.txt":
        txt_file = "./data/colors.txt"
        base_img_file = f"./data/images/colors/"
        textbox_input = ", "

    with open(txt_file) as file:
        for line in file.readlines():
            button = ctk.CTkButton(
                button_frame,
                text=line.strip(),
                corner_radius=100,
                command=lambda line=line: (
                    textbox_manager.write_text(textbox, textbox_input + line.strip()),
                    generate_buttons(buttons, button_frame, textbox, style, txt_file),
                ),
                compound="top",
                fg_color="transparent",
                hover_color="grey",
                text_color=(
                    "#F0F0F0" if ctk.get_appearance_mode() == "Dark" else "#2E2E2E"
                ),
                # image=ctk.CTkImage(
                #     Image.open(base_img_file + f"{line.strip().lower().replace(" ", "_")}.png"),
                #     size=(200, 200),
                # ),
            )

            buttons.append(button)

        file.close()

    for button in buttons:
        button.pack(side="left", padx=10, ipady=10)