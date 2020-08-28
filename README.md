# Phone-Number

In this project I use  Python *PHONENUMBERS* library.

*About Library*
-  The main object that the library deals with is a PhoneNumber object. You can create this from a string representing a phone number using the parse function, but you also need to specify the country that the phone number is being dialled from (unless the number is in E.164 format, which is globally unique).
-  You might want to get some information about the location that corresponds to a phone number. The geocoder.area_description_for_number does this, when possible.
-  For mobile numbers in some countries, you can also find out information about which carrier originally owned a phone number.
-You might also be able to retrieve a list of time zone names that the number potentially belongs to.

It is simple but amzing code. You just enter any phone number with country code and program will give you output as,

- From which country you phone number belongs
- Service provider of this number
- Time-Zone of this number
