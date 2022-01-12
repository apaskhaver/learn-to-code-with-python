# import feature.subfeature.calculator
# import feature.copyright

# print(feature.subfeature.calculator.subtract(10, 5))
# print(feature.copyright.date_of_copyright)

# from feature. import subfeature

# from feature.subfeature import calculator
# print(calculator.subtract(3, 7))

# from feature.subfeature.calculator import subtract
# print(subtract(10, 3))

# now that we've moved some of the imports into subfeature.__init__.py,
# we can access calculator methods with
import feature.subfeature
print(feature.subfeature.subtract(10, -1))
# instead of doing feature.subfeature.calculator.subtract(10, -1)