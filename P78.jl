using Plots

p_storage=zeros(1000,1000)

function p(n::Int, k::Int)
    """
    n: number of total coins
    k: max component
    the problem is try to find all the possible combination of numbers that added up equals n, 
    partitions of a number 'n' equals p(n,n),
    n can be made up with components from {1,2,3...n}, for example n=5=4+1 or 3+2
    p(n,k) can be divided into two parts, p(n-k,k) and p(n,k-1), which can be solved using recursion once we know p(n,1)=1
    """
    
    if k == 1 || n==0
        return 1
    elseif k < 1
        return 0
    elseif k > n
        return p(n,n)
    else
        return p(n-k,k)+p(n,k-1)
    end
end

function partitions(n::Int)
    return p(n, n)
end
    
#print(list(map(partitions, range(1, 8))))


function report(n::Int, temp::Int)
    println("current n: ",n," partitions: ",temp)
end

println("start searching...")
n = 94
target = 1000000
temp = partitions(n)


while temp % target != 0
    global n += 1
    global temp = partitions(n)
    report(n,temp)
end

"""
The algorithm above is impossible to solve this ploblem in one minute.

--from Stack Overflow
Wikipedia can help you here. 
I assume that the solution you already have is a recursion such as the one in the section "intermediate function". 
This can be used to find the solution to the Euler problem, but isn't fast.

A much better way is to use the recursion based on the pentagonal number theorem in the next section. 
The proof of this theorem isn't straight forward, so I don't think the authors of the problem expect that you come up with the theorem by yourself. 
Rather it is one of the problems, where they expect some literature search.

Answer:
363253009254357859308323315773967616467158361736338932270710864607092686080534 \
895417314045435376684389911706807452721591544937406153858232021581676352762505 \
545553421158554245989201590354130448112450821973350979535709118842524107301749 \
07784762924663654000000

"""