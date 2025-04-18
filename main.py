import importlib


implemented_function_list = ['add', 'sub'] #XXX

def main():
    
    print("Choose the function you want to do:")
    for f in implemented_function_list:
        print(f"-> {f}")
    
    func_name = input("\n")
    
    try:
        module = importlib.import_module(f"functions.{func_name}")
        
        first_operand = int(input("Enter first number: "))
        second_operand = int(input("Enter second number: "))
        
        result = module.execute(first_operand, second_operand)
        
        print(f"Result: {result}")
        
        
    except ImportError:
        print(f"Function '{func_name}' not found")
    except ValueError:
        print("Please enter valid numbers")
    except Exception as e:
        print(f"Error: {e}")



if __name__ == "__main__": main()
