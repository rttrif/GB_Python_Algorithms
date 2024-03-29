"""
На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу).
Сколько рукопожатий было?

Примечание. Решите задачу при помощи построения графа.
"""


def handshakes_count(n):
    nodes = [i for i in range(1, n + 1)]  # вершины графа - люди с номерами от 1 до n включительно
    edges = []  # рёбра графа - уникальные урукопожатия

    for i in nodes:
        for j in range(i + 1, n + 1):
            edges.append((i, j))

    print(f'Количество рукопожатий: {len(edges)}')
    print(f'Пары рукопожатий: {edges}')


n = int(input('Веедите количество людей: '))
handshakes_count(n)
