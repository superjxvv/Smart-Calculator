# write your code here
from collections import deque

numbers = tuple("0123456789")
alphabets = tuple("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
operator_precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
variables = {}


def check_variable_name(name):
    for i in name:
        if i not in alphabets:
            return False
    return True


def infix_to_postfix(equation):
    i = 0
    result = []
    operator_stack = deque()
    while i < len(equation):
        if equation[i][0] in numbers or equation[i] in variables \
                or (len(equation[i]) > 1 and equation[i][0] == "-"
                    and (equation[i][1] in numbers or equation[i][1:] in variables)):
            result.append(equation[i])
        elif (equation[i] in operator_precedence
              and (len(operator_stack) == 0
                   or operator_stack[len(operator_stack) - 1] == '(')) \
                or equation[i] == '(':
            operator_stack.append(equation[i])
        elif equation[i] in operator_precedence \
                and operator_precedence[equation[i]] > operator_precedence[operator_stack[len(operator_stack) - 1]]:
            operator_stack.append(equation[i])
        elif equation[i] in operator_precedence \
                and operator_precedence[equation[i]] <= operator_precedence[operator_stack[len(operator_stack) - 1]]:
            while len(operator_stack) > 0 \
                    and (operator_stack[len(operator_stack) - 1] != '('
                         and operator_precedence[equation[i]] <= operator_precedence[
                             operator_stack[len(operator_stack) - 1]]):
                result.append(operator_stack.pop())
            operator_stack.append(equation[i])
        elif equation[i] == ')':
            try:
                while operator_stack[len(operator_stack) - 1] != '(':
                    if len(operator_stack) == 0:
                        return "Invalid expression"
                    result.append(operator_stack.pop())
                operator_stack.pop()
            except IndexError:
                return "Invalid expression"
        elif equation[i][0] not in numbers and equation[i] not in variables \
                and (len(equation[i]) > 1 and equation[i][0] == "-"
                     and (equation[i][1] not in numbers or equation[i][1:] not in variables)):
            if check_variable_name(equation[i]) or (equation[i][0] == "-"
                                                    and check_variable_name(equation[i][1:])):
                return "Unknown variable"
            else:
                return "Invalid identifier"
        i += 1
    while len(operator_stack) > 0:
        result.append(operator_stack.pop())
    if '(' in result:
        return "Invalid expression"
    else:
        return result


def calculate_postfix(equation):
    result_stack = deque()
    i = 0
    try:
        while i < len(equation):
            if equation[i][0] in numbers \
                    or (len(equation[i]) > 1 and equation[i][0] == "-" and equation[i][1] in numbers):
                result_stack.append(int(equation[i]))
            elif equation[i] in variables \
                    or (len(equation[i]) > 1 and equation[i][0] == "-" and equation[i][1:] in variables):
                result_stack.append(variables.get(equation[i]))
            elif equation[i] in operator_precedence:
                x = int(result_stack.pop())
                y = int(result_stack.pop())
                if equation[i] == "+":
                    result_stack.append(y + x)
                if equation[i] == "-":
                    result_stack.append(y - x)
                if equation[i] == "*":
                    result_stack.append(y * x)
                if equation[i] == "/":
                    result_stack.append(y / x)
                if equation[i] == "^":
                    result_stack.append(y ** x)
            i += 1
    except IndexError:
        return "Invalid expression"
    else:
        if len(result_stack) > 0:
            return result_stack.pop()
        else:
            return "Invalid expression"


def process(equation):
    if len(equation) == 0:
        return "Invalid expression"
    equation = infix_to_postfix(equation)
    if equation == "Unknown variable" or equation == "Invalid identifier" or equation == "Invalid expression":
        return equation
    else:
        return calculate_postfix(equation)


def create_equation(formula):
    formula = list(formula)
    counter = False
    i = 0
    while i < len(formula):
        if formula[i] == "-":
            counter = not counter
            i += 1
            while i < len(formula) and formula[i] == "-":
                formula.pop(i - 1)
                formula.pop(i - 1)
                if counter:
                    formula.insert(i - 1, "+")
                else:
                    formula.insert(i - 1, "-")
                counter = not counter
            counter = False
        elif formula[i] == "+":
            i += 1
            while i < len(formula) and formula[i] == "+":
                formula.pop(i)
        elif formula[i] in numbers:
            i += 1
            while i < len(formula) and formula[i] in numbers:
                formula.insert(i - 1, formula.pop(i - 1) + formula.pop(i - 1))
        elif formula[i] in alphabets:
            i += 1
            while i < len(formula) and formula[i] in alphabets:
                formula.insert(i - 1, formula.pop(i - 1) + formula.pop(i - 1))
        elif formula[i] == " ":
            formula.pop(i)
        else:
            i += 1
    i = 0
    while i < len(formula):
        if formula[i] == "-" and (i == 0 or formula[i - 1] in operator_precedence):
            formula.insert(i, formula.pop(i) + formula.pop(i))
        if formula[i] == "+" and (i == 0 or formula[i - 1] in operator_precedence):
            formula.pop(i)
        i += 1
    return formula


def process_command(cmd):
    if cmd == "/exit":
        print("Bye!")
        return True
    elif cmd == "/help":
        print(
            "the program must receive the addition + and subtraction - operators as an input to distinguish operations from each other. It must support both unary and binary minus operators. Moreover, If the user has entered several operators following each other, the program still should work (like Java or Python REPL). Also, as you remember from school math, two adjacent minus signs turn into a plus. The smart calculator ought to have such a feature.")
        return False
    else:
        print("Unknown command")
        return False


def process_assignment(equation):
    try:
        key, value = equation.split("=")
    except ValueError:
        print("Invalid assignment")
        return
    else:
        value = process(create_equation(value.strip()))
        if check_variable_name(key.strip()) and value != "Invalid identifier":
            variables[key.strip()] = value
        elif value == "Invalid identifier":
            print("Invalid assignment")
        else:
            print("Invalid identifier")
            return


def process_variable(variable):
    print(process(create_equation(variable)))


stop = False
while not stop:
    command = input().strip()
    if command == "":
        continue
    elif command.startswith("/"):
        stop = process_command(command)
        continue
    elif "=" in command:
        process_assignment(command)
    else:
        process_variable(command)
