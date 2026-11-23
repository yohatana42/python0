from ft_filter import ft_filter

def main() -> None:
    
    numbers = [1, 2, 3, 4, 5]
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    print("origin:" f"{even_numbers}")

    even_numbers = list(ft_filter(lambda x: x % 2 == 0, numbers))
    print("mine:" f"{even_numbers}")

    data = [0, 1, "", "a", None, [], [1], False, True]
    even_numbers2_1 = list(filter(None, data))
    print("origin:" f"{even_numbers2_1}" " type:" f"{type(even_numbers2_1)}")

    even_numbers2_2 = list(ft_filter(None, data))
    print("mine:" f"{even_numbers2_2}" " type:" f"{type(even_numbers2_2)}")


if __name__ == "__main__":
    main()