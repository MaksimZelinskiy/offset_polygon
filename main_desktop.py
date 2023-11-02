import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Зсув полігону
def shift_polygon(polygon, segment_index, shift_amount):

    # перевірка потрібних елементів для роботи
    if segment_index < 0 or segment_index >= len(polygon):
        # помилка
        messagebox.showerror("У вас сталося помилка", f"Неправильний індекс сегменту (макс: {len(polygon)-1})")

        return polygon

    # копіювання полігону
    new_polygon = polygon.copy()

    # зсув сегмента (двух точек)
    for index_segment in [segment_index-1, segment_index]:
        x, y = new_polygon[index_segment]

        if int(shift_amount) >= 0:
            x += abs(shift_amount)
        elif int(shift_amount) < 0:
            x -= abs(shift_amount)

        new_polygon[index_segment] = (x, y)

    return new_polygon


# Візуалізація полігону (малювання його)
def visualize_polygon(polygon, title):
    # стирання попереднього
    ax.clear()

    if len(polygon) > 1:

        # цикл малювання та зʼєднання крапок
        prv_element = None
        for element in polygon:

            if prv_element != None:

                # зʼєднання попереднього елемента з новим
                ax.plot([element[0], prv_element[0]], [element[1], prv_element[1]],
                         marker='o', linestyle='-', color='b')

            # створення попереднього елемента
            prv_element = element

    else:

        for element in polygon:
            ax.plot([element[0]], [element[1]],
                    marker='o', linestyle='-', color='b')

    # створення заголовка
    ax.set_title(title)
    fig_canvas.draw()


# Функціонал для зсува
def shift_button_clicked():
    try:
        # введення індексу сегмента
        segment_index = int(segment_index_entry.get())

        # введення величини для зсуву
        shift_amount = float(shift_amount_entry.get())

    except ValueError:
        # помилка
        messagebox.showerror("У вас сталося помилка", "Неправильний формат вводу.\n\nВведіть цифру.")
        return

    # отримення глобального полігону
    global polygon

    # зсув сегменту
    shifted_polygon = shift_polygon(polygon, segment_index, shift_amount)

    # змінення полігону
    polygon = shifted_polygon
    # візуалізація полігону
    visualize_polygon(polygon, "Полігон після зсуву")


def start_shift_clicked():
    global polygon

    global segment_index_entry
    global shift_amount_entry

    # Створення елементів (кнопки, лейбели і тд.)
    segment_index_label = tk.Label(main_w, text="Індекс сегменту:")
    segment_index_label.pack()
    segment_index_entry = tk.Entry(main_w, background='#2edaff')
    segment_index_entry.pack()

    shift_amount_label = tk.Label(main_w, text="Величину для зсуву:")
    shift_amount_label.pack()
    shift_amount_entry = tk.Entry(main_w, background='#2edaff')
    shift_amount_entry.pack()

    shift_button = tk.Button(main_w, text="Зсунути сегмент", command=shift_button_clicked)
    shift_button.pack()

    # візуалізація початкового полігону
    visualize_polygon(polygon, "Полігон")

    # видалення елементів (кнопки, лейбели і тд.) для створення полігону
    add_button.pack_forget()
    start_button.pack_forget()

    x_dot_label.pack_forget()
    y_dot_label.pack_forget()

    x_dot_entry.pack_forget()
    y_dot_entry.pack_forget()


def add_dot_button_clicked():
    try:
        x_amount = float(x_dot_entry.get())
        y_amount = float(y_dot_entry.get())

    except ValueError:
        # помилка
        messagebox.showerror("У вас сталося помилка", "Неправильний формат вводу.\n\nВведіть цифру.")
        return

    global polygon

    # добавлення нових крапок для полігону
    polygon.append((x_amount, y_amount))
    visualize_polygon(polygon, "Полігон")


# полігон
polygon = []

# Створення вікна
main_w = tk.Tk()
main_w.title("Обробка полігонів ВІЯР")

# Створення фігури для вставки у вікно
figure = Figure(figsize=(6, 6))
ax = figure.add_subplot(111)
fig_canvas = FigureCanvasTkAgg(figure, master=main_w)
fig_canvas.get_tk_widget().pack()

# Створення елементів для додавання крапок (кнопки, лейбели і тд.)
x_dot_label = tk.Label(main_w, text="Введіть точки по x для полігону:")
x_dot_label.pack()
x_dot_entry = tk.Entry(main_w, background='#2edaff')
x_dot_entry.pack()

y_dot_label = tk.Label(main_w, text="Введіть точки по y для полігону:")
y_dot_label.pack()
y_dot_entry = tk.Entry(main_w, background='#2edaff')
y_dot_entry.pack()

start_button = tk.Button(main_w, text="Почати зсув", command=start_shift_clicked)
add_button = tk.Button(main_w, text="Добавити", command=add_dot_button_clicked)
add_button.pack()
start_button.pack()

# Відкриття
main_w.mainloop()
