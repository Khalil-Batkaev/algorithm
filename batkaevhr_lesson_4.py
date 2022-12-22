# https://habr.com/ru/post/557328/

class Tree:
    BLACK = 'BLACK'
    RED = 'RED'

    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
            self.color = None

    def __init__(self):
        self.root = None

    def add(self, val):
        """
        Основной метод для добавления нового элемента
        Если рута нет, то создаём его. Если он есть, то запускаем рекурсивное добавление нового элемента с постоянной
        локальной (на одном уровне дерева) ребалансировкой относительно рута и нового элемента
        """
        if self.root:
            result = self.add_node(val, self.root)
            self.root = self.rebalance(self.root)
            self.root.color = self.BLACK
            return result
        self.root = self.Node(val)
        self.root.color = self.BLACK
        return True

    def add_node(self, val, node):
        """
        Добавляем новые ноды рекурсивно проходя вглубь дерева (смещаем влево или вправо от рута).
        На каждой итерации локально проводим ребалансировку новой связки нод.
        """
        if node.val == val:
            return False
        # Если новое значение меньше родительского, то влево его
        if val < node.val:
            # Если нода уже есть, то рекурсивно уходим глубже по дереву, если нет, то создаём левую красную ноду
            if node.left:
                result = self.add_node(val, node.left)
                node.left = self.rebalance(node.left)
                return result
            node.left = self.Node(val)
            node.left.color = self.RED
            return True
        # Если новое значение больше родительского, то вправо его
        if val > node.val:
            # Если нода уже есть, то рекурсивно уходим глубже по дереву, если нет, то создаём правую красную ноду
            if node.right:
                result = self.add_node(val, node.right)
                node.right = self.rebalance(node.right)
                return result
            node.right = self.Node(val)
            node.right.color = self.RED
            return True

    def rebalance(self, node):
        is_rebalanced = False
        result = node
        while not is_rebalanced:
            is_rebalanced = True  # Если ни одно условие ребалансировки не сработало, то выход...иначе цикл
            # Если справа оказался красный нод, а слева черный или нет нода, то правый поворот
            if result.right and result.right.color == self.RED and (not result.left or result.left.color == self.BLACK):
                is_rebalanced = False
                result = self.right_swap(result)
            # Если слева два подряд красных нода: ребенок и ребенок ребенка, то левый поворот
            if result.left and result.left.left and result.left.color == result.left.left.color == self.RED:
                is_rebalanced = False
                result = self.left_swap(result)
            # Если два ребенка красные, то смена цвета
            if result.left and result.right and result.left.color == result.right.color == self.RED:
                is_rebalanced = False
                self.color_swap(result)
        return result

    def right_swap(self, node):
        """
        Правый поворот подразумевает смену родительского нода X на правого ребенка Y. Сам родительский нод X становится
        левым ребенком у Y.
        При наличии левого ребенка у правого Y (тот, что станет родительским), этот левый нод становится правым
        ребенком родительского X (тот, который сменился и стал левым).
        Цвет правого ребенка Y становится таким же, как у родительского X, а цвет родительского X становится красным.
        """
        right_child = node.right
        between_child = right_child.left
        right_child.left = node
        node.right = between_child
        right_child.color = node.color
        node.color = self.RED
        return right_child

    def left_swap(self, node):
        """
        Левый поворот подразумевает смену родительского нода Y на левого ребенка X. Сам родительский нод Y становится
        правым ребенком у X.
        При наличии правого ребенка у левого X (тот, что станет родительским), это правый нод становится левым
        ребенком у родительского Y (тот, который сменился и стал правым).
        Цвет левого ребенка X становится таким же, как у родительского Y, а цвет родительского Y становится красным.
        """
        left_child = node.left
        between_child = left_child.right
        left_child.right = node
        node.left = between_child
        left_child.color = node.color
        node.color = self.RED
        return left_child

    def color_swap(self, node):
        """
        Смена цвета детей с красного на черный, а родительского нода на красный
        """
        node.color = self.RED
        node.left.color = node.right.color = self.BLACK

    def search(self, node, val):
        if not node:
            return False
        if node.val == val:
            return True
        if node.val > val:
            return self.search(node.left, val)
        else:
            return self.search(node.right, val)

    def __contains__(self, val):
        return self.search(self.root, val)


if __name__ == '__main__':
    tree = Tree()
    tree.add(6)
    tree.add(4)
    tree.add(5)
    tree.add(2)
    tree.add(7)
    tree.add(1)
    tree.add(10)
    tree.add(3)
    tree_2 = Tree()
    tree_2.add(24)
    tree_2.add(5)
    tree_2.add(1)
    tree_2.add(15)
    tree_2.add(3)
    tree_2.add(8)
    pass
