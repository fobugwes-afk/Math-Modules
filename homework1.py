import math

angle = float(input("Enter an angle in degrees: "))

radians = math.radians(angle)

sin_value = math.sin(radians)
cos_value = math.cos(radians)
tan_value = math.tan(radians)

print("\nTrigonometric Values:")
print("Sin(", angle, ")=", sin_value)
print("Cos(", angle, ")=", cos_value)
print("Tan(", angle, ")=", tan_value)