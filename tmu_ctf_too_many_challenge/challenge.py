numbers = []
print ('starting')
with open("numbers.txt") as f:
        content = f.readlines()
for n in content:
    numbers.append(int(n.strip()))
print ('numbers are ready')

numbers.sort()
def binary_search(array, element):
    mid = 0
    start = 0
    end = len(array) - 1
    step = 0

    while (start <= end):
        
        step = step+1
        mid = (start + end) // 2

        if element == array[mid]:
            return mid

        if element < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

def func(adad) :
    javab = set()
    print('trying for %s' %adad)
    for i in numbers :
        el = adad - i
        ans = numbers[binary_search(numbers , el)]
        if binary_search(numbers , el) != -1 and ans !=i :
            if ans > i :
                javab.add((ans , i))
                #print(ans , i , ans + i , adad)
            else :
                javab.add((i , ans))
                #print(ans , i , ans + i , adad)
    return len(javab)


def get_flag(res):
    flag = []
    for i in range(len(res)):
        flag.append(chr(func(res[i])))
    flag = ''.join(flag)
    return flag


if __name__ == "__main__":
    res = [751741232, 519127658, 583555720, 3491231752, 3333111256, 481365731, 982100628, 1001121327, 3520999746,
           915725624, 3218509573, 3621224627, 3270950626, 3321456817, 3091205444, 999888800, 475855017, 448213157,
           3222412857, 820711846, 3710211491, 3119823672, 3333211607, 812955676, 971211391, 3210953872, 289789909,
           781213400, 578265122, 910021887, 653886578, 3712776506, 229812345, 582319118, 1111276998, 1151016390,
           700123328, 1074521304, 3210438183, 817210125, 501231350, 753244584, 3240911853, 415234677, 469125436,
           592610671, 612980665, 291821367, 344199617, 1011100412, 681623864, 897219249, 3132267885, 565913000,
           301203203, 3100544737, 432812663, 1012813485, 510928797, 671553831, 3216409218, 3191288433, 698777123,
           3512778698, 810476845, 3102989588, 3621432709, 812321695, 526486561, 378912454, 3316207359, 623111580,
           344209171, 537454826, 691277475, 2634678623, 1112182335, 792111856, 762989676, 666210267, 871278369,
           581009345, 391231132, 921732469, 717217468, 3101412929, 3101217354, 831912337, 532666530, 701012510,
           601365919, 492699680, 2843119525]
print("The flag is", get_flag(res))
