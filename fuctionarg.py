list =['hai','hello','welcome']
def show(x):
  print x*3
 def my_sample(fun,list):
  for item in list:
    fun(item)
my_sample(show,list)
