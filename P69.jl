using Primes

function φ(n::Int)::Int
    factors=factor(Set,n)
    return n*prod([1-1//p for p in factors]) # totient number
end



function maxtotient(n::Int)::Int
    j=0
    m=0
    for i in 2:n
        r=i/φ(i)
        if r>m
            m= r
            j=i
        end
    end
    return j
end

println(maxtotient(1000000))

