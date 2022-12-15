class table():
    
    array = []
    
    def __init__(self,row,col):
        self.array=[[1]*row for i in range(col)]

    def get_value(self,row,col):
        if row>len(self.array) or col>len(self.array[0]):
            return 'None'
        return self.array[row][col]

    def set_value(self,row,col,value):
        self.array[row][col]=value

    def n_rows(self):
        return len(self.array)
    
    def n_cols(self):
        return len(self.array[0])

    def delete_row(self,row):
        self.array.pop(row)
        
    def delete_col(self,col):
        self.array[0].pop(col)
        

    def print (self):
        for i in range (len(self.array)):
            for j in range (len(self.array[i])):
                print(self.array[i][j], end = ' ')
            print()

    def add_col(self,col):
        j=0
        for i in range (len(self.array)):
                self.array[i].append(0)
        while(len(self.array)-j>col):
            for i in range (len(self.array)):
                self.array[i][len(self.array)-j-1], self.array[i][len(self.array)-j] =  self.array[i][len(self.array)-j], self.array[i][len(self.array)-j-1]
            j+=1
                
    def add_row(self,row):
        i=0
        self.array.append([0]*len(self.array[0]))
        while(len(self.array[0])-i>row):
            for j in range (len(self.array[0])):
                self.array[len(self.array[0])-i-1][j], self.array[len(self.array[0])-i][j] =  self.array[len(self.array[0])-i][j], self.array[len(self.array[0])-i-1][j]
            i+=1            


