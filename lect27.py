row1=[1,1,1]
row2=[1,1,1]
row3=[1,1,1]
print(f"{row1}\n{row2}\n{row3}")
mat=[row1,row2,row3]
pos=input("enter the position where you want to hide a 'X'")
row_num=int(pos[0])
col_num=int(pos[1])
row_selected=mat[row_num-1]
row_selected[col_num-1]='X'
print(f"{row1}\n{row2}\n{row3}")
 