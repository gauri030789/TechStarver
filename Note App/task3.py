import tkinter as tk
from tkinter import messagebox, scrolledtext

class NotesApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Notes App")

        # Text area for notes
        self.notes_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=40, height=10)
        self.notes_text.pack(pady=10)

        # Buttons
        button_frame = tk.Frame(master)
        button_frame.pack(pady=10)

        add_button = tk.Button(button_frame, text="Add Note", command=self.add_note)
        add_button.grid(row=0, column=0, padx=10)

        display_button = tk.Button(button_frame, text="Display Notes", command=self.display_notes)
        display_button.grid(row=0, column=1, padx=10)

        delete_button = tk.Button(button_frame, text="Delete Note", command=self.delete_note)
        delete_button.grid(row=0, column=2, padx=10)

        search_button = tk.Button(button_frame, text="Search Notes", command=self.search_notes)
        search_button.grid(row=0, column=3, padx=10)

    def add_note(self):
        note_text = self.notes_text.get("1.0", "end-1c")
        if note_text.strip() != "":
            with open("notes.txt", "a") as f:
                f.write(note_text + "\n")
            messagebox.showinfo("Note Added", "Your note has been added.")
            self.notes_text.delete("1.0", tk.END)
        else:
            messagebox.showwarning("Empty Note", "Cannot add an empty note.")

    def display_notes(self):
        try:
            with open("notes.txt", "r") as f:
                notes = f.readlines()
            notes_display = "\n".join(notes)
            messagebox.showinfo("Your Notes", notes_display)
        except FileNotFoundError:
            messagebox.showwarning("No Notes Found", "No notes found. Add some notes first.")

    def delete_note(self):
        try:
            with open("notes.txt", "r") as f:
                notes = f.readlines()
            if notes:
                notes_display = "\n".join(notes)
                note_to_delete = messagebox.askquestion("Delete Note", f"Select note to delete:\n\n{notes_display}")
                if note_to_delete == "yes":
                    # Implement deletion logic here
                    pass  # Placeholder for deletion logic
            else:
                messagebox.showwarning("No Notes Found", "No notes found. Add some notes first.")
        except FileNotFoundError:
            messagebox.showwarning("No Notes Found", "No notes found. Add some notes first.")

    def search_notes(self):
        search_term = messagebox.askstring("Search Notes", "Enter search keyword:")
        if search_term:
            try:
                with open("notes.txt", "r") as f:
                    notes = f.readlines()
                matching_notes = [note for note in notes if search_term.lower() in note.lower()]
                if matching_notes:
                    notes_display = "\n".join(matching_notes)
                    messagebox.showinfo("Matching Notes", notes_display)
                else:
                    messagebox.showinfo("No Matches", f"No notes found matching '{search_term}'.")
            except FileNotFoundError:
                messagebox.showwarning("No Notes Found", "No notes found. Add some notes first.")
        else:
            messagebox.showwarning("Invalid Search", "Please enter a valid search keyword.")

if __name__ == "__main__":
    root = tk.Tk()
    app = NotesApp(root)
    root.mainloop()
