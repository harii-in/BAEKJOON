N = int(input())
st = list(input())


while True:
    s = st.count('s')
    t = st.count('t')

    if s == t:
        print(''.join(st))
        break
    
    st.pop(0)