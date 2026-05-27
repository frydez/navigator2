def generate_html_files():
    for i in range(1, 101):
        # Определяем блок (каждый блок из 4 точек)
        # Но связь между блоками нелинейная (7->3, 11->7, 15->11 и т.д.)
        
        # Влево/вправо/разворот в пределах блока из 4 точек
        block_start = ((i - 1) // 4) * 4 + 1
        block_end = block_start + 3
        
        # Нормализованная позиция в блоке (1,2,3,4)
        pos_in_block = i - block_start + 1
        
        # Влево (counter-clockwise)
        if pos_in_block == 1:
            left = block_end
        else:
            left = i - 1
        
        # Вправо (clockwise)
        if pos_in_block == 4:
            right = block_start
        else:
            right = i + 1
        
        # Разворот (на 180 градусов) - через один
        # 1<->3, 2<->4
        if pos_in_block == 1:
            u_turn = block_start + 2  # 3
        elif pos_in_block == 2:
            u_turn = block_start + 3  # 4
        elif pos_in_block == 3:
            u_turn = block_start       # 1
        else:  # pos_in_block == 4
            u_turn = block_start + 1   # 2
        
        # Вперед - сложная логика из примеров:
        # Точка 1 -> 5
        # Точка 5 -> 9
        # Точка 7 -> 3 (переход в предыдущий блок!)
        # Остальные точки: вперед неактивен
        
        if pos_in_block == 1:
            # Первая точка блока: вперед в первую точку следующего блока
            forward_link = i + 4
            if forward_link <= 100:
                forward_text = f"<a href='{forward_link}.html'>вперед</a>"
            else:
                forward_text = "вперед"
        elif pos_in_block == 3 and block_start > 1:
            # Третья точка блока (кроме первого блока): вперед в первую точку ПРЕДЫДУЩЕГО блока
            # 7->3, 11->7, 15->11 и т.д.
            forward_link = block_start - 3  # предыдущий блок, позиция 3? Нет, 7->3 это предыдущий блок позиция 3
            # Проверяем: блок 5-8, позиция 3 -> это точка 7, вперед в 3 (блок 1-4, позиция 3)
            forward_link = block_start - 3  # дает 2? Неправильно. Давайте вручную:
            # 7: block_start=5, forward_link = 5-2 = 3
            forward_link = block_start - 2
            forward_text = f"<a href='{forward_link}.html'>вперед</a>"
        else:
            forward_text = "вперед"
        
        # Особый случай: точка 3 в первом блоке (3.html) вперед неактивен
        if i == 3:
            forward_text = "вперед"
        
        # Генерируем HTML
        html_content = f"""<html>
<head>
    <title>Точка {i}</title>
</head>
<body>
    <table>
        <tr>
            <td colspan="3" align="center">
                <img src="nawi pic\\{i}.jpg" width=900>
            </td>
        </tr>
        <tr>
            <td width=300>
                &nbsp;
            </td>
            <td width=300 align="center">
                {forward_text}
            </td>
            <td width=300>
                &nbsp;
            </td>
        </tr>
        <tr>
            <td align="center">
                <a href='{left}.html'>влево</a>
            </td>
            <td align="center">
                <a href='{u_turn}.html'>разворот</a>
            </td>
            <td align="center">
                <a href='{right}.html'>вправо</a>
            </td>
        </tr>
    </table>
</body>
</html>"""
        
        filename = f"{i}.html"
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print(f"Создан файл: {filename}")

if __name__ == "__main__":
    generate_html_files()
    print("Генерация завершена! Создано 100 HTML-файлов.")
