from node import Node
class OrderedList:
    def __init__(self):
        self.head = None
    '''
    - add(elemet) method will add element in ascending order
    '''
    def add(self,element):
        temp = self.head
        previous = None

        while temp != None:
            if temp.data > element :
                break
            previous, temp = temp, temp.next
        
        new_node = Node(element)
        if previous == None :
            new_node.next, self.head = self.head, new_node
        else :
            new_node.next, previous.next = temp, new_node

    '''
        - display() method will display elements according to insertion order
    '''
    def display(self):
        if self.head == None :           #Check wether list is empty or not
            print('List is empty')
        else :
            temp = self.head
            while temp != None:
                print(temp.data,end=' ')
                temp = temp.next

    '''
        - size() method will return  size of list ie. numbers of element present in list
    '''
    def size(self):
        temp = self.head
        count = 0
        while temp != None:
            count +=1
            temp = temp.next
        return count

    '''
        - remove(element) is used to remove an element, if it is present in list
    '''
    def remove(self,data):
        temp = self.head
        previous = None
        while True:
            if temp.data == data:
                break
            previous,temp = temp,temp.next
        if previous == None :
            self.head = self.head.next
        else:
            previous.next = temp.next

    '''
        - search(element) method will return true if element is present in list
            else it will return false
    '''
    def search(self,data):
        temp = self.head
        while temp != None:
            if temp.data == data:
                return True
            temp = temp.next
        return False

    '''
        - index(element) method will take element as an argument and will return
            index of element if pressent, else will return -1
    '''
    def index(self,data):
        temp = self.head
        count = 0
        while temp != None:
            if temp.data == data:
                return count
            count += 1
            temp = temp.next
        return -1
    
    '''
        - empty() will check wether list is empty or not, it will return boolean values
    '''
    def empty(self):
        return self.head is None

    '''
        - pop() method will delete last element and return value 
    '''
    def pop(self):
        if self.head == None:
            print('list is empty')
        else:
            temp = self.head
            while temp.next != None:
                previous = temp         #previous is to store information of last node
                temp = temp.next
            value = temp.data           #storing last node data in value variable 
            if previous.next != None:
                previous.next = None    #removing last element by assigning it to None
            else:
                head = None             #if there is only 1 element then it will dereffer head
            return value

    '''
        - pop_index(index) method with argument index will take an index, if element present
            at that index it will remove that element and will return element at that index
        - If element is not there then it will return -1
    '''
    def pop_index(self,index_at):
        if self.size()-1 < index_at:
            return -1
        temp = self.head
        if index_at == 0 and head != None :
            value = head.data              #storing data of head in value tag
            head = head.next
            return value
        while index_at >1 :
            index_at -= 1
            temp = temp.next
        if temp.next != None:
            value = temp.next.data         #storing data of given index in value tag
            temp.next = temp.next.next     #escaping given index 
            return value


