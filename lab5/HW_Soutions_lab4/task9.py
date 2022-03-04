#  Да се напише програма, която да превръща температура от целзий в фаренхайт.
# Формулата е следната: (0°C × 9/5) + 32 = 32°F, където c е температурата в целзий и f температурата в
# фаренхайт.
# Примерен изход:
# 60°C is 140 in Fahrenheit
# 45°F is 7 in Celsius

try:
    temperature = float(input('Въведете температура в целзиий: '))

    F = (temperature * 9/5) + 32

    print(f'{temperature}° is {F} in Fahrenheit')

except ValueError:
    print('Въведете валидна температура')

