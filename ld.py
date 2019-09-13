# Lists #

#Task 1
nums = ["3", "5", "7", "9", "10.5"]
print(nums)

nums.append("Python")
print(nums)

# Task 2

print(nums[0])

print(nums[-1])

print(nums[1:4])

nums.remove("Python")
print(nums)


print(" ")


# Dictionaries #

weather = {
    "city": "Москва",
    "temperature": 20
}

# Task 1 
print(weather["city"])

weather["temperature"] = 15

print(weather)

# Task 2
print(weather.get("country"))

weather["country"] = "Russia"

weather["date"] = "27.05.2019"
print(weather)










