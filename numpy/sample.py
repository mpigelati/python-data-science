import numpy

my_list= [1,2,3]

#help(numpy)
#dir(numpy.itemsize())
#print(numpy.array(my_list))

#print(type(my_list))
#print(type(numpy.array(my_list)))

# array

'''my_data=[[1,2,3],[4,5,6],[7,8,9]]
print(numpy.array(my_data))'''

# Range

#myarange= numpy.arange(1,5)
#print(type(myarange))
#print(myarange)

#myarange=numpy.arange(1,10)
#print(myarange)

#myarange = numpy.arange(1,11,2)
#print(myarange)

#print(numpy.itemsize(myarange))

# array_range
x=numpy.arange(1,7)
print(x)
print(numpy.array_split(x,3))

x=numpy.arange(8.0)
print(x)
print(numpy.array_split(x,3))

#copy need to debug more

x=numpy.array ([1,2,3])
y=x
z=numpy.copy(x)
'''
for i in z:
    print(i)

for i in y:
    print(i)
'''

#numpy.zeros()

print(numpy.zeros(3))
print(numpy.zeros(2,dtype=numpy.int))
s=(3,3)
#print(numpy.zeros(s))


#print(numpy.ones(s))

#print(numpy.linspace(1,5,100))

#print(numpy.eye(3))

#print(numpy.random.rand(5,5))
#
#print(numpy.random.randn(4,4))

#print(numpy.random.randint(1,100,10))

arr=numpy.arange(25)
print(arr)

ranarr=numpy.random.random_integers(0,50,10)
print(ranarr)

print("reshape\n",arr.reshape(5,5))

# here the number of rows equal to no of column in arr  of 24


print(ranarr.max())
print(ranarr.min ())

arr=numpy.arange(0,11)
print(arr)

print(arr[1:3])
print(arr[8])
print(arr[0:5])
print(arr[:6])
print(arr[1:10:-2])

arr[0:5]=10
print(arr)

slice_of_arr = arr[0:6]
print(slice_of_arr)
slice_of_arr[:]=99
print(slice_of_arr)
print(arr)
  


