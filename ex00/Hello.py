ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}
# your code here
ft_list.append("World!")
ft_tuple = ft_tuple[0:1] + ("Japan!",)
ft_set -= {"tutu!"}
ft_set |= {"Tokyo!"}
ft_dict["Hello"] = "42Tokyo!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
