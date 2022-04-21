durations = int(input('введите секунды: '))
days = durations // 86400
data_hours = durations % 86400
hour = data_hours // 3600
data_minutes = data_hours % 3600
minutes = data_minutes // 60
seconds = minutes % 60

print(days, "день", hour, "час", minutes, "минут", seconds, "секунд")