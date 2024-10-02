import tkinter as tk
import wikipediaapi


def get_wikipedia_info():
    wiki = wikipediaapi.Wikipedia(language='ru',
                                  user_agent="MyWikipediaApp/1.0")
    search_term = entry.get()
    page = wiki.page(search_term)

    if page.exists():
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, page.summary)
        result_text.config(state=tk.DISABLED)
    else:
        result_text.config(state=tk.NORMAL)
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Страница не найдена.")
        result_text.config(state=tk.DISABLED)



root = tk.Tk()
root.resizable(width=False,height=False)
root.title("Поиск по Википедии")


entry = tk.Entry(root, width=50)
entry.pack(pady=10)


search_button = tk.Button(root, text="Найти", command=get_wikipedia_info)
search_button.pack(pady=5)


result_text = tk.Text(root, height=15, width=60, wrap='word', state=tk.DISABLED)
result_text.pack(pady=10)


root.mainloop()
# Karen Bannahyan