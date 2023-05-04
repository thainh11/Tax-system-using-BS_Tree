from node_tax import *
from Payer_Tax import *
from BSTree import *

tree= BStree()
#1
codeList = []
def inputData():
    while True:
        global code
        code = input("Enter taxpayer's code: ")
        if code not in codeList:
            codeList.append(code)
            break
        else:
            print("Code has been existed!\n")
            continue
    global name
    name = input("Enter taxpayer's name: ")

    while True:
        global income
        try:
            income = float(input("Enter taxpayer's income: "))
        except:
            print("Income must be a number!\n")
            continue
        if income > 0:
            break
        else:
            print("Income should be positive!")
            continue

    while True:
        global deduction
        try:
            deduction = float(input("Enter taxpayer's deduction amount: "))
        except:
            print("Deduction must be a number!")
            continue
        if deduction >= 0 and deduction < income:
            break
        else:
            print("Deduction should be non-negative and less than income!\n")
            continue


def loadFile():
    global codeList
    file = input("Enter file name: ")
    with open(file, 'a') as f:
        pass    
    with open(file, 'r') as f:
        records = f.readlines()
    if records == []: 
        print("Nothing in file")
        return
    i = 0
    for record in records:
        record.strip(' \n')
        words = record.split(';')
        code = words[0]
        name = words[1]
        income = float(words[2])
        deduction = float(words[3])
        if code not in codeList and income > 0 and deduction >= 0 and deduction < income:
            node1 = Node(Payer(code, name, income, deduction))
            if i == 0:
                tree.root = node1
            else:
                tree.insert(node1)
            i += 1
        codeList.append(code)
    balanceTree()
#2
def insert_Input():
    inputData()
    payer = Node(Payer(code, name, income, deduction))
    tree.insert(payer)
    balanceTree()

#3 
def in_Order_():
    tree.in_Order(tree.root)

#4
def pre_Order_():
    tree.pre_Order(tree.root)

#5
def breadth_First_():
    tree.breadth_First()

#6
def in_OrderFile():
    file = input("Enter file name: ")
    tree1 = BStree()
    with open(file, 'r') as f:
        records = f.readlines()
    if records == []: 
        print("Nothing in file")
        return
    for record in records:
        record.strip('')
        words = record.split(';')
        code = words[0]
        name = words[1]
        income = float(words[2])
        deduction = float(words[3])
        if income > 0 and deduction >= 0 and deduction < income:
            node = Node(Payer(code, name, income, deduction))
            tree1.insert(node)
    tree1.in_Order(tree1.root)

#7
def searchCode(code):
    print(f" \n{tree.findNode(code)}")

#8 
def deleteCode(code):
    if tree.isEmpty():
        print("Nothing in the list")
    else:
        tree.delete_by_copy(tree.root, code)
        balanceTree()
#9 
def balanceTree():
    tree.turnLeft(tree.in_OrderNode(tree.root))
    tree.balance_Tree(tree.root)

#10
def countTaxpayer():
    print(f"Number of taxpayers: {tree.count(tree.root)}")

print("        ______AVL TREE TAX DATA______")


list1='''
        1. Load data from file
        2. Input and insert data
        3. In-order traverse
        4. Pre-order traverse
        5. Breadth-first traverse
        6. In-order traverse to file
        7. Search by code
        8. Delete by code by copying
        9. Simply balance (bs tree)
        10. Count the number of taxpayers
    '''
print()
print("      Income tax calculation         ")


while True:
    print(list1)
    try:
        choice = int(input("Your selection (0 -> 10): "))
    except:
        print("Wrong input")
        continue

    if choice == 0:
        print("\nSystem out. Good bye!")
        exit()

    elif choice == 1:
        loadFile()
        print()
        print("Load successfully!")           
    
    elif choice == 2:
        insert_Input()
        print()
        print("Add record successfully!")       
    
    elif choice == 3:
        print("| {} | {} | {} | {} | {} |".format("Code".center(8), "Name".center(20), "Income".center(10),
                                                        "Deduction".center(12), 'Tax'.center(10)))
        print("-"*76)
        in_Order_()
    
    elif choice == 4:
        print("| {} | {} | {} | {} | {} |".format("Code".center(8), "Name".center(20), "Income".center(10),
                                                        "Deduction".center(12), 'Tax'.center(10)))
        print("-"*76)
        pre_Order_()

    elif choice == 5:
        print("| {} | {} | {} | {} | {} |".format("Code".center(8), "Name".center(20), "Income".center(10),
                                                        "Deduction".center(12), 'Tax'.center(10)))
        print("-"*76)
        breadth_First_()
    
    elif choice == 6:
        in_OrderFile()
    
    elif choice == 7:
        code = input("Enter code of tax payer want to search: ")
        searchCode(code) 

    elif choice == 8:
        code = input("Enter code of tax payer want to delete: ")          
        deleteCode(code)
        print("\nDelete record successfully!")
        print("Breath-first tree after delete node: ")
        print("| {} | {} | {} | {} | {} |".format("Code".center(8), "Name".center(20), "Income".center(10),
                                                        "Deduction".center(12), 'Tax'.center(10)))
        print("-"*76)
        breadth_First_()
                    
    elif choice == 9:
        balanceTree()
        print("\nBalance tree successfully!")
        print("Breath-first tree after balance")  
        print("| {} | {} | {} | {} | {} |".format("Code".center(8), "Name".center(20), "Income".center(10),
                                                        "Deduction".center(12), 'Tax'.center(10)))
        print("-"*76)
        breadth_First_()

    elif choice == 10:  
        countTaxpayer()
    else: 
        print("Wrong input")
        continue

