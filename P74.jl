function factorial_sum(n::Int)
    temp=0
    while n!=0
        temp+=factorial(mod(n,10))
        n÷=10
    end
    temp
end

function digital_factorial_chian(n::Int)
    chain::Array{Int}=[n]
    next=factorial_sum(n)
    while true
        if !(next in chain)
            push!(chain,next)
        else
            return length(chain)
        end
        next=factorial_sum(chain[end])
    end
end

# 100000
count=0
for i in 1:1000000
    if digital_factorial_chian(i)==60
        global count+=1
    end
end
println(count)
