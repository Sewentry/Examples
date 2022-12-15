import sys

class MinStat():

    min_array = []
    minimum = sys.maxsize
           
    def add_number(self,number):
        self.min_array.append(number)
        minimum = self.min_array[0]
        for i in range(len(self.min_array)):
            if type(self.minimum)==str:
                break
            if(len(self.min_array)==0):
                self.minimum = 'null'
                break
            elif type(number)!=int:
                self.minimum = 'null'
                break
            else:    
                if minimum > self.min_array[i]:
                    minimum = self.min_array[i]
                self.minimum = minimum
        

    def result(self):
        return self.minimum

class MaxStat():

    max_array = []
    maximum = - sys.maxsize
           
    def add_number(self,number):
        self.max_array.append(number)
        maximum = self.max_array[0]
        for i in range(len(self.max_array)):
            if type(self.maximum)==str:
                break
            if(len(self.max_array)==0):
                self.maximum = 'null'
                break
            elif type(number)!=int:
                self.maximum = 'null'
                break
            else:    
                if maximum < self.max_array[i]:
                    maximum = self.max_array[i]
                self.maximum = maximum
        

    def result(self):
        return self.maximum

class AverageStat():

    average_array =[]
    average = 0

    def add_number(self,number):
        self.average_array.append(number)
        result = 0
        for i in range(len(self.average_array)):
            if type(self.average)==str:
                break
            if(len(self.average_array)==0):
                self.maximum = 'null'
                break
            elif type(number)!=int:
                self.average = 'null'
                break
            else:    
                result+=self.average_array[i]
        self.average = result
            
        

    def result(self):
        return self.average/len(self.average_array)

value = [1,2,4,5]

aa = MinStat()
for i in range (len(value)):
    aa.add_number(value[i])
print(aa.result())  

aaa = MaxStat()
for i in range (len(value)):
    aaa.add_number(value[i])
print(aaa.result())  

aaaa = AverageStat()
for i in range (len(value)):
    aaaa.add_number(value[i])
print(aaaa.result()) 
