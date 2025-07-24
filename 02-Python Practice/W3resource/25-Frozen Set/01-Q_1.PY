def main():
    emp1 = {"name": "Bernardetta Frigg", "age": 20, "country": "Spain"}
    emp2 = {"name": "Fadhili Lilah", "age": 22, "country": "France"}
    emp3 = {"name": "Abbe Ivan", "age": 21, "country": "USA"}

    employees_data = {
        frozenset(emp1.items()): emp1,
        frozenset(emp2.items()): emp2,
        frozenset(emp3.items()): emp3
    }
    
    for key, value in employees_data.items():
        print("Key:", key)
        print("Value:", value)
        print()

if __name__ == "__main__":
    main()
