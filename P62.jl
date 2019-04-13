function permutation_hash(n::Int)
    R::Int=20777777
    hash::Int=1
    while n!=0
        hash*=(R+2*mod(n,10))
        n÷=10
    end
    hash
end

function checklen(len::Int)
    down::Int=round(10^((len-1)/3))
    up::Int=round((10^len-1)^(1/3))
    cubes=(down:up).^3
    for i in 1:up-down
        count=0
        for j in i:up-down+1
            if permutation_hash(cubes[i])==permutation_hash(cubes[j])
                count+=1
            end
        end
        if count==5
            println("result: ",down+i-1)
            return true
            break
        end
    end
end

# julia 
for i in 12:20
    println("bit: ", i)
    if check_bit(i)
        break
    end
end
