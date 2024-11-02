import turtle

def draw_branch(branch_length, level):
    if level == 0:
        return
    
    # Малюємо гілку
    turtle.forward(branch_length)
    
    # Малюємо праву гілку
    turtle.right(30)  # Поворот вправо
    draw_branch(branch_length * 0.7, level - 1)  # Зменшуємо довжину гілки на 30%
    
    # Повертаємось назад
    turtle.left(60)  # Поворот вліво
    draw_branch(branch_length * 0.7, level - 1)  # Знову зменшуємо довжину гілки на 30%
    
    # Повертаємось у вихідне положення
    turtle.right(30)  # Повертаємось вправо
    turtle.backward(branch_length)  # Повертаємось назад

def main():
    level = int(input("Введіть рівень рекурсії (ціле число): "))
    
    turtle.speed(0)  # Найшвидше малювання
    turtle.left(90)  # Поворот на 90 градусів вліво
    turtle.up()      # Піднімаємо перо
    turtle.backward(100)  # Переміщаємо назад, щоб було місце для дерева
    turtle.down()    # Опускаємо перо
    turtle.color("orange")  # Колір гілок
    
    draw_branch(100, level)  # Початкова довжина гілки - 100
    
    turtle.done()  # Завершуємо малювання

if __name__ == "__main__":
    main()