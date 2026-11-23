from ft_filter import ft_filter

def main() -> None:
    
    numbers = [1, 2, 3, 4, 5]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print("origin:" f"{even_numbers}")

    numbers = [1, 2, 3, 4, 5]
    even_numbers = list(ft_filter(lambda x: x % 2 == 0, numbers))
    print("mine:" f"{even_numbers"})


if __name__ == "__main__":
    main()