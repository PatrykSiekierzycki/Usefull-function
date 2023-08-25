It is not a program, but few usefull functions to get from user proper input.

1. getNumberRange - get from user number from proper range. (int or float)
2. getNegativeNumber - get from user negative number (int or float)
3. getPositiveNumber - get from user positive number (int or float)
4. getValueFromColection - get from user value from colection.

The functions "force" user to pass a proper value. The function handle protection.

More information about each function:
1. getNumberRange:
    Param:
        - first_str - it is a text which will be display at begining to inform user what he will pass.
        - min - minimal value for range. It can be int or float type.
        - max - maximal value for range. It can be int or float type.
        - not_in_range_str - it is a text to inform user, that the value what he pass is out of range.
        - inf_no_number - it is a text to inform user, that the value is not even a number.
        - dtype - is a type of returning data. Possible values: "int" and "float". Example of use: dtype="float".
    Return:
        - int or float - the programmist decide what data type function will return. See: above.
Information: if dtype has no proper value, function close the program.
Information: if first_str, not_in_range_str or inf_no_number the value is: None, function do not display that text.


2. getNegativeNumber:
    Param:
        - first_str - it is a text which will be display at begining to inform user what he will pass.
        - not_neg_num - it is a text to inform user, about that the value he pass is not a negative value.
        - inf_no_number - it is a text to inform user, that the value is not even a number.
        - dtype - is a type of returning data. Possible values: "int" and "float". Example of use: dtype="float".
    Return:
        - int or float type negative number.
Information: if dtype has no proper value, function close the program.
Information: if first_str, not_neg_num or inf_no_number the value is: None, function do not display that text.
Information: Do not accept 0.

3. getPositiveNumber:
    Param:
        - first_str - it is a text which will be display at begining to inform user what he will pass.
        - not_pos_num - it is a text to inform user, about that the value he pass is not a positive value.
        - inf_no_number - it is a text to inform user, that the value is not even a number.
        - dtype - is a type of returning data. Possible values: "int" and "float". Example of use: dtype="float".
    Return:
        - int or float type positive number.
Information: if dtype has no proper value, function close the program.
Information: if first_str, not_pos_num or inf_no_number the value is: None, function do not display that text.
Information: accept 0.

4. getValueFromColection:
    Param:
        - collection - the collection type with possible values, that we give user to choose.
        - first_str - it is a text which will be display at begining to inform user what he will pass.
        - if_not_in_col - is a type of returning data. Possible values: "int" and "float". Example of use: dtype="float".
    Return:
        Only one option from collection.