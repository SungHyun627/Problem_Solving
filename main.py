print('@'*20,'\n1.아이스크림 N\n2.돌아온 사각형 만들기 \n3.같은 그림 맞추기\n'+'@'*20)
game_choice=int(input('게임을 선택하세요 :'))
def reinput(a,b,c,d) :
    if a < b or a >= c :
        while 1 :
            a = int(input('%s을 다시 입력해 주세요 : ' %d))
            if b<=a<c :
                break
    return a 
if game_choice==1 :
    print('### 아이스크림 N ###')
    ice_N=int(input('N을 입력해 주세요: '))
    reinput(ice_N,7,100,'N')
    ice_P=int(input('참가 인원을 입력해 주세요 : '))
    ice_P=reinput(ice_P,2,5,'참가인원')
    print('-'*30)
    print('아이스크림 %d 시작!' %ice_N)
    ilist=[]
    button=True
    for i in range(1,ice_N+1) :
        ilist.append(i)
    while button :
        for n in range(1,ice_P+1) :
            plist=input('%d째 플레이어 : ' %n).split()
            if plist[-1] != '끝' :
                print('%d째 플레이어의 패배입니다...' %n)
                button=False
                break
            plist.remove('끝')
            for i in range(len(plist)) :
                plist[i]=int(plist[i])
            if ilist[0] != plist[0] :
                print('%d째 플레이어의 패배입니다...' %n)
                button=False
                break
            if len(plist) > 3 :
                print('%d째 플레이어의 패배입니다...' %n)
                button=False
                break
            ilist=list(set(ilist)-set(plist))
            ilist.sort()
def coordinate(n) :
    a=n.split()
    for i in range(len(a)) :
        a[i]=float(a[i])
    c1,c2,c3,c4=a[0:2],a[2:4],a[4:6],a[6:]
    n=[c1,c2,c3,c4]
    return n
def reinsert(n) :
    error=[]
    if n[0][1] <0 or n[0][0] < 0 :
        error.append('1사분면')
    if n[1][1] < 0 or n[1][0] > 0 :
        error.append('2사분면')
    if n[2][1] >0 or n[2][0] >0 :
        error.append('3사분면')
    if n[3][1] >0 or n[3][0] < 0 :
        error.append('4사분면')
    return error
def figure(n) :
    for i  in range(4) :
        x,y=[],[]
        x.append(n[i][0])
        y.append(n[i][1])
    if len(set(x)) == 4 and len(set(y)) ==4 :
        if(y[1]-y[0]/x[1]-x[0]) == (y[2]-y[1]/x[2]-x[1]) or (y[2]-y[1]/x[2]-x[1]) == (y[3]-y[2]/x[3]-x[2]) or (y[3]-y[2]/x[3]-x[2]) == (y[0]-y[3]/x[0]-x[3]) or (y[0]-y[3]/x[0]-x[3]) == (y[1]-y[0]/x[1]-x[0]) :
            figure = '삼각형'
        elif(y[1]-y[0]/x[1]-x[0]) < (y[2]-y[1]/x[2]-x[1]) or (y[2]-y[1]/x[2]-x[1]) < (y[3]-y[2]/x[3]-x[2]) or (y[3]-y[2]/x[3]-x[2]) < (y[0]-y[3]/x[0]-x[3]) or (y[0]-y[3]/x[0]-x[3]) < (y[1]-y[0]/x[1]-x[0]) :
            figure = '볼록 사각형'
        elif(y[1]-y[0]/x[1]-x[0]) > (y[2]-y[1]/x[2]-x[1]) or (y[2]-y[1]/x[2]-x[1]) > (y[3]-y[2]/x[3]-x[2]) or (y[3]-y[2]/x[3]-x[2]) > (y[0]-y[3]/x[0]-x[3]) or (y[0]-y[3]/x[0]-x[3]) > (y[1]-y[0]/x[1]-x[0]) :                
            figure = '오목 사각형'
    elif x[0]==x[3] :
        if x[1]==x[2] :
            figure = '볼록 사각형'
        elif (y[1]-y[0]/x[1]-x[0]) == (y[2]-y[1]/x[2]-x[1]) or (y[2]-y[1]/x[2]-x[1]) ==(y[3]-y[2]/x[3]-x[2]) :
            figure = '삼각형'
        else :
            figure = '오목 사각형'
    elif x[1]==x[2] :
        if (y[3]-y[2]/x[3]-x[2]) == (y[0]-y[3]/x[0]-x[3]) or (y[0]-y[3]/x[0]-x[3]) == (y[1]-y[0]/x[1]-x[0]) :
            figure = '삼각형'
        else :
            figure = '오목 사각형'
    return figure
if game_choice==2 : 
    print('### 돌아온 사각형 만들기 ###')
    print('<공격 턴>')
    while True :
        a_1=input('공격자 - 1턴: ')
        errors =reinsert(coordinate(a_1))
        if not errors:
            break
        print('ERROR - {}'.format(errors))
    while True :
        a_2=input('공격자 - 2턴: ')
        errors =reinsert(coordinate(a_2))
        if not errors:
            break
        print('ERROR - {}'.format(errors))
    print=('<수비 턴>')
    while True :
        d_1=input('수비자 - 1턴: ')
        errors =reinsert(coordinate(d_1))
        if not errors:
            break
        print('ERROR - {}'.format(errors))
    while True :
        d_2=input('수비자 - 2턴: ')
        errors =reinsert(coordinate(d_2))
        if not errors:
            break
        print('ERROR - {}'.format(errors))
    print(1)
    print('-'*30)
    print('공격자:({},{})'.format(figure(a_1),figure(a_2)))
    print('수비자:({},{})'.format(figure(d_1),figure(d_2)))
    if len(set([figure(a_1),figure(a_2)])&set(figure(d_1),figure(d_2))) == 2 :
        print('공격자 승리!')
    elif len(set([figure(a_1),figure(a_2)])&set(figure(d_1),figure(d_2))) == 1 :
        print('비김!')
    else :
        print('수비자 승리!')
if game_choice==3 :
    print('### 같은 그림 맞추기 ###')
    card_num = int(input('카드의 수 : '))
    method = input('방법(직접/트럼프): ')
    if method == '트럼프' :
        print('-'*30)
        
          
    
    
            
            
    
    
    
    
        
        
