import phonenumbers
from phonenumbers import geocoder
from phonenumbers import carrier
from phonenumbers import timezone

ch_input = input("Enter your no, with country code: \n")

ch_number = phonenumbers.parse(ch_input,'CH')
print("************COUNTRY**************")
print(geocoder.description_for_number(ch_number,"en"))

ch_carrier = phonenumbers.parse(ch_input,'RO')
print("\n************SERVICE PROVIDER***************")
print(carrier.name_for_number(ch_carrier,'en'))

ch_time = phonenumbers.parse(ch_input,"GB")
print("\n************TIME ZONE****************")
print(timezone.time_zones_for_number(ch_time))