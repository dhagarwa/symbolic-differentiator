function=raw_input('Please enter the function:')
import copy
#Defining a class polyTree
class parseTree:
    def __init__(self,cargo,left=None, right=None):
        self.cargo=cargo
        self.left=left
        self.right=right

    def __str__(self):
        return str(self.cargo)



def format_tokenlist(token_list):
    i=0
    while i<len(token_list):
        if token_list[i]==' ':
            token_list.pop(i)
        else:
            i+=1
    flag=0
    flag2=0
    i=0
    while i<len(token_list):
        if((token_list[i]>='0' and token_list[i] <= '9') or token_list[i]=='.') :
            flag2=0
            if flag==0:
                flag=1
                i +=1
            elif flag==1 and i!=0:
                token_list[i-1]=token_list[i-1] + token_list[i] 
                token_list.pop(i)
        else:
            flag2=1
            if flag==1 and i!=0:
                flag=0
                if '.' in token_list[i-1]:
                    token_list[i-1]=float(token_list[i-1])
                    i+=1
                else:
                    token_list[i-1]= int(token_list[i-1])
                    i +=1
            elif flag==0:
                i +=1
    if flag2==0:
        if '.' in token_list[i-1]:
            token_list[i-1]=float(token_list[i-1])
        else:
            token_list[i-1]=int(token_list[i-1])
            
    i=0
    while i<len(token_list):
        if(token_list[i]=='s' and token_list[i+1]=='i' and token_list[i+2]=='n'):
            token_list[i]='sin'
            del token_list[i+1]
            del token_list[i+1]
        elif token_list[i]=='c' and token_list[i+1]=='o' and token_list[i+2]=='s' :
            token_list[i]='cos'
            del token_list[i+1]
            del token_list[i+1]
        elif token_list[i]=='t' and token_list[i+1]=='a' and token_list[i+2]=='n' :
            token_list[i]='tan'
            del token_list[i+1]
            del token_list[i+1]
        elif token_list[i]=='l' and token_list[i+1]=='o' and token_list[i+2]=='g' :
            token_list[i]='log'
            del token_list[i+1]
            del token_list[i+1]
        elif token_list[i]=='s' and token_list[i+1]=='e' and token_list[i+2]=='c' :
            token_list[i]='sec'
            del token_list[i+1]
            del token_list[i+1]
        elif token_list[i]=='c' and token_list[i+1]=='o' and token_list[i+2]=='t' :
            token_list[i]='cot'
            del token_list[i+1]
            del token_list[i+1]
        elif token_list[i]=='e' and token_list[i+1]=='x' and token_list[i+2]=='p' :
            token_list[i]='exp'
            del token_list[i+1]
            del token_list[i+1]
            

        i+=1
            
    i=0
    while i<len(token_list):
        if token_list[i]=='-' and token_list[i-1]!='(' and i!=0:
            token_list[i]='+'
            token_list.insert(i+1,'(')
            token_list.insert(i+2,-1)
            token_list.insert(i+3,')')
            i+=4
        elif token_list[i]=='-' and token_list[i-1]=='(' and i!=0:
            token_list[i]='('
            token_list.insert(i+1,-1)
            token_list.insert(i+2,')')
            i+=3
        else:    
            i+=1

    i=0
    while i<len(token_list)-1:
        
        if (type(token_list[i])== type(0) or type(token_list[i])==type(0.0)) and (  token_list[i+1]== '(' or token_list[i+1]== 'x' or token_list[i+1]=='y'or token_list[i+1]=='sin' or token_list[i+1]=='cos' or token_list[i+1]=='tan' or token_list[i+1]=='log' or token_list[i+1]=='exp' or token_list[i+1]=='sec' or token_list[i+1]=='cot'):
            token_list.insert(i+1,'*')
            i +=2
        elif (token_list[i]== 'x' or token_list[i]=='y')and (type(token_list[i+1])== type(0) or type(token_list[i+1])==type(0.0) or token_list[i+1]=='sin' or token_list[i+1]=='cos' or token_list[i+1]=='tan' or token_list[i+1]=='log'or token_list[i+1]=='exp' or token_list[i+1]=='sec' or token_list[i+1]=='cot') :
            token_list.insert(i+1,'*')
            i +=2
        elif token_list[i]==')' and (token_list[i+1]=='(' or token_list[i+1]== 'x' or token_list[i+1]=='y' or type(token_list[i+1])==type(0) or type(token_list[i+1])==type(0.0) or token_list[i+1]=='sin' or token_list[i+1]=='cos' or token_list[i+1]=='tan' or token_list[i+1]=='log'or token_list[i+1]=='exp' or token_list[i+1]=='sec' or token_list[i+1]=='cot') :
            token_list.insert(i+1,'*')
            i+=2
        elif (token_list[i]=='x' or token_list[i]=='y')and (token_list[i+1]=='(' or token_list[i+1]=='x' or token_list[i+1]=='y'):
            token_list.insert(i+1,'*')
            i+=2
        else: i+=1

    return token_list


def get_token(token_list,expected):
    if token_list[0]== expected:
        del token_list[0]
        return True
    else:
        return False

def get_number(token_list):
    if get_token(token_list,'('):
        x=get_sum(token_list)
        if not get_token(token_list,')'):
            raise 'BadExpressionError', 'missing paranthesis'
        return x
    else:
        x=token_list[0]
        if type(x) != type(0) and x!= 'x' and x!='y' and type(x)!= type(0.0):
            return None
        token_list[0:1]=[]
        return parseTree(x,None,None)

def get_function(token_list):
    a=get_number(token_list)
    if len(token_list)==0 :
        return a
    if get_token(token_list,'sin'):
        b=get_function(token_list)
        return parseTree('sin',b,None)
    elif get_token(token_list,'cos'):
        b=get_function(token_list)
        return parseTree('cos',b,None)
    elif get_token(token_list,'tan'):
        b=get_function(token_list)
        return parseTree('tan',b,None)
    elif get_token(token_list,'log'):
        b=get_function(token_list)
        return parseTree('log',b,None)
    elif get_token(token_list,'sec'):
        b=get_function(token_list)
        return parseTree('sec',b,None)
    elif get_token(token_list,'cot'):
        b=get_function(token_list)
        return parseTree('cot',b,None)
    elif get_token(token_list,'exp'):
        b=get_function(token_list)
        return parseTree('exp',b,None)
    else:
        return a


def get_exponent(token_list):
    a=get_function(token_list)
    if len(token_list)==0:
        return a
    if get_token(token_list,'^'):
        b=get_exponent(token_list)
        return parseTree('^',a,b)
    else:
        return a

def get_division(token_list):
    a=get_exponent(token_list)
    if len(token_list)==0:
        return a
    if get_token(token_list,'/'):
        b=get_division(token_list)
        return parseTree('/',a,b)
    else:
        return a

def get_product(token_list):
    a=get_division(token_list)
    if len(token_list)==0:
        return a
    if get_token(token_list,'*'):
        b=get_product(token_list)
        return parseTree('*',a,b)
    else:
        return a

def get_sum(token_list):
    a=get_product(token_list)
    if len(token_list)==0:
        return a
    if get_token(token_list,'+'):
        b=get_sum(token_list)
        return parseTree('+',a,b)
    elif get_token(token_list,'-'):
        b=get_sum(token_list)
        return parseTree('-',a,b)
    else:
        return a

def tree_to_string(tree):
    if tree==None:
        return
    if tree.cargo=='x':
        return 'x'
    elif tree.cargo=='y':
        return 'y'
    elif type(tree.cargo)==type(0) or type(tree.cargo)==type(0.0):
        return str(tree.cargo)
    elif tree.cargo=='+':
        return '('+tree_to_string(tree.left)+'+'+tree_to_string(tree.right)+')'
    elif tree.cargo=='-':
        return '('+tree_to_string(tree.left)+'-'+tree_to_string(tree.right)+')'
    elif tree.cargo=='*':
        if not((type(tree.left.cargo)==type(0) or type(tree.left.cargo)==type(0.0)) and (type(tree.right.cargo)==type(0) or type(tree.right.cargo)==type(0.0))):
            return '('+tree_to_string(tree.left)+tree_to_string(tree.right)+')'
        else:
            return '('+tree_to_string(tree.left)+'*'+tree_to_string(tree.right)+')'
    elif tree.cargo=='/':
        return '('+tree_to_string(tree.left)+'/'+tree_to_string(tree.right)+')'
    elif tree.cargo=='^':
        return tree_to_string(tree.left)+'^'+tree_to_string(tree.right)
    else:
        return tree.cargo+'('+tree_to_string(tree.left)+')'

def differentiate(tree):
    if tree.cargo=='x' or tree.cargo=='y':
        return '1'
    elif type(tree.cargo)==type(0) or type(tree.cargo)==type(0.0):
        return '0'
    elif tree.cargo=='+':
        return '('+differentiate(tree.left) + '+' +differentiate(tree.right)+')'
    elif tree.cargo=='-':
        return '('+differentiate(tree.left) + '-' + diferentiate(tree.right)+')'
    elif tree.cargo=='*':
        return '('+'('+differentiate(tree.left)+')'+'*'+'('+tree_to_string(tree.right)+')' + '+' + '('+tree_to_string(tree.left)+')'+'*'+ '('+differentiate(tree.right)+')'+')'
    elif tree.cargo=='/':
        return '('+tree_to_string(tree.right)+'*'+'('+differentiate(tree.left)+')'+'-'+tree_to_string(tree.left)+'*'+'('+differentiate(tree.right)+')'+')'+'/'+'('+'('+tree_to_string(tree.right)+')'+'^'+'2'+')'
    elif tree.cargo=='sin':
        return 'cos'+tree_to_string(tree.left)+'*'+'('+differentiate(tree.left)+')'
    elif tree.cargo=='cos':
        return '(-sin'+tree_to_string(tree.left)+')'+'*'+'('+differentiate(tree.left)+')'
    elif tree.cargo=='log':
        return '('+'1/'+tree_to_string(tree.left)+')'+'('+differentiate(tree.left)+')'
    elif tree.cargo=='tan':
        return '('+'sec'+tree_to_string(tree.left)+')'+'^2'+'('+differentiate(tree.left)+')'
    elif tree.cargo=='sec':
        return '('+'sec'+tree_to_string(tree.left)+'tan'+tree_to_string(tree.left)+')'+'('+differentiate(tree.left)+')'
    elif tree.cargo=='exp':
        return '(exp('+tree_to_string(tree.left)+')'+')'+'*'+'('+differentiate(tree.left)+')'
    elif tree.cargo=='^':
        return '('+tree_to_string(tree.left)+'^'+tree_to_string(tree.right)+'*'+'('+differentiate(tree.right)+')'+'log'+tree_to_string(tree.left)+'+'+'('+tree_to_string(tree.left)+')'+'^'+'('+tree_to_string(tree.right)+'+'+'(-1))'+'('+tree_to_string(tree.right)+')'+differentiate(tree.left)+')'
    
def simplify_parseTree(tree):
    global indicator
    if tree==None:
        return
    tree.left=simplify_parseTree(tree.left)
    tree.right=simplify_parseTree(tree.right)
    if tree.cargo=='*' and (tree.left.cargo==0 or tree.right.cargo==0):
        indicator=1
        return parseTree(0,None,None)
    elif tree.cargo=='*' and (type(tree.left.cargo)==type(0) or type(tree.left.cargo)==type(0.0)) and (type(tree.right.cargo)==type(0) or type(tree.right.cargo)==type(0.0)):
        indicator=1
        return parseTree(tree.left.cargo*tree.right.cargo,None,None)
    elif tree.cargo=='*' and tree.left.cargo==1 :
        indicator=1
        return tree.right
    elif tree.cargo=='*' and tree.right.cargo==1:
        indicator=1
        return tree.left
    elif tree.cargo=='+' and tree.left.cargo==0 and tree.right.cargo!=0:
        indicator=1
        return tree.right
    elif tree.cargo=='+' and tree.left.cargo!=0 and tree.right.cargo==0:
        indicator=1
        return tree.left
    elif tree.cargo=='/' and tree.right.cargo==0 :
        raise 'Unexpected divisor encountered'
    elif tree.cargo=='/' and tree.left.cargo==0:
        indicator=1
        return parseTree(0,None,None)
    elif tree.cargo=='/' and tree.right.cargo==1:
        indicator=1
        return tree.left
    elif tree.cargo=='*' and (type(tree.left.cargo)==type(0) or type(tree.left.cargo)==type(0.0)) and  tree.right.cargo=='*' and (type(tree.right.left.cargo)==type(0) or type(tree.right.left.cargo)==type(0.0)):
        tree.left.cargo=tree.left.cargo*tree.right.left.cargo
        indicator=1
        tree.right=tree.right.right
        return tree
    elif tree.cargo=='*' and (type(tree.right.cargo)==type(0) or type(tree.right.cargo)==type(0.0)) and  tree.left.cargo=='*' and (type(tree.left.left.cargo)==type(0) or type(tree.left.left.cargo)==type(0.0)):
        tree.right.cargo=tree.right.cargo*tree.left.left.cargo
        indicator=1
        tree.left=tree.left.right
        return tree
    elif tree.cargo=='*' and (type(tree.right.cargo)==type(0) or type(tree.right.cargo)==type(0.0)) and  tree.left.cargo=='*' and (type(tree.left.right.cargo)==type(0) or type(tree.left.right.cargo)==type(0.0)):
        tree.right.cargo=tree.right.cargo*tree.left.right.cargo
        indicator=1
        tree.left=tree.left.left
        return tree   
    elif tree.cargo=='*' and (type(tree.left.cargo)==type(0) or type(tree.left.cargo)==type(0.0)) and  tree.right.cargo=='*' and (type(tree.right.right.cargo)==type(0) or type(tree.right.right.cargo)==type(0.0)):
        tree.left.cargo=tree.left.cargo*tree.right.right.cargo
        indicator=1
        tree.right=tree.right.left
        return tree
    elif tree.cargo=='*' and (type(tree.right.cargo)==type(0) or type(tree.right.cargo)==type(0.0)):
        temp=tree.left
        indicator=1
        tree.left=tree.right
        tree.right=temp
        return tree
    
    return tree

def order(lst):
    lst=level(lst)
    if len(lst)==0 or len(lst)==1: return lst
    i=1
    while i<len(lst):
        lst[i]=order(lst[i])
        i+=1
    if lst[0]!='+' and lst[0]!='*': return lst
    i=1
    while i<len(lst):
        flag=0
        j=1
        while j<len(lst)-i:
            if lst[j]>lst[j+1]:
                temp=lst[j]
                lst[j]=lst[j+1]
                lst[j+1]=temp
                flag=1
            j+=1
        if flag==0: break
        i+=1
    return lst
            
            

def simplify_basic(lst):
    lst=order(lst)
    global indicator
    if len(lst)==0 or len(lst)==1: return lst
    i=1
    while i<len(lst):
        lst[i]=simplify_basic(lst[i])
        i+=1
    if lst[0]=='+':
        i=1
        constant=0
        flag=0
        while i<len(lst):
            if type(lst[i][0])==type(0) or type(lst[i][0])==type(0.0):
                if i==2:indicator=1
                constant=constant+lst[i][0]
                lst.pop(i)
                flag=1
            else:
                i+=1
        if flag==1:        
            lst.append([constant])
        lst=order(lst)
    if lst[0]=='+' and len(lst)==2:
        indicator=1
        lst=lst[1]
        lst=order(lst)
    if lst[0]=='+' and len(lst)>=3 and lst[1][0]==0:
        indicator=1
        lst.pop(1)
    if lst[0]=='*':
        i=1
        constant=1
        flag=0
        while i<len(lst):
            if type(lst[i][0])==type(0) or type(lst[i][0])==type(0.0):
                if i==2:indicator=1
                constant=constant*lst[i][0]
                lst.pop(i)
                flag=1
            else:
                i+=1
        if flag==1:        
            lst.append([constant])
        lst=order(lst)
    if lst[0]=='*' and len(lst)==2:
        lst=lst[1]
        lst=order(lst)
        indicator=1
    if lst[0]=='*' and len(lst)>=3 and lst[1][0]==1:
        lst.pop(1)
        lst=order(lst)
        indicator=1
    if lst[0]=='*' and lst[1][0]==0:
        lst=[0]
        indicator=1
    if lst[0]=='^' and lst[1][0]==1:
        lst=[1]
        indicator=1
    if lst[0]=='^' and lst[1][0]==0 and lst[2][0]!=0:
        lst=[0]
        indicator=1
    if lst[0]=='^' and lst[2][0]==1:
        lst=lst[1]
        lst=order(lst)
        indicator=1
    if lst[0]=='^' and lst[2][0]==0 and lst[1][0]!=0:
        lst=[1]
        indicator=1
    return lst
        

def saint(tree,lst):
    if tree==None: return
    elif type(tree.cargo)==type(0) or type(tree.cargo)==type(0.0):
        lst.append(tree.cargo)
        return lst
    elif tree.cargo=='x' or tree.cargo=='y':
        lst.append(tree.cargo)
        return lst
    elif tree.cargo=='+':
        lst.append(tree.cargo)
        lst.append([])
        lst.append([])
        lst[1]=saint(tree.left,lst[1])
        lst[2]=saint(tree.right,lst[2])
        return lst
    elif tree.cargo=='-':
        lst.append(tree.cargo)
        lst.append([])
        lst.append([])
        lst[1]=saint(tree.left,lst[1])
        lst[2]=saint(tree.right,lst[2])
        return lst
    elif tree.cargo=='*':
        lst.append(tree.cargo)
        lst.append([])
        lst.append([])
        lst[1]=saint(tree.left,lst[1])
        lst[2]=saint(tree.right,lst[2])
        return lst
    elif tree.cargo=='/':
        lst.append(tree.cargo)
        lst.append([])
        lst.append([])
        lst[1]=saint(tree.left,lst[1])
        lst[2]=saint(tree.right,lst[2])
        return lst
    elif tree.cargo=='^':
        lst.append(tree.cargo)
        lst.append([])
        lst.append([])
        lst[1]=saint(tree.left,lst[1])
        lst[2]=saint(tree.right,lst[2])
        return lst
    elif tree.cargo=='sin':
        lst.append(tree.cargo)
        lst.append([])
        lst[1]=saint(tree.left,lst[1])
        return lst
    elif tree.cargo=='cos':
        lst.append(tree.cargo)
        lst.append([])
        lst[1]=saint(tree.left,lst[1])
        return lst
    elif tree.cargo=='tan':
        lst.append(tree.cargo)
        lst.append([])
        lst[1]=saint(tree.left,lst[1])
        return lst
    elif tree.cargo=='sec':
        lst.append(tree.cargo)
        lst.append([])
        lst[1]=saint(tree.left,lst[1])
        return lst
    elif tree.cargo=='exp':
        lst.append(tree.cargo)
        lst.append([])
        lst[1]=saint(tree.left,lst[1])
        return lst
    elif tree.cargo=='log':
        lst.append(tree.cargo)
        lst.append([])
        lst[1]=saint(tree.left,lst[1])
        return lst

def level(lst):
    if len(lst)==0 or len(lst)==1: return lst
    i=1
    while i<len(lst):
        lst[i]=level(lst[i])
        i+=1
    j=1
    while j<len(lst):
        if lst[0]=='+' and lst[j][0]=='+':
            i=1
            while i<len(lst[j]):
                lst.append(lst[j][i])
                i+=1
            lst.pop(j)
        elif   lst[0]=='*' and lst[j][0]=='*':
            i=1
            while i<len(lst[j]):
                lst.append(lst[j][i])
                i+=1
            lst.pop(j)
        else: j+=1
    return lst
        

def print_tree_postorder(tree):
    if tree == None: return
    print_tree_postorder(tree.left)
    print_tree_postorder(tree.right)
    print tree.cargo

indicator=0
token_list=list(function)
token_list=format_tokenlist(token_list)
tree=get_sum(token_list)
token_list2=list(differentiate(tree))
token_list2=format_tokenlist(token_list2)
derivative_tree=get_sum(token_list2)
#while True:
#    indicator=0
#    derivative_tree=simplify_parseTree(derivative_tree)
#    if indicator==0:
#        break
saint_list=[]
saint_list=saint(derivative_tree,saint_list)
while True:
    indicator=0
    saint_list=simplify_basic((saint_list))
    if indicator==0:
        break
print saint_list
