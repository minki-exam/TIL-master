class DList:
    class Node:
        def __init__(self, item, prev, link):  # 노드 생성자
            self.item = item
            self.prev = prev
            self.next = link

    def __init__(self):  # 이중연결리스트 생성자
        self.head = self.Node(None, None, None)
        self.tail = self.Node(None, self.head, None)
        self.head.next = self.tail
        self.size = 0  # 항목 수

    def size(self):
        return self.size

    def is_empty(self):
        return self.size == 0

    def insert_before(self, p, item):  # p 앞에 삽입
        t = p.prev
        n = self.Node(item, t, p)
        p.prev = n
        t.next = n
        self.size += 1

    def insert_after(self, p, item):  # p 다음에 삽입
        t = p.next
        n = self.Node(item, p, t)
        t.prev = n
        p.next = n
        self.size += 1

    def delete(self, x):  # x가 참조하는 노드 삭제
        f = x.prev
        r = x.next
        f.next = r
        r.prev = f
        self.size -= 1
        return x.item

    def print_list(self):  # 리스트 출력
        if self.is_empty():
            print('리스트 비어있음')
        else:
            p = self.head.next
            while p != self.tail:
                if p.next != self.tail:
                    print(p.item, ' <=> ', end='')
                else:
                    print(p.item)
                p = p.next


class EmptyError(Exception):  # underflow 시 에러 처리
    pass

s = DList()
s.insert_after(s.head,'apple')
s.insert_before(s.tail, 'orange')
s.insert_before(s.tail,'cherry')
s.insert_after(s.head.next,'pear')
s.print_list()
print('마지막 노드 삭제 후:\t', end='')
s.delete(s.tail.prev)
s.print_list()
print('맨 끝에 포도 삽입 후:\t', end='')
s.insert_before(s.tail,'grape')
s.print_list()
print('첫 노드 삭제 후:\t', end='')
s.delete(s.head.next)
s.print_list()
print('첫 노드 삭제 후:\t', end='')
s.delete(s.head.next)
s.print_list()
print('첫 노드 삭제 후:\t', end='')
s.delete(s.head.next)
s.print_list()
print('첫 노드 삭제 후:\t', end='')
s.delete(s.head.next)
s.print_list()