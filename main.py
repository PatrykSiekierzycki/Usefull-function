
"""
Brief: check if in string are dot or minus. Also check at what index is for minus.
Param: string.
Return: bool or (bool + haw many minus are in string; minus for this minus; and how many dots are in string).
"""
def isNumberWithDotOrMinus(user_input):

    minusCounter = 0
    minusIndex = None
    dotCounter = 0
    buffor = ""


    for index, char in enumerate(user_input):

        if char == "-":
            minusCounter += 1
            minusIndex = index
        elif char == ".":
            dotCounter += 1
        else:
            buffor = buffor + char


    if minusCounter <= 1 and dotCounter <= 1 and (minusIndex == 0 or minusIndex == None):
        numeric = buffor.isnumeric()
        if numeric is True:
            return True, minusCounter, minusIndex, dotCounter
        else:
            return False
    else:
        return False



"""
Brief: Function for prepere numeric input: remove all whitespace sign and change all "," to ".".
Param: user_input: string
Return: prepered input: string
"""
def prepereNumericInput(user_input):

    # Change all commas to dots in "user_input".
    user_input = user_input.replace(",", ".")

    # Get rid of whitespace character from "user_input".
    whitespace_list = [" ", "\t", "\n", "\v", "\f", "\r"]
    for space in whitespace_list:
        user_input = user_input.replace(space, "")

    return user_input

"""
Brief: Get from user a number from setted range, and if it is not a proper number, then force him to give proper number. If user give number with "," instead "." function return input with ".". 
Param: 
    first_str: text what will be print always before user should give the input (if is not set, just dosent't print anything);
    min: the minimal value for range.
    max: the maximal value for range.
    not_in_range_str: text what will be print always if user's input is not a in range (if is not set, just dosent't print anything);
    inf_no_number: text what will be print always when user's input is not a number (if is not set, just dosent't print anything);
    dtype: what data type function should return, possible options: int, float.
Return: positive number
"""
def getNumberRange(first_str=None, min=0.0, max=100.0, not_in_range_str=None, inf_no_number=None, dtype="int"):

    # Check is dtype has proper value.
    properDataTypes = ["int", "float"]

    if dtype not in properDataTypes:
        exit(1)

    while True:

        # Check if "first_str" parametr has other value than "None".
        if first_str == None:  # If not, do not print information.
            user_input = input()
        else:  # If has, print that string.
            user_input = input(first_str)

        # Check if user do not press only enter
        if len(user_input) == 0:  # If press only enter
            if inf_no_number == None:  # If there is no set "first_str"
                continue
            else:  # If "first_str" is setted
                print(inf_no_number)
                continue

        user_input = prepereNumericInput(user_input)

        number = user_input.isnumeric()  # Check if number is numeric

        # Check if input is numeric
        if number is False:

            pack = isNumberWithDotOrMinus(user_input)
            number = None
            minusCounter = 0
            minusIndex = None

            # If pack is tuple unpack data to variables
            if type(pack) is tuple:
                number = pack[0]
                minusCounter = pack[1]
                minusIndex = pack[2]
            elif type(pack) == bool:
                number = pack


            if number is False:
                if inf_no_number != None:
                    print(inf_no_number)
                    continue
                else:
                    continue


        # Prepere expected data type
        if dtype == "int":
            user_input = int(float(user_input))
        elif dtype == "float":
            user_input = float(user_input)
        else:
            exit(1)

        # Check if "user_input" is in range
        if user_input < min or user_input > max:
            if not_in_range_str != None:
                print(not_in_range_str)
            continue
        else:
            return user_input

"""
Brief: Get from user a negative number, and if it is not a negative number, then force him to give negative number. If user give number with "," instead "." function return input with ".".
Param: 
    first_str: text what will be print always before user should give the input (if is not set, just dosent't print anything);
    not_neg_num: text what will be print always if user's input is not a negative number (if is not set, just dosent't print anything);
    inf_no_number: text what will be print always when user's input is not a number (if is not set, just dosent't print anything);
    dtype: what data type function should return, possible options: int, float.
Return: positive number
"""
def getNegativeNumber(first_str=None, not_neg_num=None, inf_no_number = None, dtype="int"):

    minus_flag = False

    # Check is dtype has proper value.
    properDataTypes = ["int", "float"]

    if dtype not in properDataTypes:
        exit(1)

    while True:

        # Check if "first_str" parametr has other value than "None".
        if first_str == None:
            user_input = input()
        else:
            user_input = input(first_str)

        # Check if user do not press only "enter"
        if len(user_input) == 0:  # If press only enter
            if inf_no_number == None:  # If there is no set "first_str"
                continue
            else:  # If "first_str" is setted
                print(inf_no_number)
                continue

        user_input = prepereNumericInput(user_input)

        number = user_input.isnumeric()  # Check if number is numeric

        # Check if "user_input" is a minus number or with dot.
        if number is False:

            pack = isNumberWithDotOrMinus(user_input)
            number = None
            minusCounter = 0
            minusIndex = None

            # If pack is tuple unpack data to variables
            if type(pack) is tuple:
                number = pack[0]
                minusCounter = pack[1]
                minusIndex = pack[2]
            elif type(pack) == bool:
                number = pack

            if number is True and minusCounter == 1 and minusIndex == 0:
                minus_flag = True
            else:
                continue


        # Prepere expected data type
        if dtype == "int":
            user_input = int(float(user_input))
        elif dtype == "float":
            user_input = float(user_input)

        # Check if "user_input" is a negative number
        if minus_flag is False:
            if not_neg_num != None:
                print(not_neg_num)
                continue
            else:
                continue
        else:
            return user_input

"""
Brief: Get from user a positive number, and if it is not a positive number, then force him to give positive number. If user give number with "," instead "." function return input with ".". 
Param: 
    first_str: text what will be print always before user should give the input (if is not set, just dosent't print anything);
    not_pos_num: text what will be print always if user's input is not a positive number (if is not set, just dosent't print anything);
    inf_no_number: text what will be print always when user's input is not a number (if is not set, just dosent't print anything);
    dtype: what data type function should return, possible options: int, float.
Return: positive number
"""
def getPositiveNumber(first_str=None, not_pos_num=None, inf_no_number=None, dtype="int"):

    # Check is dtype has proper value.
    properDataTypes = ["int", "float"]

    if dtype not in properDataTypes:
        exit(1)

    while True:

        flag = False

        # Check if "first_str" parametr has other value than "None".
        if first_str == None:
            user_input = input()
        else:
            user_input = input(first_str)

        # Check if user do not press only enter
        if len(user_input) == 0:  # If press only enter
            if inf_no_number == None:  # If there is no set "first_str"
                continue
            else:  # If "first_str" is setted
                print(inf_no_number)
                continue

        user_input = prepereNumericInput(user_input)

        number = user_input.isnumeric()  # Check if number is numeric

        # Check if "user_input" is a minus number or with dot.
        if number is False:

            pack = isNumberWithDotOrMinus(user_input)
            number = None
            minusCounter = 0
            minusIndex = None

            # If pack is tuple unpack data to variables
            if type(pack) is tuple:
                number = pack[0]
                minusCounter = pack[1]
                minusIndex = pack[2]
            elif type(pack) == bool:
                number = pack

            # Filter: Check if "number" is good with conditions
            if number is True and (minusCounter == 1 and minusIndex == 0):
                # Check if "not_pos_num" parametr has other value than "None".
                if not_pos_num == None:
                    continue
                else:
                    print(not_pos_num)
                    continue
            elif number is True and minusCounter == 1 and minusIndex != None:
                if inf_no_number == None:
                    continue
                else:
                    print(inf_no_number)
                    continue
            elif number is False:
                if inf_no_number == None:
                    continue
                else:
                    print(inf_no_number)
                    continue


        # Prepere expected data type
        if dtype == "int":
            user_input = int(float(user_input))
        elif dtype == "float":
            user_input = float(user_input)

        return user_input

"""
Brief: Function for getting a proper value form collection. If user's input are not in collection, function "force" user, untill he get proper value.
Param: 
    collection - collection with possible values;
    first_text - text for print before user should give input (if is not set, just dosent't print anything);
    if_not_in_col - if user's input is not a proper value, the content of that variable will be print (if is not set, just dosent't print anything).
Return: Proper value, that means one from collection.
"""
def getValueFromColection(collection, first_text = None, if_not_in_col = None):

    while True:

        # Get input from user.
        if first_text != None:
            user_input = input(first_text)
        else:
            user_input = input()

        str_collection = []

        # Cast the element's type from collection to string.
        for value in collection:
            str_collection.append(str(value))

        # If "user_input" are in "str_collection".
        if user_input in str_collection:
            return user_input
        else:
            if if_not_in_col != None:
                print(if_not_in_col)
                continue
            else:
                continue
