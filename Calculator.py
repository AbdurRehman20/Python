button = "off"
button = input("Button is (on/off)?:")
while button == "on":
    index_of_operator = 0
    before_index = 0
    after_index = 0
    operator_used = None
    value = str(input())
    operators = ["/","*","+","-"]
    for each_string in value:
        index_of_operator += 1
        for operator in operators:
            if each_string == operator:
                # print(each_string) 
                # print(index_of_operator)
                index_of_operator -= 1
                operator_used = each_string
                before_index = value[:index_of_operator]
                # print(before_index)on
                index_of_operator += 1
                after_index = value[index_of_operator:]
                # print(after_index)
    if operator_used == "/":
        print(int(before_index)/int(after_index))
    elif operator_used == "*":
        print (int(before_index)*int(after_index))
    elif operator_used == "+":
        print(int(before_index)+int(after_index))
    elif operator_used == "-":
        print(int(before_index)-int(after_index))
    else:
        print("incorrect operator")
    index_of_operator = 0
    before_index = 0
    after_index = 0
    value = None
    operator_used = None
    button = input("Button is (on/off)?:")

