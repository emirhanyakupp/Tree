#receive an input in about the tree
treewidth_ = int(input())  

#create a empty string for canvas
can_ = ""  

#calculate the number of collums with using the receiving input
col = (14 + treewidth_)  

#calculate the height of the tree with using the receiving input
h_agc = (3 * treewidth_) // 2 

#define a variable about the constant height of the person
h_per = 8  

#create a list that stores the positions of the elements of the person
cre_ = [] 

#calculate the row number of the very bottom left element of the tree which is ' | ' with using receiving input
p_agc = ((14 + treewidth_) // 2) - 1  

#create a empty list in order to build the tree
cre_agc = []  

#create a list that stores the positions of the person, the list wil be used in printing and deleting the elements of the person 
for i in range(8):  
    cre_.append((max(h_agc - h_per, 0) + i) * (col + 1))
#calculate the positions of the elements of the tree
for k in range(max(h_per - h_agc, 0), max(h_agc, h_per)):  
    cre_agc.append(k * (col + 1))

#the list that will be used when the code delete the person
delt_ = [
    cre_[0] + 1, cre_[1], cre_[1] + 2, cre_[2] + 1, cre_[3], cre_[3] + 1,
    cre_[3] + 2, cre_[4] - 1, cre_[4] + 1, cre_[4] + 3, cre_[5] + 1, cre_[6],
    cre_[6] + 2, cre_[7] - 1, cre_[7] + 3
] 

#fill up the canvas with the space character ' '
for row in range(max(h_agc, 8)):  
    can_ += (14 + treewidth_) * " "
    can_ += '\n'
#define the string that will be printed
can_scene = ""  

#transform the canvas string into a list 
can_list = list(can_) 

#create a for loop that its range is calculated with receiving input
for step in range(10 + treewidth_):  
    
    #create a if block for the numbers that are less than 4 (precaution) 
    if treewidth_ >= 4:
        
        #create a if block that is nested with a for loop that delets the person's elements when the step is not 0 
        if step > 0:  
            for p in range(len(delt_)):
                can_list[delt_[p] + step] = ' '
        
        #print the person with using its elements
        can_list[cre_[0] + 2 + step] = '_' 
        can_list[cre_[1] + 1 + step] = '('
        can_list[cre_[1] + 3 + step] = ')'
        can_list[cre_[2] + 2 + step] = 'Y'
        can_list[cre_[3] + 1 + step] = '/'
        can_list[cre_[3] + 2 + step] = '|'
        can_list[cre_[3] + 3 + step] = '\\'
        can_list[cre_[4] + step] = '|'
        can_list[cre_[4] + 2 + step] = '|'
        can_list[cre_[4] + 4 + step] = '|'
        can_list[cre_[5] + 2 + step] = '|'
        can_list[cre_[6] + 1 + step] = '/'
        can_list[cre_[6] + 3 + step] = '\\'
        can_list[cre_[7] + step] = '|'
        can_list[cre_[7] + 4 + step] = '|'
        
        #print the top part of the tree
        for l in range(treewidth_ // 2):  
            can_list[(cre_agc[l] + p_agc - l)] = '/'
            can_list[(cre_agc[l] + p_agc + l + 1)] = '\\'
            
            #replace the inside of the top of the tree with space characters in order to make the person appear lost
            if treewidth_ != 4:  
                if l != 0 and l != (treewidth_ // 2) - 1:
                    for f in range(l):
                        s = 0
                        while s < (f * 2) + 2:
                            can_list[cre_agc[l] + p_agc + s - f] = ' '
                            s += 1
       
        #print the underscroll part of the top of the tree
        for p in range(treewidth_ // 2):  
            for t in range((treewidth_ // 2) - 1, (3 * treewidth_ // 2) - 1, (treewidth_ // 2) - 1):
                can_list[cre_agc[t] + p_agc + p] = '_'
                can_list[cre_agc[t] + p_agc - p + 1] = '_'
        
        #print the second and the third parts of the tree
        for u in range(treewidth_ // 2 - 1):  
            for ı in range(max(2 * (h_per - h_agc), treewidth_ // 2) + u, max(h_agc, h_per) - 2 + u, (treewidth_ // 2) - 1):
                if treewidth_ == 4:
                    can_list[cre_agc[ı - 2] + p_agc - u - 1] = '/'
                    can_list[cre_agc[ı - 2] + p_agc + u + 2] = '\\'
                if treewidth_ != 4:
                    can_list[cre_agc[ı] + p_agc - u - 1] = '/'
                    can_list[cre_agc[ı] + p_agc + u + 2] = '\\'
                    
                    #replace the inside of the second and the third parts of the tree with pace characters in order to make the person appear lost
                    if ı != treewidth_ - 2 and ı != h_agc - 3: 
                        e = ı % (treewidth_ // 2 - 1)
                        for r in range(e):
                            ş = 0
                            while ş < (r * 2) + 2:
                                can_list[cre_agc[ı] + p_agc + ş - r] = ' '
                                ş += 1
        
        #print the '|' at the bottom part of the tree
        for j in range(max(h_agc, h_per) - 2, max(h_agc, h_per)):  
            if treewidth_ == 4:
                can_list[cre_agc[j - 2] + p_agc] = '|'
                can_list[cre_agc[j - 2] + p_agc + 1] = '|'
            elif treewidth_ != 4:
                can_list[cre_agc[j] + p_agc] = '|'
                can_list[cre_agc[j] + p_agc + 1] = '|'
    
    #transform the canvas list into a string
    for a in range((col + 1) * max(h_agc, h_per)):  
        can_scene += can_list[a]

#print the canvas string with switching the end function of the print in order to print the person and tree with zero row spaces
print(can_scene, end='')  
