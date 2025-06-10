from hello_chai import chai

chai("haha chai jawla sir")

# Note:
# In the hello_chai.py file, if there are two functions with the same name (chai),
# the second one will override the first one.
# When the file is imported, only the last definition of chai which is last function chai in hello_chai file is stored in memory.
# In the main file, any call to chai will use this last (overridden) version from hello_chai.py.


