import tkinter as tk
from customtkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import sys
import subprocess

def authenticate(username, password):
    return username == "" and password == ""

def login_clicked():
    username = username_entry.get()
    password = password_entry.get()
    if authenticate(username, password):
        login_status_label.configure(text="Login successful", text_color="green")
        open_main_window()
    else:
        login_status_label.configure(text="Invalid username or password", text_color="red")
def open_main_window():
    global main_window, img_Navigation, img_AI_Chatbot, img_Hospital_System, img_talksys

    app.withdraw()

    main_window = tk.Toplevel(app)
    main_window.title("Main Window")
    main_window.geometry("850x450")
    main_window.resizable(0, 0)
    main_window.protocol("WM_DELETE_WINDOW", terminate_app)

    # side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(850, 450))
    # CTkLabel(master=main_window, text="", image=side_img).pack(expand=True, side="left")

    button_frame = CTkFrame(master=main_window, width=300, height=600)
    button_frame.pack_propagate(0)
    button_frame.pack(expand=True, side="right")

    CTkLabel(master=button_frame, text="Welcome to the Main Window!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 16)).pack(anchor="w", pady=(50, 5), padx=(25, 0))

    img_nav = Image.open("Navigation.png").resize((200, 150), Image.LANCZOS)
    img_off = Image.open("AI.png").resize((607, 607), Image.LANCZOS)
    img_hos = Image.open("Hospital.png").resize((350, 100), Image.LANCZOS)
    img_talk = Image.open("talk.png").resize((350, 100), Image.LANCZOS)

    img_Navigation = ImageTk.PhotoImage(img_nav)
    img_AI_Chatbot = ImageTk.PhotoImage(img_off)
    img_Hospital_System = ImageTk.PhotoImage(img_hos)
    img_talksys = ImageTk.PhotoImage(img_talk)

    def option1_clicked():
        main_window.withdraw()
        script_path = "/home/marwan/GUI/GeminiArabic.py"
        python_executable = sys.executable
        subprocess.Popen([python_executable, script_path])

    def start_chatbot(language):
        main_window.withdraw()
        script_path = "/home/marwan/GUI/GeminiArabic.py" if language == "Arabic" else "/home/marwan/GUI/GeminiEnglish.py"
        python_executable = sys.executable
        subprocess.Popen([python_executable, script_path])

    def option2_clicked():
        main_window.withdraw()
        side_img_data = Image.open("side-img.png")
        side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(700, 600))
        language_window = tk.Toplevel(main_window)
        language_window.title("Language Model")
        language_window.geometry("850x450")
        language_window.protocol("WM_DELETE_WINDOW", lambda: return_to_main_window(language_window))
        CTkLabel(master=language_window, text="", image=side_img).pack(expand=True, side="left")

        tk.Label(language_window, text="Please select a language").pack(padx=95, pady=10)
        tk.Button(language_window, text="Arabic", command=lambda: start_chatbot("Arabic")).pack(padx=10, pady=10)
        tk.Button(language_window, text="English", command=lambda: start_chatbot("English")).pack(padx=10, pady=10)
        tk.Button(language_window, text="Return", command=lambda: return_to_main_window(language_window)).pack(padx=10, pady=10)

    def option3_clicked():
        main_window.withdraw()
        open_clinic_options_window()

    def option4_clicked():
        main_window.withdraw()
        create_TALK_WITH_ME_window(main_window)


    # Upper frame for top two buttons
    upper_frame = tk.Frame(main_window)
    upper_frame.pack(expand=True, fill="both")

    # Lower frame for bottom two buttons
    lower_frame = tk.Frame(main_window)
    lower_frame.pack(expand=True, fill="both")


    # Top left button (Navigation)
    btn_frame1 = tk.Frame(upper_frame, width=400, height=200)
    btn_frame1.pack_propagate(0)
    btn_frame1.pack(pady=10, padx=10, side="left")
    tk.Label(btn_frame1, text="Navigation", font=("Arial", 12)).pack()
    btn_Navigation = tk.Button(btn_frame1, image=img_Navigation, command=option1_clicked)
    btn_Navigation.image = img_Navigation
    btn_Navigation.pack(expand=True)

    # Top right button (AI Chatbot)
    btn_frame2 = tk.Frame(upper_frame, width=400, height=200)
    btn_frame2.pack_propagate(0)
    btn_frame2.pack(pady=10, padx=10, side="right")
    tk.Label(btn_frame2, text="AI Chatbot", font=("Arial", 12)).pack()
    btn_AI = tk.Button(btn_frame2, image=img_AI_Chatbot, command=option2_clicked)
    btn_AI.image = img_AI_Chatbot
    btn_AI.pack(expand=True)

    # Bottom left button (Clinic)
    btn_frame3 = tk.Frame(lower_frame, width=400, height=200)
    btn_frame3.pack_propagate(0)
    btn_frame3.pack(pady=10, padx=10, side="left")
    tk.Label(btn_frame3, text="Clinic", font=("Arial", 12)).pack()
    btn_Hospital = tk.Button(btn_frame3, image=img_Hospital_System, command=option3_clicked)
    btn_Hospital.image = img_Hospital_System
    btn_Hospital.pack(expand=True)

    # Bottom right button (Talk With ME)
    btn_frame4 = tk.Frame(lower_frame, width=400, height=200)
    btn_frame4.pack_propagate(0)
    btn_frame4.pack(pady=10, padx=10, side="right")
    tk.Label(btn_frame4, text="Talk With ME", font=("Arial", 12)).pack()
    btn_Talk = tk.Button(btn_frame4, image=img_talksys, command=option4_clicked)
    btn_Talk.image = img_talksys
    btn_Talk.pack(expand=True)

    # Centering the frames inside the main_window
    upper_frame.place(relx=0.5, rely=0.35, anchor="center")
    lower_frame.place(relx=0.5, rely=0.65, anchor="center")


def open_clinic_options_window():
    clinic_options_window = tk.Toplevel(main_window)
    clinic_options_window.title("Clinic Options")
    clinic_options_window.geometry("850x450")
    clinic_options_window.configure(bg="#d3d3d3")
    clinic_options_window.protocol("WM_DELETE_WINDOW", lambda: return_to_main_window(clinic_options_window))

    def open_available_clinic():
        python_executable = sys.executable
        script_path = "/home/marwan/GUI/importtime.py"
        subprocess.Popen([python_executable, script_path])

    def open_scheduling():
        open_colored_window("Scheduling", "#90ee90")

    available_button = tk.Button(clinic_options_window, text="Available Clinic", command=open_available_clinic, bg="#601E88", fg="#ffffff", font=("Arial", 12, "bold"))
    available_button.pack(pady=50)

    scheduling_button = tk.Button(clinic_options_window, text="Scheduling", command=open_scheduling, bg="#601E88", fg="#ffffff", font=("Arial", 12, "bold"))
    scheduling_button.pack(pady=50)

    return_button = tk.Button(clinic_options_window, text="Return back", command=lambda: return_to_main_window(clinic_options_window), bg="#601E88", fg="#ffffff", font=("Arial", 12, "bold"))
    return_button.place(x=900, y=10)

def open_colored_window(title, color):
    colored_window = tk.Toplevel(clinic_options_window)
    colored_window.title(title)
    colored_window.geometry("850x450")
    colored_window.configure(bg=color)
    colored_window.protocol("WM_DELETE_WINDOW", lambda: return_to_clinic_options(colored_window))

    return_button = tk.Button(colored_window, text="Return back", command=lambda: return_to_clinic_options(colored_window), bg="#601E88", fg="#ffffff", font=("Arial", 12, "bold"))
    return_button.pack(pady=50)

def return_to_clinic_options(current_window):
    current_window.destroy()
    clinic_options_window.deiconify()

def return_to_main_window(current_window):
    current_window.destroy()
    main_window.deiconify()

def create_TALK_WITH_ME_window(parent):
    talk_with_me_window = tk.Toplevel(parent)
    talk_with_me_window.title("Talk With ME Window")
    talk_with_me_window.geometry("850x450")
    talk_with_me_window.protocol("WM_DELETE_WINDOW", lambda: return_to_main_window(talk_with_me_window))

    def toggle_entry():
        if entry_frame.winfo_viewable():
            entry_frame.pack_forget()
        else:
            entry_frame.pack(pady=10)

    def send_message(event=None):
        message = entry_message.get()
        if message:
            messagebox.showinfo("Message Sent", f"Message: {message}")
            entry_message.delete(0, tk.END)

    return_button = tk.Button(talk_with_me_window, text="Return back", command=lambda: return_to_main_window(talk_with_me_window))
    return_button.place(x=10, y=10)

    toggle_button = tk.Button(talk_with_me_window, text="Text Me", command=toggle_entry)
    toggle_button.pack(pady=25)
    toggle_button.place(x=350, y=100)

    speak_button = tk.Button(talk_with_me_window, text="Speak to Me")
    speak_button.pack(pady=75)
    speak_button.place(x=335, y=400)

    terminate_button = tk.Button(talk_with_me_window, text="End Talk", bg="red", fg="white")
    terminate_button.pack(pady=10)
    terminate_button.place(x=335, y=500)

    entry_frame = tk.Frame(talk_with_me_window)

    entry_message = tk.Entry(entry_frame, width=50)
    entry_message.pack(pady=10)

    entry_message.bind("<Return>", send_message)

    send_button = tk.Button(entry_frame, text="Send", command=send_message, bg="green", fg="white")
    send_button.pack(pady=10)

    entry_frame.pack_forget()

def terminate_app():
    app.quit()
    app.destroy()
    sys.exit()

app = CTk()
app.title("AASTMT")
app.geometry("850x450")
app.resizable(0, 0)
app.protocol("WM_DELETE_WINDOW", terminate_app)
# Load images
side_img_data = Image.open("side-img.png")
email_icon_data = Image.open("email-icon.png")
password_icon_data = Image.open("password-icon.png")
google_icon_data = Image.open("google-icon.png")

# Create CTkImage instances
side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(550, 450))
email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20, 20))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17, 17))
google_icon = CTkImage(dark_image=google_icon_data, light_image=google_icon_data, size=(17, 17))

# Create widgets for the login screen
CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

frame = CTkFrame(master=app, width=300, height=480, fg_color="#ffffff")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 24)).pack(anchor="w", pady=(50, 5), padx=(50, 0))
CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left", font=("Arial Bold", 12)).pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Username:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
username_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000")
username_entry.pack(anchor="w", padx=(25, 0))

CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left", font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
password_entry = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, text_color="#000000", show="*")
password_entry.pack(anchor="w", padx=(25, 0))

# Login button
login_button = CTkButton(master=frame, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12), text_color="#ffffff", width=225, command=login_clicked)
login_button.pack(anchor="w", pady=(40, 0), padx=(25, 0))

# Continue With Google button (with icon only)
google_button = CTkButton(master=frame, fg_color="#EEEEEE", hover_color="#EEEEEE", width=225, image=google_icon)
google_button.pack(anchor="w", pady=(20, 0), padx=(25, 0))

# Login status label
login_status_label = CTkLabel(master=frame, text="", text_color="green")
login_status_label.pack()

try:
    app.mainloop()
except KeyboardInterrupt:
    terminate_app()
