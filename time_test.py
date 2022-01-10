from qualitytime import Time, TimeUtils

tis_tijd = Time(11, 15, 32)
over_tijd = Time(10, 45, 25)

print(tis_tijd)
print(over_tijd)

show_tijd = TimeUtils.add_time(tis_tijd, over_tijd)
print("spannend")
print(show_tijd)
