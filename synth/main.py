import tkinter as tk


def main():
    window = tk.Tk()
    window.tk.call("tk", "scaling", 10.0)
    window.title("synth")

    label = tk.Label(window, text="Hello, World!")
    label.config(font=("Helvetica", 5))
    label.pack()

    window.mainloop()


if __name__ == "__main__":
    main()

