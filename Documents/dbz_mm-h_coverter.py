#Radar data
dbz_input = float(input("How much does the radar say it rains?  "))

#methz
sensible_rainfall = ((10 ** (dbz_input/10))/200) ** (5/8)

#the answer we've all been waiting for
print(round(sensible_rainfall, 2), "mm/h")