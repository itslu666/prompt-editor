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
        label_txt = "Choose an emotion"
        txt_file = "./data/character/body/emotions.txt"
        base_img_file = f"./data/images/{style}/emotions/"
        textbox_input = "\n\nA "

    elif txt_file == "./data/character/body/emotions.txt":
        label_txt = "Choose an age"
        txt_file = "./data/character/body/age.txt"
        base_img_file = f"./data/images/{style}/age/"
        textbox_input = ", "

    elif txt_file == "./data/character/body/age.txt":
        label_txt = "Choose an ethnicity"
        txt_file = "./data/character/body/ethnicity.txt"
        base_img_file = f"./data/images/{style}/ethnicity/"
        textbox_input = ", "

    elif txt_file == "./data/character/body/ethnicity.txt":
        label_txt = "Choose a gender"
        txt_file = "./data/character/body/gender.txt"
        base_img_file = f"./data/images/{style}/gender/"
        textbox_input = " "

    elif txt_file == "./data/character/body/gender.txt":
        label_txt = "Choose the hair length"
        txt_file = "./data/character/body/hair/hair_length.txt"
        base_img_file = f"./data/images/{style}/hair/length/"
        textbox_input = " with "

    elif txt_file == "./data/character/body/hair/hair_length.txt":
        label_txt = "Choose the hair style"
        txt_file = "./data/character/body/hair/hair_style.txt"
        base_img_file = f"./data/images/{style}/hair/style/"
        textbox_input = ", "

    elif txt_file == "./data/character/body/hair/hair_style.txt":
        label_txt = "Choose the hair color"
        txt_file = "./data/character/body/hair/hair_color.txt"
        base_img_file = f"./data/images/{style}/hair_colors/"
        textbox_input = ", "

    elif txt_file == "./data/character/body/hair/hair_color.txt":
        label_txt = "Choose the eye color"
        txt_file = "./data/character/body/eye_color.txt"
        base_img_file = f"./data/images/{style}/eye_colors/"
        textbox_input = " hair. The eye color is "

    elif txt_file == "./data/character/body/eye_color.txt":
        label_txt = "Choose the body type"
        txt_file = "./data/character/body/body_style.txt"
        base_img_file = f"./data/images/{style}/body_style/"
        textbox_input = " and the person looks "

    elif txt_file == "./data/character/body/body_style.txt":
        label_txt = "Choose a hat"
        txt_file = "./data/character/clothing/hat.txt"
        base_img_file = f"./data/images/{style}/clothing/hats/"
        textbox_input = " wearing following clothes: "

    

    with open(txt_file) as file:
        label = ctk.CTkLabel(button_frame, text=label_txt)
        buttons.append(label)
        
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

    buttons[0].pack()
    for button in buttons:
        button.pack(side="left", padx=10, ipady=10)