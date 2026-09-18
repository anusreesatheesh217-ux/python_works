#%%

#%% md
#4.Variables & Values (Python)
#%% md
# Characteristics of variables (python):
#%% md
#1. Dynamic Inference - Static Defined(Java) Integer aspirant_cnt=103
#%%
placeholder_name="value_stored_in_memory"
#variable, value, memory, of any datatype
aspirants_cnt=100
curtime=7
if curtime<=8:
    print(aspirants_cnt+10)
elif curtime>8:
    print(aspirants_cnt+20)
elif curtime>9:
    print(aspirants_cnt-20)
#%%
#Characteristics of variables (python):
#1. Dynamic Inference - Static Defined(Java) Integer aspirant_cnt=103;
aspirants_cnt=103
print("Dynamic inference of the type based on the values assigned",type(aspirants_cnt))
aspirants_cnt='Hundred & Four'
print("Dynamic inference of the type based on the values assigned",type(aspirants_cnt))
#%%
#2. Dynamic Typed - Static Typed (Java)
aspirants_cnt=103
print(type(aspirants_cnt))
aspirants_cnt='Hundred & Four'
print('In python we can change the type of a variable Dynamically in the later part of the program',type(aspirants_cnt))
#%%
#3. Strongly Typed - Weakly Typed
mentor_name='Irfan'
print(type(mentor_name))
aspirants_cnt=103
print(type(aspirants_cnt))
#name_and_cnt=mentor_name+aspirants_cnt#This code will not work
#print("This will not execute",name_and_cnt)
#%% md
# E. Datatypes in Python
#%% md
#1.Simple Types - str(Seq type), number(int,float,complex number)
#2.Complex Types/Collection Types - List, Dictionary, Tuples, Set
#3.Misc Types - Bool, None, range, bytes, memoryview
#%%
#Concept of hint: Hint is just for giving a clue, not for really applying the type.
name:str="Irfan"#:str is just a hint, it is not a type definition
name:str=10#This type is identified as int only, not as string because of dyn inference
print(type(name))
#%%
#1. Simple Type -
#String Type: Indexed Sequenced collection of alpha-numeric characters.
#String is Sequence hence it is Iterable/Loopable
#String is Indexed (used for identifying elements using index)
#Below string is indexed for eg: I=0, r=1, f=2....
#var= 01234567 #This is called index
name="Irfan123"
print("proving string is indexed by taking the index of name",name[0], name[1])
print("proving string is sequenced by looping below")
for i in name:
    print(i)

#Collection - Set Type: Sequenced collection of deduplicated items.
st={'r', 'f', 'i', 'a', 'n'}
#print("proving set is NOT indexed by taking the index of name")
#print(st[0]) # This will not work because set is not indexed
print("proving set is sequenced (though not indexed) by looping below")
for i in st:
    print(i)

#Number is not indexed or even not sequenced
age=40
#age[0]#Will not work because number is non INDEXED
'''
Will not work because number is non sequenced
for i in age:
    print(i)
'''
#%%
'\nWill not work because number is non sequenced\nfor i in age:\n    print(i)\n'
#%%
#Simple Type:
#2. Number (int, float, complex)
#Number : Non indexed, non Sequenced type for storing numerical values
#int: Stores whole values starting -ve to +ve infinate values.
age=40

#float:Stores fractional values with scale (before .) and precision (after .)
height=5.11 #5 is the scale and .11 is for precision (accuracy)

#complex:Complex types are number values with real & imaginary part used for electronic, scientific systems
graph_coord=10+5j
print(graph_coord.real)
print(graph_coord.imag)
#Check whether all numbers is indexed or sequenced? not both are applicable
#%%
#Simple Type:
# Boolean : It is a decision making type evaluated internally in the conditional structures.
flag1=True
print(type(flag1))
flag2=False
print(type(flag2))

if flag1:#We don't use boolean directly
    print("flag1 is positive")

if name=='Irfan123':#Booleans are naturally identified
    print("Name is irfan")

print("out of the if condition")

#%%
#2. Collection/Complex Types/Sequence Type - Level 1, Level 2 (we learn later)
#Group of or collection of values in a variable
name_simpletype='mohamed irfan'#simple type with one value assigned to a variable
full_name_collectiontype=['mohamed', 'irfan']#collection type with multiple value assigned to a variable
#%%
#Level 1
#Characteristics of Collection/Complex/Seq types
#All collection/complex types are sequenced by default (iterable)
#Not all collections are indexed (eg. dict & set are non indexed)
#Collection types can have one or multiple elements/items
#4 Types of collection Types - list, dictionary, tuple, set

#Level 2
#limitations
#Not all collections are mutable (updatable)
#Not all collections are resizable (insert/delete)
#Lets learn about collection types fundamentally
#list [] - Indexed Sequenced collection of homogeneous/similar datatype (not mandatorily) elements/items
#                       0               1                   2           3
aspirants_name_list=['Vijay kumar','Meena Velusamy','andrew Prasad','srimanasa']
aspirants_age_list=[31,22,30,31]
print("total number of indexes is ",len(aspirants_name_list)-1)
print(type(aspirants_name_list))
#How to access the elements/items of a list? using index, or by iterating
#Indexed? yes, i can access the elements/items using index
print(aspirants_name_list[0])
print(aspirants_name_list[1])

#Sequenced? yes, i can able to do looping, hence sequenced
for name in aspirants_name_list:
    print(name.capitalize())
#%%
#dict {key1:val1,key2:val2} - Sequenced collection of key value pairs
#Rather keep multiple lists and associate value using index, we can keep all the pair of values in a single dictionary.
print("name",aspirants_name_list[0],"age",aspirants_age_list[1])
#Non indexed                       0               1                   2           3
aspirants_name_age_dict={'Vijay kumar':31,'Meena Velusamy':22,'andrew Prasad':30,'srimanasa':31}
print(aspirants_name_age_dict)
print(type(aspirants_name_age_dict))

#How to access the elements/items of a dictionary? using key or by iterating
#Indexed? no, i can't access the elements/items using index
#print(aspirants_name_age_dict[0])#fails, because non indexed
print(aspirants_name_age_dict['Vijay kumar'])#use the key to access values, not index

#Sequenced? yes, i can able to do looping, hence sequenced
print("printing keys alone")
for name in aspirants_name_age_dict:#It  returns keys alone
    print(name.capitalize())
print("printing values alone")
for age in aspirants_name_age_dict.values():#It  returns values alone
    print(age)
print("printing both keys and values (items)")
for name,age in aspirants_name_age_dict.items():#It  returns items alone
    print(name,age)
#%%
#tuples () - Indexed Sequenced collection of HETROGENEOUS/different datatypes (not mandatorily) elements/items
#tuples are otherwise called as record/row
#indexed            0          1     2          3
aspirants_tuple=('Vijay kumar',31,'Chennai','IT Professional')
print(aspirants_tuple)
print(type(aspirants_tuple))
#How to access the elements/items of a tuple? using index, or by iterating
#Indexed? yes, i can access the elements/items using index
print("Let us see tuple is indexed? yes")
print(aspirants_tuple[0])
print(aspirants_tuple[1])

#Sequenced? yes, i can able to do looping, hence sequenced
print("Let us see tuple is sequenced? yes")
for i in aspirants_tuple:
    print(str(i).capitalize())
#%%
#set {value1,value2,value3} - Sequenced collection of DE-DUPLICATED HOMOGENEOUS (not mandatorily) elements/items
#Set is used for performing DE-DUPLICATION & performing set operations (union, intersect, minus) (we will learn in level2 learning)
#Not indexed            0               1               2
aspirants_set_sql1={'sandhya kalavath','khader basha','peddisetty narayana'}
aspirants_set_testing2={'shalu','singaraj patchaiappan','ashwin s t','sandhya kalavath','shalu'}
print(aspirants_set_testing2)
print(type(aspirants_set_testing2))
#How to access the elements/items of a set? not by using index, or by iterating (yes)
#Indexed? No, i can't access the elements/items using index
print("Let us see set is indexed? no")
#print(aspirants_set_sql1[0]) #This will fail

#Sequenced? yes, i can able to do looping, hence sequenced
print("Let us see tuple is sequenced? yes")
for i in aspirants_set_sql1:
    print(str(i).upper())

#Set other characteristics - Deduplication
aspirants_set_testing2={'shalu','singaraj patchaiappan','ashwin s t','sandhya kalavath','shalu'}
print(aspirants_set_testing2)

#Set other characteristics of performing set operations - Level2 items
print(aspirants_set_sql1.union(aspirants_set_testing2))
#%% md
# list, tuples, dict
#%% md
# list
select accountid from odsdb_Rathan.ods_accounts;#accountid list [1225655944140,8876511923411,6190138352945]#%% md
#
#%% md
# dict
  select Balance from odsdb_Rathan.ods_accounts a where accountid=1225655944140;#accountid list {1225655944140:36684.82,8876511923411:36688.82,6190138352945:36111.82}
#%% md
# dict & tuple
#%% md
#select Balance,currency from odsdb_Rathan.ods_accounts a where accountid=1225655944140;#accountid list {1225655944140:36684.82,8876511923411:36688.82,6190138352945:36111.82}
#%%
#set
#%%
#3. Misc Types: bytes, None
#None type: None means nothing or empty or unknown value
#None is used for initializing a variable which value is unknown
# or none is used as an identifier to denote there is no value for this operation.
aspirants_count=None
aspirants_count=100

# or none is used as an identifier to denote there is no value for this operation.
does_print_returned_anything_no=print("hello")
print(does_print_returned_anything_no)
#%%
#Bytes & Memory view: Both are not used directly, at the time of sending data across network or storing inside storages, bytes are used. Memory view is used to see the memory address of where these bytecodes are stored
empname='irfan'
network_empname=empname.encode()
print(memoryview(network_empname))
print(network_empname)
print(type(network_empname))

salary=100000
network_salary=bytes(salary)
print(type(network_salary))
print(memoryview(network_salary))
print(network_salary)

#%%
#After Datatypes:
#Standard Input & Output Operations
#Standard Input (stdio.h, conio.h) - input("prompt")
aspirant_name=input("Enter our aspirant name")#Standard input
print(type(aspirant_name))
aspirant_age=int(input("Enter our aspirant age"))#Standard input
print(type(aspirant_age))
print("value entered is ",aspirant_name)#Standard Output

print("printing something")#Print has 2+ more parameters, atleast 2 of them are important - sep(space), end (\n)
print("mohamed","irfan","kader")
print("Inceptez")
#%%
print(aspirant_name)
#Type casting & evaluation