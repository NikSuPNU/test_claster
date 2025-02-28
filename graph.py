import os
import graphviz

def generate_folder_graph(root_dir, output_file="folder_structure"):
    """
    Создаёт графическое изображение структуры папок с помощью Graphviz.

    :param root_dir: Путь к корневой папке проекта
    :param output_file: Имя выходного файла (без расширения)
    """
    dot = graphviz.Digraph(format="png")
    max_depth = 3  # Глубина
    for root, dirs, _ in os.walk(root_dir):
        for dir_name in dirs:
            parent = os.path.relpath(root, root_dir)  # Относительный путь к родителю
            child = os.path.join(parent, dir_name).replace("\\", "/")
                # Вычисляем текущую глубину относительно корневой директории
            depth = root[len(root_dir):].count(os.sep)
            
            if depth >= max_depth:
                # Очищаем список dirs, чтобы os.walk не заходил глубже
                dirs.clear()
            # Корневой узел
            if parent == ".":
                dot.node(dir_name, dir_name, shape="folder")
            else:
                dot.node(child, dir_name, shape="folder")
                dot.edge(parent, child)

    dot.render(output_file, view=True)
    print(f"Граф сохранён в {output_file}.png")

# Укажи путь к своему проекту
project_path = "путь_к_проекту"
generate_folder_graph('C:\\Users\\sheva\\pet_pjt', "folder_structure")
