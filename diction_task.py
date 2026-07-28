#1
my_dict={'name':'python','age':25}
dict_1={'city':'west godavari'}
my_dict.update(dict_1)
print(my_dict)
#2
product_info={'name':'laptop','brand':'dell','price':1200}
print(product_info['price'])
#3
my_dict={'name':'python','age':25,'city':'bhimavaram'}
my_dict.pop('city')
print(my_dict)
#4
my_dict={'name':'python','age':25,'city':'Rajuhmundry'}
print(my_dict.keys())
#5
my_dict={'name':'python','age':25,'city':'tanuku'}
print(my_dict.values())
#1.dictionary update
my_dict={'name':'python','age':25,'city':'tanuku'}
new_dict={'mailid':'python@123'}
my_dict.update(new_dict)
print(my_dict)
#2.dictionary access
my_dict={'name':'python','age':25,'city':'tanuku'}
print(my_dict['name'])
#3.Dictionary removal
my_dict={'name':'python','age':25,'city':'tanuku'}
my_dict.pop('city')
print(my_dict)
#4.Dictionary keys
my_dict={'name':'python','age':25,'city':'tanuku'}
print(my_dict.keys())
#5.Dictionary values
my_dict={'name':'python','age':25,'city':'tanuku'}
print(my_dict.values())