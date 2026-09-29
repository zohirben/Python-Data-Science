ft_list = ["Hello"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

# Lists are mutable, so we can modify them directly with append().
ft_list.append("World!")

# Tuples are immutable, so we cannot modify an element directly.
# We create a new tuple using concatenation and reassign it.
ft_tuple = ft_tuple[:1] + ("Morocco!",)

# Sets are mutable and contain unique elements, so we remove and add elements.
ft_set.remove("tutu!")
ft_set.add("Tetouan!")

# Dictionaries are mutable mappings, so we can change a value using its key.
ft_dict["Hello"] = "1337MED"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)