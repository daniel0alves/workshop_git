import importlib
from time import sleep


implemented_function_list = ['all', 'add', 'sub', 'mul'] #XXX


def print_options():
    print("Choose the function you want to do:\n")
    i=0
    for f in implemented_function_list:
        i += 1
        print(f"{i}) {f}")
        

def parse_input(input_str: str) -> str:
    func_name: str = None
    
    if input_str.isnumeric():
        if input_str == '1':
            func_name = "all"
        elif input_str == '2':
            func_name = "add"
        elif input_str == '3':
            func_name = "sub"
        elif input_str == '4':
            func_name = "mul"
    
    else: func_name = input_str
    
    return func_name


def main():
    while(True):
        print_options()
        
        input_str = input("\n")
        
        func_name = parse_input(input_str)
        
        if func_name == "all": 
            all()
        else:
            try:
                module = importlib.import_module(f"functions.{func_name}")
                
                first_operand = int(input("Enter first operand: "))
                second_operand = int(input("Enter second operand: "))
                
                result = module.execute(first_operand, second_operand)
                
                print(f"Result: {result}\n\n-----------")
                input("(enter to continue)")
                
                
            except ImportError:
                print(f"Function '{func_name}' not found")
            except ValueError:
                print("Please enter valid numbers")
            except Exception as e:
                print(f"Error: {e}")


def all():
    first_operand = int(input("Enter first operand: "))
    second_operand = int(input("Enter second operand: "))
    
    first = True
    for f in implemented_function_list:
        if first:
            first = False
            continue
        
        module = importlib.import_module(f"functions.{f}")
        result = module.execute(first_operand, second_operand)
        
        print(f"Result: {result}\n\n-----------")
        sleep(0.5)
        
    input("All DONE! (enter to continue)\n")


if __name__ == "__main__": main()
